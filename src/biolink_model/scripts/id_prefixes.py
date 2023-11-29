from linkml_runtime.utils.schemaview import SchemaView
from linkml.generators.prefixmapgen import PrefixGenerator
from linkml_runtime.utils.formatutils import camelcase
from classprefixes import BiolinkClassPrefixMap, Prefix, BiolinkClassPrefixesCollection
from linkml_runtime.dumpers.json_dumper import JSONDumper
import os

OUT_JSON = os.path.join('../../../project/prefixmap/preferred_prefixes_per_class.json')
OUT_CSV = os.path.join('../../../project/prefixmap/preferred_prefixes_per_class.csv')


class IDPrefixes:

    def __init__(self) -> None:
        self.pmsv = SchemaView('../../../class_prefixes.yaml')
        self.sv = SchemaView('../../../biolink-model.yaml')

    def dump(self):

        prefixmap = PrefixGenerator('../../../biolink-model.yaml')
        bpcc = BiolinkClassPrefixesCollection()
        for cls, clsdef in self.sv.all_classes().items():
            prefix_map = []
            if clsdef.id_prefixes and not clsdef.mixin:
                bcpm = BiolinkClassPrefixMap()
                bcpm.class_name = "biolink:" + camelcase(cls)
                counter = 0
                for prefix in clsdef.id_prefixes:
                    counter = counter + 1
                    p = Prefix(prefix=prefix, base_uri=prefixmap.namespaces[prefix], order=counter)
                    prefix_map.append(p)
                bcpm.prefix_map = prefix_map
                bpcc.biolink_class_prefixes.append(bcpm)
        jd = JSONDumper()
        jd.dump(bpcc, to_file=OUT_JSON)


if __name__ == "__main__":
    IDPrefixes().dump()
