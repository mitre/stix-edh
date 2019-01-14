# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
import json

from mixbox.vendor.six import StringIO

import stix
from stix.core import STIXPackage

import stix_edh

# All of the examples in this file should be valid STIX 1.1.1 and STIX 1.2,
# so we just modify the XML based on the version of python-stix installed.
if stix.__version__ >= "1.2.0.0":
    stix_version = "1.2"
else:
    stix_version = "1.1.1"

XML_GLOBAL = """
<stix:STIX_Package
    xmlns:marking="http://data-marking.mitre.org/Marking-1"
    xmlns:indicator="http://stix.mitre.org/Indicator-2"
    xmlns:stix="http://stix.mitre.org/stix-1"
    xmlns:ns1="http://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsType.v2.xsd"
    xmlns:ns2="urn:edm:edh:cyber:v3"
    xmlns:ns3="http://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsAssertionsType.v2.xsd"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    id="example:Package-88139233-3c7d-4913-bb5e-d2aeb079d029" version="{0}">
    <stix:STIX_Header>
        <stix:Handling>
            <marking:Marking>
                <marking:Controlled_Structure>//node() | //@*</marking:Controlled_Structure>
                <marking:Marking_Structure isam_version="2.0" xsi:type="ns1:ISAMarkingsType">
                    <ns1:Identifier>example:foo</ns1:Identifier>
                    <ns1:CreateDateTime>2015-03-06T14:35:23.375304+00:00</ns1:CreateDateTime>
                    <ns1:ResponsibleEntity>foo bar</ns1:ResponsibleEntity>
                    <ns1:AuthRef>test auth ref</ns1:AuthRef>
                </marking:Marking_Structure>
                <marking:Marking_Structure most_restrictive="false" default_marking="false" isam_version="2.0" xsi:type="ns3:ISAMarkingsAssertionType">
                    <ns2:PolicyRef>Test policy ref</ns2:PolicyRef>
                    <ns2:AuthRef>Test auth ref</ns2:AuthRef>
                    <ns2:AccessPrivilege>
                        <ns2:privilegeAction>privilege</ns2:privilegeAction>
                        <ns2:privilegeScope>privilege scope</ns2:privilegeScope>
                        <ns2:privilegeScope>another privilege scope</ns2:privilegeScope>
                        <ns2:ruleEffect>permit</ns2:ruleEffect>
                    </ns2:AccessPrivilege>
                    <ns2:FurtherSharing>
                        <ns2:sharingScope>privilege</ns2:sharingScope>
                        <ns2:ruleEffect>permit</ns2:ruleEffect>
                    </ns2:FurtherSharing>
                    <ns2:ResourceDisposition>
                        <ns2:dispositionDate>2015-03-12</ns2:dispositionDate>
                        <ns2:dispositionProcess>test</ns2:dispositionProcess>
                    </ns2:ResourceDisposition>
                    <ns2:ControlSet>foo bar</ns2:ControlSet>
                    <ns2:OriginalClassification>
                        <ns2:classifiedBy>foobar</ns2:classifiedBy>
                        <ns2:classifiedOn>2015-03-12</ns2:classifiedOn>
                        <ns2:classificationReason>foo bar</ns2:classificationReason>
                        <ns2:compilationReason>test TEST</ns2:compilationReason>
                    </ns2:OriginalClassification>
                    <ns2:DerivativeClassification>
                        <ns2:classifiedBy>TEST</ns2:classifiedBy>
                        <ns2:classifiedOn>2015-03-12</ns2:classifiedOn>
                        <ns2:derivedFrom>foo bar</ns2:derivedFrom>
                    </ns2:DerivativeClassification>
                    <ns2:Declassification>
                        <ns2:declassExemption>test</ns2:declassExemption>
                        <ns2:declassPeriod>1</ns2:declassPeriod>
                        <ns2:declassDate>2015-03-12</ns2:declassDate>
                        <ns2:declassEvent>foobar</ns2:declassEvent>
                    </ns2:Declassification>
                    <ns2:PublicRelease>
                        <ns2:releasedBy>foobar</ns2:releasedBy>
                        <ns2:releasedOn>2015-03-12</ns2:releasedOn>
                    </ns2:PublicRelease>
                    <ns3:AddlReference>
                        <ns3:URL>http://example.com/</ns3:URL>
                        <ns3:Comment>A comment</ns3:Comment>
                    </ns3:AddlReference>
                </marking:Marking_Structure>
            </marking:Marking>
        </stix:Handling>
    </stix:STIX_Header>
    <stix:Indicators>
        <stix:Indicator id="example:indicator1" timestamp="2015-02-26T21:00:37.454000+00:00" xsi:type='indicator:IndicatorType'>
            <indicator:Title>Indicator 1</indicator:Title>
            <indicator:Description>A Description for Indicator 1</indicator:Description>
        </stix:Indicator>
    </stix:Indicators>
</stix:STIX_Package>
""".format(stix_version)


class ISAMarkingsTests(unittest.TestCase):

    def test_all_versions_in_single_package(self):
        package = STIXPackage.from_xml(StringIO(XML_GLOBAL))

        self.assertTrue(isinstance(package.stix_header.handling[0].marking_structures[0], stix_edh.isa_markings.ISAMarkings))
        self.assertTrue(isinstance(package.stix_header.handling[0].marking_structures[1], stix_edh.isa_markings_assertions.ISAMarkingsAssertion))

        print(package.to_xml())

        package = STIXPackage.from_dict(package.to_dict())

        self.assertTrue(isinstance(package.stix_header.handling[0].marking_structures[0], stix_edh.isa_markings.ISAMarkings))
        self.assertTrue(isinstance(package.stix_header.handling[0].marking_structures[1], stix_edh.isa_markings_assertions.ISAMarkingsAssertion))

        json_string = json.dumps(package.to_dict())

        print(json_string)
        print("-" * 40)
