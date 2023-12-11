# Auto generated from information-resource.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-12-11T15:47:53
# Schema: Biolink-Model
#
# id: https://w3id.org/biolink/biolink-model
# description: Entity and association taxonomy and datamodel for life-sciences data
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = "4.0.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
AGRKB = CurieNamespace('AGRKB', 'http://example.org/UNKNOWN/AGRKB/')
BIOGRID = CurieNamespace('BIOGRID', 'http://identifiers.org/biogrid/')
HANCESTRO = CurieNamespace('HANCESTRO', 'http://example.org/UNKNOWN/HANCESTRO/')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
RXNORM = CurieNamespace('RXNORM', 'http://example.org/UNKNOWN/RXNORM/')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
WIKIDATA_PROPERTY = CurieNamespace('WIKIDATA_PROPERTY', 'http://example.org/UNKNOWN/WIKIDATA_PROPERTY/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCT = CurieNamespace('dct', 'http://example.org/UNKNOWN/dct/')
GFF3 = CurieNamespace('gff3', 'http://example.org/UNKNOWN/gff3/')
GPI = CurieNamespace('gpi', 'http://example.org/UNKNOWN/gpi/')
INFORES = CurieNamespace('infores', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBOINOWL = CurieNamespace('oboInOwl', 'http://www.geneontology.org/formats/oboInOwl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = INFORES


# Types

# Class references
class InformationResourceId(extended_str):
    pass


@dataclass
class InformationResourceContainer(YAMLRoot):
    """
    A collection of information resources
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["InformationResourceContainer"]
    class_class_curie: ClassVar[str] = "biolink:InformationResourceContainer"
    class_name: ClassVar[str] = "InformationResourceContainer"
    class_model_uri: ClassVar[URIRef] = INFORES.InformationResourceContainer

    information_resources: Optional[Union[Dict[Union[str, InformationResourceId], Union[dict, "InformationResource"]], List[Union[dict, "InformationResource"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="information_resources", slot_type=InformationResource, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class InformationResource(YAMLRoot):
    """
    A database or knowledgebase and its supporting ecosystem of interfaces and services that deliver content to
    consumers (e.g. web portals, APIs, query endpoints, streaming services, data downloads, etc.). A single
    Information Resource by this definition may span many different datasets or databases, and include many access
    endpoints and user interfaces. Information Resources include project-specific resources such as a Translator
    Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["InformationResource"]
    class_class_curie: ClassVar[str] = "biolink:InformationResource"
    class_name: ClassVar[str] = "InformationResource"
    class_model_uri: ClassVar[URIRef] = INFORES.InformationResource

    id: Union[str, InformationResourceId] = None
    status: Optional[Union[str, "InformationResourceStatusEnum"]] = None
    name: Optional[str] = None
    xref: Optional[Union[str, List[str]]] = empty_list()
    synonym: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[str] = None
    knowledge_level: Optional[str] = None
    agent_type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationResourceId):
            self.id = InformationResourceId(self.id)

        if self.status is not None and not isinstance(self.status, InformationResourceStatusEnum):
            self.status = InformationResourceStatusEnum(self.status)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.xref, list):
            self.xref = [self.xref] if self.xref is not None else []
        self.xref = [v if isinstance(v, str) else str(v) for v in self.xref]

        if not isinstance(self.synonym, list):
            self.synonym = [self.synonym] if self.synonym is not None else []
        self.synonym = [v if isinstance(v, str) else str(v) for v in self.synonym]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.knowledge_level is not None and not isinstance(self.knowledge_level, str):
            self.knowledge_level = str(self.knowledge_level)

        if self.agent_type is not None and not isinstance(self.agent_type, str):
            self.agent_type = str(self.agent_type)

        super().__post_init__(**kwargs)


# Enumerations
class InformationResourceStatusEnum(EnumDefinitionImpl):

    released = PermissibleValue(text="released")
    deprecated = PermissibleValue(text="deprecated")
    draft = PermissibleValue(text="draft")
    modified = PermissibleValue(text="modified")

    _defn = EnumDefinition(
        name="InformationResourceStatusEnum",
    )

# Slots
class slots:
    pass

slots.status = Slot(uri=INFORES.status, name="status", curie=INFORES.curie('status'),
                   model_uri=INFORES.status, domain=None, range=Optional[Union[str, "InformationResourceStatusEnum"]])

slots.information_resources = Slot(uri=INFORES.information_resources, name="information_resources", curie=INFORES.curie('information_resources'),
                   model_uri=INFORES.information_resources, domain=None, range=Optional[Union[Dict[Union[str, InformationResourceId], Union[dict, InformationResource]], List[Union[dict, InformationResource]]]])

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=INFORES.name, domain=None, range=Optional[str])

slots.id = Slot(uri=INFORES.id, name="id", curie=INFORES.curie('id'),
                   model_uri=INFORES.id, domain=None, range=URIRef)

slots.xref = Slot(uri=INFORES.xref, name="xref", curie=INFORES.curie('xref'),
                   model_uri=INFORES.xref, domain=None, range=Optional[Union[str, List[str]]])

slots.synonym = Slot(uri=INFORES.synonym, name="synonym", curie=INFORES.curie('synonym'),
                   model_uri=INFORES.synonym, domain=None, range=Optional[Union[str, List[str]]])

slots.description = Slot(uri=INFORES.description, name="description", curie=INFORES.curie('description'),
                   model_uri=INFORES.description, domain=None, range=Optional[str])

slots.knowledge_level = Slot(uri=INFORES.knowledge_level, name="knowledge level", curie=INFORES.curie('knowledge_level'),
                   model_uri=INFORES.knowledge_level, domain=None, range=Optional[str])

slots.agent_type = Slot(uri=INFORES.agent_type, name="agent type", curie=INFORES.curie('agent_type'),
                   model_uri=INFORES.agent_type, domain=None, range=Optional[str])
