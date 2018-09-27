from metamodel.utils.schemaloader import SchemaLoader
from metamodel.metamodel import ClassDefinition, SlotDefinition

__schema = None

def schema():
    global __schema

    if __schema is None:
        __schema = SchemaLoader(
            'https://biolink.github.io/biolink-model/biolink-model.yaml'
        ).resolve()

    return __schema

def slot_uri(s:str) -> str:
    return f'https://biolink.github.io/biolink-model/docs/{s.replace(" ", "_")}.html'

def class_uri(c:str) -> str:
    camel_case = c.title().replace(' ', '')
    return f'https://biolink.github.io/biolink-model/docs/{camel_case}.html'

def is_class(c:str) -> bool:
    return c in schema().classes

def is_slot(s:str) -> bool:
    return s.replace('_', ' ') in schema().slots

def get_class(c:str) -> ClassDefinition:
    return schema().classes.get(c)

def get_slot(s:str) -> SlotDefinition:
    return schema().slots.get(s.replace('_', ' '))
