# Class: environment


A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes

URI: [http://bioentity.io/vocab/Environment](http://bioentity.io/vocab/Environment)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[BiologicalEntity]^-\[Environment|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F],%20\[Environment]^-\[DrugExposure],%20\[Environment]^-\[Treatment],%20\[Environment]-%20related%20to(i)%20%3F>\[NamedThing])
## Mappings

 * [SIO:000955](http://semanticscience.org/resource/SIO_000955)
## Inheritance

 *  is_a: [biological entity](BiologicalEntity.md)
## Children

 *  child: [drug exposure](DrugExposure.md) - A drug exposure is an intake of a particular chemical substance
 *  child: [treatment](Treatment.md) - A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
## Used in

 *  class: [environment](Environment.md) references: [drug exposure](DrugExposure.md)
 *  class: [environment](Environment.md) references: [treatment](Treatment.md)
## Fields

 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
