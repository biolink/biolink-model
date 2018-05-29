from io import StringIO
from typing import Union, TextIO, cast
from urllib.request import Request, urlopen

import yaml

from metamodel.metamodel import SchemaDefinition
from metamodel.utils.mergeutils import merge_schemas


def load_schema(data: Union[str, TextIO]) -> SchemaDefinition:
    """ Load and flatten SchemaDefinition from a file name, a URL or a block of text

    @param data: URL, file name or block of text
    @return: Map from schema name to SchemaDefinition
    """
    if isinstance(data, str):
        if '\n' in data:
            return load_schema((cast(TextIO, StringIO(data))))  # Not sure why this doesn't work...
        elif '://' in data:
            req = Request(data)
            req.add_header("Accept", "application/json, text/json;q=0.9")
            with urlopen(req) as response:
                return load_schema(response)
        else:
            with open(data) as f:
                return load_schema(f)
    else:
        schemadefs = yaml.load(data, DupCheckYamlLoader)
        # Some schemas don't have an outermost identifier.  Construct one if necessary
        if 'name' in schemadefs:
            schemadefs = {schemadefs.pop('name'): schemadefs}
        elif 'id' in schemadefs:
            schemadefs = {schemadefs['id']: schemadefs}
        schema = None
        for sname, sdef in {k: SchemaDefinition(name=k, **v) for k, v in schemadefs.items()}.items():
            if schema is None:
                schema = sdef
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
