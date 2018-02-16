"""Generate CSVs

"""


import yaml
import logging

import pandas as pd

from .manager import *
from .generator import Generator

class CsvGenerator(Generator):
        
    def serialize(self, dirname=None, format='csv', **args):
        self.dirname = dirname
        df = self.tr(**args)
        sep = ","
        if format == 'tsv':
            sep="\t"
        print(df.to_csv(sep=sep, index=False))
    
    def tr(self, roots=None):
        schema = self.schema
        mgr = self.manager

        #roots = [mgr.classdef(x) for x in roots]
        items = []
        #print('## ROOTS: {}'.format(roots))
        
        # create list of class names
        for c in schema.classes:
            if c.abstract:
                continue
            in_subset = False
            ancs = set([x.name for x in mgr.ancestors(c)])
            
            if roots is None or len(ancs.intersection(roots)) > 0:
                in_subset = True
            if in_subset:
                items.append(self.tr_class(c))
        df = pd.DataFrame(items, columns=['id', 'mappings', 'description'])
        return df


    def tr_class(self, c):
        schema = self.schema
        mgr = self.manager
        cn = c.name
        id = mgr.class_name(c, style=NameStyle.UNDERSCORE)
        mappings = c.mappings
        if mappings is None:
            mappings = []
        
        item = {'id': id,
                'mappings': "|".join(mappings),
                'description': c.description}
        return item
