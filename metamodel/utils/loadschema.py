import os
import time
from datetime import date, datetime
from io import StringIO
from typing import Union, TextIO, cast, Optional
from urllib.request import Request, urlopen

import yaml

from metamodel.metamodel import SchemaDefinition, metamodel_version
from metamodel.utils.mergeutils import merge_schemas


def load_raw_schema(data: Union[str, TextIO],
                    source_file: str=None,
                    source_file_date: str=None,
                    source_file_size: int=None,
                    base_dir: Optional[str]=None) -> SchemaDefinition:
    """ Load and flatten SchemaDefinition from a file name, a URL or a block of text

    @param data: URL, file name or block of text
    @param source_file: Source file name for the schema
    @param source_file_date: timestamp of source file
    @param source_file_size: size of source file
    @param base_dir: Working directory of sources
    @return: Map from schema name to SchemaDefinition
    """
    if isinstance(data, str):
        if '\n' in data:
            return load_raw_schema((cast(TextIO, StringIO(data))))  # Not sure why typing doesn't see StringIO as TextIO
        elif '://' in data:
            # TODO: complete and test URL access
            req = Request(data)
            req.add_header("Accept", "application/yaml, text/yaml;q=0.9")
            with urlopen(req) as response:
                return load_raw_schema(response)
        else:
            fname = os.path.join(base_dir if base_dir else '', data)
            with open(fname) as f:
                return load_raw_schema(f, data, time.ctime(os.path.getmtime(fname)), os.path.getsize(fname))
    else:
        schemadefs = yaml.load(data, DupCheckYamlLoader)
        # Some schemas don't have an outermost identifier.  Construct one if necessary
        if 'name' in schemadefs:
            schemadefs = {schemadefs.pop('name'): schemadefs}
        elif 'id' in schemadefs:
            schemadefs = {schemadefs['id']: schemadefs}
        schema: SchemaDefinition = None
        for sname, sdef in {k: SchemaDefinition(name=k, **v) for k, v in schemadefs.items()}.items():
            if schema is None:
                schema = sdef
                schema.source_file = source_file
                schema.source_file_date = source_file_date
                schema.source_file_size = source_file_size
                schema.generation_date =  datetime.now().strftime("%Y-%m-%d %H:%M")
                schema.metamodel_version = metamodel_version
            else:
                merge_schemas(schema, sdef)
        return schema


class DupCheckYamlLoader(yaml.loader.Loader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, self.map_constructor)

    def map_constructor(self, loader,  node, deep=False):
        """ Walk the mapping, recording any duplicate keys.

        """
        mapping = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            value = loader.construct_object(value_node, deep=deep)
            if key in mapping:
                raise ValueError(f"Duplicate key: \"{key}\"")
            mapping[key] = value

        return mapping
