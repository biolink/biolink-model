from enum import Enum
from io import StringIO
from typing import Union, Dict, NewType, TextIO, cast, Type
from urllib.request import Request, urlopen

import yaml
from dataclasses import field, dataclass


def empty_list():
    return field(default_factory=list)


def empty_dict():
    return field(default_factory=dict)


def empty_set():
    return field(default_factory=set)


URI = NewType('URI', str)


@dataclass(init=False)
class Root:
    def __post_init__(self):
        self._fix_elements()

    def _fix_elements(self):
        pass


def root_representer(dumper: yaml.Dumper, data: Root):
    rval = dict()
    for k, v in data.__dict__.items():
        if not k.startswith('_') and v is not None and (not isinstance(v, (dict, list)) or v):
            rval[k] = v
    return dumper.represent_data(rval)


yaml.add_multi_representer(Root, root_representer)


def as_yaml(schema: Dict[str, object]) -> str:
    return yaml.dump(schema)
