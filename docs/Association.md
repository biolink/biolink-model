# Class: association


A typed association between two entities, supported by evidence

URI: [http://bioentity.io/vocab/Association](http://bioentity.io/vocab/Association)

![img](images/Association.png)
## Mappings

 * [OBAN:association](http://purl.obolibrary.org/obo/OBAN_association)
 * [rdf:Statement](http://purl.obolibrary.org/obo/rdf_Statement)
 * [owl:Axiom](http://purl.obolibrary.org/obo/owl_Axiom)
## Inheritance

 *  is_a: [information content entity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.
## Children

 *  child: [variant to thing association](VariantToThingAssociation.md)
 *  child: [variant to disease association](VariantToDiseaseAssociation.md)
 *  child: [chemical to thing association](ChemicalToThingAssociation.md) - An interaction between a chemical entity and another entity
 *  child: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
 *  child: [gene to disease association](GeneToDiseaseAssociation.md)
 *  child: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md) - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
 *  child: [gene to thing association](GeneToThingAssociation.md)
 *  child: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.md) - An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
 *  child: [gene to expression site association](GeneToExpressionSiteAssociation.md) - An association between a gene and an expression site, possibly qualified by stage/timing info.
 *  child: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
 *  child: [molecular interaction](MolecularInteraction.md) - An interaction at the molecular level between two physical entities
 *  child: [variant to population association](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population
 *  child: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md) - An association between a biosample and a disease or phenotype
 *  child: [gene regulatory relationship](GeneRegulatoryRelationship.md) - A regulatory relationship between two genes
 *  child: [chemical to gene association](ChemicalToGeneAssociation.md) - An interaction between a chemical entity and a gene or gene product
 *  child: [sequence feature relationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene
 *  child: [disease or phenotypic feature association to thing association](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)
 *  child: [genotype to thing association](GenotypeToThingAssociation.md)
 *  child: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md)
 *  child: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md) - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
 *  child: [biosample to thing association](BiosampleToThingAssociation.md) - An association between a biosample and something
 *  child: [disease to thing association](DiseaseToThingAssociation.md)
 *  child: [genotype to genotype part association](GenotypeToGenotypePartAssociation.md) - Any association between one genotype and a genotypic entity that is a sub-component of it
 *  child: [functional association](FunctionalAssociation.md) - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed
 *  child: [genomic sequence localization](GenomicSequenceLocalization.md) - A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
 *  child: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype
 *  child: [population to population association](PopulationToPopulationAssociation.md) - An association between a two populations
 *  child: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.md)
 *  child: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.md) - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
 *  child: [cell line to thing association](CellLineToThingAssociation.md) - An relationship between a cell line and another entity
 *  child: [chemical to pathway association](ChemicalToPathwayAssociation.md) - An interaction between a chemical entity and a biological process or pathway
 *  child: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
 *  child: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md)
 *  child: [gene to gene association](GeneToGeneAssociation.md) - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
 *  child: [genotype to gene association](GenotypeToGeneAssociation.md) - Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
 *  child: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md) - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
 *  child: [case to thing association](CaseToThingAssociation.md) - An abstract association for use where the case is the subject
 *  child: [genotype to variant association](GenotypeToVariantAssociation.md) - Any association between a genotype and a sequence variant.
## Used in

 *  class: [association](Association.md) references: [variant to thing association](VariantToThingAssociation.md)
 *  class: [association](Association.md) references: [variant to disease association](VariantToDiseaseAssociation.md)
 *  class: [association](Association.md) references: [chemical to thing association](ChemicalToThingAssociation.md)
 *  class: [association](Association.md) references: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [gene to disease association](GeneToDiseaseAssociation.md)
 *  class: [association](Association.md) references: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [gene to thing association](GeneToThingAssociation.md)
 *  class: [association](Association.md) references: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.md)
 *  class: [association](Association.md) references: [gene to expression site association](GeneToExpressionSiteAssociation.md)
 *  class: [association](Association.md) references: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [molecular interaction](MolecularInteraction.md)
 *  class: [association](Association.md) references: [variant to population association](VariantToPopulationAssociation.md)
 *  class: [association](Association.md) references: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [gene regulatory relationship](GeneRegulatoryRelationship.md)
 *  class: [association](Association.md) references: [chemical to gene association](ChemicalToGeneAssociation.md)
 *  class: [association](Association.md) references: [sequence feature relationship](SequenceFeatureRelationship.md)
 *  class: [association](Association.md) references: [disease or phenotypic feature association to thing association](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)
 *  class: [association](Association.md) references: [genotype to thing association](GenotypeToThingAssociation.md)
 *  class: [association](Association.md) references: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [biosample to thing association](BiosampleToThingAssociation.md)
 *  class: [association](Association.md) references: [disease to thing association](DiseaseToThingAssociation.md)
 *  class: [association](Association.md) references: [genotype to genotype part association](GenotypeToGenotypePartAssociation.md)
 *  class: [association](Association.md) references: [functional association](FunctionalAssociation.md)
 *  class: [association](Association.md) references: [genomic sequence localization](GenomicSequenceLocalization.md)
 *  class: [association](Association.md) references: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [population to population association](PopulationToPopulationAssociation.md)
 *  class: [association](Association.md) references: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.md)
 *  class: [association](Association.md) references: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [cell line to thing association](CellLineToThingAssociation.md)
 *  class: [association](Association.md) references: [chemical to pathway association](ChemicalToPathwayAssociation.md)
 *  class: [association](Association.md) references: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [gene to gene association](GeneToGeneAssociation.md)
 *  class: [association](Association.md) references: [genotype to gene association](GenotypeToGeneAssociation.md)
 *  class: [association](Association.md) references: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [case to thing association](CaseToThingAssociation.md)
 *  class: [association](Association.md) references: [genotype to variant association](GenotypeToVariantAssociation.md)
## Fields

 * _[association type](association_type.md)_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: [ontology class](OntologyClass.md)
    * __Local__
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: string [required]
    * __Local__
 * _[negated](negated.md)_
    * _if set to true, then the association is negated i.e. is not true_
    * range: boolean
    * __Local__
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * __Local__
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: string [required]
    * __Local__
 * _[qualifiers](qualifiers.md)_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: [ontology class](OntologyClass.md)*
    * __Local__
 * _[publications](publications.md)_
    * _connects an association to publications supporting the association_
    * range: [publication](Publication.md)*
    * __Local__
 * _[provided by](provided_by.md)_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: [provider](Provider.md)
    * __Local__
 * _[association slot](association_slot.md)_
    * _any slot that relates an association to another entity_
    * range: string
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
