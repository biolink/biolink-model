---
parent: Entities
title: biolink:InformationContentEntity
grand_parent: Classes
layout: default
---

# Class: InformationContentEntity


a piece of information that typically describes some topic of discourse or is used as support.

URI: [biolink:InformationContentEntity](https://w3id.org/biolink/vocab/InformationContentEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[NamedThing],[ContributorAssociation]-%20subject%201..1%3E[InformationContentEntity%7Clicense:string%20%3F;rights:string%20%3F;format:string%20%3F;creation_date:date%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[InformationContentEntity]%5E-[Publication],[InformationContentEntity]%5E-[EvidenceType],[InformationContentEntity]%5E-[DatasetVersion],[InformationContentEntity]%5E-[DatasetSummary],[InformationContentEntity]%5E-[DatasetDistribution],[InformationContentEntity]%5E-[Dataset],[InformationContentEntity]%5E-[ConfidenceLevel],[NamedThing]%5E-[InformationContentEntity],[EvidenceType],[DatasetVersion],[DatasetSummary],[DatasetDistribution],[Dataset],[ContributorAssociation],[ConfidenceLevel],[Attribute],[Agent])

---


## Identifier prefixes

 * doi

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [ConfidenceLevel](ConfidenceLevel.md) - Level of confidence in a statement
 * [Dataset](Dataset.md) - an item that refers to a collection of data from a data source.
 * [DatasetDistribution](DatasetDistribution.md) - an item that holds distribution level information about a dataset.
 * [DatasetSummary](DatasetSummary.md) - an item that holds summary level information about a dataset.
 * [DatasetVersion](DatasetVersion.md) - an item that holds version level information about a dataset.
 * [EvidenceType](EvidenceType.md) - Class of evidence that supports an association
 * [Publication](Publication.md) - Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Biolink category subclasses.

## Referenced by class

 *  **[ContributorAssociation](ContributorAssociation.md)** *[contributor association➞subject](contributor_association_subject.md)*  <sub>REQ</sub>  **[InformationContentEntity](InformationContentEntity.md)**

## Attributes


### Own

 * [creation date](creation_date.md)  <sub>OPT</sub>
     * Description: date on which an entity was created. This can be applied to nodes or edges
     * range: [Date](types/Date.md)
 * [format](format.md)  <sub>OPT</sub>
     * range: [String](types/String.md)
 * [license](license.md)  <sub>OPT</sub>
     * range: [String](types/String.md)
 * [rights](rights.md)  <sub>OPT</sub>
     * range: [String](types/String.md)

### Inherited from entity:

 * [id](id.md)  <sub>REQ</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>0..*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)
 * [type](type.md)  <sub>OPT</sub>
     * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
     * Description: a human-readable description of an entity
     * range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [source](source.md)  <sub>OPT</sub>
     * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
     * range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..*</sub>
     * Description: connects an association to the agent (person, organization or group) that provided it
     * range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..*</sub>
     * Description: connects any entity to an attribute
     * range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from macromolecular machine mixin:

 * [macromolecular machine mixin➞name](macromolecular_machine_mixin_name.md)  <sub>OPT</sub>
     * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * range: [SymbolType](types/SymbolType.md)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
     * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [format](format.md)  <sub>OPT</sub>
     * range: [String](types/String.md)
 * [license](license.md)  <sub>OPT</sub>
     * range: [String](types/String.md)
 * [rights](rights.md)  <sub>OPT</sub>
     * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | information |
|  | | information artefact |
|  | | information entity |
| **Exact Mappings:** | | IAO:0000030 |
| **Narrow Mappings:** | | UMLSSG:CONC |
|  | | UMLSSC:T077 |
|  | | UMLSST:cnce |
|  | | UMLSSC:T078 |
|  | | UMLSST:idcn |
|  | | UMLSSC:T079 |
|  | | UMLSST:tmco |
|  | | UMLSSC:T080 |
|  | | UMLSST:qlco |
|  | | UMLSSC:T081 |
|  | | UMLSST:qnco |
|  | | UMLSSC:T082 |
|  | | UMLSST:spco |
|  | | UMLSSC:T089 |
|  | | UMLSST:rnlw |
|  | | UMLSSC:T102 |
|  | | UMLSST:grpa |
|  | | UMLSSC:T169 |
|  | | UMLSST:ftcn |
|  | | UMLSSC:T171 |
|  | | UMLSST:lang |
|  | | UMLSSC:T185 |
|  | | UMLSST:clas |

