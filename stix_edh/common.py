# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import collections

# external
import stix.utils
from mixbox.vendor.six import text_type

# internal
from stix_edh import utils


class NMTokens(collections.MutableSequence):
    """Takes an xs:NMTOKENS string (a whitespace separated string of tokens)
    and converts it into a mutable sequence type.

    """
    def __init__(self, value=None):
        self._inner = []

        if not value:
            return

        values = utils.nmtokens_parse(value)
        self.extend(values)

    def insert(self, index, value):
        if not value:
            return

        if stix.utils.is_sequence(value):
            error = "Cannot insert() '{0}'. Use extend().".format(type(value))
            raise TypeError(error)
        elif utils.strip_whitespace(value) != value:
            error = "Input value cannot contain whitespace."
            raise ValueError(error)

        return self._inner.insert(index, value)

    def __delitem__(self, index):
        return self._inner.__delitem__(index)

    def __setitem__(self, index, value):
        return self._inner.__setitem__(index, value)

    def __getitem__(self, index):
        return self._inner.__getitem__(index)

    def __len__(self):
        return self._inner.__len__()

    def __unicode__(self):
        return text_type(utils.nmtokens_serialize(self._inner))

    def __str__(self):
        return text_type(self).encode("utf-8")

    def to_list(self):
        return [x for x in self]

    def to_dict(self):
        if len(self._inner) == 1:
            return self._inner[0]
        return [x for x in self]

    @classmethod
    def from_dict(cls, d):
        return NMTokens(d)
    
    def to_obj(self, ns_info=None):
        if len(self._inner) == 0:
            return None
        return utils.nmtokens_serialize(self._inner)
    
    @classmethod
    def from_obj(cls, obj):
        return NMTokens(utils.nmtokens_parse(obj))
