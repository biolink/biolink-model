"""
Base class for generators
"""

import logging

from .manager import *
    
class Generator(object):
    
    def __init__(self):
        """
        Create a new instance

        Arguments
        ---------
        - schema : SchemaDefinition
        """
        self.schema = None
