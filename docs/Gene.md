# Class: gene




URI: [http://bioentity.io/vocab/Gene](http://bioentity.io/vocab/Gene)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneOrGeneProduct]^-\[Gene|id(i):identifier_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F;has_biological_sequence(i):biological_sequence%20%3F;name(i):label_type%20%3F],%20\[Gene]-%20related%20to(i)%20%3F>\[NamedThing],%20\[Gene]-%20molecularly%20interacts%20with(i)%20%3F>\[MolecularEntity],%20\[Gene]-%20regulates,%20entity%20to%20entity(i)%20%3F>\[MolecularEntity],%20\[Gene]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[Gene]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[Gene]-%20in%20pathway%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[Gene]-%20in%20complex%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[Gene]-%20in%20cell%20population%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[Gene]-%20expressed%20in(i)%20%3F>\[AnatomicalEntity],%20\[Gene]-%20genetically%20interacts%20with%20%3F>\[Gene],%20\[Gene]-%20has%20gene%20product%20%3F>\[GeneProduct],%20\[Gene]-%20gene%20associated%20with%20condition%20%3F>\[DiseaseOrPhenotypicFeature])
## Mappings

 * [SO:0000704](http://purl.obolibrary.org/obo/SO_0000704)
 * [SIO:010035](http://semanticscience.org/resource/SIO_010035)
 * [WD:Q7187](http://purl.obolibrary.org/obo/WD_Q7187)
 * [UMLSSG:GENE](http://purl.obolibrary.org/obo/UMLSSG_GENE)
## Inheritance

 *  is_a: [gene or gene product](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
## Children

## Used in

 *  class: [gene](Gene.md) references: [gene or gene product](GeneOrGeneProduct.md)
 *  class: [gene](Gene.md) references: [macromolecular machine](MacromolecularMachine.md)
## Fields

 * _[genetically interacts with](genetically_interacts_with.md) *subsets: translator_minimal*_
    * _holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality._
    * range: [gene](Gene.md)
    * __Local__
 * _[has gene product](has_gene_product.md) *subsets: translator_minimal*_
    * _holds between a gene and a transcribed and/or translated product generated from it_
    * range: [gene product](GeneProduct.md)
    * __Local__
 * _[gene associated with condition](gene_associated_with_condition.md) *subsets: translator_minimal*_
    * _holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with_
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[molecularly interacts with](molecularly_interacts_with.md) *subsets: translator_minimal*_
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[regulates, entity to entity](regulates_entity_to_entity.md) *subsets: translator_minimal*_
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[biomarker for](biomarker_for.md) *subsets: translator_minimal*_
    * _holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature._
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [thing with taxon](ThingWithTaxon.md)
 * _[in pathway with](in_pathway_with.md) *subsets: translator_minimal*_
    * _holds between two genes or gene products that are part of in the same biological pathway_
    * range: [gene or gene product](GeneOrGeneProduct.md)
    * inherited from: [gene or gene product](GeneOrGeneProduct.md)
 * _[in complex with](in_complex_with.md) *subsets: translator_minimal*_
    * _holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex_
    * range: [gene or gene product](GeneOrGeneProduct.md)
    * inherited from: [gene or gene product](GeneOrGeneProduct.md)
 * _[in cell population with](in_cell_population_with.md) *subsets: translator_minimal*_
    * _holds between two genes or gene products that are expressed in the same cell type or population _
    * range: [gene or gene product](GeneOrGeneProduct.md)
    * inherited from: [gene or gene product](GeneOrGeneProduct.md)
 * _[expressed in](expressed_in.md) *subsets: translator_minimal*_
    * _holds between a gene or gene product and an anatomical entity in which it is expressed_
    * range: [anatomical entity](AnatomicalEntity.md)
    * inherited from: [gene or gene product](GeneOrGeneProduct.md)
