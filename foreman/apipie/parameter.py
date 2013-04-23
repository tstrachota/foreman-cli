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


class Parameter(ApipieApi):


    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] domain_id  id of domain 
    # @option params [String] host_id  id of host 
    # @option params [String] hostgroup_id  id of hostgroup 
    # @option params [String] operatingsystem_id  id of operating system 
    # @option params [String] page  paginate results 
    # @option params [String] per_page  number of entries per request 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def index(self, params = {}):
        url = Parameter.fill_params_in_url("/api/host/:host_id/parameters", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id  id of parameter 
    # @option params [String] domain_id  id of domain 
    # @option params [String] host_id  id of host 
    # @option params [String] hostgroup_id  id of hostgroup 
    # @option params [String] operatingsystem_id  id of operating system 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def show(self, params = {}):
        url = Parameter.fill_params_in_url("/api/host/:host_id/parameters/:id", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id  id of parameter 
    # @option params [String] domain_id  id of domain 
    # @option params [String] host_id  id of host 
    # @option params [String] hostgroup_id  id of hostgroup 
    # @option params [String] operatingsystem_id  id of operating system 
    # @option params [Hash] parameter
    #   allowed keys are:
    #   * name [String]
    #   * value [String]
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def create(self, params = {}):
        url = Parameter.fill_params_in_url("/api/host/:host_id/parameters/:id", params)
        return self._connection.POST(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id  id of parameter 
    # @option params [String] domain_id  id of domain 
    # @option params [String] host_id  id of host 
    # @option params [String] hostgroup_id  id of hostgroup 
    # @option params [String] operatingsystem_id  id of operating system 
    # @option params [Hash] parameter
    #   allowed keys are:
    #   * name [String]
    #   * value [String]
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def update(self, params = {}):
        url = Parameter.fill_params_in_url("/api/host/:host_id/parameters/:id", params)
        return self._connection.PUT(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id  id of parameter 
    # @option params [String] domain_id  id of domain 
    # @option params [String] host_id  id of host 
    # @option params [String] hostgroup_id  id of hostgroup 
    # @option params [String] operatingsystem_id  id of operating system 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def destroy(self, params = {}):
        url = Parameter.fill_params_in_url("/api/host/:host_id/parameters/:id", params)
        return self._connection.DELETE(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [Object] domain_id Part of +/api/domain/:domain_id/parameters+ path
    # @option params [Object] host_id Part of +/api/host/:host_id/parameters+ path
    # @option params [Object] hostgroup_id Part of +/api/hostgroup/:hostgroup_id/parameters+ path
    # @option params [Object] operatingsystem_id Part of +/api/operatingsystem/:operatingsystem_id/parameters+ path
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def reset(self, params = {}):
        url = Parameter.fill_params_in_url("/api/host/:host_id/parameters", params)
        return self._connection.DELETE(url, params)
