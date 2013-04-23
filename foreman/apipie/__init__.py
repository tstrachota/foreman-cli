# -*- coding: utf-8 -*-
#
# Copyright © 2012 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

import re

import base64
import kerberos
from kerberos import GSSError
import httplib
import logging
import os
import urllib
import mimetypes
import sys

try:
    import json
except ImportError:
    import simplejson as json

from M2Crypto import SSL, httpslib


class AuthenticationStrategy(object):

    @classmethod
    def _get_connection(cls, host, port, protocol):
        if protocol == "https":
            return httplib.HTTPSConnection(host, port)
        else:
            return httplib.HTTPConnection(host, port)

    @classmethod
    def set_headers(cls, headers):
        return headers

    def connect(self, host, port, protocol):
        return self._get_connection(host, port, protocol)

class NoAuthentication(AuthenticationStrategy):

    def connect(self, host, port, protocol):
        return self._get_connection(host, port, protocol)

class BasicAuthentication(AuthenticationStrategy):

    def __init__(self, username, password):
        super(BasicAuthentication, self).__init__()
        self.__username = username
        self.__password = password

    def set_headers(self, headers):
        raw = ':'.join((self.__username, self.__password))
        encoded = base64.encodestring(raw)[:-1]
        headers['Authorization'] = 'Basic ' + encoded
        return headers

    def connect(self, host, port, protocol):
        return self._get_connection(host, port, protocol)


class SSLAuthentication(AuthenticationStrategy):

    def __init__(self, certfile, keyfile):
        super(SSLAuthentication, self).__init__()
        self.__certfile = certfile
        self.__keyfile = keyfile
        self.__check_cert_and_key()

    def __check_cert_and_key(self):
        if not os.access(self.__certfile, os.R_OK):
            raise RuntimeError(_('certificate file %s does not exist or cannot be read')
                               % self.__certfile)
        if not os.access(self.__keyfile, os.R_OK):
            raise RuntimeError(_('key file %s does not exist or cannot be read')
                               % self.__keyfile)

    def connect(self, host, port, protocol):
        if protocol != "https":
            raise AuthenticationError(_("can't authenticate via certificate when not using https connection"))
        ssl_context = SSL.Context('sslv3')
        ssl_context.load_cert(self.__certfile, self.__keyfile)
        return httpslib.HTTPSConnection(host, port, ssl_context=ssl_context)


class KerberosAuthentication(AuthenticationStrategy):

    def __init__(self, host):
        super(KerberosAuthentication, self).__init__()
        self.__host = host

    def set_headers(self, headers):
        ctx = kerberos.authGSSClientInit("HTTP@" + self.__host, \
            gssflags=kerberos.GSS_C_DELEG_FLAG|kerberos.GSS_C_MUTUAL_FLAG|kerberos.GSS_C_SEQUENCE_FLAG)[1]
        kerberos.authGSSClientStep(ctx, '')
        tgt = kerberos.authGSSClientResponse(ctx)

        if tgt:
            headers['Authorization'] = 'Negotiate %s' % tgt
            return headers
        else:
            raise AuthenticationError(_("Couldn't authenticate via kerberos"))


    def connect(self, host, port, protocol):
        self._get_connection(host, port, protocol)



class ServerRequestError(Exception):
    """
    Exception to indicate a less than favorable response from the server.
    The arguments are [0] the response status as an integer and
    [1] the response message as a dict, if we managed to decode from json,
    or a str if we didn't [2] potentially a traceback, if the server response
    was a python error, otherwise it will be None
    """
    def __init__(self, response):
        self.response = response

    def __str__(self):
        return str(self.response.status)

class AuthenticationError(Exception):
    """
    Exception to indicate a less than favorable response from the server.
    The arguments are [0] the response status as an integer and
    [1] the response message as a dict, if we managed to decode from json,
    or a str if we didn't [2] potentially a traceback, if the server response
    was a python error, otherwise it will be None
    """
    pass


class Response(object):

    def __init__(self, response):
      self.status = response.status
      self.headers = response.getheaders()
      self.body = Response._get_body(response)
      self.__msg = response.msg

    def get_header(self, header, default=None):
        return self.__msg.getheader(header, default)

    @classmethod
    def _get_body(cls, response):
        response_body = response.read()
        try:
            response_body = json.loads(response_body, encoding='utf-8')
        except ValueError:
            pass
        return response_body


