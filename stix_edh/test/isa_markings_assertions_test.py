# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import unittest

# external
from stix.test import EntityTestCase

# internal
from stix_edh.test import cyber_profile_test
from stix_edh.isa_markings_assertions import ISAMarkingsAssertion, AddlReference


class AddlReferenceTests(EntityTestCase, unittest.TestCase):
    klass = AddlReference

    _full_dict = {
        'url': 'http://example.com/',
        'comment': 'A comment'
    }


class ISAMarkingsAssertionsTests(EntityTestCase, unittest.TestCase):
    klass = ISAMarkingsAssertion

    _full_dict = {
        'isam_version': '2.0',
        'policy_ref': 'Test policy ref',
        'auth_ref': 'Test auth ref',
        'access_privilege': [
            cyber_profile_test.AccessPrivilegeTests._full_dict
        ],
        'further_sharing': [
            cyber_profile_test.FurtherSharingTests._full_dict
        ],
        'resource_disposition': cyber_profile_test.ResourceDispositionTests._full_dict,
        'control_set': {'value': [u'foo', u'bar']},
        'original_classification': cyber_profile_test.OriginalClassificationTests._full_dict,
        'default_marking': False,
        'most_restrictive': False,
        'derivative_classification': cyber_profile_test.DerivativeClassificationTests._full_dict,
        'declassification': cyber_profile_test.DeclassificationTests._full_dict,
        'public_release': cyber_profile_test.PublicReleaseTests._full_dict,
        'addl_reference': AddlReferenceTests._full_dict,
        'xsi:type': 'isam-assert-v2:ISAMarkingsAssertionType'
    }
