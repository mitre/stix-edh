stix-edh
========

An extension to python-stix supporting STIX Data Markings for the `Enhance
Shared Situational Awareness (ESSA) <https://www.us-cert.gov/essa>`_
Initiative's Information Sharing Architecture (ISA) Access Control Specification
(ACS), which are based on the US Intelligence Community's Enterprise Data Header
(EDH) specification.

About the version numbers
-------------------------

There are two versions of the ISA Marking extensions for STIX. Both are included
in separate subpackages within ``stix_edh``.

1. **Version 1.0** (``stix_edh.v1``), published February 26, 2015:

   - https://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsType.xsd
   - https://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsAssertionsType.xsd
   - https://www.us-cert.gov/sites/default/files/STIX_Namespace/SD-EDH_Profile_Cyber.xsd

   Note that this uses version **2.0** of the Smart Data EDH Cyber Profile, and
   corresponds to ACS Version 2.0.

2. **Version 2.0** (``stix_edh.v2``), published January 19, 2016:

   - https://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsType.v2.xsd
   - https://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsAssertionsType.v2.xsd
   - https://www.us-cert.gov/sites/default/files/STIX_Namespace/SD-EDH_Profile_Cyber.v3.xsd

   Note that this uses version **3.0** of the Smart Data EDH Cyber Profile, and
   corresponds to ACS Version 3.0.

The ``stix-edh`` library itself uses `semantic versioning <http://semver.org/>`_,
and the version numbers are unrelated to the versions of EDH, ACS, or ISA.

Usage
-----

To parse XML using with EDH data markings, just ``import stix_edh`` **after**
``import stix``.

.. code:: python

    import stix
    import stix_edh  # automatically registers extensions with python-stix

    # Go on to parse your stix package
    from stix.core import STIXPackage
    package = STIXPackage.from_xml('stix.xml')


To create data markings, create an instance of ``ISAMarkings`` or
``ISAMarkingsAssertions`` from either the ``stix_edh.v1`` or ``stix_edh.v2``
package, and add it to a   ``MarkingSpecification`` object as a
``MarkingStructure``. See ``examples/create-isa.py`` in the source repository
for more information.

Requirements
------------

* Python 2.6, 2.7, or 3.3+
* python-stix
  * for STIX 1.1.1:  >= 1.1.1.8 and < 1.2.0.0
  * for STIX 1.2:  >= 1.2.0.3
* mixbox > 1.0.1


Notice
------

This software was produced for the U. S. Government, and is subject to the
Rights in Data-General Clause 52.227-14, Alt. IV (DEC 2007).

Copyright (c) 2017, The MITRE Corporation. All Rights Reserved.
