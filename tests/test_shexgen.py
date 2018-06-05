import os

from metamodel.utils.schemaloader import load_raw_schema
from metamodel.generators.shexgen import ShexGenerator


def test_school_model():
    cwd = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(cwd, '..', 'biolink-model.yaml')) as f:
        schema = load_raw_schema(f)
    g = ShexGenerator(schema=schema)
    print(g.serialize())


if __name__ == "__main__":
    test_school_model()