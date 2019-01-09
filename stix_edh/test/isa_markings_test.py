# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
from stix.test import EntityTestCase
from stix_edh.isa_markings import ISAMarkings


class ISAMarkingsTests(EntityTestCase, unittest.TestCase):
    klass = ISAMarkings

    _full_dict = {
        'isam_version': '2.0',
        'identifier': 'example:foo',
        'create_date_time': '2015-03-06T14:35:23.375304+00:00',
        'responsible_entity': {'value': ['foo', 'bar']},
        'auth_ref': 'test auth ref',
        'xsi:type': 'isam-v2:ISAMarkingsType'
    }
