# -*- coding: utf-8 -*-
#
# Copyright © 2013 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from apipie import ApipieApi


class Medium(ApipieApi):


    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] order  for example, name asc, or name desc 
    # @option params [String] page  paginate results 
    # @option params [String] per_page  number of entries per request 
    # @option params [String] search  filter results 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def index(self, params = {}):
        url = Medium.fill_params_in_url("/api/media", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def show(self, params = {}):
        url = Medium.fill_params_in_url("/api/media/:id", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [Hash] medium
    #   allowed keys are:
    #   * name [String]  name of media 
    #   * os_family [String]  the family that the operating system belongs to.  available families:  archlinux  debian  redhat  solaris  suse  windows  
    #   * path [String]  the path to the medium, can be a url or a valid nfs server (exclusive of the architecture).  for example mirror.averse.net/centos/$version/os/$arch where $arch will be substituted for the host's actual os architecture and $version, $major and $minor will be substituted for the version of the operating system.  solaris and debian media may also use $release. 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def create(self, params = {}):
        url = Medium.fill_params_in_url("/api/media", params)
        return self._connection.POST(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    # @option params [Hash] medium
    #   allowed keys are:
    #   * name [String]  name of media 
    #   * os_family [String, nil]  the family that the operating system belongs to.  available families:  archlinux  debian  redhat  solaris  suse  windows  
    #   * path [String]  the path to the medium, can be a url or a valid nfs server (exclusive of the architecture).  for example mirror.averse.net/centos/$version/os/$arch where $arch will be substituted for the host's actual os architecture and $version, $major and $minor will be substituted for the version of the operating system.  solaris and debian media may also use $release. 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def update(self, params = {}):
        url = Medium.fill_params_in_url("/api/media/:id", params)
        return self._connection.PUT(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def destroy(self, params = {}):
        url = Medium.fill_params_in_url("/api/media/:id", params)
        return self._connection.DELETE(url, params)
