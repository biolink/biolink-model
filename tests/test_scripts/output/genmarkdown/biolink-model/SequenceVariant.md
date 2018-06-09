# Class: sequence variant


An allele that varies in its sequence from what is considered the reference allele at that locus.

URI: [http://bioentity.io/vocab/SequenceVariant](http://bioentity.io/vocab/SequenceVariant)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GenomicEntity]^-\[SequenceVariant|name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F;has_gene:string%20*;has_biological_sequence:biological_sequence%20%3F;id:identifier_type%20%3F],%20\[SequenceVariant]-%20related%20to(i)%20%3F>\[NamedThing],%20\[SequenceVariant]-%20molecularly%20interacts%20with(i)%20%3F>\[MolecularEntity],%20\[SequenceVariant]-%20regulates,%20entity%20to%20entity(i)%20%3F>\[MolecularEntity],%20\[SequenceVariant]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[SequenceVariant]-%20in%20taxon(i)%20%3F>\[OrganismTaxon])
## Mappings

 * [GENO:0000002](http://purl.obolibrary.org/obo/GENO_0000002)
 * [WD:Q15304597](http://purl.obolibrary.org/obo/WD_Q15304597)
 * [SIO:010277](http://semanticscience.org/resource/SIO_010277)
 * [VMC:Allele](http://purl.obolibrary.org/obo/VMC_Allele)
## Inheritance

 *  is_a: [genomic entity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
## Children

## Used in

 *  class: [genotype to variant association](GenotypeToVariantAssociation.md) references: [sequence variant](SequenceVariant.md)
 *  class: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.md) references: [sequence variant](SequenceVariant.md)
 *  class: [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.md) references: [sequence variant](SequenceVariant.md)
 *  class: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md) references: [sequence variant](SequenceVariant.md)
 *  class: [variant to population association](VariantToPopulationAssociation.md) references: [sequence variant](SequenceVariant.md)
 *  class: [variant to thing association](VariantToThingAssociation.md) references: [sequence variant](SequenceVariant.md)
## Fields

 * _[has biological sequence](has_biological_sequence.md)_
    * _connects a genomic feature to its sequence_
    * range: [biological sequence](BiologicalSequence.md)
    * __Local__
 * _[has gene](has_gene.md)_
    * _Each allele can be associated with any number of genes_
    * range: string*
    * __Local__
 * _[id](id.md) *subsets*: (translator_minimal)_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: [identifier type](IdentifierType.md)
    * Example: [ZFIN:ZDB-ALT-980203-1091](http://purl.obolibrary.org/obo/ZFIN_ZDB-ALT-980203-1091) ti282a allele from ZFIN
    * Example: [ClinVarVariant:17681](http://purl.obolibrary.org/obo/ClinVarVariant_17681) NM_007294.3(BRCA1):c.2521C>T (p.Arg841Trp)
    * __Local__
 * _[biomarker for](biomarker_for.md) *subsets*: (translator_minimal)_
    * _holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature._
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[category](category.md) *subsets*: (translator_minimal)_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[description](description.md) *subsets*: (translator_minimal)_
    * _a human-readable description of a thing_
    * range: [narrative text](NarrativeText.md)
    * inherited from: [named thing](NamedThing.md)
 * _[full name](full_name.md)_
    * _a long-form human readable name for a thing_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[has phenotype](has_phenotype.md) *subsets*: (translator_minimal)_
    * _holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). _
    * range: [phenotype](Phenotype.md)
    * inherited from: [biological entity](BiologicalEntity.md)
 * _[in taxon](in_taxon.md) *subsets*: (translator_minimal)_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [thing with taxon](ThingWithTaxon.md)
 * _[iri](iri.md) *subsets*: (translator_minimal)_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: [iri type](IriType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[molecularly interacts with](molecularly_interacts_with.md) *subsets*: (translator_minimal)_
    * _holds between two entities that make physical contact as part of some interaction_
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[name](name.md) *subsets*: (translator_minimal)_
    * _A human-readable name for a thing_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[node property](node_property.md)_
    * _A grouping for any property that holds between a node and a value_
    * range: string
    * inherited from: [named thing](NamedThing.md)
 * _[regulates, entity to entity](regulates_entity_to_entity.md) *subsets*: (translator_minimal)_
    * _describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be._
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[systematic synonym](systematic_synonym.md)_
    * _more commonly used for gene symbols in yeast_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
