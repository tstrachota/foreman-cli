#
# Katello Organization actions
# Copyright 2013 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 2 (GPLv2). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv2
# along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.
#
# Red Hat trademarks are not licensed under GPLv2. No permission is
# granted to use or replicate Red Hat trademarks that are incorporated
# in this software or its documentation.
#

import os
from foreman.cli import ForemanCommand


class List(ForemanCommand):

    description = _('list all users in the system')
    name = 'list'

    def _setup_options(self):
      #self.create_option('--name', _("user's name"))
      pass

    def run(self, options):
        print self.api.user.index().body
        #self.prompt.write(users)
        self.prompt.write("XXX")
        return os.EX_OK


