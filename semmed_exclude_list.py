# Auto generated from semmed-exclude-list-model.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-07-13T17:12:25
# Schema: semmed-exclude-list-model
#
# id: https://w3id.org/biolink/biolink-model
# description: Model that represents a semmed exclude list object
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
version = "3.5.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
INFORES = CurieNamespace('infores', 'https://w3id.org/biolink/vocab/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
OBOINOWL = CurieNamespace('oboInOwl', 'http://www.geneontology.org/formats/oboInOwl#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SEL = CurieNamespace('sel', 'https://w3id.org/biolink/vocab/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = SEL


# Types

# Class references



@dataclass
class ExcludeListContainer(YAMLRoot):
    """
    A collection of exclusion objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ExcludeListContainer
    class_class_curie: ClassVar[str] = "biolink:ExcludeListContainer"
    class_name: ClassVar[str] = "ExcludeListContainer"
    class_model_uri: ClassVar[URIRef] = SEL.ExcludeListContainer

    excluded_semmedb_records: Optional[Union[Union[dict, "ExcludedSemmedbRecord"], List[Union[dict, "ExcludedSemmedbRecord"]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.excluded_semmedb_records, list):
            self.excluded_semmedb_records = [self.excluded_semmedb_records] if self.excluded_semmedb_records is not None else []
        self.excluded_semmedb_records = [v if isinstance(v, ExcludedSemmedbRecord) else ExcludedSemmedbRecord(**as_dict(v)) for v in self.excluded_semmedb_records]

        super().__post_init__(**kwargs)


@dataclass
class ExcludedSemmedbRecord(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = BIOLINK.ExcludedSemmedbRecord
    class_class_curie: ClassVar[str] = "biolink:ExcludedSemmedbRecord"
    class_name: ClassVar[str] = "ExcludedSemmedbRecord"
    class_model_uri: ClassVar[URIRef] = SEL.ExcludedSemmedbRecord

    semmeddb_subject_code: Optional[str] = None
    semmeddb_subject_t_code: Optional[str] = None
    semmeddb_predicate: Optional[str] = None
    semmeddb_object_code: Optional[str] = None
    semmeddb_object_t_code: Optional[str] = None
    notes: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.semmeddb_subject_code is not None and not isinstance(self.semmeddb_subject_code, str):
            self.semmeddb_subject_code = str(self.semmeddb_subject_code)

        if self.semmeddb_subject_t_code is not None and not isinstance(self.semmeddb_subject_t_code, str):
            self.semmeddb_subject_t_code = str(self.semmeddb_subject_t_code)

        if self.semmeddb_predicate is not None and not isinstance(self.semmeddb_predicate, str):
            self.semmeddb_predicate = str(self.semmeddb_predicate)

        if self.semmeddb_object_code is not None and not isinstance(self.semmeddb_object_code, str):
            self.semmeddb_object_code = str(self.semmeddb_object_code)

        if self.semmeddb_object_t_code is not None and not isinstance(self.semmeddb_object_t_code, str):
            self.semmeddb_object_t_code = str(self.semmeddb_object_t_code)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.semmeddb_subject_code = Slot(uri=SEL.semmeddb_subject_code, name="semmeddb_subject_code", curie=SEL.curie('semmeddb_subject_code'),
                   model_uri=SEL.semmeddb_subject_code, domain=None, range=Optional[str])

slots.semmeddb_subject_t_code = Slot(uri=SEL.semmeddb_subject_t_code, name="semmeddb_subject_t_code", curie=SEL.curie('semmeddb_subject_t_code'),
                   model_uri=SEL.semmeddb_subject_t_code, domain=None, range=Optional[str])

slots.semmeddb_predicate = Slot(uri=SEL.semmeddb_predicate, name="semmeddb_predicate", curie=SEL.curie('semmeddb_predicate'),
                   model_uri=SEL.semmeddb_predicate, domain=None, range=Optional[str])

slots.semmeddb_object_code = Slot(uri=SEL.semmeddb_object_code, name="semmeddb_object_code", curie=SEL.curie('semmeddb_object_code'),
                   model_uri=SEL.semmeddb_object_code, domain=None, range=Optional[str])

slots.semmeddb_object_t_code = Slot(uri=SEL.semmeddb_object_t_code, name="semmeddb_object_t_code", curie=SEL.curie('semmeddb_object_t_code'),
                   model_uri=SEL.semmeddb_object_t_code, domain=None, range=Optional[str])

slots.notes = Slot(uri=SEL.notes, name="notes", curie=SEL.curie('notes'),
                   model_uri=SEL.notes, domain=None, range=Optional[str])

slots.excluded_semmedb_records = Slot(uri=SEL.excluded_semmedb_records, name="excluded_semmedb_records", curie=SEL.curie('excluded_semmedb_records'),
                   model_uri=SEL.excluded_semmedb_records, domain=None, range=Optional[Union[Union[dict, ExcludedSemmedbRecord], List[Union[dict, ExcludedSemmedbRecord]]]])
