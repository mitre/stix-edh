# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# python-stix
import stix

from mixbox import fields

# internal bindings
from stix_edh.bindings import cyber_profile


class AccessPrivilege(stix.Entity):
    _binding = cyber_profile
    _binding_class = _binding.AccessPrivilegeType
    _namespace = 'urn:edm:edh:cyber:v3'

    privilege_action = fields.TypedField("privilegeAction", type_="stix_edh.common.NMTokens", key_name="privilege_action")
    privilege_scope = fields.TypedField("privilegeScope", type_="stix_edh.common.NMTokens", multiple=True, key_name="privilege_scope")
    rule_effect = fields.TypedField("ruleEffect", type_="stix_edh.common.NMTokens", key_name="rule_effect")

    def __init__(self):
        super(AccessPrivilege, self).__init__()

    def add_privilege_scope(self, value):
        from stix_edh import common

        if not value:
            return

        nmtokens = common.NMTokens(value)
        self.privilege_scope.append(nmtokens)


class ResourceDisposition(stix.Entity):
    _binding = cyber_profile
    _binding_class = _binding.ResourceDispositionType
    _namespace = 'urn:edm:edh:cyber:v3'

    disposition_date = fields.DateField("dispositionDate", key_name="disposition_date")
    disposition_process = fields.TypedField("dispositionProcess", type_="stix_edh.common.NMTokens", key_name="disposition_process")

    def __init__(self):
        super(ResourceDisposition, self).__init__()


class OriginalClassification(stix.Entity):
    _binding = cyber_profile
    _binding_class = _binding.OriginalClassificationType
    _namespace = 'urn:edm:edh:cyber:v3'

    classified_by = fields.TypedField("classifiedBy", type_="stix_edh.common.NMTokens", key_name="classified_by")
    classified_on = fields.DateField("classifiedOn", key_name="classified_on")
    classification_reason = fields.TypedField("classificationReason", type_="stix_edh.common.NMTokens", key_name="classification_reason")
    compilation_reason = fields.TypedField("compilationReason", type_="stix_edh.common.NMTokens", key_name="compilation_reason")

    def __init__(self):
        super(OriginalClassification, self).__init__()


class DerivativeClassification(stix.Entity):
    _binding = cyber_profile
    _binding_class = _binding.DerivativeClassificationType
    _namespace = 'urn:edm:edh:cyber:v3'

    classified_by = fields.TypedField("classifiedBy", type_="stix_edh.common.NMTokens", key_name="classified_by")
    classified_on = fields.DateField("classifiedOn", key_name="classified_on")
    derived_from = fields.TypedField("derivedFrom", type_="stix_edh.common.NMTokens", key_name="derived_from")

    def __init__(self):
        super(DerivativeClassification, self).__init__()


class FurtherSharing(stix.Entity):
    _binding = cyber_profile
    _binding_class = _binding.FurtherSharingType
    _namespace = "urn:edm:edh:cyber:v3"

    rule_effect = fields.TypedField("ruleEffect", key_name="rule_effect")
    sharing_scope = fields.TypedField("sharingScope", type_="stix_edh.common.NMTokens", key_name="sharing_scope")

    def __init__(self):
        super(FurtherSharing, self).__init__()


class Declassification(stix.Entity):
    _binding = cyber_profile
    _binding_class = _binding.DeclassificationType
    _namespace = 'urn:edm:edh:cyber:v3'

    declass_exemption = fields.TypedField("declassExemption", type_="stix_edh.common.NMTokens", key_name="declass_exemption")
    declass_period = fields.IntegerField("declassPeriod", key_name="declass_period")
    declass_date = fields.DateField("declassDate", key_name="declass_date")
    declass_event = fields.TypedField("declassEvent", type_="stix_edh.common.NMTokens", key_name="declass_event")

    def __init__(self):
        super(Declassification, self).__init__()


class PublicRelease(stix.Entity):
    _binding = cyber_profile
    _binding_class = _binding.PublicReleaseType
    _namespace = 'urn:edm:edh:cyber:v3'

    released_by = fields.TypedField("releasedBy", type_="stix_edh.common.NMTokens", key_name="released_by")
    released_on = fields.DateField("releasedOn", key_name="released_on")

    def __init__(self):
        super(PublicRelease, self).__init__()
