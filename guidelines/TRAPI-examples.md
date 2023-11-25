---
title: "TRAPI Examples"
parent: "Biolink Model Guidelines"
layout: default
nav_order: 3
---

### TRAPI Examples

For reference, [here is the TRAPI 1.3 data representation](https://github.com/NCATSTranslator/ReasonerAPI/blob/b43cc5d95a9ae3678401092d1ddb97a5b0b82aae/TranslatorReasonerAPI.yaml#L852) for qualifiers.

The summary of TRAPI 1.3 support for qualifiers is as follows:

* Add a ‘qualifiers’ property to the Edge object
* Define a new Qualifier object 
* Extend QEdge model to include support for qualifier-constraints

To represent a query for "what decreases degradation of ESR1 protein", a TRAPI query graph would look like this:
```json
{
  "query_graph": {
    "nodes": {
      "n0": {
        "categories": ["biolink:ChemicalEntity"]
      },
      "n1": {
        "categories": ["biolink:GeneOrGeneProduct"],
        "ids": ["HGNC:3467"]
      }
    },
    "edges": {
      "e01": {
        "subject": "n0",
        "object": "n1",
        "predicates": [
          "biolink:affects"
        ],
        "qualifier_constraints": [
          {
            "qualifier_set": [
              {
                "qualifier_type_id": "biolink:object_aspect_qualifier",
                "qualifier_value": "degradation"
              },
              {
                "qualifier_type_id": "biolink:object_direction_qualifier",
                "qualifier_value": "decreased"
              }
            ]
          }
        ]
      }
    }
  }
}
```

and a TRAPI result would look like this:

```json
{
  "knowledge_graph": {
    "nodes": {
      "n0": {
        "categories": ["biolink:ChemicalEntity"],
        "name": "Bisphenol A"
      },
      "n1": {
        "categories": ["biolink:Gene"],
        "name": "ESR1"
      }
    },
    "edges": {
      "x17770": {
        "predicate": "biolink:affects",
        "subject": "PUBCHEM.COMPOUND:6623",
        "object": "HGNC:3467",
        "qualifiers": [
          {
            "qualifier_type_id": "biolink:object_aspect_qualifier",
            "qualifier_value": "degradation"
          },
          {
            "qualifier_type_id": "biolink:object_direction_qualifier",
            "qualifier_value": "decreased"
          }
        ]
      }
    }
  },
  "results": [
    {
      "node_bindings": {
        "n0": [
          {
            "id": "PUBCHEM.COMPOUND:6623"
          }
        ],
        "n1": [
          {
            "id": "HGNC:3467"
          }
        ]
      },
      "edge_bindings": {
        "e01": [
          {
            "id": "x17770"
          }
        ]
      }
    }
  ]
}
```
