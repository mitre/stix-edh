#!/usr/bin/env python

# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import print_function

# python-stix
from stix.utils import dates
from stix.core import STIXPackage, STIXHeader
from stix.data_marking import Marking, MarkingSpecification

# stix-edh
from stix_edh.v1.isa_markings import ISAMarkings


def main():
    # Make the ISA Markings structure
    isa = ISAMarkings()
    isa.create_date_time = dates.now()
    isa.identifier = "this:is:a:test"

    # Wire up the STIX marking types
    marking_spec = MarkingSpecification()
    marking_spec.controlled_structure = "//node | //@*"
    marking_spec.marking_structures.append(isa)  # Add the ISA marking structure

    handling = Marking()
    handling.marking.append(marking_spec)

    # Create the STIX Package and add our data markings to the handling section.
    package = STIXPackage()
    package.stix_header = STIXHeader(title="ISA Markings Test")
    package.stix_header.handling = handling

    print(package.to_xml(include_schemalocs=True))

if __name__ == '__main__':
    main()
