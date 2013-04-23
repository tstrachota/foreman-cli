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


class TemplateCombination(ApipieApi):


    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] config_template_id
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def index(self, params = {}):
        url = TemplateCombination.fill_params_in_url("/api/config_templates/:config_template_id/template_combinations", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] config_template_id
    # @option params [Hash] template_combination
    #   allowed keys are:
    #   * environment_id [String, nil]  environment id 
    #   * hostgroup_id [String, nil]  hostgroup id 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def create(self, params = {}):
        url = TemplateCombination.fill_params_in_url("/api/config_templates/:config_template_id/template_combinations", params)
        return self._connection.POST(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def show(self, params = {}):
        url = TemplateCombination.fill_params_in_url("/api/template_combinations/:id", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def destroy(self, params = {}):
        url = TemplateCombination.fill_params_in_url("/api/template_combinations/:id", params)
        return self._connection.DELETE(url, params)
