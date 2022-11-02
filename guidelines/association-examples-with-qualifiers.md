---
title: "Association Examples with Qualifiers"
parent: "Biolink Model Guidelines"
layout: default
nav_order: 1
---

## Chemical affects Gene Association

Here we take some real-world examples of knowledge statements from a variety of sources
and describe how they would be represented in Biolink Model.

### Example 1: 

"Methionine deficiency results in increased expression of ADRB2 in adipose tissue"

- json
```json
{
  "id": "e0",
  "category": "biolink:ChemicalAffectsGeneAsociation",
  "subject": "CHEBI:16811", # methionine
  "subject_aspect_qualifier": "abundance",
  "subject_direction_qualifier": "decreased",
  "predicate": "biolink:affects",
  "qualified_predicate": "biolink:causes",
  "object": "NCBIGene:154", # ADRB2
  "object_aspect_qualifier" : "expression",
  "object_direction_qualifier" : "increased",
  "biolink:original_knowledge_source": "infores:molepro",
  "biolink:anatomical_context_qualifier": "UBERON:0001013" # adipose tissue
}
```

- KGX flat file (edges.tsv)
```tsv
subject, predicate, object, qualified_predicate, subject_aspect_qualifier, subject_direction_qualifier, object_aspect_qualifier, object_direction_qualifier, anatomical_context_qualifier
CHEBI:16811, biolink:affects, NCBIGene:154, biolink:causes, abundance, decreased, expression, increased, UBERON:0001013
```

- TRAPI (Translator API specification, knowledge graph representation)

https://github.com/NCATSTranslator/ReasonerAPI/blob/master/examples/Message/subject_and_object_qualifiers.json

```json
{
  "knowledge_graph": {
    "nodes": {
      "PUBCHEM.COMPOUND:6137": {
        "categories": [
          "biolink:ChemicalEntity"
        ],
        "name": "Methionine"
      },
      "HGNC:286": {
        "categories": [
          "biolink:GeneOrGeneProduct"
        ],
        "name": "ADRB2"
      }
    },
    "edges": {
      "x17770": {
        "predicate": "biolink:affects",
        "subject": "PUBCHEM.COMPOUND:6137",
        "object": "HGNC:286",
        "qualifiers": [
          {
            "qualifier_type_id": "biolink:subject_aspect_qualifier",
            "qualifier_value": "abundance"
          },
          {
            "qualifier_type_id": "biolink:subject_direction_qualifier",
            "qualifier_value": "decreased"
          },
          {
            "qualifier_type_id": "biolink:qualified_predicate",
            "qualifier_value": "causes"
          },
          {
            "qualifier_type_id": "biolink:object_aspect_qualifier",
            "qualifier_value": "expression"
          },
          {
            "qualifier_type_id": "biolink:object_direction_qualifier",
            "qualifier_value": "increased"
          }
        ]
      }
    }
  }
}
```


### Example 2:

""