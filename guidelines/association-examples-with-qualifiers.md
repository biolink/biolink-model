---
title: "Association Examples with Qualifiers"
parent: "Biolink Model Guidelines"
layout: default
nav_order: 2
---

## Chemical affects Gene Association

Here we take some real-world examples of knowledge statements from a variety of sources
and describe how they would be represented in Biolink Model.

### Example 1: 

"Methionine deficiency results in increased expression of ADRB2 in adipose tissue"

In keeping with our modeling paradigms (see [Curating The Model](guidelines/curating-the-model.md))
- Nodes should represent core domain concepts
- Use qualifiers to compose full node semantics
- The ‘core triple’ should remain true if qualifiers are ignored. (except 'negation', 'negation' should never be ignored)
- Control predicate proliferation
- Represent information consistently

We need to break this statement into its core components that are most likely going to be shared across many statements
and data sources.  In this example sentence, we can first break it apart into three parts or core components:
- Methionine (biolink:subject)
- affects (biolink:predicate)
- ADRB2 (biolink:object)

This is our "core triple" and its subject and object are broken down from the example above so that they are concepts
that are most likely to be shared across many statements and data sources.  We might find more data sources that talk
about "Methionine" than "Methionine deficiency" and we might find more data sources that talk about "ADRB2" as a "thing"
than "increased expression of ADRB2 in adipose tissue".  So we want to break down the example sentence into its core 
components without making a false statement.  

Notes: 
- Use of the Biolink model does not require, always, the use of less specific subject and
object concepts, some use knowledge graphs may choose to use a more specific subject and object category to fulfill their 
use cases.  But for this example, we apply Biolink categories at a higher level in the core triple to increase the 
connectivity possibilities of the data.

- Note the use of the "affects" predicate.  Here we are careful to use a predicate that keeps the core triple true despite
our modification of the subject and object.  If we were to use "increases expression of" as a predicate here, we would 
be invalidating the "core tripe is true" principle.

- Despite our preference for connectivity, we don't want to lose the specificity of our original knowledge statement.  
We can capture the nuance and specificity (expression, abundance) in qualifiers.

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