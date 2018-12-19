# Class: association


A typed association between two entities, supported by evidence

URI: [http://w3id.org/biolink/vocab/Association](http://w3id.org/biolink/vocab/Association)

![img](images/Association.png)
## Mappings

 * [OBAN:association](http://purl.obolibrary.org/obo/OBAN_association)
 * [rdf:Statement](http://purl.obolibrary.org/obo/rdf_Statement)
 * [owl:Axiom](http://purl.obolibrary.org/obo/owl_Axiom)
## Inheritance

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
 * [association.id](association_id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
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
