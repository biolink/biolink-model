"""Generate CSVs

"""
from typing import List

from metamodel.metamodel import SchemaDefinition, ClassDefinition


class CsvGenerator:
    def __init__(self, schema: SchemaDefinition) -> None:
        self.dirname = None
        self.sep = None
        self.schema = schema
        
    def serialize(self, dirname: str=None, format: str='csv', roots=None):
        self.dirname = dirname
        assert format in ('csv', 'tsv'), "Unrecognized format"
        self.sep = ',' if format == 'csv' else '\t' if format == 'tsv'
        df = self.tr(roots)
        print(df.to_csv(sep=sep, index=False))
    
    def tr(self, roots=None):
        #roots = [mgr.classdef(x) for x in roots]
        items = []
        #print('## ROOTS: {}'.format(roots))
        
        # create list of class names
        for cname, c in self.schema.classes.items():
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

    def ancestors(self, c: ClassDefinition) -> List[ClassDefinition]:
