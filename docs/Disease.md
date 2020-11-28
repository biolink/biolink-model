---
parent: Entities
title: biolink:Disease
grand_parent: Classes
layout: default
---

# Class: Disease




URI: [biolink:Disease](https://w3id.org/biolink/vocab/Disease)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingToDiseaseAssociationMixin],[OrganismTaxon],[NamedThing],[DiseaseToThingAssociationMixin],[DiseaseToExposureAssociation],[DiseaseOrPhenotypicFeature],[DiseaseToExposureAssociation]-%20subject%201..1%3E[Disease%7Cid(i):string;category(i):category_type%20%2B;iri(i):iri_type%20%3F;name(i):label_type%20%3F;source(i):label_type%20%3F],[DiseaseToThingAssociationMixin]-%20subject%201..1%3E[Disease],[ThingToDiseaseAssociationMixin]-%20object%201..1%3E[Disease],[DiseaseOrPhenotypicFeature]%5E-[Disease],[Attribute])

---


## Identifier prefixes

 * MONDO
 * DOID
 * OMIM
 * ORPHANET
 * EFO
 * UMLS
 * MESH
 * MEDDRA
 * NCIT
 * SNOMEDCT
 * medgen
 * ICD10
 * ICD9
 * ICD0
 * HP
 * MP

## Parents

 *  is_a: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.

## Referenced by class

 *  **[DiseaseToExposureAssociation](DiseaseToExposureAssociation.md)** *[disease to exposure association➞subject](disease_to_exposure_association_subject.md)*  <sub>REQ</sub>  **[Disease](Disease.md)**
 *  **[DiseaseToThingAssociationMixin](DiseaseToThingAssociationMixin.md)** *[disease to thing association mixin➞subject](disease_to_thing_association_mixin_subject.md)*  <sub>REQ</sub>  **[Disease](Disease.md)**
 *  **[NamedThing](NamedThing.md)** *[manifestation of](manifestation_of.md)*  <sub>0..*</sub>  **[Disease](Disease.md)**
 *  **[ThingToDiseaseAssociationMixin](ThingToDiseaseAssociationMixin.md)** *[thing to disease association mixin➞object](thing_to_disease_association_mixin_object.md)*  <sub>REQ</sub>  **[Disease](Disease.md)**

## Attributes


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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | condition |
|  | | disorder |
|  | | medical condition |
| **Exact Mappings:** | | MONDO:0000001 |
|  | | DOID:4 |
|  | | WIKIDATA:Q12136 |
|  | | SIO:010299 |
|  | | UMLSSG:DISO |
|  | | UMLSSC:T047 |
|  | | UMLSST:dsyn |
| **Narrow Mappings:** | | UMLSSC:T019 |
|  | | UMLSST:cgab |
|  | | UMLSSC:T020 |
|  | | UMLSST:acab |
|  | | UMLSSC:T037 |
|  | | UMLSST:inpo |
|  | | UMLSSC:T046 |
|  | | UMLSST:patf |
|  | | UMLSSC:T048 |
|  | | UMLSST:mobd |
|  | | UMLSSC:T049 |
|  | | UMLSST:comd |
|  | | UMLSSC:T190 |
|  | | UMLSST:anab |
|  | | UMLSSC:T191 |
|  | | UMLSST:neop |

