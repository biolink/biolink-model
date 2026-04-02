# Biolink Entity Matrix Spreadsheet

## Overview

`biolink_entity_matrix.xlsx` contains a matrix of biolink subject and object class combinations, intended for cataloging which data sources provide edges for each subject-object pair.

Generated from `biolink-model.yaml` (v4.3.7) using `linkml_runtime.SchemaView` to programmatically extract all classes and association constraints. No classes were manually added or guessed.

## Tabs

### Tab 1: Entity Matrix - Data Sources

A blank 157x157 matrix where:
- **Rows** = subject biolink classes (all `named thing` descendants, excluding associations)
- **Columns** = object biolink classes (same set)
- **Cells** = empty, to be filled in manually with data source names

**Example usage:** At the intersection of `gene` (row) and `phenotypic feature` (column), write "Monarch Initiative" to indicate that Monarch provides gene-to-phenotypic-feature edges.

### Tab 2: Association Constraints

Same 157x157 matrix, but pre-filled based on the `subject` and `object` range constraints defined in biolink association classes:
- **Green cells** indicate that at least one biolink association class defines that subject-object combination
- **Cell values** list the association class name(s) that define the pairing
- Ranges were expanded through the `is_a` hierarchy (e.g., if an association declares `subject` range as `gene or gene product`, all descendants of that class are included)

This tab shows which subject-object combinations are formally modeled in the biolink schema via the 104 association classes.

## How It Was Generated

```python
from linkml_runtime.utils.schemaview import SchemaView

sv = SchemaView('biolink-model.yaml')

# Entity classes: all descendants of 'named thing' excluding associations
# Association constraints: induced slots for 'subject' and 'object' on each association class,
#   expanded via class_descendants() to capture the full is_a hierarchy
```

## Entity Classes (157)

All descendants of `named thing` that are not associations, including classes such as:
- gene, protein, disease, phenotypic feature, pathway, drug, chemical entity
- anatomical entity, cell, cellular component, gross anatomical structure
- organism taxon, individual organism, population of individual organisms
- sequence variant, genotype, haplotype, genome
- publication, article, book, dataset
- clinical finding, clinical trial, treatment, procedure
- exposure event, environmental exposure, drug exposure
- and many more (see Tab 1 headers for the full list)

## Association Classes (104)

All descendants of `association`, including classes such as:
- gene to disease association, gene to phenotypic feature association
- variant to disease association, genotype to phenotypic feature association
- chemical to disease or phenotypic feature association
- disease to phenotypic feature association
- and many more (see Tab 2 cell values for the full list)
