#!/usr/bin/env python

# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import print_function

import stix
import stix_edh
import stixmarx

from stix.utils import silence_warnings

FILE_REVOKED = "revoked-example.xml"


@silence_warnings
def main():
    container = stixmarx.parse(FILE_REVOKED)
    global_markings = container.global_markings

    for marking in global_markings:
        print(marking.to_dict())

    for indicator in container.package.indicators:
        # Get markings from Indicator or any descendants.
        markings = container.get_markings(indicator, descendants=True)
        print(indicator.id_, len(markings))
        print(markings)

if __name__ == "__main__":
    main()
