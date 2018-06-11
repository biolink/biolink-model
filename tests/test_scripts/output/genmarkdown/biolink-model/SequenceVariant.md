# Class: sequence variant


An allele that varies in its sequence from what is considered the reference allele at that locus.

URI: [http://bioentity.io/vocab/SequenceVariant](http://bioentity.io/vocab/SequenceVariant)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SequenceVariant|has_gene:string%20*;has_biological_sequence:biological_sequence%20%3F;id:identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[SequenceVariant]-%20regulates,%20entity%20to%20entity(i)%20%3F>\[MolecularEntity],%20\[SequenceVariant]-%20molecularly%20interacts%20with(i)%20%3F>\[MolecularEntity],%20\[SequenceVariant]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[SequenceVariant]-%20related%20to(i)%20%3F>\[NamedThing],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20sequence%20variant%20qualifier(i)%20%3F>\[SequenceVariant],%20\[VariantToPhenotypicFeatureAssociation]-%20subject(i)>\[SequenceVariant],%20\[VariantToThingAssociation]-%20subject(i)>\[SequenceVariant],%20\[SequenceVariantModulatesTreatmentAssociation]-%20subject(i)>\[SequenceVariant],%20\[GenotypeToVariantAssociation]-%20object(i)>\[SequenceVariant],%20\[VariantToPopulationAssociation]-%20subject(i)>\[SequenceVariant],%20\[GenomicEntity]^-\[SequenceVariant])
## Mappings

 * [GENO:0000002](http://purl.obolibrary.org/obo/GENO_0000002)
 * [WD:Q15304597](http://purl.obolibrary.org/obo/WD_Q15304597)
 * [SIO:010277](http://semanticscience.org/resource/SIO_010277)
 * [VMC:Allele](http://purl.obolibrary.org/obo/VMC_Allele)
## Inheritance

 *  is_a: genomic entity
## Children

## Used in

 *  class: **genotype to variant association** *genotype to variant association object* **sequence variant**
 *  class: **sequence variant modulates treatment association** *sequence variant modulates treatment association subject* **sequence variant**
 *  class: **gene has variant that contributes to disease association** *sequence variant qualifier* **sequence variant**
 *  class: **variant to phenotypic feature association** *variant to phenotypic feature association subject* **sequence variant**
 *  class: **variant to population association** *variant to population association subject* **sequence variant**
 *  class: **variant to thing association** *variant to thing association subject* **sequence variant**
## Fields

 * _sequence variant has biological sequence_
    * _connects a genomic feature to its sequence_
    * range: biological sequence
    * __Local__
 * _sequence variant has gene_
    * _Each allele can be associated with any number of genes_
    * range: **string***
    * __Local__
 * _sequence variant id_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: identifier type
    * Example: [ZFIN:ZDB-ALT-980203-1091](http://purl.obolibrary.org/obo/ZFIN_ZDB-ALT-980203-1091) ti282a allele from ZFIN
    * Example: [ClinVarVariant:17681](http://purl.obolibrary.org/obo/ClinVarVariant_17681) NM_007294.3(BRCA1):c.2521C>T (p.Arg841Trp)
    * __Local__
 * _biomarker for_
    * _holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature._
    * range: disease or phenotypic feature
    * inherited from: molecular entity
 * _category_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: label type
    * inherited from: named thing
 * _description_
    * _a human-readable description of a thing_
    * range: narrative text
    * inherited from: named thing
 * _full name_
    * _a long-form human readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _has phenotype_
    * _holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). _
    * range: phenotype
    * inherited from: biological entity
 * _in taxon_
    * _connects a thing to a class representing a taxon_
    * range: organism taxon
    * inherited from: thing with taxon
 * _iri_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: iri type
    * inherited from: named thing
 * _molecularly interacts with_
    * _holds between two entities that make physical contact as part of some interaction_
    * range: molecular entity
    * inherited from: molecular entity
 * _name_
    * _A human-readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _node property_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * inherited from: named thing
 * _regulates, entity to entity_
    * _describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be._
    * range: molecular entity
    * inherited from: molecular entity
 * _related to_
    * _A grouping for any relationship type that holds between any two things_
    * range: named thing
    * inherited from: named thing
 * _systematic synonym_
    * _more commonly used for gene symbols in yeast_
    * range: label type
    * inherited from: named thing
