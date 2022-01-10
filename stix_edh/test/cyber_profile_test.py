# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase

from stix_edh.cyber_profile import (
    AccessPrivilege, Declassification, DerivativeClassification,
    OriginalClassification, PublicRelease, ResourceDisposition, FurtherSharing
)


class AccessPrivilegeTests(EntityTestCase, unittest.TestCase):
    klass = AccessPrivilege

    _full_dict = {
        'privilege_action': "privilege",
        'privilege_scope': [
            {'value': [u"privilege", u"scope"]},
        ],
        'rule_effect': 'permit'
    }


class FurtherSharingTests(EntityTestCase, unittest.TestCase):
    klass = FurtherSharing

    _full_dict = {
        'sharing_scope': [ {'value': [ u"privilege" ]}],
        'rule_effect': 'permit'
    }


class ResourceDispositionTests(EntityTestCase, unittest.TestCase):
    klass = ResourceDisposition

    _full_dict = {
        'disposition_date': "2015-03-12",
        'disposition_process': "test"
    }


class OriginalClassificationTests(EntityTestCase, unittest.TestCase):
    klass = OriginalClassification

    _full_dict = {
        'classified_by': 'foobar',
        'classified_on': '2015-03-12',
        'classification_reason': {'value': ['foo', 'bar']},
        'compilation_reason': {'value': [u'test', u'TEST']}
    }


class DerivativeClassificationTests(EntityTestCase, unittest.TestCase):
    klass = DerivativeClassification

    _full_dict = {
        'classified_by': 'TEST',
        'classified_on': '2015-03-12',
        'derived_from': {'value': [u'foo', u'bar']}
    }


class DeclassificationTests(EntityTestCase, unittest.TestCase):
    klass = Declassification

    _full_dict = {
        'declass_exemption': 'test',
        'declass_period': 1,
        'declass_date': '2015-03-12',
        'declass_event': 'foobar'
    }


class PublicReleaseTests(EntityTestCase, unittest.TestCase):
    klass = PublicRelease

    _full_dict = {
        'released_by': 'foobar',
        'released_on': '2015-03-12'
    }
