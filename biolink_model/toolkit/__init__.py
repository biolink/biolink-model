import os, biolink_model

from metamodel.metamodel import SchemaDefinition, ClassDefinition, SlotDefinition, ClassDefinitionName, \
    TypeDefinition, Element, SlotDefinitionName, TypeDefinitionName, PrefixLocalName

from typing import List, Set, Union, TextIO, Optional, TypeVar
from functools import lru_cache

from .toolkit_generator import ToolkitGenerator

generator = None

def load_generator(schema:Union[str, TextIO, SchemaDefinition]=None) -> ToolkitGenerator:
    """
    Loads the generator object that is used for each of the methods in this file
    """
    global generator

    if generator is None:
        if schema is None:
            generator = ToolkitGenerator(biolink_model.path)
            generator.serialize()
        else:
            generator = ToolkitGenerator(schema)
            generator.serialize()

    return generator

def is_edgelabel(s:str) -> bool:
    """
    Takes a string and checks that it is an edge label, that is checks that the
    entity it refers to inherits from "related to" and uses underscores rather
    than spaces.
    """
    if ' ' in s:
        return False
    else:
        ancestors = load_generator().ancestors(s.replace('_', ' '))
        return 'related to' in ancestors

def is_category(s:str) -> bool:
    """
    Takes a string and checks that it is a category: that it inherits
    from "named thing"
    """
    ancestors = load_generator().ancestors(s)
    return 'named thing' in ancestors and 'association' not in ancestors

def get_element(name:str) -> Optional[Element]:
    return load_generator().obj_for(name.replace('_', ' '))

def get_all_by_mapping(curie:str) -> Optional[List[str]]:
    """
    Gets the set of biolink entities that the given curie maps to
    """
    try:
        return list(generator.mappings[curie])
    except:
        return None

@lru_cache()
def get_by_mapping(curie:str) -> Optional[str]:
    """
    Gets the biolink entity of the highest level of inheritance that the given
    curie maps to. If no such entity exists, arbitrarily chooses one entity
    and returns it.
    """
    try:
        g = load_generator()
        entities = get_all_by_mapping(curie)

        if entities is None:
            return None

        for e in entities:
            e = e.replace('_', ' ')
            ancestors = g.ancestors(e)
            ancestors.remove(e)
            if not any(a in entities for a in ancestors):
                return e

        if entities != []:
            return entities[0]
        else:
            return None

    except KeyError:
        return None
