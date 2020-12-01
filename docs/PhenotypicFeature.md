---
parent: Entities
title: biolink:PhenotypicFeature
grand_parent: Classes
layout: default
---

# Class: PhenotypicFeature




URI: [biolink:PhenotypicFeature](https://w3id.org/biolink/vocab/PhenotypicFeature)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingToPhenotypicFeatureAssociationMixin],[ThingToPhenotypicFeatureAssociationMixin]-%20object%201..1%3E[PhenotypicFeature%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[DiseaseOrPhenotypicFeature]%5E-[PhenotypicFeature],[OrganismTaxon],[NamedThing],[DiseaseOrPhenotypicFeature],[BiologicalEntity],[Attribute],[Agent])

---


## Identifier prefixes

 * HP
 * EFO
 * NCIT
 * UMLS
 * MEDDRA
 * MP
 * ZP
 * UPHENO
 * APO
 * FBcv
 * WBPhenotype
 * SNOMEDCT
 * MESH

## Parents

 *  is_a: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.

## Referenced by class

 *  **[BiologicalEntity](BiologicalEntity.md)** *[has phenotype](has_phenotype.md)*  <sub>0..*</sub>  **[PhenotypicFeature](PhenotypicFeature.md)**
 *  **[ThingToPhenotypicFeatureAssociationMixin](ThingToPhenotypicFeatureAssociationMixin.md)** *[thing to phenotypic feature association mixin➞object](thing_to_phenotypic_feature_association_mixin_object.md)*  <sub>REQ</sub>  **[PhenotypicFeature](PhenotypicFeature.md)**

## Attributes


### Inherited from entity:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a resource. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for an entity. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (translator_minimal)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Agent](Agent.md)

### Inherited from material sample:

 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any named thing to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | sign |
|  | | symptom |
|  | | phenotype |
|  | | trait |
|  | | endophenotype |
| **Exact Mappings:** | | UPHENO:0001001 |
|  | | SIO:010056 |
|  | | WIKIDATA:Q104053 |
| **Narrow Mappings:** | | UMLSSC:T184 |
|  | | UMLSST:sosy |
|  | | WIKIDATA:Q169872 |
|  | | WIKIDATA:Q25203551 |
|  | | HP:0000118 |

