# Yet Another MetaModel (YAMM)

This directory contains information and code about the metamodel
formalism used to specify the biolink model.

It is in theory generic, so it may move to a standalone repo in the
future.

## Spec

YAMM is self-specifying

 * [../meta.yaml](../meta.yaml) - the yamm model specified in yamm

This is used to generate the marshmallow schema and the python class definitions

## Code

 * [metamodel.py](metamodel.py) - python OO model (auto-generated from meta.yaml)
 * [generators](generators) - various YAMM to code and other representations

