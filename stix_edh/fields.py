# Copyright (c) 2019, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# This is an auto-generated file.
# stix_edh	-	1.0.1

__date__ = "2019-01-14 12:15:31.667000"


# Maps Python instance attribute names to XML instance field names for
# Python API classes.
ISA_FIELDS = {
    "stix_edh.common.NMTokens": {
        "value": "text()",
    },
    "stix_edh.cyber_profile.AccessPrivilege": {
        "privilege_action": "privilegeAction",
        "privilege_scope": "privilegeScope",
        "rule_effect": "ruleEffect",
    },
    "stix_edh.cyber_profile.Declassification": {
        "declass_date": "declassDate",
        "declass_event": "declassEvent",
        "declass_exemption": "declassExemption",
        "declass_period": "declassPeriod",
    },
    "stix_edh.cyber_profile.DerivativeClassification": {
        "classified_by": "classifiedBy",
        "classified_on": "classifiedOn",
        "derived_from": "derivedFrom",
    },
    "stix_edh.cyber_profile.FurtherSharing": {
        "rule_effect": "ruleEffect",
        "sharing_scope": "sharingScope",
    },
    "stix_edh.cyber_profile.OriginalClassification": {
        "classification_reason": "classificationReason",
        "classified_by": "classifiedBy",
        "classified_on": "classifiedOn",
        "compilation_reason": "compilationReason",
    },
    "stix_edh.cyber_profile.PublicRelease": {
        "released_by": "releasedBy",
        "released_on": "releasedOn",
    },
    "stix_edh.cyber_profile.ResourceDisposition": {
        "disposition_date": "dispositionDate",
        "disposition_process": "dispositionProcess",
    },
    "stix_edh.isa_markings.ISAMarkings": {
        "auth_ref": "AuthRef",
        "create_date_time": "CreateDateTime",
        "id_": "@id",
        "identifier": "Identifier",
        "idref": "@idref",
        "isam_version": "@isam_version",
        "marking_model_name": "@marking_model_name",
        "marking_model_ref": "@marking_model_ref",
        "responsible_entity": "ResponsibleEntity",
    },
    "stix_edh.isa_markings_assertions.AddlReference": {
        "comment": "Comment",
        "url": "URL",
    },
    "stix_edh.isa_markings_assertions.ISAMarkingsAssertion": {
        "access_privilege": "AccessPrivilege",
        "addl_reference": "AddlReference",
        "auth_ref": "AuthRef",
        "control_set": "ControlSet",
        "declassification": "Declassification",
        "default_marking": "@default_marking",
        "derivative_classification": "DerivativeClassification",
        "further_sharing": "FurtherSharing",
        "id_": "@id",
        "idref": "@idref",
        "isam_version": "@isam_version",
        "marking_model_name": "@marking_model_name",
        "marking_model_ref": "@marking_model_ref",
        "most_restrictive": "@most_restrictive",
        "original_classification": "OriginalClassification",
        "policy_ref": "PolicyRef",
        "public_release": "PublicRelease",
        "resource_disposition": "ResourceDisposition",
    },
}
