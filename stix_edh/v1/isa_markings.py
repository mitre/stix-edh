# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# python-stix
import stix
import stix.data_marking as dm

# mixbox
from mixbox import fields

# relative
from stix_edh.v1.bindings import isa_markings


@stix.register_extension
class ISAMarkings(dm.MarkingStructure):
    _binding = isa_markings
    _binding_class = _binding.ISAMarkingsType
    _namespace = 'http://www.us-cert.gov/essa/Markings/ISAMarkings'
    _XSI_TYPE = 'isam-v1:ISAMarkingsType'

    isam_version = fields.TypedField("isam_version")
    identifier = fields.TypedField("Identifier", key_name="identifier")
    create_date_time = fields.DateTimeField("CreateDateTime", key_name="create_date_time")
    responsible_entity = fields.TypedField("ResponsibleEntity", type_="stix_edh.common.NMTokens", key_name="responsible_entity")
    auth_ref = fields.TypedField("AuthRef", key_name="auth_ref")

    def __init__(self):
        super(ISAMarkings, self).__init__()
        self.isam_version = '1.0'
