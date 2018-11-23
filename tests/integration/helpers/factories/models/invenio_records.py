# -*- coding: utf-8 -*-
#
# This file is part of INSPIRE.
# Copyright (C) 2014-2018 CERN.
#
# INSPIRE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# INSPIRE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with INSPIRE. If not, see <http://www.gnu.org/licenses/>.
#
# In applying this license, CERN does not waive the privileges and immunities
# granted to it by virtue of its status as an Intergovernmental Organization
# or submit itself to any jurisdiction.

"""INSPIRE module that adds more fun to the platform."""

from __future__ import absolute_import, division, print_function

import random
import factory
import pytest

from invenio_records.models import RecordMetadata

from helpers.factories.models.base import BaseFactory
from helpers.providers.faker import faker


class RecordMetadataFactory(BaseFactory):
    class Meta:
        model = RecordMetadata

    @classmethod
    def _adjust_kwargs(cls, **kwargs):
        data = kwargs.pop("data", None)
        if data:
            kwargs["json"].update(data)
        return kwargs

    json = factory.Dict(faker.record(with_control_number=True))
