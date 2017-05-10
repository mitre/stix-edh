#!/usr/bin/env python

# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import print_function
import pprint

import stix
import stix_edh

from stix.core import STIXPackage

FILENAMES = ("revoked-example.xml", "smtp-example.xml")


def divider():
    print()
    print("-" * 50)
    print()


def main():
    for fn in FILENAMES:
        print("FILENAME:", fn)

        package = STIXPackage.from_xml(fn)

        print(package.to_xml())
        divider()
        pprint.pprint(package.to_dict())
        divider()

if __name__ == "__main__":
    main()
