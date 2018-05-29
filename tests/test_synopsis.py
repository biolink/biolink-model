import os
import unittest

from metamodel.schemaloader import load_schema
from metamodel.schemasynopsis import SchemaSynopsis, ClassType, References, TypeType, SlotType

update_source: bool = False


class SynopsisTestCase(unittest.TestCase):

    def compare_synopsis(self, yaml_fname, model_name) -> None:
        cwd = os.path.abspath(os.path.dirname(__file__))
        path = os.path.abspath(os.path.join(cwd, '..', yaml_fname))
        sourcedir = os.path.join(cwd, 'source')

        meta_schema = load_schema(path)
        synopsis = SchemaSynopsis().eval_schema(meta_schema[model_name]).summary()
        sourcepath = os.path.join(sourcedir, model_name + '_synopsis.txt')
        if update_source:
            with open(sourcepath, 'w') as masterf:
                masterf.write(synopsis)

        with open(sourcepath) as masterf:
            self.assertEqual(masterf.read(), synopsis)
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

        s = SchemaSynopsis()
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
