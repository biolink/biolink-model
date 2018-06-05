# Class: association


A typed association between two entities, supported by evidence

URI: http://bioentity.io/vocab/Association

![img](http://yuml.me/diagram/nofunky/class/\[InformationContentEntity]^-\[Association|subject:string;negated:boolean%20%3F;object:string;association_slot:string%20%3F],%20\[Association]^-\[AnatomicalEntityToAnatomicalEntityAssociation],%20\[Association]^-\[BiosampleToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[BiosampleToThingAssociation],%20\[Association]^-\[CaseToPhenotypicFeatureAssociation],%20\[Association]^-\[CaseToThingAssociation],%20\[Association]^-\[CellLineToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[CellLineToThingAssociation],%20\[Association]^-\[ChemicalToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[ChemicalToGeneAssociation],%20\[Association]^-\[ChemicalToPathwayAssociation],%20\[Association]^-\[ChemicalToThingAssociation],%20\[Association]^-\[DiseaseOrPhenotypicFeatureAssociationToThingAssociation],%20\[Association]^-\[DiseaseToPhenotypicFeatureAssociation],%20\[Association]^-\[DiseaseToThingAssociation],%20\[Association]^-\[EntityToPhenotypicFeatureAssociation],%20\[Association]^-\[EnvironmentToPhenotypicFeatureAssociation],%20\[Association]^-\[FunctionalAssociation],%20\[Association]^-\[GeneRegulatoryRelationship],%20\[Association]^-\[GeneToDiseaseAssociation],%20\[Association]^-\[GeneToExpressionSiteAssociation],%20\[Association]^-\[GeneToGeneAssociation],%20\[Association]^-\[GeneToPhenotypicFeatureAssociation],%20\[Association]^-\[GeneToThingAssociation],%20\[Association]^-\[GenomicSequenceLocalization],%20\[Association]^-\[GenotypeToGeneAssociation],%20\[Association]^-\[GenotypeToGenotypePartAssociation],%20\[Association]^-\[GenotypeToPhenotypicFeatureAssociation],%20\[Association]^-\[GenotypeToThingAssociation],%20\[Association]^-\[GenotypeToVariantAssociation],%20\[Association]^-\[MolecularInteraction],%20\[Association]^-\[PopulationToPopulationAssociation],%20\[Association]^-\[SequenceFeatureRelationship],%20\[Association]^-\[SequenceVariantModulatesTreatmentAssociation],%20\[Association]^-\[ThingToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[VariantToDiseaseAssociation],%20\[Association]^-\[VariantToPhenotypicFeatureAssociation],%20\[Association]^-\[VariantToPopulationAssociation],%20\[Association]^-\[VariantToThingAssociation],%20\[Association]-%20association_type%20%3F>\[OntologyClass],%20\[Association]-%20relation>\[RelationshipType],%20\[Association]-%20qualifiers%20*>\[OntologyClass],%20\[Association]-%20publications%20*>\[Publication],%20\[Association]-%20provided_by%20%3F>\[Provider],%20)
## Mappings

 * [OBAN:association](http://purl.obolibrary.org/obo/OBAN_association)
 * [rdf:Statement](http://purl.obolibrary.org/obo/rdf_Statement)
 * [owl:Axiom](http://purl.obolibrary.org/obo/owl_Axiom)
## Inheritance

 *  is_a: [information content entity](InformationContentEntity.md)
## Children

 *  child: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md)
 *  child: [variant to disease association](VariantToDiseaseAssociation.md)
 *  child: [biosample to thing association](BiosampleToThingAssociation.md)
 *  child: [population to population association](PopulationToPopulationAssociation.md)
 *  child: [gene regulatory relationship](GeneRegulatoryRelationship.md)
 *  child: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
 *  child: [genotype to thing association](GenotypeToThingAssociation.md)
 *  child: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
 *  child: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.md)
 *  child: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md)
 *  child: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md)
 *  child: [variant to thing association](VariantToThingAssociation.md)
 *  child: [chemical to gene association](ChemicalToGeneAssociation.md)
 *  child: [case to thing association](CaseToThingAssociation.md)
 *  child: [gene to thing association](GeneToThingAssociation.md)
 *  child: [molecular interaction](MolecularInteraction.md)
 *  child: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md)
 *  child: [variant to population association](VariantToPopulationAssociation.md)
 *  child: [genomic sequence localization](GenomicSequenceLocalization.md)
 *  child: [genotype to gene association](GenotypeToGeneAssociation.md)
 *  child: [disease or phenotypic feature association to thing association](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)
 *  child: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)
 *  child: [gene to disease association](GeneToDiseaseAssociation.md)
 *  child: [gene to gene association](GeneToGeneAssociation.md)
 *  child: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.md)
 *  child: [chemical to pathway association](ChemicalToPathwayAssociation.md)
 *  child: [genotype to variant association](GenotypeToVariantAssociation.md)
 *  child: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md)
 *  child: [functional association](FunctionalAssociation.md)
 *  child: [disease to thing association](DiseaseToThingAssociation.md)
 *  child: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)
 *  child: [cell line to thing association](CellLineToThingAssociation.md)
 *  child: [sequence feature relationship](SequenceFeatureRelationship.md)
 *  child: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.md)
 *  child: [genotype to genotype part association](GenotypeToGenotypePartAssociation.md)
 *  child: [gene to expression site association](GeneToExpressionSiteAssociation.md)
 *  child: [chemical to thing association](ChemicalToThingAssociation.md)
 *  child: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md)
