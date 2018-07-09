import os
import unittest

from metamodel.metamodel import SchemaDefinition, SchemaDefinitionId, SchemaDefinitionName
from metamodel.utils.schemaloader import SchemaLoader
from metamodel.utils.schemasynopsis import SchemaSynopsis
from metamodel.utils.typereferences import ClassType, TypeType, SlotType, References
from tests import refresh_files

update_source: bool = False


class SynopsisTestCase(unittest.TestCase):

    def compare_synopsis(self, yaml_fname, model_name) -> None:
        cwd = os.path.abspath(os.path.dirname(__file__))
        path = os.path.abspath(os.path.join(cwd, '..', yaml_fname))
        sourcedir = os.path.join(cwd, 'source')

        meta_schema = SchemaLoader(path).resolve()
        synopsis = SchemaSynopsis(meta_schema)
        errors = synopsis.errors()
        if errors:
            print("***** ERRORS *****")
            error_str = '\n'.join(errors)
            print(error_str)
            self.assertFalse(True, "Errors encountered")
        summary = synopsis.summary()

        sourcepath = os.path.join(sourcedir, model_name + '_synopsis.txt')
        if update_source or refresh_files:
            with open(sourcepath, 'w') as masterf:
                masterf.write(summary)
            if refresh_files:
                print(f'{sourcepath} updated')

        with open(sourcepath) as masterf:
            self.assertEqual(masterf.read(), summary)
        self.assertFalse(update_source, "update_source must be set to false")

    def test_code(self):
        self.assertEqual('Class', str(ClassType))
        r = References()
        r.addref(ClassType, "a")
        r.addref(TypeType, "b")
        r.addref(SlotType, "c")
        self.assertEqual("References(classrefs={'a'}, slotrefs={'c'}, typerefs={'b'})", repr(r))
        with self.assertRaises(TypeError):
            r.addref(None, 'd')         # Lint check error ok here

        s = SchemaSynopsis(SchemaDefinition(id=SchemaDefinitionId('test'), name=SchemaDefinitionName('test')))
        s.add_ref(SlotType, 's1', ClassType, 'c1', )
        self.assertEqual('SchemaSynopsis(classes=set(), slots=set(), types=set(), slotrefs={}, '
                         "typerefs={}, classrefs={'c1': References(classrefs=set(), slotrefs={'s1'}, "
                         'typerefs=set())}, unions={}, isarefs={}, mixinrefs={}, '
                         'roots=References(classrefs=set(), slotrefs=set(), typerefs=set()), '
                         'mixins=References(classrefs=set(), slotrefs=set(), typerefs=set()), '
                         'abstracts=References(classrefs=set(), slotrefs=set(), typerefs=set()), '
                         'domainrefs={}, rangerefs={}, inverses={}, slotdomains={}, mtdomains=set(), '
                         'typeofs={}, classslots={}, slotclasses={}, definingslots={}, slotusages={}, '
                         'applytos={})', repr(s))

    def test_meta_synopsis(self):
        self.compare_synopsis('meta.yaml', 'metamodel')

    def test_biolink_synopsis(self):
        self.compare_synopsis('biolink-model.yaml', 'biolink model')


if __name__ == '__main__':
    unittest.main()
