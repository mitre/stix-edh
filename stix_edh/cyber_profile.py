# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields
import stix
import stix.utils

# internal
from stix_edh import utils
from stix_edh.bindings import cyber_profile


def validate_token(instance, value):
    """Validate xsd:NMTOKEN string"""
    if value is not None:
        if stix.utils.is_sequence(value):
            error = ("Value '{value}' for instance {instance.__class__} is not permitted."
                     "Only a single token (string) is permitted.")
            error = error.format(**locals())
            raise TypeError(error)
        elif utils.strip_whitespace(value) != value:
            error = "Input value '{value}' cannot contain whitespace for instance {instance.__class__}!"
            error = error.format(**locals())
            raise TypeError(error)


def validate_enum_token(instance, value):
    """Validate xsd:NMTOKEN that contain an enumeration constraint."""
    if value is not None:
        if hasattr(instance, "_ALLOWED_VALUES"):
            allowed = instance._ALLOWED_VALUES
            if value not in allowed:
                error = "Value for enum {instance.__class__} must be one of {allowed}. Received '{value}'"
                error = error.format(**locals())
                raise ValueError(error)
        elif stix.utils.is_sequence(value):
            error = ("Value '{value}' for instance {instance.__class__} is not permitted."
                     "Only a single token (string) is permitted.")
            error = error.format(**locals())
            raise TypeError(error)
        elif utils.strip_whitespace(value) != value:
            error = "Input value '{value}' cannot contain whitespace for instance {instance.__class__}!"
            error = error.format(**locals())
            raise TypeError(error)


class AccessPrivilege(stix.Entity):
    _binding = cyber_profile
    _binding_class = _binding.AccessPrivilegeType
    _namespace = 'urn:edm:edh:cyber:v3'
    _ALLOWED_VALUES = ('permit', 'deny')

    privilege_action = fields.TypedField("privilegeAction", key_name="privilege_action", preset_hook=validate_token)
    privilege_scope = fields.TypedField("privilegeScope", type_="stix_edh.common.NMTokens", multiple=True, key_name="privilege_scope")
    rule_effect = fields.TypedField("ruleEffect", key_name="rule_effect", preset_hook=validate_enum_token)

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
    disposition_process = fields.TypedField("dispositionProcess", key_name="disposition_process", preset_hook=validate_token)

    def __init__(self):
        super(ResourceDisposition, self).__init__()


class OriginalClassification(stix.Entity):
    _binding = cyber_profile
    _binding_class = _binding.OriginalClassificationType
    _namespace = 'urn:edm:edh:cyber:v3'

    classified_by = fields.TypedField("classifiedBy", key_name="classified_by", preset_hook=validate_token)
    classified_on = fields.DateField("classifiedOn", key_name="classified_on")
    classification_reason = fields.TypedField("classificationReason", type_="stix_edh.common.NMTokens", key_name="classification_reason")
    compilation_reason = fields.TypedField("compilationReason", type_="stix_edh.common.NMTokens", key_name="compilation_reason")

    def __init__(self):
        super(OriginalClassification, self).__init__()


class DerivativeClassification(stix.Entity):
    _binding = cyber_profile
    _binding_class = _binding.DerivativeClassificationType
    _namespace = 'urn:edm:edh:cyber:v3'

    classified_by = fields.TypedField("classifiedBy", key_name="classified_by", preset_hook=validate_token)
    classified_on = fields.DateField("classifiedOn", key_name="classified_on")
    derived_from = fields.TypedField("derivedFrom", type_="stix_edh.common.NMTokens", key_name="derived_from")

    def __init__(self):
        super(DerivativeClassification, self).__init__()


class FurtherSharing(stix.Entity):
    _binding = cyber_profile
    _binding_class = _binding.FurtherSharingType
    _namespace = 'urn:edm:edh:cyber:v3'
    _ALLOWED_VALUES = ('permit', 'deny')

    rule_effect = fields.TypedField("ruleEffect", key_name="rule_effect", preset_hook=validate_enum_token)
    sharing_scope = fields.TypedField("sharingScope", key_name="sharing_scope", type_="stix_edh.common.NMTokens", multiple=True)

    def __init__(self):
        super(FurtherSharing, self).__init__()


class Declassification(stix.Entity):
    _binding = cyber_profile
    _binding_class = _binding.DeclassificationType
    _namespace = 'urn:edm:edh:cyber:v3'

    declass_exemption = fields.TypedField("declassExemption", key_name="declass_exemption", preset_hook=validate_token)
    declass_period = fields.IntegerField("declassPeriod", key_name="declass_period")
    declass_date = fields.DateField("declassDate", key_name="declass_date")
    declass_event = fields.TypedField("declassEvent", key_name="declass_event", preset_hook=validate_token)

    def __init__(self):
        super(Declassification, self).__init__()


class PublicRelease(stix.Entity):
    _binding = cyber_profile
    _binding_class = _binding.PublicReleaseType
    _namespace = 'urn:edm:edh:cyber:v3'

    released_by = fields.TypedField("releasedBy", key_name="released_by", preset_hook=validate_token)
    released_on = fields.DateField("releasedOn", key_name="released_on")

    def __init__(self):
        super(PublicRelease, self).__init__()