## Used in

 *  class: [association](Association.md) references: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [variant to disease association](VariantToDiseaseAssociation.md)
 *  class: [association](Association.md) references: [biosample to thing association](BiosampleToThingAssociation.md)
 *  class: [association](Association.md) references: [population to population association](PopulationToPopulationAssociation.md)
 *  class: [association](Association.md) references: [gene regulatory relationship](GeneRegulatoryRelationship.md)
 *  class: [association](Association.md) references: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [genotype to thing association](GenotypeToThingAssociation.md)
 *  class: [association](Association.md) references: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.md)
 *  class: [association](Association.md) references: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [variant to thing association](VariantToThingAssociation.md)
 *  class: [association](Association.md) references: [chemical to gene association](ChemicalToGeneAssociation.md)
 *  class: [association](Association.md) references: [case to thing association](CaseToThingAssociation.md)
 *  class: [association](Association.md) references: [gene to thing association](GeneToThingAssociation.md)
 *  class: [association](Association.md) references: [molecular interaction](MolecularInteraction.md)
 *  class: [association](Association.md) references: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [variant to population association](VariantToPopulationAssociation.md)
 *  class: [association](Association.md) references: [genomic sequence localization](GenomicSequenceLocalization.md)
 *  class: [association](Association.md) references: [genotype to gene association](GenotypeToGeneAssociation.md)
 *  class: [association](Association.md) references: [disease or phenotypic feature association to thing association](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)
 *  class: [association](Association.md) references: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [gene to disease association](GeneToDiseaseAssociation.md)
 *  class: [association](Association.md) references: [gene to gene association](GeneToGeneAssociation.md)
 *  class: [association](Association.md) references: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.md)
 *  class: [association](Association.md) references: [chemical to pathway association](ChemicalToPathwayAssociation.md)
 *  class: [association](Association.md) references: [genotype to variant association](GenotypeToVariantAssociation.md)
 *  class: [association](Association.md) references: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [functional association](FunctionalAssociation.md)
 *  class: [association](Association.md) references: [disease to thing association](DiseaseToThingAssociation.md)
 *  class: [association](Association.md) references: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [cell line to thing association](CellLineToThingAssociation.md)
 *  class: [association](Association.md) references: [sequence feature relationship](SequenceFeatureRelationship.md)
 *  class: [association](Association.md) references: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.md)
 *  class: [association](Association.md) references: [genotype to genotype part association](GenotypeToGenotypePartAssociation.md)
 *  class: [association](Association.md) references: [gene to expression site association](GeneToExpressionSiteAssociation.md)
 *  class: [association](Association.md) references: [chemical to thing association](ChemicalToThingAssociation.md)
 *  class: [association](Association.md) references: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md)
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
