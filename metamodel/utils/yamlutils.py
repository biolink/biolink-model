from typing import Dict

import yaml
from dataclasses import dataclass


@dataclass(init=False)
class YAMLRoot:
    def __post_init__(self):
        self._fix_elements()

    def _fix_elements(self):
        pass


def root_representer(dumper: yaml.Dumper, data: YAMLRoot):
    rval = dict()
    for k, v in data.__dict__.items():
        if not k.startswith('_') and v is not None and (not isinstance(v, (dict, list)) or v):
            rval[k] = v
    return dumper.represent_data(rval)


yaml.add_multi_representer(YAMLRoot, root_representer)


def as_yaml(schema: YAMLRoot) -> str:
    return yaml.dump(schema)
