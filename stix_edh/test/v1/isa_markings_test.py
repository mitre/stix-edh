# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase

from stix_edh.v1.isa_markings import ISAMarkings


class ISAMarkingsTests(EntityTestCase, unittest.TestCase):
    klass = ISAMarkings

    _full_dict = {
        'isam_version': '1.0',
        'identifier': 'example:foo',
        'create_date_time': '2015-03-06T14:35:23.375304+00:00',
        'responsible_entity': ['foo', 'bar'],
        'auth_ref': 'test auth ref',
        'xsi:type': 'isam-v1:ISAMarkingsType'
    }
