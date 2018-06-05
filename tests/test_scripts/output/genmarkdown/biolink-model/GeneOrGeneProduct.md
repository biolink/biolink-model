# Class: gene or gene product


a union of genes or gene products. Frequently an identifier for one will be used as proxy for another

URI: http://bioentity.io/vocab/GeneOrGeneProduct

![img](http://yuml.me/diagram/nofunky/class/\[MacromolecularMachine]^-\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]^-\[Gene],%20\[GeneOrGeneProduct]^-\[GeneProduct],%20\[GeneOrGeneProduct]-%20in_pathway_with%20%3F>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]-%20in_complex_with%20%3F>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]-%20in_cell_population_with%20%3F>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]-%20expressed_in%20%3F>\[AnatomicalEntity],%20)
## Mappings

## Inheritance

 *  is_a: [macromolecular machine](MacromolecularMachine.md)
## Children

 *  child: [gene product](GeneProduct.md)
 *  child: [gene](Gene.md)
## Used in

 *  class: [gene or gene product](GeneOrGeneProduct.md) references: [gene product](GeneProduct.md)
 *  class: [gene or gene product](GeneOrGeneProduct.md) references: [gene](Gene.md)
## Fields

 * _[in pathway with](in_pathway_with.md) *subsets: translator_minimal*_
    * _holds between two genes or gene products that are part of in the same biological pathway_
    * range: [gene or gene product](GeneOrGeneProduct.md)
    * inherited from: [coexists with](coexists_with.md) *subsets: translator_minimal*
 * _[in complex with](in_complex_with.md) *subsets: translator_minimal*_
    * _holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex_
    * range: [gene or gene product](GeneOrGeneProduct.md)
    * inherited from: [coexists with](coexists_with.md) *subsets: translator_minimal*
 * _[in cell population with](in_cell_population_with.md) *subsets: translator_minimal*_
    * _holds between two genes or gene products that are expressed in the same cell type or population _
    * range: [gene or gene product](GeneOrGeneProduct.md)
    * inherited from: [coexists with](coexists_with.md) *subsets: translator_minimal*
 * _[expressed in](expressed_in.md) *subsets: translator_minimal*_
    * _holds between a gene or gene product and an anatomical entity in which it is expressed_
    * range: [anatomical entity](AnatomicalEntity.md)
    * inherited from: [related to](related_to.md)
