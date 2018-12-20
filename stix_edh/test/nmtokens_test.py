# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from mixbox.vendor.six import text_type

from stix_edh.common import NMTokens


class NMTokensTests(unittest.TestCase):

    def test_insert_list(self):
        nmtokens = NMTokens()
        self.assertRaises(TypeError, nmtokens.append, [1, 2, 3])

    def test_insert_space_delimited(self):
        nmtokens = NMTokens()
        self.assertRaises(ValueError, nmtokens.append, "this should fail")

    def test_init_list(self):
        nmtokens = NMTokens(['a', 'b', 'c'])
        self.assertEqual(len(nmtokens), 3)

    def test_init_fail(self):
        self.assertRaises(TypeError, NMTokens, ['a', [1, 2, 3], ['b']])

    def test_string_split(self):
        nm = NMTokens(["This", "is", "a", "test"])
        self.assertEquals("This is a test", str(nm))

    def test_unicode_split(self):
        nm = NMTokens([u"This", u"is", u"a", u"test"])
        self.assertEquals(u"This is a test", text_type(nm))
