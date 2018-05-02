---
layout: default
---

## drug


A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease

URI: [http://bioentity.io/vocab/Drug](http://bioentity.io/vocab/Drug)


![img](http://yuml.me/diagram/nofunky/class/[chemical substance|]^-[drug|], [drug|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|])
## Mappings

 * [WD:Q12140](http://purl.obolibrary.org/obo/WD_Q12140)
 * [CHEBI:23888](http://purl.obolibrary.org/obo/CHEBI_23888)

## Inheritance

 *  is_a: [chemical substance](ChemicalSubstance.html)

## Children



## Fields

 * [id](id.html)
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
