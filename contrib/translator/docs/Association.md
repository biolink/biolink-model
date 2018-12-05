# Class: association


A typed association between two entities, supported by evidence

URI: [http://w3id.org/biolink/vocab/Association](http://w3id.org/biolink/vocab/Association)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Association|subject:string;negated:boolean%20%3F;object:string;association_slot:string%20%3F;id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):iri_type%20*;uri(i):uri%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;title(i):label_type%20%3F]-%20related%20to(i)%20%3F>\[NamedThing],%20\[Association]-%20provided%20by%20%3F>\[Provider],%20\[Association]-%20publications%20*>\[Publication],%20\[Association]-%20qualifiers%20*>\[OntologyClass],%20\[Association]-%20relation>\[RelationshipType],%20\[Association]-%20association%20type%20%3F>\[OntologyClass],%20\[Association]^-\[VariantToThingAssociation],%20\[Association]^-\[VariantToPopulationAssociation],%20\[Association]^-\[VariantToPhenotypicFeatureAssociation],%20\[Association]^-\[VariantToDiseaseAssociation],%20\[Association]^-\[ThingToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[SequenceVariantModulatesTreatmentAssociation],%20\[Association]^-\[SequenceFeatureRelationship],%20\[Association]^-\[PopulationToPopulationAssociation],%20\[Association]^-\[PairwiseInteractionAssociation],%20\[Association]^-\[GenotypeToVariantAssociation],%20\[Association]^-\[GenotypeToThingAssociation],%20\[Association]^-\[GenotypeToPhenotypicFeatureAssociation],%20\[Association]^-\[GenotypeToGenotypePartAssociation],%20\[Association]^-\[GenotypeToGeneAssociation],%20\[Association]^-\[GenomicSequenceLocalization],%20\[Association]^-\[GeneToThingAssociation],%20\[Association]^-\[GeneToPhenotypicFeatureAssociation],%20\[Association]^-\[GeneToGeneAssociation],%20\[Association]^-\[GeneToExpressionSiteAssociation],%20\[Association]^-\[GeneToDiseaseAssociation],%20\[Association]^-\[GeneRegulatoryRelationship],%20\[Association]^-\[FunctionalAssociation],%20\[Association]^-\[EnvironmentToPhenotypicFeatureAssociation],%20\[Association]^-\[EntityToPhenotypicFeatureAssociation],%20\[Association]^-\[DiseaseToThingAssociation],%20\[Association]^-\[DiseaseToPhenotypicFeatureAssociation],%20\[Association]^-\[DiseaseOrPhenotypicFeatureAssociationToThingAssociation],%20\[Association]^-\[ChemicalToThingAssociation],%20\[Association]^-\[ChemicalToPathwayAssociation],%20\[Association]^-\[ChemicalToGeneAssociation],%20\[Association]^-\[ChemicalToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[CellLineToThingAssociation],%20\[Association]^-\[CellLineToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[CaseToThingAssociation],%20\[Association]^-\[CaseToPhenotypicFeatureAssociation],%20\[Association]^-\[BiosampleToThingAssociation],%20\[Association]^-\[BiosampleToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[AnatomicalEntityToAnatomicalEntityAssociation],%20\[InformationContentEntity]^-\[Association])
## Mappings

 * [OBAN:association](http://purl.obolibrary.org/obo/OBAN_association)
 * [rdf:Statement](http://purl.obolibrary.org/obo/rdf_Statement)
 * [owl:Axiom](http://purl.obolibrary.org/obo/owl_Axiom)
## Inheritance

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.
## Children

 * [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
 * [BiosampleToDiseaseOrPhenotypicFeatureAssociation](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md) - An association between a biosample and a disease or phenotype
 * [BiosampleToThingAssociation](BiosampleToThingAssociation.md) - An association between a biosample and something
 * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
 * [CaseToThingAssociation](CaseToThingAssociation.md) - An abstract association for use where the case is the subject
 * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype
 * [CellLineToThingAssociation](CellLineToThingAssociation.md) - An relationship between a cell line and another entity
 * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
 * [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) - An interaction between a chemical entity and a gene or gene product
 * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) - An interaction between a chemical entity and a biological process or pathway
 * [ChemicalToThingAssociation](ChemicalToThingAssociation.md) - An interaction between a chemical entity and another entity
 * [DiseaseOrPhenotypicFeatureAssociationToThingAssociation](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)
 * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
 * [DiseaseToThingAssociation](DiseaseToThingAssociation.md)
 * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
 * [EnvironmentToPhenotypicFeatureAssociation](EnvironmentToPhenotypicFeatureAssociation.md) - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
 * [FunctionalAssociation](FunctionalAssociation.md) - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed
 * [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) - A regulatory relationship between two genes
 * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)
 * [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) - An association between a gene and an expression site, possibly qualified by stage/timing info.
 * [GeneToGeneAssociation](GeneToGeneAssociation.md) - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
 * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md)
 * [GeneToThingAssociation](GeneToThingAssociation.md)
 * [GenomicSequenceLocalization](GenomicSequenceLocalization.md) - A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
 * [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) - Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
 * [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) - Any association between one genotype and a genotypic entity that is a sub-component of it
 * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
 * [GenotypeToThingAssociation](GenotypeToThingAssociation.md)
 * [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) - Any association between a genotype and a sequence variant.
 * [PairwiseInteractionAssociation](PairwiseInteractionAssociation.md) - An interaction at the molecular level between two physical entities
 * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) - An association between a two populations
 * [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene
 * [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) - An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
 * [ThingToDiseaseOrPhenotypicFeatureAssociation](ThingToDiseaseOrPhenotypicFeatureAssociation.md)
 * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md)
 * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)
 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population
 * [VariantToThingAssociation](VariantToThingAssociation.md)
## Used in

## Fields

 * [association slot](association_slot.md)
    * Description: any slot that relates an association to another entity
    * range: **string**
    * __Local__
 * [association type](association_type.md)
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * __Local__
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * __Local__
 * [object](object.md)
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: **string** [required]
    * __Local__
 * [provided by](provided_by.md)
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * __Local__
 * [publications](publications.md)
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)*
    * __Local__
 * [qualifiers](qualifiers.md)
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)*
    * __Local__
 * [relation](relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [RelationshipType](RelationshipType.md) [required]
    * __Local__
 * [subject](subject.md)
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: **string** [required]
    * __Local__
 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [id](id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [iri](iri.md) *subsets*: (translator_minimal)
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [name](name.md) *subsets*: (translator_minimal)
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [node property](node_property.md)
    * Description: A grouping for any property that holds between a node and a value
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [title](title.md)
    * Description: Narrative text describing the entity
    * range: [LabelType](LabelType.md)
    * inherited from: [InformationContentEntity](InformationContentEntity.md)
 * [uri](uri.md)
    * Description: URI expansion of CURIE
    * range: [uri](uri.md)
    * inherited from: [NamedThing](NamedThing.md)
