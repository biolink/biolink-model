from linkml_runtime.utils.schemaview import SchemaView
from linkml.generators.prefixmapgen import PrefixGenerator
from linkml_runtime.utils.formatutils import camelcase
from classprefixes import BiolinkClassPrefixMap, Prefix
from linkml_runtime.dumpers.json_dumper import JSONDumper
import os

OUT_JSON = os.path.join('../prefix-map/preferred_prefixes_per_class.json')

class IDPrefixes:

    def __init__(self) -> None:
        self.sv = SchemaView('../biolink-model.yaml')

    def dump(self):

        prefixmap = PrefixGenerator('../biolink-model.yaml')
        bcpm = BiolinkClassPrefixMap()

        for cls, clsdef in self.sv.all_classes().items():
            prefix_map = []
            if clsdef.id_prefixes and not clsdef.mixin:
                for prefix in clsdef.id_prefixes:
                    p = Prefix(prefix=prefix, base_uri=prefixmap.namespaces[prefix])
                    prefix_map.append(p)
                bcpm.class_name = "biolink:"+camelcase(cls)
                bcpm.prefix_map = prefix_map

        jd = JSONDumper()
        jd.dump(bcpm, to_file=OUT_JSON)

if __name__ == "__main__":
    IDPrefixes().dump()
