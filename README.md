[![Build Status](https://travis-ci.org/biolink/biolink-model.svg?branch=master)](https://travis-ci.org/biolink/biolink-model)

# biolink-models

Browse the model: [https://biolink.github.io/biolink-model](https://biolink.github.io/biolink-model)

# Intro

A high level datamodel of biological entities (genes, diseases,
phenotypes, pathways, individuals, substances, etc) and their
associations.

The immediate goal is to provide a __reference datamodel__ that is
independent of storage technology (solr, neo4j, csvs, etc). 

The specification of the reference biolink model is a [single YAML
file](biolink-model.yaml) following a custom meta-model. The basic
elements of the YAML are:

 - definitions of upper level *classes* representing both named things
(genes, phenotypes, etc) and associations between them
 - definitions of *slots* (aka properties) that can be used to relate
   members of these classes to other classes or datatypes


