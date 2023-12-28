#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2013 by Pablo Martín <goinnn@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Run the tests for django-multiselectfield."""
import os
import sys

import django
from django.conf import ENVIRONMENT_VARIABLE
from django.core import management

if len(sys.argv) == 1:
    os.environ[ENVIRONMENT_VARIABLE] = 'example.settings'
else:
    os.environ[ENVIRONMENT_VARIABLE] = sys.argv[1]

django.setup()

print(django.VERSION)

management.call_command('test', 'app')
