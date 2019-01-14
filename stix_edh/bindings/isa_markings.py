# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#
# Generated Mon Feb 23 13:51:21 2015 by generateDS.py version 2.9a.
#

# external
from mixbox.binding_utils import *
from stix.bindings import register_extension
from stix.bindings import data_marking as dm

# internal
from stix_edh.bindings import edh_common

XML_NS = "http://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsType.v2.xsd"

#
# Data representation classes.
#


@register_extension
class ISAMarkingsType(dm.MarkingStructureType):
    """ISA Marking Version 2.0"""

    xmlns          = XML_NS
    xmlns_prefix   = "isam-v2"
    xml_type       = "ISAMarkingsType"
    xsi_type       = "%s:%s" % (xmlns_prefix, xml_type)

    subclass = None
    superclass = dm.MarkingStructureType

    def __init__(self, idref=None, marking_model_ref=None, marking_model_name=None, id=None, isam_version=None, Identifier=None, CreateDateTime=None, ResponsibleEntity=None, AuthRef=None):
        super(ISAMarkingsType, self).__init__(idref, marking_model_ref, marking_model_name, id)
        self.isam_version = _cast(None, isam_version)
        self.Identifier = Identifier
        self.CreateDateTime = CreateDateTime
        self.ResponsibleEntity = ResponsibleEntity
        self.AuthRef = AuthRef
    def factory(*args_, **kwargs_):
        if ISAMarkingsType.subclass:
            return ISAMarkingsType.subclass(*args_, **kwargs_)
        else:
            return ISAMarkingsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Identifier(self): return self.Identifier
    def set_Identifier(self, Identifier): self.Identifier = Identifier
    def get_CreateDateTime(self): return self.CreateDateTime
    def set_CreateDateTime(self, CreateDateTime): self.CreateDateTime = CreateDateTime
    def get_ResponsibleEntity(self): return self.ResponsibleEntity
    def set_ResponsibleEntity(self, ResponsibleEntity): self.ResponsibleEntity = ResponsibleEntity
    def get_AuthRef(self): return self.AuthRef
    def set_AuthRef(self, AuthRef): self.AuthRef = AuthRef
    def get_isam_version(self): return self.isam_version
    def set_isam_version(self, isam_version): self.isam_version = isam_version
    def hasContent_(self):
        if (
            self.Identifier is not None or
            self.CreateDateTime is not None or
            self.ResponsibleEntity is not None or
            self.AuthRef is not None or
            super(ISAMarkingsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ISAMarkingsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ISAMarkingsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='ISAMarkingsType'):
        super(ISAMarkingsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ISAMarkingsType')
        if self.isam_version is not None and 'isam_version' not in already_processed:
            already_processed.add('isam_version')
            lwrite(' isam_version="%s"' % self.isam_version)
        if 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            lwrite(' xsi:type="%s"' % self.xsi_type)
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ISAMarkingsType', fromsubclass_=False, pretty_print=True):
        super(ISAMarkingsType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Identifier is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Identifier>%s</%s:Identifier>%s' % (nsmap[namespace_], quote_xml(self.Identifier), nsmap[namespace_], eol_))
        if self.CreateDateTime is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:CreateDateTime>%s</%s:CreateDateTime>%s' % (nsmap[namespace_], quote_xml(self.CreateDateTime), nsmap[namespace_], eol_))
        if self.ResponsibleEntity is not None:
            self.ResponsibleEntity.export(lwrite, level, nsmap, namespace_, name_='ResponsibleEntity', pretty_print=pretty_print)
        if self.AuthRef is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:AuthRef>%s</%s:AuthRef>%s' % (nsmap[namespace_], quote_xml(self.AuthRef), nsmap[namespace_], eol_))
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('isam_version', node)
        if value is not None and 'isam_version' not in already_processed:
            already_processed.add('isam_version')
            self.isam_version = value
        super(ISAMarkingsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Identifier':
            self.set_Identifier(child_.text)
        elif nodeName_ == 'CreateDateTime':
            CreateDateTime_ = child_.text
            CreateDateTime_ = self.gds_validate_string(CreateDateTime_, node, 'CreateDateTime')
            self.CreateDateTime = CreateDateTime_
        elif nodeName_ == 'ResponsibleEntity':
            self.gds_validate_string(child_.text, node, 'ResponsibleEntity')
            obj_ = edh_common.NMTOKENS.factory()
            obj_.build(child_)
            self.ResponsibleEntity = obj_
        elif nodeName_ == 'AuthRef':
            self.set_AuthRef(child_.text)
        super(ISAMarkingsType, self).buildChildren(child_, node, nodeName_, True)
# end class ISAMarkingsType


GDSClassesMapping = {}


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass


def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ISAMarkings'
        rootClass = ISAMarkingsType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_=rootTag,
    #     namespacedef_='',
    #     pretty_print=True)
    return rootObj


def parseString(inString):
    from mixbox.vendor.six import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'ISAMarkings'
        rootClass = ISAMarkingsType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="Indicator",
    #     namespacedef_='')
    return rootObj

__all__ = [
    "ISAMarkingsType",
]
