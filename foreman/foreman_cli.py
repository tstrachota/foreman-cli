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

import os
from gettext import gettext as _

from foreman.commands import fake, user, shell

# -- framework hook -----------------------------------------------------------

def initialize(context):

    fk = context.cli.create_section('fake', _('example actions'))
    fk.add_command(fake.Example(context))

    loc = context.cli.create_section('location', _('location specific actions'))
    loc.add_command(fake.Fake(context, "create"))
    loc.add_command(fake.Fake(context, "list"))
    loc.add_command(fake.Fake(context, "update"))
    loc.add_command(fake.Fake(context, "delete"))

    usr = context.cli.create_section('user', _('user specific actions'))
    usr.add_command(user.List(context))

    context.cli.add_command(shell.Shell(context))


