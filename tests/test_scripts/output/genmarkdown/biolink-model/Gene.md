# Class: gene




URI: http://bioentity.io/vocab/Gene

![img](http://yuml.me/diagram/nofunky/class/\[GeneOrGeneProduct]^-\[Gene],%20\[Gene]-%20genetically_interacts_with%20%3F>\[Gene],%20\[Gene]-%20has_gene_product%20%3F>\[GeneProduct],%20\[Gene]-%20gene_associated_with_condition%20%3F>\[DiseaseOrPhenotypicFeature],%20)
## Mappings

 * [SO:0000704](http://purl.obolibrary.org/obo/SO_0000704)
 * [SIO:010035](http://semanticscience.org/resource/SIO_010035)
 * [WD:Q7187](http://purl.obolibrary.org/obo/WD_Q7187)
 * [UMLSSG:GENE](http://purl.obolibrary.org/obo/UMLSSG_GENE)
## Inheritance

 *  is_a: [gene or gene product](GeneOrGeneProduct.md)
## Children

## Used in

 *  class: [gene](Gene.md) references: [gene or gene product](GeneOrGeneProduct.md)
 *  class: [gene](Gene.md) references: [macromolecular machine](MacromolecularMachine.md)
## Fields

 * _[genetically interacts with](genetically_interacts_with.md) *subsets: translator_minimal*_
    * _holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality._
    * range: [gene](Gene.md)
    * inherited from: [interacts with](interacts_with.md) *subsets: translator_minimal*
 * _[has gene product](has_gene_product.md) *subsets: translator_minimal*_
    * _holds between a gene and a transcribed and/or translated product generated from it_
    * range: [gene product](GeneProduct.md)
    * inherited from: [related to](related_to.md)
 * _[gene associated with condition](gene_associated_with_condition.md) *subsets: translator_minimal*_
    * _holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with_
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
    * inherited from: [related to](related_to.md)
