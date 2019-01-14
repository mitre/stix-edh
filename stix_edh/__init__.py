# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


def _register_stix_edh():
    # Make sure this is imported if it hasn't already been
    import stix

    # Register the EDH data marking extensions
    import stix_edh.isa_markings
    import stix_edh.isa_markings_assertions


def _update_namespaces():
    # Update the python-stix namespace dictionary
    import stix.utils.nsparser as nsparser
    import stix_edh.namespaces as namespaces
    import mixbox.namespaces

    for ns in namespaces.ISA_NAMESPACES:
        nsparser.STIX_NAMESPACES.add_namespace(ns)
        mixbox.namespaces.register_namespace(ns)


def _update_marking_fields():
    # Update the stixmarx fields to apply/resolve stix_edh objects
    try:
        import stixmarx.fields as mfields
        import stix_edh.fields as internal_fields
        mfields.update_field_mappings(internal_fields.ISA_FIELDS)
    except (ImportError, ImportWarning):
        pass


from .version import __version__  # noqa

_register_stix_edh()
_update_namespaces()
_update_marking_fields()
