# Class: gene or gene product


a union of genes or gene products. Frequently an identifier for one will be used as proxy for another

URI: [http://bioentity.io/vocab/GeneOrGeneProduct](http://bioentity.io/vocab/GeneOrGeneProduct)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneOrGeneProduct|id(i):identifier_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F;has_biological_sequence(i):biological_sequence%20%3F;name(i):label_type%20%3F]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[GeneOrGeneProduct]-%20regulates,%20entity%20to%20entity(i)%20%3F>\[MolecularEntity],%20\[GeneOrGeneProduct]-%20molecularly%20interacts%20with(i)%20%3F>\[MolecularEntity],%20\[GeneOrGeneProduct]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[GeneOrGeneProduct]-%20related%20to(i)%20%3F>\[NamedThing],%20\[GeneOrGeneProduct]-%20expressed%20in%20%3F>\[AnatomicalEntity],%20\[GeneOrGeneProduct]-%20in%20cell%20population%20with%20%3F>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]-%20in%20complex%20with%20%3F>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]-%20in%20pathway%20with%20%3F>\[GeneOrGeneProduct],%20\[ChemicalToGeneAssociation]-%20object(i)>\[GeneOrGeneProduct],%20\[AnatomicalEntity]-%20expresses(i)%20%3F>\[GeneOrGeneProduct],%20\[GeneAsAModelOfDiseaseAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneRegulatoryRelationship]-%20object(i)>\[GeneOrGeneProduct],%20\[GeneRegulatoryRelationship]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneToDiseaseAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneToExpressionSiteAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneToGeneAssociation]-%20object(i)>\[GeneOrGeneProduct],%20\[GeneToGeneAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneToPhenotypicFeatureAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneToThingAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]-%20in%20cell%20population%20with%20%3F>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]-%20in%20complex%20with%20%3F>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]-%20in%20pathway%20with%20%3F>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]^-\[GeneProduct],%20\[GeneOrGeneProduct]^-\[Gene],%20\[MacromolecularMachine]^-\[GeneOrGeneProduct])
## Mappings

## Inheritance

 *  is_a: macromolecular machine
## Children

 * gene
 * gene product
## Used in

 *  class: **chemical to gene association** *chemical to gene association object* **gene or gene product**
 *  class: **anatomical entity** *expresses* **gene or gene product**
 *  class: **gene as a model of disease association** *gene as a model of disease association subject* **gene or gene product**
 *  class: **gene has variant that contributes to disease association** *gene has variant that contributes to disease association subject* **gene or gene product**
 *  class: **gene regulatory relationship** *gene regulatory relationship object* **gene or gene product**
 *  class: **gene regulatory relationship** *gene regulatory relationship subject* **gene or gene product**
 *  class: **gene to disease association** *gene to disease association subject* **gene or gene product**
 *  class: **gene to expression site association** *gene to expression site association subject* **gene or gene product**
 *  class: **gene to gene association** *gene to gene association object* **gene or gene product**
 *  class: **gene to gene association** *gene to gene association subject* **gene or gene product**
 *  class: **gene to phenotypic feature association** *gene to phenotypic feature association subject* **gene or gene product**
 *  class: **gene to thing association** *gene to thing association subject* **gene or gene product**
 *  class: **gene or gene product** *in cell population with* **gene or gene product**
 *  class: **gene or gene product** *in complex with* **gene or gene product**
 *  class: **gene or gene product** *in pathway with* **gene or gene product**
## Fields

 * _expressed in_
    * _holds between a gene or gene product and an anatomical entity in which it is expressed_
    * range: anatomical entity
    * __Local__
 * _in cell population with_
    * _holds between two genes or gene products that are expressed in the same cell type or population _
    * range: gene or gene product
    * __Local__
 * _in complex with_
    * _holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex_
    * range: gene or gene product
    * __Local__
 * _in pathway with_
    * _holds between two genes or gene products that are part of in the same biological pathway_
    * range: gene or gene product
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
 * _macromolecular machine name_
    * _A human-readable name for a thing_
    * range: label type
    * inherited from: macromolecular machine
 * _molecularly interacts with_
    * _holds between two entities that make physical contact as part of some interaction_
    * range: molecular entity
    * inherited from: molecular entity
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
