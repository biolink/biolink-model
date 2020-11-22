---
parent: Entities
title: biolink:Disease
grand_parent: Classes
layout: default
---

# Class: Disease




URI: [biolink:Disease](https://w3id.org/biolink/vocab/Disease)

MONDO:0000001
{: .mapping-label }

DOID:4
{: .mapping-label }

WIKIDATA:Q12136
{: .mapping-label }

SIO:010299
{: .mapping-label }

UMLSSG:DISO
{: .mapping-label }

UMLSSC:T019
{: .mapping-label }

UMLSST:cgab
{: .mapping-label }

UMLSSC:T020
{: .mapping-label }

UMLSST:acab
{: .mapping-label }

UMLSSC:T037
{: .mapping-label }

UMLSST:inpo
{: .mapping-label }

UMLSSC:T046
{: .mapping-label }

UMLSST:patf
{: .mapping-label }

UMLSSC:T047
{: .mapping-label }

UMLSST:dsyn
{: .mapping-label }

UMLSSC:T048
{: .mapping-label }

UMLSST:mobd
{: .mapping-label }

UMLSSC:T049
{: .mapping-label }

UMLSST:comd
{: .mapping-label }

UMLSSC:T184
{: .mapping-label }

UMLSST:sosy
{: .mapping-label }

UMLSSC:T190
{: .mapping-label }

UMLSST:anab
{: .mapping-label }

UMLSSC:T191
{: .mapping-label }

UMLSST:neop
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingToDiseaseAssociationMixin],[OrganismTaxon],[NamedThing],[DiseaseToThingAssociationMixin],[DiseaseToExposureAssociation],[DiseaseOrPhenotypicFeature],[DiseaseToExposureAssociation]-%20subject%201..1%3E[Disease%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[DiseaseToThingAssociationMixin]-%20subject%201..1%3E[Disease],[ThingToDiseaseAssociationMixin]-%20object%201..1%3E[Disease],[DiseaseOrPhenotypicFeature]%5E-[Disease])

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


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
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
| **Mappings:** | | MONDO:0000001 |
|  | | DOID:4 |
|  | | WIKIDATA:Q12136 |
|  | | SIO:010299 |
|  | | UMLSSG:DISO |
|  | | UMLSSC:T019 |
|  | | UMLSST:cgab |
|  | | UMLSSC:T020 |
|  | | UMLSST:acab |
|  | | UMLSSC:T037 |
|  | | UMLSST:inpo |
|  | | UMLSSC:T046 |
|  | | UMLSST:patf |
|  | | UMLSSC:T047 |
|  | | UMLSST:dsyn |
|  | | UMLSSC:T048 |
|  | | UMLSST:mobd |
|  | | UMLSSC:T049 |
|  | | UMLSST:comd |
|  | | UMLSSC:T184 |
|  | | UMLSST:sosy |
|  | | UMLSSC:T190 |
|  | | UMLSST:anab |
|  | | UMLSSC:T191 |
|  | | UMLSST:neop |

