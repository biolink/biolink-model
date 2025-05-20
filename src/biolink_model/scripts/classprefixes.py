# Auto generated from class_prefixes.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-05-15T01:43:08
# Schema: BiolinkClassPrefixes
#
# id: biolink-model-class-prefixes
# description: preferred order identifier prefixes per class in Biolink Model
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import URI, URIorCURIE

metamodel_version = "1.7.0"
version = "4.2.6-rc5"

# Namespaces
BIOGRID = CurieNamespace('BIOGRID', 'http://identifiers.org/biogrid/')
OIO = CurieNamespace('OIO', 'http://www.geneontology.org/formats/oboInOwl#')
SO = CurieNamespace('SO', 'http://purl.obolibrary.org/obo/SO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = BIOLINK


# Types

# Class references



@dataclass(repr=False)
class BiolinkClassPrefixMap(YAMLRoot):
    """
    preferred order identifier prefixes per class in Biolink Model
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["BiolinkClassPrefixMap"]
    class_class_curie: ClassVar[str] = "biolink:BiolinkClassPrefixMap"
    class_name: ClassVar[str] = "BiolinkClassPrefixMap"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiolinkClassPrefixMap

    prefix_map: Optional[Union[Union[dict, "Prefix"], list[Union[dict, "Prefix"]]]] = empty_list()
    class_name: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.prefix_map, list):
            self.prefix_map = [self.prefix_map] if self.prefix_map is not None else []
        self.prefix_map = [v if isinstance(v, Prefix) else Prefix(**as_dict(v)) for v in self.prefix_map]

        if self.class_name is not None and not isinstance(self.class_name, URIorCURIE):
            self.class_name = URIorCURIE(self.class_name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiolinkClassPrefixesCollection(YAMLRoot):
    """
    collection of BiolinkClassPrefixes objects
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["BiolinkClassPrefixesCollection"]
    class_class_curie: ClassVar[str] = "biolink:BiolinkClassPrefixesCollection"
    class_name: ClassVar[str] = "BiolinkClassPrefixesCollection"
    class_model_uri: ClassVar[URIRef] = BIOLINK.BiolinkClassPrefixesCollection

    biolink_class_prefixes: Optional[Union[Union[dict, BiolinkClassPrefixMap], list[Union[dict, BiolinkClassPrefixMap]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.biolink_class_prefixes, list):
            self.biolink_class_prefixes = [self.biolink_class_prefixes] if self.biolink_class_prefixes is not None else []
        self.biolink_class_prefixes = [v if isinstance(v, BiolinkClassPrefixMap) else BiolinkClassPrefixMap(**as_dict(v)) for v in self.biolink_class_prefixes]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Prefix(YAMLRoot):
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK["Prefix"]
    class_class_curie: ClassVar[str] = "biolink:Prefix"
    class_name: ClassVar[str] = "Prefix"
    class_model_uri: ClassVar[URIRef] = BIOLINK.Prefix

    prefix: Optional[str] = None
    base_uri: Optional[Union[str, URI]] = None
    order: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.prefix is not None and not isinstance(self.prefix, str):
            self.prefix = str(self.prefix)

        if self.base_uri is not None and not isinstance(self.base_uri, URI):
            self.base_uri = URI(self.base_uri)

        if self.order is not None and not isinstance(self.order, int):
            self.order = int(self.order)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.biolink_class_prefixes = Slot(uri=BIOLINK.biolink_class_prefixes, name="biolink_class_prefixes", curie=BIOLINK.curie('biolink_class_prefixes'),
                   model_uri=BIOLINK.biolink_class_prefixes, domain=None, range=Optional[Union[Union[dict, BiolinkClassPrefixMap], list[Union[dict, BiolinkClassPrefixMap]]]])

slots.prefix_map = Slot(uri=BIOLINK.prefix_map, name="prefix_map", curie=BIOLINK.curie('prefix_map'),
                   model_uri=BIOLINK.prefix_map, domain=None, range=Optional[Union[Union[dict, Prefix], list[Union[dict, Prefix]]]])

slots.class_name = Slot(uri=BIOLINK.class_name, name="class_name", curie=BIOLINK.curie('class_name'),
                   model_uri=BIOLINK.class_name, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.base_uri = Slot(uri=BIOLINK.base_uri, name="base_uri", curie=BIOLINK.curie('base_uri'),
                   model_uri=BIOLINK.base_uri, domain=None, range=Optional[Union[str, URI]])

slots.prefix = Slot(uri=BIOLINK.prefix, name="prefix", curie=BIOLINK.curie('prefix'),
                   model_uri=BIOLINK.prefix, domain=None, range=Optional[str])

slots.order = Slot(uri=BIOLINK.order, name="order", curie=BIOLINK.curie('order'),
                   model_uri=BIOLINK.order, domain=None, range=Optional[int])
