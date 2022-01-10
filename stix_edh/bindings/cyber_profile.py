# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


#
# Generated Tue Mar 10 10:17:55 2015 by generateDS.py version 2.9a.
#
# Generated Thu Jan  6 18:24:41 2022 by generateDS.py version 2.9a.
#

# stdlib
import warnings as warnings_

# external
from mixbox.binding_utils import *

# internal
from stix_edh.bindings import edh_common

XML_NS = "urn:edm:edh:cyber:v3"

#
# Data representation classes.
#


class PolicyType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, PolicyRule=None):
        if PolicyRule is None:
            self.PolicyRule = []
        else:
            self.PolicyRule = PolicyRule
    def factory(*args_, **kwargs_):
        if PolicyType.subclass:
            return PolicyType.subclass(*args_, **kwargs_)
        else:
            return PolicyType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def add_PolicyRule(self, value): self.PolicyRule.append(value)
    def get_PolicyRule(self): return self.PolicyRule
    def set_PolicyRule(self, PolicyRule): self.PolicyRule = PolicyRule
    def hasContent_(self):
        if (
            self.PolicyRule
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='PolicyType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PolicyType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='PolicyType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='PolicyType', fromsubclass_=False, pretty_print=True):
        for PolicyRule_ in self.PolicyRule:
            PolicyRule_.export(lwrite, level, nsmap, namespace_, name_='PolicyRule', pretty_print=pretty_print)
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
        if nodeName_ == 'PolicyRule':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <PolicyRule> element')
            self.set_PolicyRule(obj_)
        elif nodeName_ == 'OriginalClassification':
            obj_ = OriginalClassificationType.factory()
            obj_.build(child_)
            self.set_PolicyRule(obj_)
        elif nodeName_ == 'DerivativeClassification':
            obj_ = DerivativeClassificationType.factory()
            obj_.build(child_)
            self.set_PolicyRule(obj_)
        elif nodeName_ == 'Declassification':
            obj_ = DeclassificationType.factory()
            obj_.build(child_)
            self.set_PolicyRule(obj_)
        elif nodeName_ == 'PublicRelease':
            obj_ = PublicReleaseType.factory()
            obj_.build(child_)
            self.set_PolicyRule(obj_)
        elif nodeName_ == 'ResourceDisposition':
            obj_ = ResourceDispositionType.factory()
            obj_.build(child_)
            self.set_PolicyRule(obj_)
        elif nodeName_ == 'AccessPrivilege':
            obj_ = AccessPrivilegeType.factory()
            obj_.build(child_)
            self.set_PolicyRule(obj_)
# end class PolicyType