class ServerConnection(object):
    """
    Katello server connection class.

    @ivar host: host name of the katello server
    @ivar port: port the katello server is listening on (443)
    @ivar protocol: protocol the katello server is using (http, https)
    @ivar path_prefix: mount point of the katello api (/katello/api)
    @ivar headers: dictionary of http headers to send in requests
    """
    auth_method = NoAuthentication()

    #---------------------------------------------------------------------------
    def __init__(self, host, port=443, protocol='https', path_prefix='', accept_lang=None):
        assert protocol in ('http', 'https')

        self.host = host
        self.port = port
        self.protocol = protocol
        self.path_prefix = "/"+path_prefix
        self.headers = {}

        default_headers = {'Accept': 'application/json',
                           'content-type': 'application/json',
                           'User-Agent': 'katello-cli/0.1'}
        self.headers.update(default_headers)

        if accept_lang:
            self.headers.update( { 'Accept-Language': accept_lang } )

    # credentials setters -----------------------------------------------------
    def set_auth_method(self, auth_method):
        self.auth_method = auth_method

    # protected server connection methods -------------------------------------

    def _connect(self):
        # make an appropriate connection to the server and cache it
        return self.auth_method.connect(self.host, self.port, self.protocol)

    def _set_auth_headers(self):
        self.auth_method.set_headers(self.headers)


    # protected request utilities ---------------------------------------------

    def _build_url(self, path, queries=None):
        queries = queries or {}

        # build the request url from the path and queries dict or tuple
        if not path.startswith(self.path_prefix):
            path = '/'.join((self.path_prefix, path))

        # make sure the path is ascii and uses appropriate characters
        path = urllib.quote(path.encode('utf-8'))
        for key, value in queries.items():
            if isinstance(value, basestring):
                queries[key] = value.encode('utf-8')

        queries = urllib.urlencode(queries)
        if queries:
            path = '?'.join((path, queries))
        return path


    def _request(self, method, path, queries=None, body=None, multipart=False, custom_headers=None):
        queries = queries or {}
        custom_headers = custom_headers or {}

        # make a request to the server and return the response
        connection = self._connect()
        url = self._build_url(path, queries)

        content_type, body = self._prepare_body(body, multipart)

        self.headers['content-type']   = content_type
        self.headers['content-length'] = str(len(body) if body else 0)
        self._set_auth_headers()

        connection.request(method, url, body=body, headers=dict(self.headers.items() + custom_headers.items()))
        return self._process_response(connection.getresponse())


    def _process_response(self, response):
        """
        Try to parse the response
        @type response: HTTPResponse
        @param response: http response
        @rtype: (int, string)
        @return: tuple of the response status and response body
        """
        response = Response(response)

        # if response.status >= 300:
        #     raise ServerRequestError(response)
        return response


    def _prepare_body(self, body, multipart):
        """
        Encode body according to needs as json or multipart
        @type body: any
        @param body: data to encode
        @type multipart: boolean
        @param multipart: set True for multipart requests
        @rtype: (string, string)
        @return: tuple of the content type and the encoded body
        """
        content_type = 'application/json'
        if multipart:
            content_type, body = self._encode_multipart_formdata(body)
        elif not isinstance(body, (type(None), file)):
            content_type, body = self._encode_json(body)

        return (content_type, body)

    def _flatten_to_multipart(self, data, key=None):
        """
        Encode data recursively as if they were sent by http form
        @type key: string
        @param key: name of the parent field (None for the first one)
        @type data: any
        @param data: data to encode
        @rtype: [(string, string)]
        @return: list of tuples of the field name and field value
        """

        if isinstance(data, (dict)):
            #flatten dictionaries
            result = []
            for (sub_key, value) in data.items():
                if key is None:
                    name = str(sub_key)
                else:
                    name = str(key)+'['+str(sub_key)+']'
                result.extend(self._flatten_to_multipart(value, name))
            return result

        elif isinstance(data, (list, tuple)):
            #flatten lists and tuples
            result = []
            for value in data:
                if key is None:
                    name = str(key)
                else:
                    name = str(key)+'[]'
                result.extend(self._flatten_to_multipart(value, name))
            return result

        else:
            #flatten other datatypes
            return [(key, data)]



    def _encode_multipart_formdata(self, data):
        """
        Encode data for httplib request
        @type data: any
        @param data: data to encode for the request
        @rtype: (string, string)
        @return: tuple of the content type and encoded data
        """
        fields = self._flatten_to_multipart(data)

        boundary = '----------BOUNDARY_$'
        lines = []

        for (key, value) in fields:
            if isinstance(value, (file)):
                filename = value.name
                content  = value.read()

                lines.append('--' + boundary)
                lines.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (str(key), str(filename)))
                lines.append('Content-Type: %s' % self._get_content_type(filename))
                lines.append('')
                lines.append(content)
            else:
                lines.append('--' + boundary)
                lines.append('Content-Disposition: form-data; name="%s"' % str(key))
                lines.append('')
                lines.append(value)
        lines.append('--' + boundary + '--')
        lines.append('')

        body = '\r\n'.join(lines)
        content_type = 'multipart/form-data; boundary=%s' % boundary
        return content_type, body

    def _encode_json(self, data):
        content_type = 'application/json'
        data = json.dumps(data)
        return content_type, data

    @classmethod
    def _get_content_type(cls, filename):
        """
        Guess content type from file name
        @type filename: string
        @param filename: name of the file to gues type from
        @rtype: string
        @return: http content type
        """
        return mimetypes.guess_type(filename)[0] or 'application/octet-stream'


    # request methods ---------------------------------------------------------
    # pylint: disable=C0103
    def DELETE(self, path, body=None, custom_headers=None):
        """
        Send a DELETE request to the katello server.
        @type path: str
        @param path: path of the resource to delete
        @rtype: (int, dict or None or str)
        @return: tuple of the http response status and the response body
        @raise ServerRequestError: if the request fails
        """
        return self._request('DELETE', path, body=body, custom_headers=None)

    def GET(self, path, queries=None, custom_headers=None):
        """
        Send a GET request to the katello server.
        @type path: str
        @param path: path of the resource to get
        @type queries: dict or iterable of tuple pairs
        @param queries: dictionary of iterable of key, value pairs to send as
                        query parameters in the request
        @type custom_headers: dict or iterable of tuple pairs
        @param custom_headers: custom headers
        @rtype: (int, dict or None or str)
        @return: tuple of the http response status and the response body
        @raise ServerRequestError: if the request fails
        """
        return self._request('GET', path, queries, custom_headers=custom_headers)

    def HEAD(self, path, custom_headers=None):
        """
        Send a HEAD request to the katello server.
        @type path: str
        @param path: path of the resource to check
        @rtype: (int, dict or None or str)
        @return: tuple of the http response status and the response body
        @raise ServerRequestError: if the request fails
        """
        return self._request('HEAD', path, custom_headers=None)

    def POST(self, path, body=None, multipart=False, custom_headers=None):
        """
        Send a POST request to the katello server.
        @type path: str
        @param path: path of the resource to post to
        @type body: dict or None
        @param body: (optional) dictionary for json encoding of post parameters
        @type multipart: boolean
        @param multipart: set True for multipart posts
        @type custom_headers: dict or iterable of tuple pairs
        @param custom_headers: custom headers
        @rtype: (int, dict or None or str)
        @return: tuple of the http response status and the response body
        @raise ServerRequestError: if the request fails
        """
        return self._request('POST', path, body=body, multipart=multipart, custom_headers=custom_headers)

    def PUT(self, path, body, multipart=False, custom_headers=None):
        """
        Send a PUT request to the katello server.
        @type path: str
        @param path: path of the resource to put
        @type body: dict
        @param body: dictionary for json encoding of resource
        @type multipart: boolean
        @param multipart: set True for multipart puts
        @type custom_headers: dict or iterable of tuple pairs
        @param custom_headers: custom headers
        @rtype: (int, dict or None or str)
        @return: tuple of the http response status and the response body
        @raise ServerRequestError: if the request fails
        """
        return self._request('PUT', path, body=body, multipart=multipart, custom_headers=custom_headers)




class ApipieApi(object):

    def __init__(self, connection):
        self._connection = connection

    @classmethod
    def params_in_path(cls, url):
        return re.findall(':([^\/]*)', url)

    @classmethod
    def fill_params_in_url(cls, url, params):
      params = params or {}
      url = url + "/"

      # insert param values
      url_param_names = ApipieApi.params_in_path(url)
      for param_name in url_param_names:
          if not param_name in params:
              raise Exception("missing param '%s' in parameters" % param_name)

          url = url.replace(":%s/" % param_name, "%s/" % str(params.get(param_name)))
          del params[param_name]
      return url


