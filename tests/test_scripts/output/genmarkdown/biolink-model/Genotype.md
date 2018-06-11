# Class: genotype


An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background

URI: [http://bioentity.io/vocab/Genotype](http://bioentity.io/vocab/Genotype)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Genotype|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F;has_biological_sequence(i):biological_sequence%20%3F]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[Genotype]-%20regulates,%20entity%20to%20entity(i)%20%3F>\[MolecularEntity],%20\[Genotype]-%20molecularly%20interacts%20with(i)%20%3F>\[MolecularEntity],%20\[Genotype]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[Genotype]-%20related%20to(i)%20%3F>\[NamedThing],%20\[Genotype]-%20has%20zygosity%20%3F>\[Zygosity],%20\[GenotypeToVariantAssociation]-%20subject(i)>\[Genotype],%20\[GenotypeToGenotypePartAssociation]-%20object(i)>\[Genotype],%20\[GenotypeToThingAssociation]-%20subject(i)>\[Genotype],%20\[GenotypeToGeneAssociation]-%20subject(i)>\[Genotype],%20\[GenotypeToPhenotypicFeatureAssociation]-%20subject(i)>\[Genotype],%20\[GenotypeToGenotypePartAssociation]-%20subject(i)>\[Genotype],%20\[GenomicEntity]^-\[Genotype])
## Mappings

 * [GENO:0000536](http://purl.obolibrary.org/obo/GENO_0000536)
 * [SIO:001079](http://semanticscience.org/resource/SIO_001079)
## Inheritance

 *  is_a: genomic entity
## Children

## Used in

 *  class: **genotype to gene association** *genotype to gene association subject* **genotype**
 *  class: **genotype to genotype part association** *genotype to genotype part association object* **genotype**
 *  class: **genotype to genotype part association** *genotype to genotype part association subject* **genotype**
 *  class: **genotype to phenotypic feature association** *genotype to phenotypic feature association subject* **genotype**
 *  class: **genotype to thing association** *genotype to thing association subject* **genotype**
 *  class: **genotype to variant association** *genotype to variant association subject* **genotype**
## Fields

 * _has zygosity_
    * _A grouping for any property that holds between a node and a value_
    * range: zygosity
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
 * _has biological sequence_
    * _connects a genomic feature to its sequence_
    * range: biological sequence
    * inherited from: genomic entity
 * _has phenotype_
    * _holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). _
    * range: phenotype
    * inherited from: biological entity
 * _id_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: identifier type
    * inherited from: named thing
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
