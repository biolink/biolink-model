---
parent: Classes
title: biolink:Association
grand_parent: Browse Biolink Model
layout: default
---

# Class: Association


A typed association between two entities, supported by evidence

URI: [biolink:Association](https://w3id.org/biolink/vocab/Association)

OBAN:association
{: .mapping-label }

rdf:Statement
{: .mapping-label }

owl:Axiom
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VariantToThingAssociation],[VariantToPopulationAssociation],[VariantToPhenotypicFeatureAssociation],[VariantToDiseaseAssociation],[ThingToDiseaseOrPhenotypicFeatureAssociation],[SequenceVariantModulatesTreatmentAssociation],[SequenceFeatureRelationship],[SequenceAssociation],[Publication],[Provider],[PopulationToPopulationAssociation],[PairwiseInteractionAssociation],[OrganismalEntityAsAModelOfDiseaseAssociation],[OntologyClass],[NamedThing],[MaterialSampleToThingAssociation],[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation],[MaterialSampleDerivationAssociation],[GenotypeToVariantAssociation],[GenotypeToThingAssociation],[GenotypeToPhenotypicFeatureAssociation],[GenotypeToGenotypePartAssociation],[GenotypeToGeneAssociation],[GenotypeToDiseaseAssociation],[GeneToThingAssociation],[GeneToPhenotypicFeatureAssociation],[GeneToGeneAssociation],[GeneToExpressionSiteAssociation],[GeneToDiseaseAssociation],[GeneRegulatoryRelationship],[FunctionalAssociation],[ExposureEventToPhenotypicFeatureAssociation],[EntityToPhenotypicFeatureAssociation],[DiseaseToThingAssociation],[DiseaseToPhenotypicFeatureAssociation],[DiseaseOrPhenotypicFeatureAssociationToThingAssociation],[ChemicalToThingAssociation],[ChemicalToPathwayAssociation],[ChemicalToGeneAssociation],[ChemicalToDiseaseOrPhenotypicFeatureAssociation],[ChemicalToChemicalAssociation],[CellLineToThingAssociation],[CellLineToDiseaseOrPhenotypicFeatureAssociation],[CaseToThingAssociation],[CaseToPhenotypicFeatureAssociation],[Provider]%3Cprovided%20by%200..%2A-%20[Association%7Crelation:uriorcurie;id:string;negated:boolean%20%3F],[Publication]%3Cpublications%200..%2A-%20[Association],[OntologyClass]%3Cqualifiers%200..%2A-%20[Association],[OntologyClass]%3Cassociation%20type%200..1-%20[Association],[NamedThing]%3Cobject%201..1-%20[Association],[NamedThing]%3Csubject%201..1-%20[Association],[Association]%5E-[VariantToThingAssociation],[Association]%5E-[VariantToPopulationAssociation],[Association]%5E-[VariantToPhenotypicFeatureAssociation],[Association]%5E-[VariantToDiseaseAssociation],[Association]%5E-[ThingToDiseaseOrPhenotypicFeatureAssociation],[Association]%5E-[SequenceVariantModulatesTreatmentAssociation],[Association]%5E-[SequenceFeatureRelationship],[Association]%5E-[SequenceAssociation],[Association]%5E-[PopulationToPopulationAssociation],[Association]%5E-[PairwiseInteractionAssociation],[Association]%5E-[OrganismalEntityAsAModelOfDiseaseAssociation],[Association]%5E-[MaterialSampleToThingAssociation],[Association]%5E-[MaterialSampleToDiseaseOrPhenotypicFeatureAssociation],[Association]%5E-[MaterialSampleDerivationAssociation],[Association]%5E-[GenotypeToVariantAssociation],[Association]%5E-[GenotypeToThingAssociation],[Association]%5E-[GenotypeToPhenotypicFeatureAssociation],[Association]%5E-[GenotypeToGenotypePartAssociation],[Association]%5E-[GenotypeToGeneAssociation],[Association]%5E-[GenotypeToDiseaseAssociation],[Association]%5E-[GeneToThingAssociation],[Association]%5E-[GeneToPhenotypicFeatureAssociation],[Association]%5E-[GeneToGeneAssociation],[Association]%5E-[GeneToExpressionSiteAssociation],[Association]%5E-[GeneToDiseaseAssociation],[Association]%5E-[GeneRegulatoryRelationship],[Association]%5E-[FunctionalAssociation],[Association]%5E-[ExposureEventToPhenotypicFeatureAssociation],[Association]%5E-[EntityToPhenotypicFeatureAssociation],[Association]%5E-[DiseaseToThingAssociation],[Association]%5E-[DiseaseToPhenotypicFeatureAssociation],[Association]%5E-[DiseaseOrPhenotypicFeatureAssociationToThingAssociation],[Association]%5E-[ChemicalToThingAssociation],[Association]%5E-[ChemicalToPathwayAssociation],[Association]%5E-[ChemicalToGeneAssociation],[Association]%5E-[ChemicalToDiseaseOrPhenotypicFeatureAssociation],[Association]%5E-[ChemicalToChemicalAssociation],[Association]%5E-[CellLineToThingAssociation],[Association]%5E-[CellLineToDiseaseOrPhenotypicFeatureAssociation],[Association]%5E-[CaseToThingAssociation],[Association]%5E-[CaseToPhenotypicFeatureAssociation],[Association]%5E-[AnatomicalEntityToAnatomicalEntityAssociation],[AnatomicalEntityToAnatomicalEntityAssociation])

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
 * [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md)
 * [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) - Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
 * [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) - Any association between one genotype and a genotypic entity that is a sub-component of it
 * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
 * [GenotypeToThingAssociation](GenotypeToThingAssociation.md)
 * [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) - Any association between a genotype and a sequence variant.
 * [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) - An association between a material sample and the material entity it is derived from
 * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) - An association between a material sample and a disease or phenotype
 * [MaterialSampleToThingAssociation](MaterialSampleToThingAssociation.md) - An association between a material sample and something
 * [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md)
 * [PairwiseInteractionAssociation](PairwiseInteractionAssociation.md) - An interaction at the molecular level between two physical entities
 * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) - An association between a two populations
 * [SequenceAssociation](SequenceAssociation.md) - An association between a sequence feature and a genomic entity it is localized to.
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
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
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

