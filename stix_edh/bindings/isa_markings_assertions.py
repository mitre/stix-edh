# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#
# Generated Mon Feb 23 13:51:45 2015 by generateDS.py version 2.9a.
#

# external
from mixbox.binding_utils import *
from stix.bindings import register_extension
from stix.bindings import data_marking as dm

# internal
from stix_edh.bindings import cyber_profile, edh_common

XML_NS = "http://www.us-cert.gov/sites/default/files/STIX_Namespace/ISAMarkingsAssertionsType.v2.xsd"

#
# Data representation classes.
#


@register_extension
class ISAMarkingsAssertionType(dm.MarkingStructureType):
    """Indicates whether or not this marking structure denotes the most
    restrictive applied to this structure. Only used in STIX header.
    Can only be used if the Controlled_Structure is set to
    //node() Indicates that this is the default marking for this STIX
    document; only used in STIX header. Can only be used if the
    Controlled_Structure is set to //node() ISA Marking Version.

    """
    xmlns = XML_NS
    xmlns_prefix   = "isam-assert-v2"
    xml_type       = "ISAMarkingsAssertionType"
    xsi_type       = "%s:%s" % (xmlns_prefix, xml_type)

    subclass = None
    superclass = dm.MarkingStructureType

    def __init__(self, idref=None, marking_model_ref=None, marking_model_name=None, id=None, most_restrictive=False, default_marking=False, isam_version=None, PolicyRef=None, AuthRef=None, AccessPrivilege=None, FurtherSharing=None, ResourceDisposition=None, ControlSet=None, OriginalClassification=None, DerivativeClassification=None, Declassification=None, PublicRelease=None, AddlReference=None):
        super(ISAMarkingsAssertionType, self).__init__(idref, marking_model_ref, marking_model_name, id)
        self.most_restrictive = _cast(bool, most_restrictive)
        self.default_marking = _cast(bool, default_marking)
        self.isam_version = _cast(None, isam_version)
        self.PolicyRef = PolicyRef
        self.AuthRef = AuthRef
        if AccessPrivilege is None:
            self.AccessPrivilege = []
        else:
            self.AccessPrivilege = AccessPrivilege
        if FurtherSharing is None:
            self.FurtherSharing = []
        else:
            self.FurtherSharing = FurtherSharing
        self.ResourceDisposition = ResourceDisposition
        self.ControlSet = ControlSet
        self.OriginalClassification = OriginalClassification
        self.DerivativeClassification = DerivativeClassification
        self.Declassification = Declassification
        self.PublicRelease = PublicRelease
        self.AddlReference = AddlReference
    def factory(*args_, **kwargs_):
        if ISAMarkingsAssertionType.subclass:
            return ISAMarkingsAssertionType.subclass(*args_, **kwargs_)
        else:
            return ISAMarkingsAssertionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_PolicyRef(self): return self.PolicyRef
    def set_PolicyRef(self, PolicyRef): self.PolicyRef = PolicyRef
    def get_AuthRef(self): return self.AuthRef
    def set_AuthRef(self, AuthRef): self.AuthRef = AuthRef
    def get_AccessPrivilege(self): return self.AccessPrivilege
    def set_AccessPrivilege(self, AccessPrivilege): self.AccessPrivilege = AccessPrivilege
    def add_AccessPrivilege(self, value): self.AccessPrivilege.append(value)
    def insert_AccessPrivilege(self, index, value): self.AccessPrivilege[index] = value
    def get_FurtherSharing(self): return self.FurtherSharing
    def set_FurtherSharing(self, FurtherSharing): self.FurtherSharing = FurtherSharing
    def add_FurtherSharing(self, value): self.FurtherSharing.append(value)
    def insert_FurtherSharing(self, index, value): self.FurtherSharing[index] = value
    def get_ResourceDisposition(self): return self.ResourceDisposition
    def set_ResourceDisposition(self, ResourceDisposition): self.ResourceDisposition = ResourceDisposition
    def get_ControlSet(self): return self.ControlSet
    def set_ControlSet(self, ControlSet): self.ControlSet = ControlSet
    def get_OriginalClassification(self): return self.OriginalClassification
    def set_OriginalClassification(self, OriginalClassification): self.OriginalClassification = OriginalClassification
    def get_DerivativeClassification(self): return self.DerivativeClassification
    def set_DerivativeClassification(self, DerivativeClassification): self.DerivativeClassification = DerivativeClassification
    def get_Declassification(self): return self.Declassification
    def set_Declassification(self, Declassification): self.Declassification = Declassification
    def get_PublicRelease(self): return self.PublicRelease
    def set_PublicRelease(self, PublicRelease): self.PublicRelease = PublicRelease
    def get_AddlReference(self): return self.AddlReference
    def set_AddlReference(self, AddlReference): self.AddlReference = AddlReference
    def get_most_restrictive(self): return self.most_restrictive
    def set_most_restrictive(self, most_restrictive): self.most_restrictive = most_restrictive
    def get_default_marking(self): return self.default_marking
    def set_default_marking(self, default_marking): self.default_marking = default_marking
    def get_isam_version(self): return self.isam_version
    def set_isam_version(self, isam_version): self.isam_version = isam_version
    def hasContent_(self):
        if (
            self.PolicyRef is not None or
            self.AuthRef is not None or
            self.AccessPrivilege or
            self.FurtherSharing or
            self.ResourceDisposition is not None or
            self.ControlSet is not None or
            self.OriginalClassification is not None or
            self.DerivativeClassification is not None or
            self.Declassification is not None or
            self.PublicRelease is not None or
            self.AddlReference is not None or
            super(ISAMarkingsAssertionType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ISAMarkingsAssertionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ISAMarkingsAssertionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='edh2cyberMarkingAssert:', name_='ISAMarkingsAssertionType'):
        super(ISAMarkingsAssertionType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ISAMarkingsAssertionType')
        if self.most_restrictive is not None and 'most_restrictive' not in already_processed:
            already_processed.add('most_restrictive')
            lwrite(' most_restrictive="%s"' % self.gds_format_boolean(self.most_restrictive, input_name='most_restrictive'))
        if self.default_marking is not None and 'default_marking' not in already_processed:
            already_processed.add('default_marking')
            lwrite(' default_marking="%s"' % self.gds_format_boolean(self.default_marking, input_name='default_marking'))
        if self.isam_version is not None and 'isam_version' not in already_processed:
            already_processed.add('isam_version')
            lwrite(' isam_version="%s"' % self.isam_version)
        if 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            lwrite(' xsi:type="%s"' % self.xsi_type)
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ISAMarkingsAssertionType', fromsubclass_=False, pretty_print=True):
        super(ISAMarkingsAssertionType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.PolicyRef is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:PolicyRef>%s</%s:PolicyRef>%s' % (nsmap[cyber_profile.XML_NS], quote_xml(self.PolicyRef), nsmap[cyber_profile.XML_NS], eol_))
        if self.AuthRef is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:AuthRef>%s</%s:AuthRef>%s' % (nsmap[cyber_profile.XML_NS], quote_xml(self.AuthRef), nsmap[cyber_profile.XML_NS], eol_))
        for AccessPrivilege_ in self.AccessPrivilege:
            AccessPrivilege_.export(lwrite, level, nsmap, cyber_profile.XML_NS, name_='AccessPrivilege', pretty_print=pretty_print)
        for FurtherSharing_ in self.FurtherSharing:
            FurtherSharing_.export(lwrite, level, nsmap, cyber_profile.XML_NS, name_='FurtherSharing', pretty_print=pretty_print)
        if self.ResourceDisposition is not None:
            self.ResourceDisposition.export(lwrite, level, nsmap, cyber_profile.XML_NS, name_='ResourceDisposition', pretty_print=pretty_print)
        if self.ControlSet is not None:
            self.ControlSet.export(lwrite, level, nsmap, cyber_profile.XML_NS, name_='ControlSet', pretty_print=pretty_print)
        if self.OriginalClassification is not None:
            self.OriginalClassification.export(lwrite, level, nsmap, cyber_profile.XML_NS, name_='OriginalClassification', pretty_print=pretty_print)
        if self.DerivativeClassification is not None:
            self.DerivativeClassification.export(lwrite, level, nsmap, cyber_profile.XML_NS, name_='DerivativeClassification', pretty_print=pretty_print)
        if self.Declassification is not None:
            self.Declassification.export(lwrite, level, nsmap, cyber_profile.XML_NS, name_='Declassification', pretty_print=pretty_print)
        if self.PublicRelease is not None:
            self.PublicRelease.export(lwrite, level, nsmap, cyber_profile.XML_NS, name_='PublicRelease', pretty_print=pretty_print)
        if self.AddlReference is not None:
            self.AddlReference.export(lwrite, level, nsmap, namespace_, name_='AddlReference', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('most_restrictive', node)
        if value is not None and 'most_restrictive' not in already_processed:
            already_processed.add('most_restrictive')
            if value in ('true', '1'):
                self.most_restrictive = True
            elif value in ('false', '0'):
                self.most_restrictive = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('default_marking', node)
        if value is not None and 'default_marking' not in already_processed:
            already_processed.add('default_marking')
            if value in ('true', '1'):
                self.default_marking = True
            elif value in ('false', '0'):
                self.default_marking = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('isam_version', node)
        if value is not None and 'isam_version' not in already_processed:
            already_processed.add('isam_version')
            self.isam_version = value
        super(ISAMarkingsAssertionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'PolicyRef':
            self.set_PolicyRef(child_.text)
        elif nodeName_ == 'AuthRef':
            self.set_AuthRef(child_.text)
        elif nodeName_ == 'AccessPrivilege':
            obj_ = cyber_profile.AccessPrivilegeType.factory()
            obj_.build(child_)
            self.AccessPrivilege.append(obj_)
        elif nodeName_ == 'FurtherSharing':
            obj_ = cyber_profile.FurtherSharingType.factory()
            obj_.build(child_)
            self.FurtherSharing.append(obj_)
        elif nodeName_ == 'ResourceDisposition':
            obj_ = cyber_profile.ResourceDispositionType.factory()
            obj_.build(child_)
            self.set_ResourceDisposition(obj_)
        elif nodeName_ == 'ControlSet':
            self.gds_validate_string(child_.text, node, 'ControlSet')
            obj_ = edh_common.NMTOKENS.factory()
            obj_.build(child_)
            self.ControlSet = obj_
        elif nodeName_ == 'OriginalClassification':
            obj_ = cyber_profile.OriginalClassificationType.factory()
            obj_.build(child_)
            self.set_OriginalClassification(obj_)
        elif nodeName_ == 'DerivativeClassification':
            obj_ = cyber_profile.DerivativeClassificationType.factory()
            obj_.build(child_)
            self.set_DerivativeClassification(obj_)
        elif nodeName_ == 'Declassification':
            obj_ = cyber_profile.DeclassificationType.factory()
            obj_.build(child_)
            self.set_Declassification(obj_)
        elif nodeName_ == 'PublicRelease':
            obj_ = cyber_profile.PublicReleaseType.factory()
            obj_.build(child_)
            self.set_PublicRelease(obj_)
        elif nodeName_ == 'AddlReference':
            obj_ = AddlReferenceType.factory()
            obj_.build(child_)
            self.set_AddlReference(obj_)
        super(ISAMarkingsAssertionType, self).buildChildren(child_, node, nodeName_, True)
# end class ISAMarkingsAssertionType


class AddlReferenceType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, URL=None, Comment=None):
        self.URL = URL
        self.Comment = Comment
    def factory(*args_, **kwargs_):
        if AddlReferenceType.subclass:
            return AddlReferenceType.subclass(*args_, **kwargs_)
        else:
            return AddlReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_URL(self): return self.URL
    def set_URL(self, URL): self.URL = URL
    def get_Comment(self): return self.Comment
    def set_Comment(self, Comment): self.Comment = Comment
    def hasContent_(self):
        if (
            self.URL is not None or
            self.Comment is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AddlReferenceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AddlReferenceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='edh2cyberMarkingAssert:', name_='AddlReferenceType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AddlReferenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.URL is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:URL>%s</%s:URL>%s' % (nsmap[namespace_], quote_xml(self.URL), nsmap[namespace_], eol_))
        if self.Comment is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Comment>%s</%s:Comment>%s' % (nsmap[namespace_], quote_xml(self.Comment), nsmap[namespace_], eol_))
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'URL':
            URL_ = child_.text
            URL_ = self.gds_validate_string(URL_, node, 'URL')
            self.URL = URL_
        elif nodeName_ == 'Comment':
            Comment_ = child_.text
            Comment_ = self.gds_validate_string(Comment_, node, 'Comment')
            self.Comment = Comment_
# end class AddlReferenceType

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
        rootTag = 'ISAMarkingsAssertions'
        rootClass = ISAMarkingsAssertionType
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
        rootTag = 'ISAMarkingsAssertions'
        rootClass = ISAMarkingsAssertionType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="Indicator",
    #     namespacedef_='')
    return rootObj

__all__ = [
    "ISAMarkingsAssertionType",
    "AddlReferenceType"
]
