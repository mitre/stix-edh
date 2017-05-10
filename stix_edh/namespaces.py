# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox.namespaces import Namespace
import itertools


ISA_V1_NAMESPACES = [
    # ISA v1/EDH v2
    Namespace('http://www.us-cert.gov/essa/Markings/ISAMarkingAssertions', 'isam-assert-v1', 'http://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsAssertionsType.xsd'),
    Namespace('http://www.us-cert.gov/essa/Markings/ISAMarkings', 'isam-v1', 'http://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsType.xsd'),
    Namespace('urn:edm:edh:v2', 'edh-v2', 'http://www.us-cert.gov/sites/default/files/STIX_Namespace/SD-EDH_Profile_Cyber.xsd')
]

ISA_V2_NAMESPACES = [
    # ISA v2/EDH v3
    Namespace('http://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsAssertionsType.v2.xsd', 'isam-assert-v2', 'http://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsAssertionsType.v2.xsd'),
    Namespace('http://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsType.v2.xsd', 'isam-v2', 'http://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsType.v2.xsd'),
    Namespace('urn:edm:edh:cyber:v3', 'edh-v3', 'http://www.us-cert.gov/sites/default/files/STIX_Namespace/SD-EDH_Profile_Cyber.v3.xsd')
]

ALL_ISA_NAMESPACES = itertools.chain(
    ISA_V1_NAMESPACES,
    ISA_V2_NAMESPACES
)
