# """
# Base class for generators
# """
# import abc
# from typing import Optional
#
# from metamodel.metamodel import SchemaDefinition
# from .manager import Manager
#
#
# class Generator(metaclass=abc.ABCMeta):
#
#     def __init__(self, schema: SchemaDefinition=None, manager: Optional[Manager]=None) -> None:
#         """
#         Create a new instance
#
#         Arguments
#         ---------
#         - schema : SchemaDefinition
#         """
#         self.schema = schema
#         self.manager = manager if manager else Manager(schema)
#
#     @staticmethod
#     def id_to_url(id_: str) -> str:
#         uri = id_
#         if ':' in id_:
#             # TODO! use PC
#             if id_.startswith('SIO:'):
#                 uri = id_.replace('SIO:', 'http://semanticscience.org/resource/SIO_')
#             elif id_.startswith('HGNC:'):
#                 uri = 'https://monarchinitiative.org/gene/' + id_
#             else:
#                 frag = id_.replace(':', '_')
#                 base = 'http://purl.obolibrary.org/obo/'
#                 uri = base+frag
#         return uri