class PolicyRuleType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, extensiontype_=None):
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if PolicyRuleType.subclass:
            return PolicyRuleType.subclass(*args_, **kwargs_)
        else:
            return PolicyRuleType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='PolicyRuleType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PolicyRuleType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='PolicyRuleType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            lwrite(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite(' xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='PolicyRuleType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class PolicyRuleType


class OriginalClassificationType(PolicyRuleType):
    subclass = None
    superclass = PolicyRuleType
    def __init__(self, classifiedBy=None, classifiedOn=None, classificationReason=None, compilationReason=None):
        super(OriginalClassificationType, self).__init__()
        self.classifiedBy = classifiedBy
        self.classifiedOn = classifiedOn
        self.classificationReason = classificationReason
        self.compilationReason = compilationReason
    def factory(*args_, **kwargs_):
        if OriginalClassificationType.subclass:
            return OriginalClassificationType.subclass(*args_, **kwargs_)
        else:
            return OriginalClassificationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_classifiedBy(self): return self.classifiedBy
    def set_classifiedBy(self, classifiedBy): self.classifiedBy = classifiedBy
    def get_classifiedOn(self): return self.classifiedOn
    def set_classifiedOn(self, classifiedOn): self.classifiedOn = classifiedOn
    def get_classificationReason(self): return self.classificationReason
    def set_classificationReason(self, classificationReason): self.classificationReason = classificationReason
    def get_compilationReason(self): return self.compilationReason
    def set_compilationReason(self, compilationReason): self.compilationReason = compilationReason
    def hasContent_(self):
        if (
            self.classifiedBy is not None or
            self.classifiedOn is not None or
            self.classificationReason is not None or
            self.compilationReason is not None or
            super(OriginalClassificationType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='OriginalClassificationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='OriginalClassificationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='OriginalClassificationType'):
        super(OriginalClassificationType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='OriginalClassificationType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='OriginalClassificationType', fromsubclass_=False, pretty_print=True):
        super(OriginalClassificationType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.classifiedBy is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:classifiedBy>%s</%s:classifiedBy>%s' % (nsmap[namespace_], quote_xml(self.classifiedBy), nsmap[namespace_], eol_))
        if self.classifiedOn is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:classifiedOn>%s</%s:classifiedOn>%s' % (nsmap[namespace_], quote_xml(self.classifiedOn), nsmap[namespace_], eol_))
        if self.classificationReason is not None:
            self.classificationReason.export(lwrite, level, nsmap, namespace_, name_='classificationReason', pretty_print=pretty_print)
        if self.compilationReason is not None:
            self.compilationReason.export(lwrite, level, nsmap, namespace_, name_='compilationReason', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(OriginalClassificationType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'classifiedBy':
            classifiedBy_ = child_.text
            classifiedBy_ = self.gds_validate_string(classifiedBy_, node, 'classifiedBy')
            self.classifiedBy = classifiedBy_
        elif nodeName_ == 'classifiedOn':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_, node, 'classifiedOn')
            self.classifiedOn = dval_
        elif nodeName_ == 'classificationReason':
            self.gds_validate_string(child_.text, node, 'classificationReason')
            obj_ = edh_common.NMTOKENS.factory()
            obj_.build(child_)
            self.classificationReason = obj_
        elif nodeName_ == 'compilationReason':
            self.gds_validate_string(child_.text, node, 'compilationReason')
            obj_ = edh_common.NMTOKENS.factory()
            obj_.build(child_)
            self.compilationReason = obj_
        super(OriginalClassificationType, self).buildChildren(child_, node, nodeName_, True)
# end class OriginalClassificationType


class DerivativeClassificationType(PolicyRuleType):
    subclass = None
    superclass = PolicyRuleType
    def __init__(self, classifiedBy=None, classifiedOn=None, derivedFrom=None):
        super(DerivativeClassificationType, self).__init__()
        self.classifiedBy = classifiedBy
        self.classifiedOn = classifiedOn
        self.derivedFrom = derivedFrom
    def factory(*args_, **kwargs_):
        if DerivativeClassificationType.subclass:
            return DerivativeClassificationType.subclass(*args_, **kwargs_)
        else:
            return DerivativeClassificationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_classifiedBy(self): return self.classifiedBy
    def set_classifiedBy(self, classifiedBy): self.classifiedBy = classifiedBy
    def get_classifiedOn(self): return self.classifiedOn
    def set_classifiedOn(self, classifiedOn): self.classifiedOn = classifiedOn
    def get_derivedFrom(self): return self.derivedFrom
    def set_derivedFrom(self, derivedFrom): self.derivedFrom = derivedFrom
    def hasContent_(self):
        if (
            self.classifiedBy is not None or
            self.classifiedOn is not None or
            self.derivedFrom is not None or
            super(DerivativeClassificationType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='DerivativeClassificationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DerivativeClassificationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='DerivativeClassificationType'):
        super(DerivativeClassificationType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DerivativeClassificationType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='DerivativeClassificationType', fromsubclass_=False, pretty_print=True):
        super(DerivativeClassificationType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.classifiedBy is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:classifiedBy>%s</%s:classifiedBy>%s' % (nsmap[namespace_], quote_xml(self.classifiedBy), nsmap[namespace_], eol_))
        if self.classifiedOn is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:classifiedOn>%s</%s:classifiedOn>%s' % (nsmap[namespace_], quote_xml(self.classifiedOn), nsmap[namespace_], eol_))
        if self.derivedFrom is not None:
            self.derivedFrom.export(lwrite, level, nsmap, namespace_, name_='derivedFrom', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DerivativeClassificationType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'classifiedBy':
            classifiedBy_ = child_.text
            classifiedBy_ = self.gds_validate_string(classifiedBy_, node, 'classifiedBy')
            self.classifiedBy = classifiedBy_
        elif nodeName_ == 'classifiedOn':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_, node, 'classifiedOn')
            self.classifiedOn = dval_
        elif nodeName_ == 'derivedFrom':
            self.gds_validate_string(child_.text, node, 'derivedFrom')
            obj_ = edh_common.NMTOKENS.factory()
            obj_.build(child_)
            self.derivedFrom = obj_
        super(DerivativeClassificationType, self).buildChildren(child_, node, nodeName_, True)
# end class DerivativeClassificationType


class DeclassificationType(PolicyRuleType):
    subclass = None
    superclass = PolicyRuleType
    def __init__(self, declassExemption=None, declassPeriod=None, declassDate=None, declassEvent=None):
        super(DeclassificationType, self).__init__()
        self.declassExemption = declassExemption
        self.declassPeriod = declassPeriod
        self.declassDate = declassDate
        self.declassEvent = declassEvent
    def factory(*args_, **kwargs_):
        if DeclassificationType.subclass:
            return DeclassificationType.subclass(*args_, **kwargs_)
        else:
            return DeclassificationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_declassExemption(self): return self.declassExemption
    def set_declassExemption(self, declassExemption): self.declassExemption = declassExemption
    def get_declassPeriod(self): return self.declassPeriod
    def set_declassPeriod(self, declassPeriod): self.declassPeriod = declassPeriod
    def get_declassDate(self): return self.declassDate
    def set_declassDate(self, declassDate): self.declassDate = declassDate
    def get_declassEvent(self): return self.declassEvent
    def set_declassEvent(self, declassEvent): self.declassEvent = declassEvent
    def hasContent_(self):
        if (
            self.declassExemption is not None or
            self.declassPeriod is not None or
            self.declassDate is not None or
            self.declassEvent is not None or
            super(DeclassificationType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='DeclassificationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DeclassificationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='DeclassificationType'):
        super(DeclassificationType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='DeclassificationType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='DeclassificationType', fromsubclass_=False, pretty_print=True):
        super(DeclassificationType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.declassExemption is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:declassExemption>%s</%s:declassExemption>%s' % (nsmap[namespace_], quote_xml(self.declassExemption), nsmap[namespace_], eol_))
        if self.declassPeriod is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:declassPeriod>%s</%s:declassPeriod>%s' % (nsmap[namespace_], self.gds_format_integer(self.declassPeriod, input_name='declassPeriod'), nsmap[namespace_], eol_))
        if self.declassDate is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:declassDate>%s</%s:declassDate>%s' % (nsmap[namespace_], quote_xml(self.declassDate), nsmap[namespace_], eol_))
        if self.declassEvent is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:declassEvent>%s</%s:declassEvent>%s' % (nsmap[namespace_], quote_xml(self.declassEvent), nsmap[namespace_], eol_))
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(DeclassificationType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'declassExemption':
            declassExemption_ = child_.text
            declassExemption_ = self.gds_validate_string(declassExemption_, node, 'declassExemption')
            self.declassExemption = declassExemption_
        elif nodeName_ == 'declassPeriod':
            sval_ = child_.text
            try:
                ival_ = int(sval_)
            except (TypeError, ValueError) as exp:
                raise_parse_error(child_, 'requires integer: %s' % exp)
            ival_ = self.gds_validate_integer(ival_, node, 'declassPeriod')
            self.declassPeriod = ival_
        elif nodeName_ == 'declassDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_, node, 'declassDate')
            self.declassDate = dval_
        elif nodeName_ == 'declassEvent':
            declassEvent_ = child_.text
            declassEvent_ = self.gds_validate_string(declassEvent_, node, 'declassEvent')
            self.declassEvent = declassEvent_
        super(DeclassificationType, self).buildChildren(child_, node, nodeName_, True)
# end class DeclassificationType


class PublicReleaseType(PolicyRuleType):
    subclass = None
    superclass = PolicyRuleType
    def __init__(self, releasedBy=None, releasedOn=None):
        super(PublicReleaseType, self).__init__()
        self.releasedBy = releasedBy
        self.releasedOn = releasedOn
    def factory(*args_, **kwargs_):
        if PublicReleaseType.subclass:
            return PublicReleaseType.subclass(*args_, **kwargs_)
        else:
            return PublicReleaseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_releasedBy(self): return self.releasedBy
    def set_releasedBy(self, releasedBy): self.releasedBy = releasedBy
    def get_releasedOn(self): return self.releasedOn
    def set_releasedOn(self, releasedOn): self.releasedOn = releasedOn
    def hasContent_(self):
        if (
            self.releasedBy is not None or
            self.releasedOn is not None or
            super(PublicReleaseType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='PublicReleaseType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PublicReleaseType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='PublicReleaseType'):
        super(PublicReleaseType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='PublicReleaseType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='PublicReleaseType', fromsubclass_=False, pretty_print=True):
        super(PublicReleaseType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.releasedBy is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:releasedBy>%s</%s:releasedBy>%s' % (nsmap[namespace_], quote_xml(self.releasedBy), nsmap[namespace_], eol_))
        if self.releasedOn is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:releasedOn>%s</%s:releasedOn>%s' % (nsmap[namespace_], quote_xml(self.releasedOn), nsmap[namespace_], eol_))
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(PublicReleaseType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'releasedBy':
            releasedBy_ = child_.text
            releasedBy_ = self.gds_validate_string(releasedBy_, node, 'releasedBy')
            self.releasedBy = releasedBy_
        elif nodeName_ == 'releasedOn':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_, node, 'releasedOn')
            self.releasedOn = dval_
        super(PublicReleaseType, self).buildChildren(child_, node, nodeName_, True)
# end class PublicReleaseType


class ResourceDispositionType(PolicyRuleType):
    subclass = None
    superclass = PolicyRuleType
    def __init__(self, dispositionDate=None, dispositionProcess=None):
        super(ResourceDispositionType, self).__init__()
        self.dispositionDate = dispositionDate
        self.dispositionProcess = dispositionProcess
    def factory(*args_, **kwargs_):
        if ResourceDispositionType.subclass:
            return ResourceDispositionType.subclass(*args_, **kwargs_)
        else:
            return ResourceDispositionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_dispositionDate(self): return self.dispositionDate
    def set_dispositionDate(self, dispositionDate): self.dispositionDate = dispositionDate
    def get_dispositionProcess(self): return self.dispositionProcess
    def set_dispositionProcess(self, dispositionProcess): self.dispositionProcess = dispositionProcess
    def hasContent_(self):
        if (
            self.dispositionDate is not None or
            self.dispositionProcess is not None or
            super(ResourceDispositionType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ResourceDispositionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ResourceDispositionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='ResourceDispositionType'):
        super(ResourceDispositionType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ResourceDispositionType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ResourceDispositionType', fromsubclass_=False, pretty_print=True):
        super(ResourceDispositionType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.dispositionDate is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:dispositionDate>%s</%s:dispositionDate>%s' % (nsmap[namespace_], quote_xml(self.dispositionDate), nsmap[namespace_], eol_))
        if self.dispositionProcess is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:dispositionProcess>%s</%s:dispositionProcess>%s' % (nsmap[namespace_], quote_xml(self.dispositionProcess), nsmap[namespace_], eol_))
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(ResourceDispositionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'dispositionDate':
            sval_ = child_.text
            dval_ = self.gds_parse_date(sval_, node, 'dispositionDate')
            self.dispositionDate = dval_
        elif nodeName_ == 'dispositionProcess':
            dispositionProcess_ = child_.text
            dispositionProcess_ = self.gds_validate_string(dispositionProcess_, node, 'dispositionProcess')
            self.dispositionProcess = dispositionProcess_
        super(ResourceDispositionType, self).buildChildren(child_, node, nodeName_, True)
# end class ResourceDispositionType


class AccessPrivilegeType(PolicyRuleType):
    subclass = None
    superclass = PolicyRuleType
    def __init__(self, privilegeAction=None, privilegeScope=None, ruleEffect=None):
        super(AccessPrivilegeType, self).__init__()
        self.privilegeAction = privilegeAction
        if privilegeScope is None:
            self.privilegeScope = []
        else:
            self.privilegeScope = privilegeScope
        self.ruleEffect = ruleEffect
    def factory(*args_, **kwargs_):
        if AccessPrivilegeType.subclass:
            return AccessPrivilegeType.subclass(*args_, **kwargs_)
        else:
            return AccessPrivilegeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_privilegeAction(self): return self.privilegeAction
    def set_privilegeAction(self, privilegeAction): self.privilegeAction = privilegeAction
    def get_privilegeScope(self): return self.privilegeScope
    def set_privilegeScope(self, privilegeScope): self.privilegeScope = privilegeScope
    def add_privilegeScope(self, value): self.privilegeScope.append(value)
    def insert_privilegeScope(self, index, value): self.privilegeScope[index] = value
    def get_ruleEffect(self): return self.ruleEffect
    def set_ruleEffect(self, ruleEffect): self.ruleEffect = ruleEffect
    def validate_RuleEffectEnum(self, value):
        # Validate type RuleEffectEnum, a restriction on xsd:NMTOKEN.
        if value is not None:
            value = str(value)
            enumerations = ['permit', 'deny']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if enumeration_respectee is False:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on RuleEffectEnum' % {"value" : value.encode("utf-8")} )
    def hasContent_(self):
        if (
            self.privilegeAction is not None or
            self.privilegeScope or
            self.ruleEffect is not None or
            super(AccessPrivilegeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AccessPrivilegeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AccessPrivilegeType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='AccessPrivilegeType'):
        super(AccessPrivilegeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='AccessPrivilegeType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AccessPrivilegeType', fromsubclass_=False, pretty_print=True):
        super(AccessPrivilegeType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.privilegeAction is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:privilegeAction>%s</%s:privilegeAction>%s' % (nsmap[namespace_], quote_xml(self.privilegeAction), nsmap[namespace_], eol_))
        for privilegeScope_ in self.privilegeScope:
            privilegeScope_.export(lwrite, level, nsmap, namespace_, name_='privilegeScope', pretty_print=pretty_print)
        if self.ruleEffect is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:ruleEffect>%s</%s:ruleEffect>%s' % (nsmap[namespace_], quote_xml(self.ruleEffect), nsmap[namespace_], eol_))
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(AccessPrivilegeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'privilegeAction':
            privilegeAction_ = child_.text
            privilegeAction_ = self.gds_validate_string(privilegeAction_, node, 'privilegeAction')
            self.privilegeAction = privilegeAction_
        elif nodeName_ == 'privilegeScope':
            self.gds_validate_string(child_.text, node, 'privilegeScope')
            obj_ = edh_common.NMTOKENS.factory()
            obj_.build(child_)
            self.privilegeScope.append(obj_)
        elif nodeName_ == 'ruleEffect':
            ruleEffect_ = child_.text
            ruleEffect_ = self.gds_validate_string(ruleEffect_, node, 'ruleEffect')
            self.ruleEffect = ruleEffect_
            self.validate_RuleEffectEnum(self.ruleEffect)    # validate type RuleEffectEnum
        super(AccessPrivilegeType, self).buildChildren(child_, node, nodeName_, True)
# end class AccessPrivilegeType


class FurtherSharingType(PolicyRuleType):
    subclass = None
    superclass = PolicyRuleType
    def __init__(self, sharingScope=None, ruleEffect=None):
        super(FurtherSharingType, self).__init__()
        if sharingScope is None:
            self.sharingScope = []
        else:
            self.sharingScope = sharingScope
        self.ruleEffect = ruleEffect
    def factory(*args_, **kwargs_):
        if FurtherSharingType.subclass:
            return FurtherSharingType.subclass(*args_, **kwargs_)
        else:
            return FurtherSharingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_sharingScope(self): return self.sharingScope
    def set_sharingScope(self, sharingScope): self.sharingScope = sharingScope
    def add_sharingScope(self, value): self.sharingScope.append(value)
    def insert_sharingScope(self, index, value): self.sharingScope[index] = value
    def get_ruleEffect(self): return self.ruleEffect
    def set_ruleEffect(self, ruleEffect): self.ruleEffect = ruleEffect
    def validate_RuleEffectEnum(self, value):
        # Validate type RuleEffectEnum, a restriction on xsd:NMTOKEN.
        if value is not None:
            value = str(value)
            enumerations = ['permit', 'deny']
            enumeration_respectee = False
            for enum in enumerations:
                if value == enum:
                    enumeration_respectee = True
                    break
            if enumeration_respectee is False:
                warnings_.warn('Value "%(value)s" does not match xsd enumeration restriction on RuleEffectEnum' % {"value" : value.encode("utf-8")} )
    def hasContent_(self):
        if (
            self.sharingScope is not None or
            self.ruleEffect is not None or
            super(FurtherSharingType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='FurtherSharingType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='FurtherSharingType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='FurtherSharingType'):
        super(FurtherSharingType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='FurtherSharingType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='FurtherSharingType', fromsubclass_=False, pretty_print=True):
        super(FurtherSharingType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for sharingScope_ in self.sharingScope:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:sharingScope>%s</%s:sharingScope>%s' % (nsmap[namespace_], quote_xml(self.sharingScope), nsmap[namespace_], eol_))
        if self.ruleEffect is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:ruleEffect>%s</%s:ruleEffect>%s' % (nsmap[namespace_], quote_xml(self.ruleEffect), nsmap[namespace_], eol_))
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(FurtherSharingType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'sharingScope':
            self.gds_validate_string(child_.text, node, 'sharingScope')
            obj_ = edh_common.NMTOKENS.factory()
            obj_.build(child_)
            self.sharingScope.append(obj_)
        elif nodeName_ == 'ruleEffect':
            ruleEffect_ = child_.text
            ruleEffect_ = self.gds_validate_string(ruleEffect_, node, 'ruleEffect')
            self.ruleEffect = ruleEffect_
            self.validate_RuleEffectEnum(self.ruleEffect)    # validate type RuleEffectEnum
        super(FurtherSharingType, self).buildChildren(child_, node, nodeName_, True)
# end class FurtherSharingType

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
        rootTag = 'AccessPrivilege'
        rootClass = AccessPrivilegeType
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
        rootTag = 'AccessPrivilege'
        rootClass = AccessPrivilegeType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="Indicator",
    #     namespacedef_='')
    return rootObj

__all__ = [
    "AccessPrivilegeType",
    "DeclassificationType",
    "DerivativeClassificationType",
    "FurtherSharingType",
    "OriginalClassificationType",
    "PolicyRuleType",
    "PolicyType",
    "PublicReleaseType",
    "ResourceDispositionType"
]
