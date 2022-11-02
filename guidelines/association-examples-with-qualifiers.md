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

In keeping with our modeling paradigms ([Curating The Model](guidelines/curating-the-model.md))
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

This is our "core triple". 

Some design decisions that went into selecting this core triple:
- Use of the Biolink model does not require, always, the use of less specific subject and
object concepts, some use knowledge graphs may choose to use a more specific subject and object category to fulfill their 
use cases.  But for this example, we apply Biolink categories at a higher level in the core triple to increase the 
connectivity possibilities of the data.

- The "affects" predicate was chose here because we are being careful to use a predicate that keeps the core triple true despite
our choice of subject and object.  If we were to use "increases expression of" as a predicate here, we would 
be invalidating the "core tripe is true" principle (as our subject, "Methionine" is the opposite of "Methionine deficiency").

Despite our preference for connectivity, we don't want to lose the specificity of our original knowledge statement.  
We can capture the nuance and specificity (expression, abundance) in qualifiers.  The aspect of Methionine that we 
want to capture is the "decreased abundance" of it.  The aspect of ADRB2 that we want to capture is the "increased expression" of it.
These two aspects, "abundance" and "expression" are represented in the Biolink model as "aspect qualifiers". 
The direction of the aspect, is represented in the Biolink model as "direction qualifiers".  Finally, we can have a 
qualifier that applies to the entirety of the fully qualified statement, an "anatomical context qualifier" that expresses
that this statement all takes place in the "adipose tissue." Therefore, the fully 
qualified statement, using our core triple would be: 


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

"Fenofibrate binds to PPARA protein"  - This is a simple `Chemical interacts with Gene` statement (no qualifiers needed)

```json
{
  "id": "e0",
  "category": "biolink:ChemicalAffectsGeneAsociation",
  "subject": "CHEBI:5001"  # Fenofibrate
  "predicate": "biolink:physically_interacts_with"
  "object": "NCBIGene:5465"  # PPARA
}
```

### Example 3:

"Cyclophosphamide affects the hydroxylation of CYP2B6" - A simple chemical affects gene (aspect) Statement  - no direction to the effect. 

```json
{
  "id": "e0",
  "category": "biolink:ChemicalAffectsGeneAsociation",
  "subject": "CHEBI:16811"  # Cyclophosphamide,
  "predicate": "biolink:affects",
  "object": "NCBIGene:154"  # CYP2B6,
  "object_aspect_qualifier": "hydroxylation"
}
```

### Example 4:

"Bisphenol A results in decreased degradation of ESR1 protein" - A Statement where the effect has a direction (decreased)
    
```json
    {
    "id": "e0",
    "category": "biolink:ChemicalAffectsGeneAsociation",
    "subject": "CHEBI:16811"  # Bisphenol A,
    "predicate": "biolink:affects",
    "qualified_predicate": "biolink:causes",
    "object": "NCBIGene:2099"  # ESR1,
    "object_aspect_qualifier": "degradation",
    "object_direction_qualifier": "decreased"
    }
```

### Example 5: 

"Bisphenol A is associated with decreased degradation of ESR1 protein" - A (hypothetical) chemical associated_with 
gene (aspect)  Statement with same S/O concepts as above

```json
{
  "id": "e0",
  "category": "biolink:ChemicalAffectsGeneAsociation",
  "subject": "CHEBI:16811"  # Bisphenol A,
  "predicate": "biolink:associated_with",
  "object": "NCBIGene:2099"  # ESR1,
  "object_aspect_qualifier": "degradation",
  "object_direction_qualifier": "decreased"
}
```

### Example 6:

"Progesterone metabolites cause decreased methylation of APP promoter mutant forms" - A more complex example where a 
metabolite of the specified chemical is the effector of a heavily qualified Statement object.

```json
{
  "id": "e0",
  "category": "biolink:ChemicalAffectsGeneAsociation",
  "subject": "CHEBI:17026"  # Progesterone,
  "predicate": "biolink:affects",
  "qualified_predicate": "biolink:causes",
  "object": "NCBIGene:351"  # APP,
  "object_aspect_qualifier": "methylation",
  "object_direction_qualifier": "decreased",
  "object_part_qualifier": "promoter",
  "object_form_or_variant_qualifier": "mutant"
}
```

### Example 7:

“Hexachlorobenzene analog causes increased methylation of CDKN2A enhancer alternative form”  - Another complex example 
where an analog of a specified chemical is the effector of a heavily qualified Statement object.

```json
{
  "id": "e0",
  "category": "biolink:ChemicalAffectsGeneAsociation",
  "subject": "CHEBI:16811"  # Hexachlorobenzene,
  "subject_form_or_variant_qualifier": "analog",
  "predicate": "biolink:affects",
  "qualified_predicate": "biolink:causes",
  "object": "NCBIGene:1029"  # CDKN2A,
  "object_aspect_qualifier": "methylation",
  "object_direction_qualifier": "increased",
  "object_part_qualifier": "enhancer",
  "object_form_or_variant_qualifier": "modified"
}
```

### Example 8:

"Fenofibrate is an agonist of PPARA protein” - Chemical increases  gene activity, via a specific control mechanism (agonism)

```json
{
  "id": "e0",
  "category": "biolink:ChemicalAffectsGeneAsociation",
  "subject": "CHEBI:5001"  # Fenofibrate,
  "predicate": "biolink:afects",
  "qualified_predicate": "biolink:causes",
  "object": "NCBIGene:5465"  # PPARA,
  "object_aspect_qualifier": "activity",
  "object_direction_qualifier": "increased",
  "causal_mechanism_qualifier": "agonism"
}
```
