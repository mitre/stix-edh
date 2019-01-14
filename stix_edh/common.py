# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import collections

# external
from mixbox import entities, fields
from mixbox.vendor.six import text_type
import stix.utils

# internal
from stix_edh import utils
from stix_edh.bindings import edh_common


class NMTokens(collections.MutableSequence, entities.Entity):
    """Takes an xs:NMTOKENS string (a whitespace separated string of tokens)
    and converts it into a mutable sequence type.

    """
    _binding = edh_common
    _binding_class = _binding.NMTOKENS
    _namespace = 'http://www.w3.org/2001/XMLSchema'

    value = fields.TypedField("valueOf_", key_name="value")

    def __init__(self, value=None):
        super(NMTokens, self).__init__()
        self.value = []

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

        return self.value.insert(index, value)

    def __delitem__(self, index):
        return self.value.__delitem__(index)

    def __setitem__(self, index, value):
        return self.value.__setitem__(index, value)

    def __getitem__(self, index):
        return self.value.__getitem__(index)

    def __len__(self):
        return self.value.__len__()

    def __unicode__(self):
        return utils.nmtokens_serialize(self.value)

    def __str__(self):
        return utils.nmtokens_serialize(self.value)

    def to_list(self):
        return [x for x in self]

    def to_dict(self):
        d = {}
        for x in self:
            if 'value' not in d:
                d['value'] = []
            d['value'].append(x)
        return d
