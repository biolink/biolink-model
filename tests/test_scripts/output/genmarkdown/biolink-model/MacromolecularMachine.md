# Class: macromolecular machine


A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.

URI: http://bioentity.io/vocab/MacromolecularMachine

![img](http://yuml.me/diagram/nofunky/class/\[GenomicEntity]^-\[MacromolecularMachine|name:label_type%20%3F],%20\[MacromolecularMachine]^-\[GeneOrGeneProduct],%20\[MacromolecularMachine]^-\[MacromolecularComplex],%20)
## Mappings

## Inheritance

 *  is_a: [genomic entity](GenomicEntity.md)
## Children

 *  child: [gene or gene product](GeneOrGeneProduct.md)
 *  child: [macromolecular complex](MacromolecularComplex.md)
## Used in

 *  class: [macromolecular machine](MacromolecularMachine.md) references: [gene or gene product](GeneOrGeneProduct.md)
 *  class: [macromolecular machine](MacromolecularMachine.md) references: [macromolecular complex](MacromolecularComplex.md)
## Fields

 * _[name](name.md) *subsets: translator_minimal*_
    * _A human-readable name for a thing_
    * range: [label type](LabelType.md)
    * inherited from: [name](name.md) *subsets: translator_minimal*
