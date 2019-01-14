# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


#
# Generated Tue Mar 10 10:17:55 2015 by generateDS.py version 2.9a.
#

# external
from mixbox.binding_utils import *

# internal
from stix_edh import utils

XML_NS = "http://www.w3.org/2001/XMLSchema"

#
# Data representation classes.
#


class NMTOKENS(GeneratedsSuper):
    subclass = None
    superclass = None

    def __init__(self, valueOf_=None):
        if valueOf_ is None:
            self.valueOf_ = []
        else:
            self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if NMTOKENS.subclass:
            return NMTOKENS.subclass(*args_, **kwargs_)
        else:
            return NMTOKENS(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def add_valueOf_(self, value): self.valueOf_.append(value)
    def insert_valueOf_(self, index, value): self.valueOf_[index] = value
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='NMTOKENS', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '',))
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(utils.nmtokens_serialize(self.valueOf_)))
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_=XML_NS, name_='NMTOKENS'):
        pass
    def exportChildren(self, lwrite, level, namespace_=XML_NS, name_='NMTOKENS', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        self.__sourcenode__ = node
        self.valueOf_ = utils.nmtokens_parse(get_all_text_(node))
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class NMTOKENS
