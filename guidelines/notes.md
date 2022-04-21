# Installation and Usage Notes

The Biolink Model is defined as a YAML. Any changes or edits are to be made to this YAML.

We make use of [linkML](https://github.com/linkml) library to generate various artifacts from the YAML.


## Installation

The generation of Biolink Model artifacts requires Python 3.7+ because it makes extensive use of 
Python `dataclasses` library. 

The standard approach is to install Python 3.7+ on your machine (see: [http://python.org/]() for details).


## Generate artifacts

All artifact generation is driven by the Makefile:

```bash
make all
```

### Generate Python dataclasses

To generate Python dataclasses,
```bash
make python
```

### Generate ShEx

To generate Shape Expressions,
```bash
make shex
```

### Generate JSON-LD context

To generate Biolink Model JSON-LD context,
```bash
make context.jsonld
```
