import yaml
from dataclasses import dataclass
from jsonasobj import JsonObj

from metamodel.utils.formatutils import camelcase, underscore


@dataclass(init=False)
class YAMLRoot(JsonObj):
    def __post_init__(self):
        self._fix_elements()

    def _fix_elements(self):
        pass

    def _default(self, obj):
        """ JSON serializer callback.
        1) Filter out empty values (None, {}, [] and False) and mangle the names
        2) Add ID entries for dictionary entries

        :param obj: YAMLRoot object to serialize
        :return: Serialized version of obj
        """
        from metamodel.metamodel import ClassDefinition, SlotDefinition, TypeDefinition

        if isinstance(obj, JsonObj):
            rval = dict()
            for k, v in obj.__dict__.items():
                if not k.startswith('_') and v is not None and (not isinstance(v, (dict, list, bool)) or v):
                    if isinstance(v, dict):
                        itemslist = []
                        for vk, vv in v.items():
                            if isinstance(vv, ClassDefinition):
                                vv['@id'] = camelcase(vk)
                            elif isinstance(vv, (SlotDefinition, TypeDefinition)):
                                if k != 'slot_usage':
                                    vv['@id'] = underscore(vk)
                            itemslist.append(vv)
                        rval[k] = itemslist
                    else:
                        rval[k] = v
            return rval
        else:
            return super()._default(obj)


def root_representer(dumper: yaml.Dumper, data: YAMLRoot):
    """ YAML callback -- used to filter out empty values (None, {}, [] and false)

    @param dumper: data dumper
    @param data: data to be dumped
    @return:
    """
    rval = dict()
    for k, v in data.__dict__.items():
        if not k.startswith('_') and v is not None and (not isinstance(v, (dict, list)) or v):
            rval[k] = v
    return dumper.represent_data(rval)


yaml.add_multi_representer(YAMLRoot, root_representer)


def as_yaml(schema: YAMLRoot) -> str:
    return yaml.dump(schema)
