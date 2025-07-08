---
title: "Knowledge Source Retrieval Provenance"
parent: "Biolink Model Guidelines"
layout: default
nav_order: 9
---

# Knowledge Source Retrieval Provenance

### What is Source Retrieval Provenance?
'Source retrieval provenance' describes the set of Information Resources through which the knowledge expressed in an 
Edge was passed, through various retrieval and/or transform operations, on its way to its current serialized form. 
For example, the provenance of a Gene-Chemical Edge in a message to a Translator ARA (e.g. ARAGORN) might be traced 
through the Translator KP that provided it (e.g. MolePro), one or more intermediate aggregator resources (e.g. ChEMBL), 
and back to the resource that originally created/curated it (e.g. ClinicalTrials.org).

 ```
 ARAGORN (NCATS Translator Automatic Relay Agent  --retrieved_from-->   MolePro  --retrieved_from-->  ChEMBL  --retrieved_from-->  ClinicalTrials.gov
 ```

To be clear, source retrieval provenance concerns the mechanical retrieval and transformation of data between web 
accessible information systems. It does not trace the source of knowledge back to specific publications or data sets.
And it is not concerned with the reasoning, inference or analysis activities that generate knowledge from evidence 
in the first place.

### A Shared Set of Biolink Edge Properties (Standardize the Key)
We define the following hierarchy of edge properties in Biolink for recording Information Resources through which knowledge expressed in a given edge was retrieved on its way to its presently serialized form (e.g. a TRAPI message sent to an ARA). Full definitions and metadata for each can be found in the Biolink Model.
 
- biolink:knowledge_source (doesn't commit to the resource being aggregator, primary, or original. an abstract grouping property).
  - biolink:primary_knowledge_source (used for the furthest upstream resource in the chain that the data creator can identify)
  - biolink:aggregator_knowledge_source (retrieved and possibly transformed the knowledge from some other information resource)
- biolink:supporting_data_source (used for resources providing data that reasons with or computes on to generate new knowledge)
 
### Implementation Guidance: 

These properties allow data creators to indicate the role of each source in the provenance trail of knowledge expressed in a given Edge, to whatever extent this role is known. 
Our recommendation would be for data creators to minimally distinguish primary (most upstream) from aggregator / intermediate sources - as this distinction should be knowable in all cases.
If the data creator is confident that the primary source was the original source, they can use the original_knowledge_source property. 
In practice, for a linear chain of retrieval, one source should be declared primary or original, and the rest aggregators.
Knowledge Providers will add source provenance related to upstream sources, as well as the provenance related to themselves in their data/messages.  

### A Shared Identifiers for Information Resources (Standardize the Value)

We also define a standard ‘InfoRes identifier’ for each Information Resource that provides data. The identifier component of the IRI is a short form human readable name or abbreviation.  
The following are examples of InfoRes IRI identifiers and their CURIE forms:
External Resource CURIE: infores:dgidb
Translator Resource CURIE: infores:molepro
