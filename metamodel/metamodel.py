

## CLASSES

class Definition(object):
    """
    base class
    """
    def __init__(self,
                 name=None,
                 singular_name=None,
                 is_a=None,
                 description=None,
                 abstract=None,
                 mappings=None):
        self.name=name
        self.singular_name=singular_name
        self.is_a=is_a
        self.description=description
        self.abstract=abstract
        self.mappings=mappings

class SlotDefinition(Definition):
    """
    A property or slot
    """
    def __init__(self,
                 identifier=None,
                 domain=None,
                 range=None,
                 multivalued=None,
                 path=None,
                 name=None,
                 singular_name=None,
                 is_a=None,
                 description=None,
                 abstract=None,
                 mappings=None):
        self.identifier=identifier
        self.domain=domain
        self.range=range
        self.multivalued=multivalued
        self.path=path
        self.name=name
        self.singular_name=singular_name
        self.is_a=is_a
        self.description=description
        self.abstract=abstract
        self.mappings=mappings

class SlotUsageDefinition(SlotDefinition):
    """
    A usage of slot in the context of a class
    """
    def __init__(self,
                 **args):
        super().__init__(**args)
        
class ClassDefinition(Definition):
    """
    A class or interface
    """
    def __init__(self,
                 mixins=None,
                 slots=None,
                 slot_usage=None,
                 name=None,
                 singular_name=None,     
                 is_a=None,
                 description=None,
                 abstract=None,
                 mappings=None):
        self.mixins=mixins
        self.slots=slots
        self.slot_usage=slot_usage
        self.name=name
        self.singular_name=singular_name 
        self.is_a=is_a
        self.description=description     
        self.abstract=abstract
        self.mappings=mappings

    def __str__(self):
        return "mixins={} slots={} slot_usage={} name={} singular_name={} is_a={} description={} abstract={} mappings={} ".format(self.mixins,self.slots,self.slot_usage,self.name,self.singular_name,self.is_a,self.description,self.abstract,self.mappings)
    def __repr__(self):
        return self.__str__()

class TypeDefinition(Definition):
    """
    A type definition
    """
    def __init__(self,
                 mixins=None,
                 name=None,
                 singular_name=None,
                 is_a=None,
                 description=None,
                 abstract=None,
                 mappings=None):
        self.mixins=mixins
        self.name=name
        self.singular_name=singular_name
        self.is_a=is_a
        self.description=description
        self.abstract=abstract
        self.mappings=mappings

class SchemaDefinition(Definition):
    """
    A collection of definitions
    """
    def __init__(self,
                 slots=None,
                 classes=None,
                 types=None,
                 name=None,
                 singular_name=None,
                 is_a=None,
                 description=None,
                 abstract=None,
                 mappings=None):
        self.slots=slots
        self.classes=classes
        self.types=types
        self.name=name
        self.singular_name=singular_name
        self.is_a=is_a
        self.description=description
        self.abstract=abstract
        self.mappings=mappings

