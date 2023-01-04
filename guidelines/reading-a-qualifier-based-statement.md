---
title: "Reading a Qualifier-Based Statement"
parent: "Biolink Model Guidelines"
layout: default
nav_order: 3
---

## Reading a Qualifier-Based Statement

Here we provide below a guide for how to ‘read’ the meaning of an Association Statement by composing the semantics encoded in its SPOQ slots.  Note that many such Associations will consist only of a subject-predicate-object triple - in which case a reading of the statement expressed is straight-forward.  When qualifiers are included, this introduces a second level of meaning that complements the statement made by the core SPO triple. This idea that there can be two related statements at two levels of granularity encoded in a single Association is a critical idea behind the qualifier-based approach:
The first level is the Core Triple Reading of the Association, which considers only the subject, predicate, and object slots.  This reading must be clear and true.
The second level is the Full Statement Reading of the Association, which considers the semantics added by qualifier slots (subject/object qualifiers, and statement qualifiers).  This reading must also be clear and true as well (which often requires use of a qualified_predicate). 
Note that the Full Statement Reading provides additional detail or context for the claim made in the core triple. It should not represent a completely independent or unrelated statement.

### Example: Composing Qualifier Semantics
The example below shows a complex Association Statement that utilizes each of these types of node qualifier slots to 
represent a record from the CTD database that asserts “A Hexachlorobenzene metabolite increases methylation of a 
mutant form of the CDKN2A promoter in the nucleus of HeLa cells”.

```
subject: CHEBI:5692 # Hexachlorobenzene
subject_derivative: metabolite
predicate: biolink:affects
qualified_predicate: biolink:causes
object:  NCBIGene:1029 # CDKN2A
object_part: promoter
object_form_or_variant: mutant_form
object_aspect:  methylation
object_direction: increased
object_context: "UBERON:0001013" # nucleus, 
experimental_context_qualifier: HeLa cells
```

To extract the assertions encoded in this structure:
- Read the Core S-P-O Triple:  This first layer of meaning is comprised only of the ‘core concepts’ captured in the subject and object slots, and the predicate which expresses a true,  high-level relationship between them.
“Hexachlorobenzene affects CDKN2A”
- Compose the Full Subject and Object Concepts:  
When there are subject/object qualifiers in the Association, combine the core concepts with their qualifiers to compose their full meaning.
  - Full/composed subject concept = “Hexachlorobenzene metabolite”
  - Full/composed object concept = “Increased Methylation of a mutant form of the CDKN2A promoter in the nucleus”
- Read the Full Statement:  
  - Read the relationship between the composed subject and object concepts, along with additional info/context provided by 
any statement-level qualifiers or quantifiers.  
  - When provided, the qualified_predicate should be used in this full statement reading.  
`“Hexachlorobenzene metabolite causes Increased methylation of a mutant form of the CDKN2A promoter in the nucleus of HeLa cells”`

### Example: Ordered Application of Qualifier Semantics to Compose an Object Node Concept

In cases where  there are multiple qualifiers on a single subject or object concept, we can provide conventions for the
order in quch qualifier semantics are layered onto the core concept.  This can facilitate the semantic interpretation 
of a statement, and remove ambiguity where different qualifier ordering results in subtly different statement meaning 
(see Box 2).

- object: the simple core concept ‘X’
  - e.g. the CDKN2A gene
- object_part: a particular part of ‘X’ 
  - e.g. the promoter of the CDKN2A gene
- object_form_or_variant:  a particular form of this part of ‘X’
  - e.g. a modified form of the promoter of the CDKN2A gene
- object_aspect: a particular aspect of this form of this part of ‘X’ (e.g. its abundance, its transport)
  - e.g. methylation of a modified form of the promoter of the CDKN2A gene
- object_direction:  an increase or decrease in this particular aspect of ‘X’
  - e.g. increased methylation of a modified form of the CDKN2A promoter 
- object_context: an inc/dec of a particular aspect of this form of this part of ‘X’, in a particular context
  - e.g. increased methylation of a modified form of the CDKN2A promoter in the nucleus

Importantly, each new qualifier layer applies to the concept composed by all qualifiers preceding it. So in the 
example above, the ‘methylation’ aspect applies to the concept composed by the three qualifiers preceding it 
(‘a mutant form of the promoter of the CDKN2A gene’), not directly to the core concept (‘CDKN2A’).


