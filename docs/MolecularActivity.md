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

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClass],[Occurrent],[NamedThing],[MolecularEntity],[MacromolecularMachineMixin]%3Cenabled%20by%200..%2A-++[MolecularActivity%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[MolecularEntity]%3Chas%20output%200..%2A-%20[MolecularActivity],[MolecularEntity]%3Chas%20input%200..%2A-%20[MolecularActivity],[MacromolecularMachineToMolecularActivityAssociation]-%20object%201..1%3E[MolecularActivity],[MolecularActivity]uses%20-.-%3E[Occurrent],[MolecularActivity]uses%20-.-%3E[OntologyClass],[BiologicalProcessOrActivity]%5E-[MolecularActivity],[MacromolecularMachineToMolecularActivityAssociation],[MacromolecularMachineMixin],[BiologicalProcessOrActivity],[Attribute],[Agent])

---


## Identifier prefixes

 * GO
 * REACT
 * RHEA
 * MetaCyc
 * EC
 * TCDB
 * KEGG.REACTION
 * KEGG.RCLASS
 * KEGG.ENZYME
 * UMLS
 * BIGG.REACTION

## Parents

 *  is_a: [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities in a biological system.

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity.
 *  mixin: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.

## Referenced by class

 *  **[Occurrent](Occurrent.md)** *[actively involves](actively_involves.md)*  <sub>0..\*</sub>  **[MolecularActivity](MolecularActivity.md)**
 *  **[Occurrent](Occurrent.md)** *[capability of](capability_of.md)*  <sub>0..\*</sub>  **[MolecularActivity](MolecularActivity.md)**
 *  **[MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md)** *[macromolecular machine to molecular activity association➞object](macromolecular_machine_to_molecular_activity_association_object.md)*  <sub>1..1</sub>  **[MolecularActivity](MolecularActivity.md)**

## Attributes


### Own

 * [molecular activity➞enabled by](molecular_activity_enabled_by.md)  <sub>0..\*</sub>
     * Description: The gene product, gene, or complex that catalyzes the reaction
     * Range: [MacromolecularMachineMixin](MacromolecularMachineMixin.md)
     * in subsets: (translator_minimal)
 * [molecular activity➞has input](molecular_activity_has_input.md)  <sub>0..\*</sub>
     * Description: A chemical entity that is the input for the reaction
     * Range: [MolecularEntity](MolecularEntity.md)
     * in subsets: (translator_minimal)
 * [molecular activity➞has output](molecular_activity_has_output.md)  <sub>0..\*</sub>
     * Description: A chemical entity that is the output for the reaction
     * Range: [MolecularEntity](MolecularEntity.md)
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
 * [source](source.md)  <sub>0..1</sub>
     * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: connects an association to the agent (person, organization or group) that provided it
     * Range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from macromolecular machine mixin:

 * [macromolecular machine mixin➞name](macromolecular_machine_mixin_name.md)  <sub>0..1</sub>
     * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * Range: [SymbolType](types/SymbolType.md)
     * in subsets: (translator_minimal,samples)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [NamedThing](NamedThing.md)
     * in subsets: (translator_minimal)

### Domain for slot:

 * [molecular activity➞enabled by](molecular_activity_enabled_by.md)  <sub>0..\*</sub>
     * Description: The gene product, gene, or complex that catalyzes the reaction
     * Range: [MacromolecularMachineMixin](MacromolecularMachineMixin.md)
     * in subsets: (translator_minimal)
 * [molecular activity➞has input](molecular_activity_has_input.md)  <sub>0..\*</sub>
     * Description: A chemical entity that is the input for the reaction
     * Range: [MolecularEntity](MolecularEntity.md)
     * in subsets: (translator_minimal)
 * [molecular activity➞has output](molecular_activity_has_output.md)  <sub>0..\*</sub>
     * Description: A chemical entity that is the output for the reaction
     * Range: [MolecularEntity](MolecularEntity.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | molecular function |
|  | | molecular event |
|  | | reaction |
| **Exact Mappings:** | | GO:0003674 |
|  | | STY:T044 |

