---
title: "Frequently Asked Questions"
parent: "Biolink Model Guidelines"
layout: default
nav_order: 6
---

### What happens if I have a concept, property, or edge in a graph that is not in the Biolink Model?

Please submit a ticket to our issue tracker: https://github.com/biolink/biolink-model/issues or submit
a pull request with your changes to the Biolink Model.

Note: a PR or ticket will be addressed faster by the modeling team by following these guidelines:

- All of our modeling and example data should be as clear as possible. 
- Textual annotations on classes, slots and enumerations should be written with minimal jargon
- If it is necessary to retain external content as-is, like descriptions, they should be attributed using the 
appropriate LinkML meta-slots, and we should also strive to provide clarification in appropriate meta-slots
- The structural definitions of elements (relationships with other elements) should agree with the textual description
(and vice versa)
- Team members  adding new modeling bear the responsibility of re-using existing elements or demonstrating to the team 
how their proposed alternative modeling is generally superior. When there are disagreements about modeling style, the 
disagreeing parties should each prepare two different implementations of the required modeling and talk through the 
advantages and disadvantages of each. This can be simplified by keeping pull requests small. Diligent modeling efforts 
should be acknowledged, especially for newer contributors. A decision to not merge
in part of the work does not mean that the work isn’t appreciated or has been thrown away, as closed but unmerged pull 
requests could be revisited in the future.
- LinkML provides micro-crediting metaslots. They can be used to acknowledge contributors outside of GitHub pull
request crediting and to time-stamp additions and changes.  They should be employed whenever possible, giving by default,
maximum credit to all parties that have significantly contributed to the model element.
https://linkml.io/linkml-model/latest/docs/contributors/
https://linkml.io/linkml-model/latest/docs/created_by/
https://linkml.io/linkml-model/latest/docs/created_on/
https://linkml.io/linkml-model/latest/docs/modified_by/
https://linkml.io/linkml-model/latest/docs/last_updated_on/




### What is the difference between `predicate` and `category`?

