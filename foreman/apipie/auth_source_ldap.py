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


class AuthSourceLdap(ApipieApi):


    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] page  paginate results 
    # @option params [String] per_page  number of entries per request 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def index(self, params = {}):
        url = AuthSourceLdap.fill_params_in_url("/api/auth_source_ldaps", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def show(self, params = {}):
        url = AuthSourceLdap.fill_params_in_url("/api/auth_source_ldaps/:id", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [Hash] auth_source_ldap
    #   allowed keys are:
    #   * account [String]
    #   * account_password [String]  required if onthefly_register is true 
    #   * attr_firstname [String]  required if onthefly_register is true 
    #   * attr_lastname [String]  required if onthefly_register is true 
    #   * attr_login [String]  required if onthefly_register is true 
    #   * attr_mail [String]  required if onthefly_register is true 
    #   * base_dn [String]
    #   * host [String]
    #   * name [String]
    #   * onthefly_register [String]
    #   * port [String]  defaults to 389 
    #   * tls [String]
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def create(self, params = {}):
        url = AuthSourceLdap.fill_params_in_url("/api/auth_source_ldaps", params)
        return self._connection.POST(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    # @option params [Hash] auth_source_ldap
    #   allowed keys are:
    #   * account [String]
    #   * account_password [String]  required if onthefly_register is true 
    #   * attr_firstname [String]  required if onthefly_register is true 
    #   * attr_lastname [String]  required if onthefly_register is true 
    #   * attr_login [String]  required if onthefly_register is true 
    #   * attr_mail [String]  required if onthefly_register is true 
    #   * base_dn [String]
    #   * host [String]
    #   * name [String]
    #   * onthefly_register [String]
    #   * port [String]  defaults to 389 
    #   * tls [String]
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def update(self, params = {}):
        url = AuthSourceLdap.fill_params_in_url("/api/auth_source_ldaps/:id", params)
        return self._connection.PUT(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def destroy(self, params = {}):
        url = AuthSourceLdap.fill_params_in_url("/api/auth_source_ldaps/:id", params)
        return self._connection.DELETE(url, params)
