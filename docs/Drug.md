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

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon],[NamedThing],[MolecularEntity],[Mixture],[ChemicalSubstance]%3Chas%20excipient%200..%2A-%20[Drug%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[ChemicalSubstance]%3Chas%20active%20ingredient%200..%2A-%20[Drug],[Drug]uses%20-.-%3E[Mixture],[MolecularEntity]%5E-[Drug],[ChemicalSubstance])

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

### Inherited from mixture:

 * [has constituent](has_constituent.md)  <sub>0..*</sub>
    * Description: one or more chemical substances within a mixture
    * range: [ChemicalSubstance](ChemicalSubstance.md)

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

