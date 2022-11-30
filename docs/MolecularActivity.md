---
parent: Entities
title: biolink:MolecularActivity
grand_parent: Classes
layout: default
---

# Class: MolecularActivity


An execution of a molecular function carried out by a gene product or macromolecular complex.

URI: [biolink:MolecularActivity](https://w3id.org/biolink/vocab/MolecularActivity)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[OntologyClass],[Occurrent],[NucleicAcidEntity],[MolecularEntity],[MolecularActivityToPathwayAssociation],[MolecularActivityToMolecularActivityAssociation],[MolecularActivityToChemicalEntityAssociation],[MacromolecularMachineMixin]%3Cenabled%20by%200..%2A-++[MolecularActivity%7Cprovided_by(i):string%20%2A;xref(i):uriorcurie%20%2A;category(i):category_type%20%2B;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F],[MolecularEntity]%3Chas%20output%200..%2A-%20[MolecularActivity],[MolecularEntity]%3Chas%20input%200..%2A-%20[MolecularActivity],[MacromolecularMachineToMolecularActivityAssociation]-%20object%201..1%3E[MolecularActivity],[MolecularActivityToChemicalEntityAssociation]-%20subject%201..1%3E[MolecularActivity],[MolecularActivityToMolecularActivityAssociation]-%20object%201..1%3E[MolecularActivity],[MolecularActivityToMolecularActivityAssociation]-%20subject%201..1%3E[MolecularActivity],[MolecularActivityToPathwayAssociation]-%20subject%201..1%3E[MolecularActivity],[MolecularActivity]uses%20-.-%3E[Occurrent],[MolecularActivity]uses%20-.-%3E[OntologyClass],[BiologicalProcessOrActivity]%5E-[MolecularActivity],[MacromolecularMachineToMolecularActivityAssociation],[MacromolecularMachineMixin],[ChemicalEntityOrGeneOrGeneProduct],[BiologicalProcessOrActivity],[Attribute])

---


## Identifier prefixes

 * GO
 * REACT
 * RHEA
 * metacyc.reaction
 * EC
 * TCDB
 * KEGG.REACTION
 * KEGG.RCLASS
 * KEGG.ENZYME
 * KEGG.ORTHOLOGY
 * UMLS
 * BIGG.REACTION
 * SEED.REACTION
 * METANETX.REACTION

## Parents

 *  is_a: [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities in a biological system.

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity.
 *  mixin: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.

## Referenced by class

 *  **[Occurrent](Occurrent.md)** *[actively involved in](actively_involved_in.md)*  <sub>0..\*</sub>  **[MolecularActivity](MolecularActivity.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[catalyzes](catalyzes.md)*  <sub>0..\*</sub>  **[MolecularActivity](MolecularActivity.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[is substrate of](is_substrate_of.md)*  <sub>0..\*</sub>  **[MolecularActivity](MolecularActivity.md)**
 *  **[MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[MolecularActivity](MolecularActivity.md)**
 *  **[MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[MolecularActivity](MolecularActivity.md)**
 *  **[MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[MolecularActivity](MolecularActivity.md)**
 *  **[MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[MolecularActivity](MolecularActivity.md)**
 *  **[MolecularActivityToPathwayAssociation](MolecularActivityToPathwayAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[MolecularActivity](MolecularActivity.md)**

## Attributes


### Own

 * [enabled by](enabled_by.md)  <sub>0..\*</sub>
     * Description: holds between a process and a physical entity, where the physical entity executes the process
     * Range: [PhysicalEntity](PhysicalEntity.md)
     * in subsets: (translator_minimal)
 * [has input](has_input.md)  <sub>0..\*</sub>
     * Description: holds between a process and a continuant, where the continuant is an input into the process
     * Range: [Occurrent](Occurrent.md)
     * in subsets: (translator_minimal)
 * [has output](has_output.md)  <sub>0..\*</sub>
     * Description: holds between a process and a continuant, where the continuant is an output of the process
     * Range: [Occurrent](Occurrent.md)
     * in subsets: (translator_minimal)

### Inherited from entity:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>0..1</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * Range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)
 * [type](type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from gene product mixin:

 * [xref](xref.md)  <sub>0..\*</sub>
     * Description: Alternate CURIEs for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (translator_minimal)

### Inherited from macromolecular machine mixin:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)

### Inherited from named thing:

 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     * Range: [String](types/String.md)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..\*</sub>
     * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * Range: [OrganismTaxon](OrganismTaxon.md)
     * in subsets: (translator_minimal)

### Domain for slot:

 * [enabled by](enabled_by.md)  <sub>0..\*</sub>
     * Description: holds between a process and a physical entity, where the physical entity executes the process
     * Range: [PhysicalEntity](PhysicalEntity.md)
     * in subsets: (translator_minimal)
 * [has input](has_input.md)  <sub>0..\*</sub>
     * Description: holds between a process and a continuant, where the continuant is an input into the process
     * Range: [Occurrent](Occurrent.md)
     * in subsets: (translator_minimal)
 * [has output](has_output.md)  <sub>0..\*</sub>
     * Description: holds between a process and a continuant, where the continuant is an output of the process
     * Range: [Occurrent](Occurrent.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | molecular function |
|  | | molecular event |
|  | | reaction |
| **Exact Mappings:** | | GO:0003674 |
|  | | STY:T044 |

