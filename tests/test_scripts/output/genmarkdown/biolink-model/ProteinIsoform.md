# Class: protein isoform


Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/

URI: [http://bioentity.io/vocab/ProteinIsoform](http://bioentity.io/vocab/ProteinIsoform)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Protein]^-\[ProteinIsoform|id(i):identifier_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F;has_biological_sequence(i):biological_sequence%20%3F;name(i):label_type%20%3F],%20\[ProteinIsoform]-%20related%20to(i)%20%3F>\[NamedThing],%20\[ProteinIsoform]-%20molecularly%20interacts%20with(i)%20%3F>\[MolecularEntity],%20\[ProteinIsoform]-%20regulates,%20entity%20to%20entity(i)%20%3F>\[MolecularEntity],%20\[ProteinIsoform]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[ProteinIsoform]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[ProteinIsoform]-%20in%20pathway%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[ProteinIsoform]-%20in%20complex%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[ProteinIsoform]-%20in%20cell%20population%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[ProteinIsoform]-%20expressed%20in(i)%20%3F>\[AnatomicalEntity],%20\[ProteinIsoform]uses%20-.->\[GeneProductIsoform])
## Mappings

## Inheritance

 *  is_a: [protein](Protein.md) - A gene product that is composed of a chain of amino acid sequences and is produced by ribosome-mediated translation of mRNA
 *  mixin: [gene product isoform](GeneProductIsoform.md) - This is an abstract class that can be mixed in with different kinds of gene products to indicate that the gene product is intended to represent a specific isoform rather than a canonical or reference or generic product. The designation of canonical or reference may be arbitrary, or it may represent the superclass of all isoforms.
## Children

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
