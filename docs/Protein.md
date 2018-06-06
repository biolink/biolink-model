# Class: protein


A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA

URI: [http://bioentity.io/vocab/Protein](http://bioentity.io/vocab/Protein)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneProduct]^-\[Protein|id(i):identifier_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F;has_biological_sequence(i):biological_sequence%20%3F;name(i):label_type%20%3F],%20\[Protein]^-\[ProteinIsoform],%20\[Protein]-%20related%20to(i)%20%3F>\[NamedThing],%20\[Protein]-%20molecularly%20interacts%20with(i)%20%3F>\[MolecularEntity],%20\[Protein]-%20regulates,%20entity%20to%20entity(i)%20%3F>\[MolecularEntity],%20\[Protein]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[Protein]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[Protein]-%20in%20pathway%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[Protein]-%20in%20complex%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[Protein]-%20in%20cell%20population%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[Protein]-%20expressed%20in(i)%20%3F>\[AnatomicalEntity])
## Mappings

 * [PR:000000001](http://purl.obolibrary.org/obo/PR_000000001)
 * [SIO:010043](http://semanticscience.org/resource/SIO_010043)
 * [WD:Q8054](http://purl.obolibrary.org/obo/WD_Q8054)
## Inheritance

 *  is_a: [gene product](GeneProduct.md) - The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
## Children

 *  child: [protein isoform](ProteinIsoform.md) - Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
## Used in

 *  class: [protein](Protein.md) references: [protein isoform](ProteinIsoform.md)
 *  class: [protein](Protein.md) references: [gene product](GeneProduct.md)
## Fields

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
