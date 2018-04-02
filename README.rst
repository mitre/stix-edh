stix-edh
========

|Build_Status| |Version|

An extension to python-stix supporting STIX Data Markings for the `Enhance
Shared Situational Awareness (ESSA) <https://www.us-cert.gov/essa>`_
Initiative's Information Sharing Architecture (ISA) Access Control Specification
(ACS), which are based on the US Intelligence Community's Enterprise Data Header
(EDH) specification.

About the version numbers
-------------------------

stix-edh supports **version 2.0** of the ISA Marking extensions for STIX,
published January 19, 2016:

   - https://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsType.v2.xsd
   - https://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsAssertionsType.v2.xsd
   - https://www.us-cert.gov/sites/default/files/STIX_Namespace/SD-EDH_Profile_Cyber.v3.xsd

These schemas use version **3.0** of the Smart Data EDH Cyber Profile, and
correspond to ACS Version 3.0.

**NOTE:** stix-edh does **not** currently support version 1.0 of the ISA Marking
extensions (published February 26, 2015), which use the schemas below. Version
1.0 of the ISA Marking extensions use version **2.0** of the Smart Data EDH
Cyber Profile, and corresponds to ACS Version 2.0.

   - https://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsType.xsd
   - https://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsAssertionsType.xsd
   - https://www.us-cert.gov/sites/default/files/STIX_Namespace/SD-EDH_Profile_Cyber.xsd

The ``stix-edh`` library itself uses `semantic versioning
<http://semver.org/>`_, and the version numbers are unrelated to the versions of
EDH, ACS, or ISA.

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

To create data markings, create an instance of ``stix_edh.ISAMarkings`` or
``stix_edh.ISAMarkingsAssertions``, and add it to a ``MarkingSpecification``
object as a ``MarkingStructure``. See ``examples/create-isa.py`` in the source
repository for more information.

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

.. |Build_Status| image:: https://travis-ci.org/mitre/stix-edh.svg?branch=master
   :target: https://travis-ci.org/mitre/stix-edh
.. |Version| image:: https://img.shields.io/pypi/v/stix-edh.svg?maxAge=3600
   :target: https://pypi.python.org/pypi/stix-edh/
