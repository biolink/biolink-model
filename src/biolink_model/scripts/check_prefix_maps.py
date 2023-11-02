import json
from pprint import pprint
import os
from curies import Converter


class CheckPrefixMaps:

    def __init__(self) -> None:
        self.prefix_map = json.load(open('../../../project/prefixmap/biolink-model-prefix-map.json'))

    def dump(self):
        pprint(self.prefix_map)


if __name__ == "__main__":
    CheckPrefixMaps().dump()
