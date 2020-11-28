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

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Occurrent],[MacromolecularMachine]%3Cenabled%20by%200..%2A-%20[MolecularActivity%7Cid(i):string;category(i):category_type%20%2B;iri(i):iri_type%20%3F;name(i):label_type%20%3F;source(i):label_type%20%3F],[ChemicalSubstance]%3Chas%20output%200..%2A-%20[MolecularActivity],[ChemicalSubstance]%3Chas%20input%200..%2A-%20[MolecularActivity],[MacromolecularMachineToMolecularActivityAssociation]-%20object%201..1%3E[MolecularActivity],[MolecularActivity]uses%20-.-%3E[Occurrent],[BiologicalProcessOrActivity]%5E-[MolecularActivity],[MacromolecularMachineToMolecularActivityAssociation],[MacromolecularMachine],[ChemicalSubstance],[BiologicalProcessOrActivity],[Attribute])

---


## Identifier prefixes

 * GO
 * REACT
 * RHEA
 * MetaCyc
 * EC
 * KEGG

## Parents

 *  is_a: [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity

## Referenced by class

 *  **[MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md)** *[macromolecular machine to molecular activity association➞object](macromolecular_machine_to_molecular_activity_association_object.md)*  <sub>REQ</sub>  **[MolecularActivity](MolecularActivity.md)**

## Attributes


### Own

 * [molecular activity➞enabled by](molecular_activity_enabled_by.md)  <sub>0..*</sub>
    * Description: The gene product, gene, or complex that catalyzes the reaction
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [molecular activity➞has input](molecular_activity_has_input.md)  <sub>0..*</sub>
    * Description: A chemical entity that is the input for the reaction
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [molecular activity➞has output](molecular_activity_has_output.md)  <sub>0..*</sub>
    * Description: A chemical entity that is the output for the reaction
    * range: [ChemicalSubstance](ChemicalSubstance.md)

### Inherited from material sample:

 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any named thing to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

### Inherited from resource mixin:

 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [molecular activity➞enabled by](molecular_activity_enabled_by.md)  <sub>0..*</sub>
    * Description: The gene product, gene, or complex that catalyzes the reaction
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [molecular activity➞has input](molecular_activity_has_input.md)  <sub>0..*</sub>
    * Description: A chemical entity that is the input for the reaction
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [molecular activity➞has output](molecular_activity_has_output.md)  <sub>0..*</sub>
    * Description: A chemical entity that is the output for the reaction
    * range: [ChemicalSubstance](ChemicalSubstance.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | molecular function |
|  | | molecular event |
|  | | reaction |
| **Exact Mappings:** | | GO:0003674 |
|  | | UMLSSC:T044 |
|  | | UMLSST:moft |