- `predicate` is an association slot and must have a value from the [`related to` hierarchy](https://biolink.github.io/biolink-model/docs/related_to)
- `category` (or `rdf:type`) is a slot and must have a value from the [`named thing`](https://biolink.github.io/biolink-model/docs/NamedThing)
or the [`association`](https://biolink.github.io/biolink-model/docs/Association) hierarchy.


### How do I assign Biolink classes and slots (e.g. nodes and attributes) to my data source?

Many data sources have their own data model that is not Biolink Model. They have their own objects and properties that 
might use different syntax, capture data at a different semantic level or a different granularity, or use different
identifiers.

Biolink Model uses components from the LinkML metamodel components (like `id_prefixes`, `exact, narrow, related, 
broad mappings`, `aliases`, `descriptions`) to help convey the concepts in the model to users.  However, this process
is often not automated and requires human curation.  Sometimes, capturing a higher level 


### What are some examples of Biolink Model usage?

The [NCATS Biomedical Translator Consortium](https://ncats.nih.gov/translator) has adopted Biolink Model as an open-source upper-level 
data model that supports semantic harmonization and reasoning across diverse Translator ‘knowledge sources’. 
The model serves a central role in the Translator program and forms the architectural basis of the Translator system, 
as described below. 

The Translator program aims to develop a comprehensive, relational, N-dimensional infrastructure designed to integrate disparate data 
sources—including objective signs and symptoms of disease, drug effects, chemical and genetic interactions, cell and organ pathology, 
and other relevant biological entities and relations—and reason over the integrated data to rapidly derive biomedical insights. 
The ultimate goal of Translator is to augment human reasoning and thereby accelerate translational science and knowledge discovery. 

To achieve its ambitious goal, the Translator project assembled a diverse interdisciplinary team and a variety of biomedical data 
sources, including electronic health record data, clinical trial data, genomic and other -omics data, chemical reaction data, and 
drug data. There are hundreds of data sources in the Translator ecosystem, each of which had its own data representation and were 
in formats that were not compatible or interoperable. Moreover, groups within the Translator Consortium had integrated the data 
sources as knowledge sources within independent KGs, but these KGs were developed using different technologies and formalisms 
such as property graphs in Neo4j and semantically-linked data via RDF and OWL. 

In order to interoperate between knowledge sources and reason across KGs, Biolink Model was adopted as the common dialect, thus 
enabling queries over the entire Translator KG ecosystem. The result was a federated, harmonized ecosystem that supports advanced 
reasoning and inference to derive biomedical insights based on user queries.

An example Translator use case involved a collaboration with investigators at the Hugh Kaul Precision Medicine Institute (PMI) at 
the University of Alabama at Birmingham. PMI investigators posed the following natural-language question to the Translator Consortium: 
what chemicals or drugs might be used to treat neurological disorders such as epilepsy that are associated with genomic 
variants of RHOBTB2? The investigators noted that RHOBTB2 variants cause an accumulation of RHOBTB2 protein and that this 
accumulation is believed to be the cause of the neurological disorder. 

To answer the PMI investigator’s question, Translator team members structured the following query: 
> NCBIGene:23221 (CURIE for RHOBTB2) -> [biolink:entity_regulates_entity, biolink:genetically_interacts_with] -> biolink:Protein, 
biolink:Gene -> [biolink:related_to] -> biolink:SmallMolecule

(see Figure 2 below). Because of the hierarchical structure of the Biolink model,
the use of biolink:related_to also will return more specific predicates such as biolink:negatively_regulates and biolink:positively_regulates. 
The objective was to identify drugs or chemicals that might regulate RHOBTB2 in some manner and thereby reduce the variant-induced 
accumulation of RHOBTB2 and associated neurological symptoms. As all nodes and edges within the Translator KG ecosystem are 
annotated to Biolink Model classes and attributes, a Translator query can be constructed from a natural-language user question 
and return results across a multitude of independent data sources. In addition, because the model employs hierarchical classes, 
with inheritance and polymorphism, natural-language queries translated to graph queries using Biolink Model syntax can be 
constructed at varying levels of granularity and return results from all levels of the hierarchy. Finally, because Biolink 
Model provides attributes on both edges and nodes that record provenance and evidence for these knowledge statements, each 
result is annotated with the trail of evidence that supports it.

When Translator team members sent the query to the Translator system, it returned several candidates of interest to PMI investigators, 
including fostamatinib disodium (CHEMBL.COMPOUND:CHEMBL3989516) and ruxolitinib (CHEMBL.COMPOUND:CHEMBL1789941). 
A review of the supporting evidence provided by Translator indicates that these are approved drugs that either directly or 
indirectly reduce or otherwise regulate the expression of RHOBTB2. Thus, Biolink Model helped Translator teams bring data 
together into a single system, thereby reducing the burden on the user to find and manually assemble data from these independent resources 
(see citation below).

![Figure 2](images/translator_example_figure2.png)
Figure 2. An overview of the Translator architecture that supports biomedical KG-based question-answering, including the 
role of Biolink Model, in the context of an example question. In this example, a user has posed the natural-language question: 
what chemicals or drugs might be used to treat neurological disorders such as epilepsy that are associated with genomic variants of 
RHOBTB2? The question is translated into a graph query, as shown in the top left panel, which is then translated into a 
Translator standard machine query (not shown). The KG shown in the second panel from the left is derived from a variety
of diverse ‘knowledge sources’, a subset of which are displayed in the figure, that are exposed by Translator ‘knowledge providers’. 
Biolink Model provides standardization and semantic harmonization across the disparate knowledge sources, thereby allowing 
them to be integrated into a KG capable of supporting question-answering. In this example, Translator provided two answers or 
results of interest to the investigative team that posed the question, namely, fostamatinib disodium and ruxolitinib, as shown 
in the bottom left panel. 

###### Citing Biolink Model
Unni DR, Moxon SAT, Bada M, Brush M, Bruskiewich R, Caufield JH, Clemons PA, Dancik V, Dumontier M, Fecho K, Glusman G, 
Hadlock JJ, Harris NL, Joshi A, Putman T, Qin G, Ramsey SA, Shefchek KA, Solbrig H, Soman K, Thessen AE, Haendel MA, 
Bizon C, Mungall CJ, The Biomedical Data Translator Consortium (2022).
Biolink Model: A universal schema for knowledge graphs in clinical, biomedical, and translational science. Clin Transl Sci. Wiley; 2022 Jun 6; [https://onlinelibrary.wiley.com/doi/10.1111/cts.13302](https://onlinelibrary.wiley.com/doi/10.1111/cts.13302)
