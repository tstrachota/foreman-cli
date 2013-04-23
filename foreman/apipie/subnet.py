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


class Subnet(ApipieApi):


    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] order  sort results 
    # @option params [String] page  paginate results 
    # @option params [String] per_page  number of entries per request 
    # @option params [String] search  filter results 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def index(self, params = {}):
        url = Subnet.fill_params_in_url("/api/subnets", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def show(self, params = {}):
        url = Subnet.fill_params_in_url("/api/subnets/:id", params)
        return self._connection.GET(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [Hash] subnet
    #   allowed keys are:
    #   * dhcp_id [String]  dhcp proxy to use within this subnet 
    #   * dns_id [String]  dns proxy to use within this subnet 
    #   * domain_ids [String]  domains in which this subnet is part 
    #   * tftp_id [String]  tftp proxy to use within this subnet 
    #   * dns_primary [String]  primary dns for this subnet 
    #   * dns_secondary [String]  secondary dns for this subnet 
    #   * from [String]  starting ip address for ip auto suggestion 
    #   * gateway [String]  primary dns for this subnet 
    #   * mask [String]  netmask for this subnet 
    #   * name [String]  subnet name 
    #   * network [String]  subnet network 
    #   * to [String]  ending ip address for ip auto suggestion 
    #   * vlanid [String]  vlan id for this subnet 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def create(self, params = {}):
        url = Subnet.fill_params_in_url("/api/subnets", params)
        return self._connection.POST(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id  subnet numeric identifier 
    # @option params [Hash] subnet
    #   allowed keys are:
    #   * dhcp_id [String, nil]  dhcp proxy to use within this subnet 
    #   * dns_id [String, nil]  dns proxy to use within this subnet 
    #   * domain_ids [String, nil]  domains in which this subnet is part 
    #   * tftp_id [String, nil]  tftp proxy to use within this subnet 
    #   * dns_primary [String, nil]  primary dns for this subnet 
    #   * dns_secondary [String, nil]  secondary dns for this subnet 
    #   * from [String, nil]  starting ip address for ip auto suggestion 
    #   * gateway [String, nil]  primary dns for this subnet 
    #   * mask [String]  netmask for this subnet 
    #   * name [String]  subnet name 
    #   * network [String]  subnet network 
    #   * to [String, nil]  ending ip address for ip auto suggestion 
    #   * vlanid [String, nil]  vlan id for this subnet 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def update(self, params = {}):
        url = Subnet.fill_params_in_url("/api/subnets/:id", params)
        return self._connection.PUT(url, params)

    # @param [Hash] params a hash of params to be passed to the service
    # @option params [String] id  subnet numeric identifier 
    #
    # @param [Hash] headers additional http headers
    # @return [Array] First item: parsed data; second item: raw body
    def destroy(self, params = {}):
        url = Subnet.fill_params_in_url("/api/subnets/:id", params)
        return self._connection.DELETE(url, params)
