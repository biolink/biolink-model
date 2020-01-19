---
parent: Classes
title: biolink:Association
grand_parent: Browse Biolink Model
---

# Type: Association


A typed association between two entities, supported by evidence

URI: [biolink:Association](https://w3id.org/biolink/vocab/Association)

OBAN:association
{: .mapping-label }

rdf:Statement
{: .mapping-label }

owl:Axiom
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by%200..1-%20\[Association&#124;relation:uriorcurie;id:nodeidentifier;negated:boolean%20%3F],%20\[Publication]<publications%200..*-%20\[Association],%20\[OntologyClass]<qualifiers%200..*-%20\[Association],%20\[OntologyClass]<association%20type%200..1-%20\[Association],%20\[NamedThing]<object%201..1-%20\[Association],%20\[NamedThing]<subject%201..1-%20\[Association],%20\[Association]^-\[VariantToThingAssociation],%20\[Association]^-\[VariantToPopulationAssociation],%20\[Association]^-\[VariantToPhenotypicFeatureAssociation],%20\[Association]^-\[VariantToDiseaseAssociation],%20\[Association]^-\[ThingToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[SequenceVariantModulatesTreatmentAssociation],%20\[Association]^-\[SequenceFeatureRelationship],%20\[Association]^-\[PopulationToPopulationAssociation],%20\[Association]^-\[PairwiseInteractionAssociation],%20\[Association]^-\[MaterialSampleToThingAssociation],%20\[Association]^-\[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[MaterialSampleDerivationAssociation],%20\[Association]^-\[GenotypeToVariantAssociation],%20\[Association]^-\[GenotypeToThingAssociation],%20\[Association]^-\[GenotypeToPhenotypicFeatureAssociation],%20\[Association]^-\[GenotypeToGenotypePartAssociation],%20\[Association]^-\[GenotypeToGeneAssociation],%20\[Association]^-\[GenomicSequenceLocalization],%20\[Association]^-\[GeneToThingAssociation],%20\[Association]^-\[GeneToPhenotypicFeatureAssociation],%20\[Association]^-\[GeneToGeneAssociation],%20\[Association]^-\[GeneToExpressionSiteAssociation],%20\[Association]^-\[GeneToDiseaseAssociation],%20\[Association]^-\[GeneRegulatoryRelationship],%20\[Association]^-\[FunctionalAssociation],%20\[Association]^-\[ExposureEventToPhenotypicFeatureAssociation],%20\[Association]^-\[EntityToPhenotypicFeatureAssociation],%20\[Association]^-\[DiseaseToThingAssociation],%20\[Association]^-\[DiseaseToPhenotypicFeatureAssociation],%20\[Association]^-\[DiseaseOrPhenotypicFeatureAssociationToThingAssociation],%20\[Association]^-\[ChemicalToThingAssociation],%20\[Association]^-\[ChemicalToPathwayAssociation],%20\[Association]^-\[ChemicalToGeneAssociation],%20\[Association]^-\[ChemicalToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[ChemicalToChemicalAssociation],%20\[Association]^-\[CellLineToThingAssociation],%20\[Association]^-\[CellLineToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[CaseToThingAssociation],%20\[Association]^-\[CaseToPhenotypicFeatureAssociation],%20\[Association]^-\[AnatomicalEntityToAnatomicalEntityAssociation])

---


## Children

 * [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
 * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
 * [CaseToThingAssociation](CaseToThingAssociation.md) - An abstract association for use where the case is the subject
 * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype
 * [CellLineToThingAssociation](CellLineToThingAssociation.md) - An relationship between a cell line and another entity
 * [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) - A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.
 * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
 * [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) - An interaction between a chemical entity and a gene or gene product
 * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) - An interaction between a chemical entity and a biological process or pathway
 * [ChemicalToThingAssociation](ChemicalToThingAssociation.md) - An interaction between a chemical entity and another entity
 * [DiseaseOrPhenotypicFeatureAssociationToThingAssociation](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)
 * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
 * [DiseaseToThingAssociation](DiseaseToThingAssociation.md)
 * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
 * [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
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
 * [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) - An association between a material sample and the material entity it is derived from
 * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) - An association between a material sample and a disease or phenotype
 * [MaterialSampleToThingAssociation](MaterialSampleToThingAssociation.md) - An association between a material sample and something
 * [PairwiseInteractionAssociation](PairwiseInteractionAssociation.md) - An interaction at the molecular level between two physical entities
 * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) - An association between a two populations
 * [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene
 * [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) - An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
 * [ThingToDiseaseOrPhenotypicFeatureAssociation](ThingToDiseaseOrPhenotypicFeatureAssociation.md)
 * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md)
 * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md)
 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population
 * [VariantToThingAssociation](VariantToThingAssociation.md)

## Referenced by class


## Attributes


### Own

 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [Nodeidentifier](types/Nodeidentifier.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [association slot](association_slot.md)  <sub>OPT</sub>
    * Description: any slot that relates an association to another entity
    * range: [String](types/String.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [Nodeidentifier](types/Nodeidentifier.md)
    * in subsets: (translator_minimal)
 * [change is catalyzed by](change_is_catalyzed_by.md)  <sub>0..*</sub>
    * Description: hyperedge connecting an association between two causally connected entities (for example, two chemical entities, or a chemical entity in that changes location) and the gene product, gene, or complex that enables or catalyzes the change.
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [clinical modifier qualifier](clinical_modifier_qualifier.md)  <sub>OPT</sub>
    * Description: Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
    * range: [ClinicalModifier](ClinicalModifier.md)
 * [edge label](edge_label.md)  <sub>REQ</sub>
    * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * range: [LabelType](types/LabelType.md)
 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)
 * [has confidence level](has_confidence_level.md)  <sub>OPT</sub>
    * Description: connects an association to a qualitative term denoting the level of confidence
    * range: [ConfidenceLevel](ConfidenceLevel.md)
 * [has evidence](has_evidence.md)  <sub>OPT</sub>
    * Description: connects an association to an instance of supporting evidence
    * range: [EvidenceType](EvidenceType.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [onset qualifier](onset_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [quantifier qualifier](quantifier_qualifier.md)  <sub>OPT</sub>
    * Description: A measurable quantity for the object of the association
    * range: [OntologyClass](OntologyClass.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [sequence variant qualifier](sequence_variant_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in an association where the variant
    * range: [SequenceVariant](SequenceVariant.md)
 * [severity qualifier](severity_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)
 * [sex qualifier](sex_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
    * range: [BiologicalSex](BiologicalSex.md)
 * [stage qualifier](stage_qualifier.md)  <sub>OPT</sub>
    * Description: stage at which expression takes place
    * range: [LifeStage](LifeStage.md)
 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | OBAN:association |
|  | | rdf:Statement |
|  | | owl:Axiom |
| **Comments:** | | This is roughly the model used by biolink and ontobio at the moment |

