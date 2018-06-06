# Class: biological sex




URI: [http://bioentity.io/vocab/BiologicalSex](http://bioentity.io/vocab/BiologicalSex)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Attribute]^-\[BiologicalSex],%20\[BiologicalSex]^-\[GenotypicSex],%20\[BiologicalSex]^-\[PhenotypicSex],%20\[BiologicalSex]-%20subclass%20of(i)%20%3F>\[OntologyClass])
## Mappings

 * [PATO:0000047](http://purl.obolibrary.org/obo/PATO_0000047)
## Inheritance

 *  is_a: [attribute](Attribute.md) - A property or characteristic of an entity
## Children

 *  child: [phenotypic sex](PhenotypicSex.md) - An attribute corresponding to the phenotypic sex of the individual, based upon the reproductive organs present.
 *  child: [genotypic sex](GenotypicSex.md) - An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
## Used in

 *  class: [biological sex](BiologicalSex.md) references: [phenotypic sex](PhenotypicSex.md)
 *  class: [biological sex](BiologicalSex.md) references: [genotypic sex](GenotypicSex.md)
## Fields

 * _[subclass of](subclass_of.md) *subsets: translator_minimal*_
    * _holds between two classes where the domain class is a specialization of the range class_
    * range: [ontology class](OntologyClass.md)
    * inherited from: [ontology class](OntologyClass.md)
