---
parent: Entities
title: biolink:OrganismalEntity
grand_parent: Classes
layout: default
---

# Class: OrganismalEntity


A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

URI: [biolink:OrganismalEntity](https://w3id.org/biolink/vocab/OrganismalEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[PopulationOfIndividualOrganisms],[OrganismalEntityAsAModelOfDiseaseAssociation],[Attribute]%3Chas%20attribute%200..%2A-++[OrganismalEntity%7Cid(i):string;category(i):category_type%20%2B;iri(i):iri_type%20%3F;name(i):label_type%20%3F;source(i):label_type%20%3F],[OrganismalEntityAsAModelOfDiseaseAssociation]-%20subject%201..1%3E[OrganismalEntity],[OrganismalEntity]%5E-[PopulationOfIndividualOrganisms],[OrganismalEntity]%5E-[LifeStage],[OrganismalEntity]%5E-[IndividualOrganism],[OrganismalEntity]%5E-[CellLine],[OrganismalEntity]%5E-[AnatomicalEntity],[BiologicalEntity]%5E-[OrganismalEntity],[LifeStage],[IndividualOrganism],[ExposureEvent],[CellLine],[BiologicalEntity],[Attribute],[AnatomicalEntity])

---


## Parents

 *  is_a: [BiologicalEntity](BiologicalEntity.md)

## Children

 * [AnatomicalEntity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part
 * [CellLine](CellLine.md)
 * [IndividualOrganism](IndividualOrganism.md)
 * [LifeStage](LifeStage.md) - A stage of development or growth of an organism, including post-natal adult stages
 * [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) - A collection of individuals from the same taxonomic class distinguished by one or more characteristics. Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance for Genome Resources]

## Referenced by class

 *  **[ExposureEvent](ExposureEvent.md)** *[has receptor](has_receptor.md)*  <sub>OPT</sub>  **[OrganismalEntity](OrganismalEntity.md)**
 *  **[OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md)** *[organismal entity as a model of disease association➞subject](organismal_entity_as_a_model_of_disease_association_subject.md)*  <sub>REQ</sub>  **[OrganismalEntity](OrganismalEntity.md)**

## Attributes


### Own

 * [organismal entity➞has attribute](organismal_entity_has_attribute.md)  <sub>0..*</sub>
    * Description: may be an organism attribute
    * range: [Attribute](Attribute.md)

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

 * [organismal entity➞has attribute](organismal_entity_has_attribute.md)  <sub>0..*</sub>
    * Description: may be an organism attribute
    * range: [Attribute](Attribute.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Exact Mappings:** | | WIKIDATA:Q7239 |
|  | | UMLSSG:LIVB |

