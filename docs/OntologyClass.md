# Class: OntologyClass
_a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type._




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:OntologyClass](https://w3id.org/biolink/vocab/OntologyClass)




## Inheritance

* **OntologyClass**
    * [RelationshipType](RelationshipType.md)
    * [GeneOntologyClass](GeneOntologyClass.md)
    * [UnclassifiedOntologyClass](UnclassifiedOntologyClass.md)
    * [TaxonomicRank](TaxonomicRank.md)




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Attribute](Attribute.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [BiologicalSex](BiologicalSex.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [PhenotypicSex](PhenotypicSex.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [GenotypicSex](GenotypicSex.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [SeverityValue](SeverityValue.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [OrganismAttribute](OrganismAttribute.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [Inheritance](Inheritance.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [Zygosity](Zygosity.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [ClinicalModifier](ClinicalModifier.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [ClinicalCourse](ClinicalCourse.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [Onset](Onset.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_attribute_type](has_attribute_type.md) | range | ontology class |
| [Association](Association.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [ContributorAssociation](ContributorAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GeneExpressionMixin](GeneExpressionMixin.md) | [quantifier_qualifier](quantifier_qualifier.md) | range | ontology class |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [quantifier_qualifier](quantifier_qualifier.md) | range | ontology class |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [interacting_molecules_category](interacting_molecules_category.md) | range | ontology class |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [quantifier_qualifier](quantifier_qualifier.md) | range | ontology class |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [quantifier_qualifier](quantifier_qualifier.md) | range | ontology class |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [FunctionalAssociation](FunctionalAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [SequenceAssociation](SequenceAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [qualifiers](qualifiers.md) | range | ontology class |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [qualifiers](qualifiers.md) | range | ontology class |



## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* MESH

* UMLS

* KEGG.BRITE










## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ontology class
id_prefixes:
- MESH
- UMLS
- KEGG.BRITE
exact_mappings:
- owl:Class
- schema:Class
description: a concept or class in an ontology, vocabulary or thesaurus. Note that
  nodes in a biolink compatible KG can be considered both instances of biolink classes,
  and OWL classes in their own right. In general you should not need to use this class
  directly. Instead, use the appropriate biolink class. For example, for the GO concept
  of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.
comments:
- This is modeled as a mixin. 'ontology class' should not be the primary type of a
  node in the KG. Instead you should use an informative bioloink category, such as
  AnatomicalEntity (for Uberon classes), ChemicalSubstance (for CHEBI or CHEMBL),
  etc
- Note that formally this is a metaclass. Instances of this class are instances in
  the graph, but can be the object of 'type' edges. For example, if we had a node
  in the graph representing a specific brain of a specific patient (e.g brain001),
  this could have a category of bl:Sample, and by typed more specifically with an
  ontology class UBERON:nnn, which has as category bl:AnatomicalEntity
examples:
- value: UBERON:0000955
  description: the class 'brain' from the Uberon anatomy ontology
from_schema: https://w3id.org/biolink/biolink-model
see_also:
- https://github.com/biolink/biolink-model/issues/486
mixin: true

```
</details>

### Induced

<details>
```yaml
name: ontology class
id_prefixes:
- MESH
- UMLS
- KEGG.BRITE
exact_mappings:
- owl:Class
- schema:Class
description: a concept or class in an ontology, vocabulary or thesaurus. Note that
  nodes in a biolink compatible KG can be considered both instances of biolink classes,
  and OWL classes in their own right. In general you should not need to use this class
  directly. Instead, use the appropriate biolink class. For example, for the GO concept
  of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.
comments:
- This is modeled as a mixin. 'ontology class' should not be the primary type of a
  node in the KG. Instead you should use an informative bioloink category, such as
  AnatomicalEntity (for Uberon classes), ChemicalSubstance (for CHEBI or CHEMBL),
  etc
- Note that formally this is a metaclass. Instances of this class are instances in
  the graph, but can be the object of 'type' edges. For example, if we had a node
  in the graph representing a specific brain of a specific patient (e.g brain001),
  this could have a category of bl:Sample, and by typed more specifically with an
  ontology class UBERON:nnn, which has as category bl:AnatomicalEntity
examples:
- value: UBERON:0000955
  description: the class 'brain' from the Uberon anatomy ontology
from_schema: https://w3id.org/biolink/biolink-model
see_also:
- https://github.com/biolink/biolink-model/issues/486
mixin: true

```
</details>