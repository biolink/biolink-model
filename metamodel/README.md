# Yet Another MetaModel (YAMM)

This directory contains information and code about the metamodel
formalism used to specify the biolink model.

It is in theory generic, so it may move to a standalone repo in the
future.

## Spec

YAMM is self-specifying

 * [../meta.yaml](../meta.yaml) - the yamm model specified in yamm

## Code

 * [metamodel.py](metamodel.py) - python OO model (auto-generated from meta.yaml)
 * [metaschema.py](metaschema.py) - marshmallow definitions (for reading yaml into OO model)
 * generators
    * [golr_yaml_gen.py](golr_yaml_gen.py)
    * [jsonschemagen.py](jsonschemagen.py)
    * [pygen.py](pygen.py)
