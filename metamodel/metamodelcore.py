from io import StringIO
from typing import Union, Dict, NewType, TextIO, cast, Type
from urllib.request import Request, urlopen

import yaml
from dataclasses import field


def empty_list():
    return field(default_factory=list)


def empty_dict():
    return field(default_factory=dict)


URI = NewType('URI', str)


class Builtin:
    pass


string = Builtin()
double = Builtin()
time = Builtin()


class Root:
    pass


class DupCheckYamlLoader(yaml.loader.Loader):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, self.map_constructor)

    def map_constructor(self, loader,  node, deep=False):
        """Walk the mapping, recording any duplicate keys.

        """
        mapping = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            value = loader.construct_object(value_node, deep=deep)
            if key in mapping:
                raise ValueError(f"Duplicate key: \"{key}\"")
            mapping[key] = value

        return mapping


def load_schema(data: Union[str, TextIO], cls: Type) -> Dict[str, "SchemaDefinition"]:
    if isinstance(data, str):
        if '\n' in data:
            return load_schema((cast(TextIO, StringIO(data))), cls)  # Not sure why this doesn't work...
        elif '://' in data:
            req = Request(data)
            req.add_header("Accept", "application/json, text/json;q=0.9")
            with urlopen(req) as response:
                return load_schema(response, cls)
        else:
            with open(data) as f:
                return load_schema(f, cls)
    else:
        obj = yaml.load(data, DupCheckYamlLoader)
        return {k: cls(name=k, **v) for k, v in obj.items()}


def root_representer(dumper: yaml.Dumper, data: Root):
    rval = dict()
    for k, v in data.__dict__.items():
        if not k.startswith('_') and v is not None and (not isinstance(v, (dict, list)) or v):
            rval[k] = v
    return dumper.represent_data(rval)


yaml.add_multi_representer(Root, root_representer)


def as_yaml(schema: Dict[str, object]) -> str:
    return yaml.dump(schema)
