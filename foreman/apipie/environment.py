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


class Environment(ApipieApi):


    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] order  sort results 
    # @option params [String] page  paginate results 
    # @option params [String] per_page  number of entries per request 
    # @option params [String] search  filter results 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def index(self, params = {}):
        url = Environment.fill_params_in_url("/api/environments", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def show(self, params = {}):
        url = Environment.fill_params_in_url("/api/environments/:id", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [Hash] environment
    #   allowed keys are:
    #   * name [String]
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def create(self, params = {}):
        url = Environment.fill_params_in_url("/api/environments", params)
        return self._connection.POST(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    # @option params [Hash] environment
    #   allowed keys are:
    #   * name [String]
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def update(self, params = {}):
        url = Environment.fill_params_in_url("/api/environments/:id", params)
        return self._connection.PUT(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def destroy(self, params = {}):
        url = Environment.fill_params_in_url("/api/environments/:id", params)
        return self._connection.DELETE(url, params)
