# Class: association


A typed association between two entities, supported by evidence

URI: [http://bioentity.io/vocab/Association](http://bioentity.io/vocab/Association)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Association|subject:string;negated:boolean%20%3F;object:string;association_slot:string%20%3F;id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F]-%20related%20to(i)%20%3F>\[NamedThing],%20\[Association]-%20provided%20by%20%3F>\[Provider],%20\[Association]-%20publications%20*>\[Publication],%20\[Association]-%20qualifiers%20*>\[OntologyClass],%20\[Association]-%20relation>\[RelationshipType],%20\[Association]-%20association%20type%20%3F>\[OntologyClass],%20\[Association]^-\[VariantToThingAssociation],%20\[Association]^-\[VariantToPopulationAssociation],%20\[Association]^-\[VariantToPhenotypicFeatureAssociation],%20\[Association]^-\[VariantToDiseaseAssociation],%20\[Association]^-\[ThingToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[SequenceVariantModulatesTreatmentAssociation],%20\[Association]^-\[SequenceFeatureRelationship],%20\[Association]^-\[PopulationToPopulationAssociation],%20\[Association]^-\[MolecularInteraction],%20\[Association]^-\[GenotypeToVariantAssociation],%20\[Association]^-\[GenotypeToThingAssociation],%20\[Association]^-\[GenotypeToPhenotypicFeatureAssociation],%20\[Association]^-\[GenotypeToGenotypePartAssociation],%20\[Association]^-\[GenotypeToGeneAssociation],%20\[Association]^-\[GenomicSequenceLocalization],%20\[Association]^-\[GeneToThingAssociation],%20\[Association]^-\[GeneToPhenotypicFeatureAssociation],%20\[Association]^-\[GeneToGeneAssociation],%20\[Association]^-\[GeneToExpressionSiteAssociation],%20\[Association]^-\[GeneToDiseaseAssociation],%20\[Association]^-\[GeneRegulatoryRelationship],%20\[Association]^-\[FunctionalAssociation],%20\[Association]^-\[EnvironmentToPhenotypicFeatureAssociation],%20\[Association]^-\[EntityToPhenotypicFeatureAssociation],%20\[Association]^-\[DiseaseToThingAssociation],%20\[Association]^-\[DiseaseToPhenotypicFeatureAssociation],%20\[Association]^-\[DiseaseOrPhenotypicFeatureAssociationToThingAssociation],%20\[Association]^-\[ChemicalToThingAssociation],%20\[Association]^-\[ChemicalToPathwayAssociation],%20\[Association]^-\[ChemicalToGeneAssociation],%20\[Association]^-\[ChemicalToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[CellLineToThingAssociation],%20\[Association]^-\[CellLineToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[CaseToThingAssociation],%20\[Association]^-\[CaseToPhenotypicFeatureAssociation],%20\[Association]^-\[BiosampleToThingAssociation],%20\[Association]^-\[BiosampleToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[AnatomicalEntityToAnatomicalEntityAssociation],%20\[InformationContentEntity]^-\[Association])
## Mappings

 * [OBAN:association](http://purl.obolibrary.org/obo/OBAN_association)
 * [rdf:Statement](http://purl.obolibrary.org/obo/rdf_Statement)
 * [owl:Axiom](http://purl.obolibrary.org/obo/owl_Axiom)
## Inheritance

 *  is_a: information content entity
## Children

 * anatomical entity to anatomical entity association
 * biosample to disease or phenotypic feature association
 * biosample to thing association
 * case to phenotypic feature association
 * case to thing association
 * cell line to disease or phenotypic feature association
 * cell line to thing association
 * chemical to disease or phenotypic feature association
 * chemical to gene association
 * chemical to pathway association
 * chemical to thing association
 * disease or phenotypic feature association to thing association
 * disease to phenotypic feature association
 * disease to thing association
 * entity to phenotypic feature association
 * environment to phenotypic feature association
 * functional association
 * gene regulatory relationship
 * gene to disease association
 * gene to expression site association
 * gene to gene association
 * gene to phenotypic feature association
 * gene to thing association
 * genomic sequence localization
 * genotype to gene association
 * genotype to genotype part association
 * genotype to phenotypic feature association
 * genotype to thing association
 * genotype to variant association
 * molecular interaction
 * population to population association
 * sequence feature relationship
 * sequence variant modulates treatment association
 * thing to disease or phenotypic feature association
 * variant to disease association
 * variant to phenotypic feature association
 * variant to population association
 * variant to thing association
## Used in

## Fields

 * _association slot_
    * _any slot that relates an association to another entity_
    * range: **string**
    * __Local__
 * _association type_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: ontology class
    * __Local__
 * _negated_
    * _if set to true, then the association is negated i.e. is not true_
    * range: **boolean**
    * __Local__
 * _object_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: **string** [required]
    * __Local__
 * _provided by_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: provider
    * __Local__
 * _publications_
    * _connects an association to publications supporting the association_
    * range: publication*
    * __Local__
 * _qualifiers_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: ontology class*
    * __Local__
 * _relation_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: relationship type [required]
    * __Local__
 * _subject_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: **string** [required]
    * __Local__
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
 * _id_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: identifier type
    * inherited from: named thing
 * _iri_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: iri type
    * inherited from: named thing
 * _name_
    * _A human-readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _node property_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * inherited from: named thing
 * _related to_
    * _A grouping for any relationship type that holds between any two things_
    * range: named thing
    * inherited from: named thing
 * _systematic synonym_
    * _more commonly used for gene symbols in yeast_
    * range: label type
    * inherited from: named thing
