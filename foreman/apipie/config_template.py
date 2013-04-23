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


class ConfigTemplate(ApipieApi):


    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] order  sort results 
    # @option params [String] page  paginate results 
    # @option params [String] per_page  number of entries per request 
    # @option params [String] search  filter results 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def index(self, params = {}):
        url = ConfigTemplate.fill_params_in_url("/api/config_templates", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def show(self, params = {}):
        url = ConfigTemplate.fill_params_in_url("/api/config_templates/:id", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [Hash] config_template
    #   allowed keys are:
    #   * operatingsystem_ids [String]  array of operating systems id to associate the template with 
    #   * template_kind_id [String, nil]  not relevant for snippet 
    #   * audit_comment [String, nil]
    #   * name [String]  template name 
    #   * snippet [String, nil]
    #   * template [String]
    #   * template_combinations_attributes [String]  array of template combinations (hostgroup_id, environment_id) 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def create(self, params = {}):
        url = ConfigTemplate.fill_params_in_url("/api/config_templates", params)
        return self._connection.POST(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    # @option params [Hash] config_template
    #   allowed keys are:
    #   * operatingsystem_ids [String]  array of operating systems id to associate the template with 
    #   * template_kind_id [String, nil]  not relevant for snippet 
    #   * audit_comment [String, nil]
    #   * name [String]  template name 
    #   * snippet [String]
    #   * template [String]
    #   * template_combinations_attributes [String]  array of template combinations (hostgroup_id, environment_id) 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def update(self, params = {}):
        url = ConfigTemplate.fill_params_in_url("/api/config_templates/:id", params)
        return self._connection.PUT(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] version  template version 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def revision(self, params = {}):
        url = ConfigTemplate.fill_params_in_url("/api/config_templates/revision", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def destroy(self, params = {}):
        url = ConfigTemplate.fill_params_in_url("/api/config_templates/:id", params)
        return self._connection.DELETE(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def build_pxe_default(self, params = {}):
        url = ConfigTemplate.fill_params_in_url("/api/config_templates/build_pxe_default", params)
        return self._connection.GET(url, params)
