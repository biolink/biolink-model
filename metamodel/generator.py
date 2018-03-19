"""
Base class for generators
"""

import logging

from .manager import Manager
    
class Generator(object):
    
    def __init__(self, schema=None, manager=None):
        """
        Create a new instance

        Arguments
        ---------
        - schema : SchemaDefinition
        """
        self.schema = schema
        if manager is None:
            manager = Manager(schema)
        self.manager = manager

    def id_to_url(self, id):
        uri = id
        if ':' in id:
            # TODO! use PC
            if id.startswith('SIO:'):
                uri = id.replace('SIO:', 'http://semanticscience.org/resource/SIO_')
            elif id.startswith('HGNC:'):
                uri = 'https://monarchinitiative.org/gene/' + id
            else:
                frag = id.replace(':','_')
                base = 'http://purl.obolibrary.org/obo/'
                uri = base+frag
        return uri
