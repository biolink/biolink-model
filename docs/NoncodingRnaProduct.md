# Class: noncoding RNA product




URI: [http://bioentity.io/vocab/NoncodingRnaProduct](http://bioentity.io/vocab/NoncodingRnaProduct)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[RnaProduct]^-\[NoncodingRnaProduct|id(i):identifier_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F;has_biological_sequence(i):biological_sequence%20%3F;name(i):label_type%20%3F],%20\[NoncodingRnaProduct]^-\[Microrna],%20\[NoncodingRnaProduct]-%20related%20to(i)%20%3F>\[NamedThing],%20\[NoncodingRnaProduct]-%20molecularly%20interacts%20with(i)%20%3F>\[MolecularEntity],%20\[NoncodingRnaProduct]-%20regulates,%20entity%20to%20entity(i)%20%3F>\[MolecularEntity],%20\[NoncodingRnaProduct]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[NoncodingRnaProduct]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[NoncodingRnaProduct]-%20in%20pathway%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[NoncodingRnaProduct]-%20in%20complex%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[NoncodingRnaProduct]-%20in%20cell%20population%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[NoncodingRnaProduct]-%20expressed%20in(i)%20%3F>\[AnatomicalEntity])
## Mappings

 * [SIO:001235](http://semanticscience.org/resource/SIO_001235)
 * [SO:0000655](http://purl.obolibrary.org/obo/SO_0000655)
## Inheritance

 *  is_a: [RNA product](RnaProduct.md)
## Children

 *  child: [microRNA](Microrna.md)
## Used in

 *  class: [noncoding RNA product](NoncodingRnaProduct.md) references: [microRNA](Microrna.md)
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
