---
layout: default
---

[![Build Status](https://travis-ci.org/biolink/biolink-model.svg?branch=master)](https://travis-ci.org/biolink/biolink-model)

# Biolink Model 2.0 Migration Guide

### Summary of chemical changes in Biolink-Model 2.0.0

![Chemical Hierarchy for Biolink-Model 2.0.0](images/chemical_entity.png)

 * Refactor of the 'Molecular Entity' and 'Chemical Substance' classes and hierarchy.
 * 'Genomic Entity' is now a 'mixin' rather than a class.
 * 'Chemical Substance' class is deprecated in favor of 'Small Molecular Entity' (child of 'Molecular Entity').
 * New classes: 'Chemical Entity', 'Chemical Aggregate', 'Complex Chemical Aggregat'e, 'Small Molecular Entity', 'Polypeptide', 'Nucleic Acid Entity'.
 * 'Gene' now is a child of 'Nucleic Acid Entity'.
 * 'Nucleic Acid Entity' now groups DNA, RNA, etc.
 * 'Protein' is a child of 'Polypeptide'.
 * 'Carbohydrate', 'FoodComponent', and 'Metabolite' are deprecated.

### Summary of evidence/provenance related changes in Biolink-Model 2.0.0
 
 * New classes: 'Information Resource'
 * New association slots (edge properties): 'knowledge source', 'primary knowledge source', 'original knowledge source', 'aggregator knowledge source', 'supporting data source'

### Summary of reaction related changes in Biolink-Model 2.0.0
![reaction_image_cont](images/reactions-cont.png) 
![reaction_image](images/reactions.png) 

 * New association classes: ‘Reaction To Participant Association’, ‘Reaction To Catalyst Association’.
 * New predicates (and inverses): 'catalyzes', 'has substrate', 'consumes'.
 * EC numbers help define the 'Molecular Activity' class.  

### Inverses 

 * added inverses for the majority of biolink predicates.
 * primary direction of predicate tagged with 'biolink:canonical_predicate'.

### Deprecated items removed
 
 * assciation_id, edge label, association type, disease or phenotypic feature association to location association.
