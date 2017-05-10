# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox.vendor.six import iteritems, string_types


def listify(item):
    """Converts `item` into a list object.

    If `item` is a list, it will be returned. If `item` is a non-string
    iterable collection, a it will be converted into a list. Otherwise, `item`
    will be wrapped in a list object.

    """
    if not item:
        return []
    elif isinstance(item, list):
        return item
    elif is_iterable(item):
        return [x for x in item]
    else:
        return [item]


def nmtokens_parse(string):
    """Parses an xs:NMTOKENS value and converts it into a list object.

    """
    if not string:
        return []
    elif is_iterable(string):
        return string
    else:
        return string.split()


def nmtokens_serialize(items):
    """Returns an xs:NMTOKENS representation of `items`.

    Args:
        items: An iterable collection of string values or a single string value.

    """
    return ' '.join(listify(items))


def obj_from_dict(obj, dictionary, **kwargs):
    """Converts a `dictionary` into a stix-edh object.

    Args:
        dictionary: A dictionary representation of a stix-edh object.
        **kwargs: A key-to-class mapping if the the corresponding value is a
            dictionary representation of a stix-edh object.

    """
    get = dictionary.get

    for key, klass in iteritems(kwargs):
        if klass:
            val = klass.from_dict(get(key))
        else:
            val = get(key)

        setattr(obj, key, val)


def strip_whitespace(string):
    """Returns a copy of `string` with its whitespace removed

    """
    return ''.join(string.split())


def is_iterable(item):
    """Returns True if `item` has an ``__iter__()`` method.

    """
    return hasattr(item, "__iter__") and not isinstance(item, string_types)
