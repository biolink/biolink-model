#!/usr/bin/python3
"""
This initial version of the scripts assumes that the 'predicates' TSV file
has the structure of the Anne Thessen September 2020 predicate inventory at
https://docs.google.com/spreadsheets/d/1bnEk6Fs6n_pCYL73cl4G4_igbeCtilV7xEvt3W6hS9k/edit#gid=0
"""
from sys import stdout
from typing import Union, TextIO
import argparse

# from linkml_runtime.linkml_model.meta import SchemaDefinition


class PredicateInventory():

    # def __init__(self, schema: Union[str, TextIO, SchemaDefinition], predicates, log) -> None:
    def __init__(self, schema: Union[str, TextIO], predicates, log) -> None:
        self.schema = schema
        self.predicates = predicates
        if log:
            self.log = open(log, 'w')
        else:
            self.log = None  # defaults to stdout

        print("Schema: ", schema, file=self.log)
        print("Predicates: ", predicates, file=self.log)

    def parse(self):
        n = 0
        with open(self.predicates, 'r') as predicates:
            # skip the header
            header = predicates.readline().split('\t')
            print("Headers: ", header, self.log)

            # skip the definitions
            definitions = predicates.readline().split('\t')
            print("Definitions: ", definitions, file=self.log)

            for line in predicates:
                n += 1
                if n % 10:
                    # Process each line
                    field = line.split('\t')

                    # Review log predicates with "Biolink Slot" mappings (i.e. edge_label mapped predicates)
                    if field[5]:
                        # Ignore mappings where the "Source Relationship ID" is empty?
                        if not field[2]:
                            print("Empty Source ID: ", field[0], "|", field[1], "| |", field[5], file=self.log)
                            continue

                        # Ignore mappings where the "Source Relationship ID"
                        # is already identical to the Biolink predicate
                        if field[2] == field[5]:
                            print("Source ID equals Biolink Slot: ", field[0], "|", field[1], "|", field[2], "|", field[5], file=self.log)
                            continue

                        print("Check: ", field[0], "|", field[1], "|", field[2], "|", field[5], file=self.log)

                    elif field[2]:
                        #  Perhaps we can now use a non-empty "Source Relationship ID" to attempt a Biolink Mapping
                        print("Resolve: ", field[0], "|", field[1], "|", field[2], "'?", file=self.log)

                    else:
                        #  do something with the exceptions here?
                        #  or don't bother for now, since they are easily reviewed in the original file?
                        print("Exception: ", field[0], "|", field[1], "|", field[2], "|", field[5], file=self.log)
                        continue


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='A generator for parsing an input TSV of predicate info')
    parser.add_argument('--schema',  help='the YAML Schema file', required=True)
    parser.add_argument('--predicates',  help='the TSV file of predicate inventory to be scanned', required=True)
    parser.add_argument('--log', help='the output log file', default=None)

    args = parser.parse_args()
    PredicateInventory(schema=args.schema, predicates=args.predicates, log=args.log).parse()
