---
parent: Entities
title: biolink:Treatment
grand_parent: Classes
layout: default
---

# Class: Treatment


A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'

URI: [biolink:Treatment](https://w3id.org/biolink/vocab/Treatment)

OGMS:0000090
{: .mapping-label }

SIO:001398
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DrugExposure]%3Chas%20part%201..%2A-%20[Treatment%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[SequenceVariantModulatesTreatmentAssociation]-%20object%201..1%3E[Treatment],[ExposureEvent]%5E-[Treatment],[SequenceVariantModulatesTreatmentAssociation],[ExposureEvent],[DrugExposure],[DiseaseOrPhenotypicFeature])

---


## Parents

 *  is_a: [ExposureEvent](ExposureEvent.md) - A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

## Referenced by class

 *  **[SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md)** *[sequence variant modulates treatment association➞object](sequence_variant_modulates_treatment_association_object.md)*  <sub>REQ</sub>  **[Treatment](Treatment.md)**
 *  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)** *[treated by](treated_by.md)*  <sub>0..*</sub>  **[Treatment](Treatment.md)**

## Attributes


### Own

 * [treatment➞has part](treatment_has_part.md)  <sub>1..*</sub>
    * range: [DrugExposure](DrugExposure.md)

### Inherited from gene product:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Inherited from named thing:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [treatment➞has part](treatment_has_part.md)  <sub>1..*</sub>
    * range: [DrugExposure](DrugExposure.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | medical action |
| **Mappings:** | | OGMS:0000090 |
|  | | SIO:001398 |

