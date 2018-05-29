import os

from metamodel.schemaloader import load_schema
from metamodel.shexgen import ShexGenerator


def test_school_model():
    cwd = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(cwd, '..', 'biolink-model.yaml')) as f:
        schema = load_schema(f)
    g = ShexGenerator(schema=schema)
    print(g.serialize())


if __name__ == "__main__":
    test_school_model()