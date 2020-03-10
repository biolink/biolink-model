---
layout: default
title: Working with Biolink Model
nav_order: 4
---

# Working with Biolink Model

For Biolink Model, the main source of truth is the [YAML](biolink-model.yaml).

If you would like to work with the model in a programmatic way then make use of [Biolink Model Toolkit](https://github.com/biolink/biolink-model-toolkit).

It is a lightweight API on top of the YAML.

Biolink Model Toolkit provides several methods for accessing and navigating the classes and slots defined in the YAML.
It also provides lookup operations that allows easy navigation of various elements in the model.

The toolkit makes use of [biolinkml](https://github.com/biolink/biolinkml), the same metamodeling framework used for 
building the model.
