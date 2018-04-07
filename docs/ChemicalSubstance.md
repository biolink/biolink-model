---
layout: default
---

## chemical substance


May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part

URI: [http://bioentity.io/vocab/ChemicalSubstance](http://bioentity.io/vocab/ChemicalSubstance)


![img](http://yuml.me/diagram/nofunky/class/[molecular entity]^-[chemical substance], [chemical substance]-in taxon >[organism taxon], [ontology class]^-[organism taxon])
## Mappings

 * [SIO:010004](http://semanticscience.org/resource/SIO_010004)
 * [UMLSSG:CHEM](http://purl.obolibrary.org/obo/UMLSSG_CHEM)
 * [WD:Q79529](http://purl.obolibrary.org/obo/WD_Q79529)
 * [CHEBI:24431](http://purl.obolibrary.org/obo/CHEBI_24431)

## Inheritance

 *  is_a: [molecular entity](MolecularEntity.html)

## Children

 *  child: [drug](Drug.html)

## Used in

 *  class: [chemical to thing association](ChemicalToThingAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [chemical to pathway association](ChemicalToPathwayAssociation.html) references: [chemical substance](ChemicalSubstance.html)
 *  class: [chemical to gene association](ChemicalToGeneAssociation.html) references: [chemical substance](ChemicalSubstance.html)

## Fields

 * [id](id.html)
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
