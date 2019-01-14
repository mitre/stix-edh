# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields
import stix
import stix.data_marking as dm

# internal
from stix_edh.bindings import isa_markings_assertions


@stix.register_extension
class ISAMarkingsAssertion(dm.MarkingStructure):
    _binding = isa_markings_assertions
    _binding_class = _binding.ISAMarkingsAssertionType
    _namespace = 'http://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsAssertionsType.v2.xsd'
    _XSI_TYPE = 'isam-assert-v2:ISAMarkingsAssertionType'

    isam_version = fields.TypedField("isam_version")
    most_restrictive = fields.BooleanField("most_restrictive")
    default_marking = fields.BooleanField("default_marking")
    policy_ref = fields.TypedField("PolicyRef", key_name="policy_ref")
    auth_ref = fields.TypedField("AuthRef", key_name="auth_ref")
    access_privilege = fields.TypedField("AccessPrivilege", type_="stix_edh.cyber_profile.AccessPrivilege", multiple=True, key_name="access_privilege")
    further_sharing = fields.TypedField("FurtherSharing", type_="stix_edh.cyber_profile.FurtherSharing", multiple=True, key_name="further_sharing")
    resource_disposition = fields.TypedField("ResourceDisposition", type_="stix_edh.cyber_profile.ResourceDisposition", key_name="resource_disposition")
    control_set = fields.TypedField("ControlSet", type_="stix_edh.common.NMTokens", key_name="control_set")
    original_classification = fields.TypedField("OriginalClassification", type_="stix_edh.cyber_profile.OriginalClassification", key_name="original_classification")
    derivative_classification = fields.TypedField("DerivativeClassification", type_="stix_edh.cyber_profile.DerivativeClassification", key_name="derivative_classification")
    declassification = fields.TypedField("Declassification", type_="stix_edh.cyber_profile.Declassification", key_name="declassification")
    public_release = fields.TypedField("PublicRelease", type_="stix_edh.cyber_profile.PublicRelease", key_name="public_release")
    addl_reference = fields.TypedField("AddlReference", type_="stix_edh.isa_markings_assertions.AddlReference", key_name="addl_reference")

    def __init__(self):
        super(ISAMarkingsAssertion, self).__init__()
        self.isam_version = '2.0'


class AddlReference(stix.Entity):
    _binding = isa_markings_assertions
    _binding_class = _binding.AddlReferenceType
    _namespace = 'http://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsAssertionsType.v2.xsd'

    url = fields.TypedField("URL")
    comment = fields.TypedField("Comment")

    def __init__(self, url=None, comment=None):
        super(AddlReference, self).__init__()
        self.url = url
        self.comment = comment
