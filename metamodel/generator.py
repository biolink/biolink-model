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
