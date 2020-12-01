---
parent: Entities
title: biolink:Drug
grand_parent: Classes
layout: default
---

# Class: Drug


A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease

URI: [biolink:Drug](https://w3id.org/biolink/vocab/Drug)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[NamedThing],[MolecularEntity],[Mixture],[ChemicalSubstance]%3Chas%20excipient%200..%2A-%20[Drug%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ChemicalSubstance]%3Chas%20active%20ingredient%200..%2A-%20[Drug],[Drug]uses%20-.-%3E[Mixture],[MolecularEntity]%5E-[Drug],[ChemicalSubstance],[Attribute],[Agent])

---


## Identifier prefixes

 * PHARMGKB.DRUG

## Parents

 *  is_a: [MolecularEntity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)

## Uses Mixins

 *  mixin: [Mixture](Mixture.md) - The physical combination of two or more molecular entities in which the identities are retained and are mixed in the form of solutions, suspensions and colloids.

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[has drug](has_drug.md)*  <sub>OPT</sub>  **[Drug](Drug.md)**

## Attributes


### Own

 * [has active ingredient](has_active_ingredient.md)  <sub>0..*</sub>
    * Description: one or more chemical substance which are the active ingredient(s) of a drug
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [has excipient](has_excipient.md)  <sub>0..*</sub>
    * Description: one or more (generally inert) chemical substances which are formulated alongside the active ingredient of a drug
    * range: [ChemicalSubstance](ChemicalSubstance.md)

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

### Inherited from mixture:

 * [has constituent](has_constituent.md)  <sub>0..*</sub>
    * Description: one or more chemical substances within a mixture
    * range: [ChemicalSubstance](ChemicalSubstance.md)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [has active ingredient](has_active_ingredient.md)  <sub>0..*</sub>
    * Description: one or more chemical substance which are the active ingredient(s) of a drug
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [has excipient](has_excipient.md)  <sub>0..*</sub>
    * Description: one or more (generally inert) chemical substances which are formulated alongside the active ingredient of a drug
    * range: [ChemicalSubstance](ChemicalSubstance.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | The CHEBI ID represents a role rather than a substance |
| **Exact Mappings:** | | WIKIDATA:Q12140 |
|  | | CHEBI:23888 |
|  | | UMLSSC:T200 |
|  | | UMLSST:clnd |
| **Narrow Mappings:** | | UMLSSC:T195 |
|  | | UMLSST:antb |
| **Broad Mappings:** | | UMLSSC:T121 |
|  | | UMLSST:phsu |

