# Class: EvidenceType
_Class of evidence that supports an association_





URI: [biolink:EvidenceType](https://w3id.org/biolink/vocab/EvidenceType)




## Inheritance

* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * [InformationContentEntity](InformationContentEntity.md)
            * **EvidenceType**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [license](license.md) | [string](string.md) | 0..1 | None  | . |
| [rights](rights.md) | [string](string.md) | 0..1 | None  | . |
| [format](format.md) | [string](string.md) | 0..1 | None  | . |
| [creation_date](creation_date.md) | [date](date.md) | 0..1 | date on which an entity was created. This can be applied to nodes or edges  | . |
| [id](id.md) | [string](string.md) | 1..1 | A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI  | . |
| [iri](iri.md) | [iri_type](iri_type.md) | 0..1 | An IRI for an entity. This is determined by the id using expansion rules.  | . |
| [category](category.md) | [NamedThing](NamedThing.md) | 1..* | Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}  | . |
| [type](type.md) | [string](string.md) | 0..1 | None  | . |
| [name](name.md) | [label_type](label_type.md) | 0..1 | A human-readable name for an attribute or entity.  | . |
| [description](description.md) | [narrative_text](narrative_text.md) | 0..1 | a human-readable description of an entity  | . |
| [source](source.md) | [label_type](label_type.md) | 0..1 | a lightweight analog to the association class 'provided by' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.  | . |
| [provided_by](provided_by.md) | [Agent](Agent.md) | 0..* | connects an association to the agent (person, organization or group) that provided it  | . |
| [has_attribute](has_attribute.md) | [Attribute](Attribute.md) | 0..* | connects any entity to an attribute  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Association](Association.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [ContributorAssociation](ContributorAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [FunctionalAssociation](FunctionalAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [SequenceAssociation](SequenceAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [has_evidence](has_evidence.md) | range | evidence type |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [has_evidence](has_evidence.md) | range | evidence type |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: evidence type
aliases:
- evidence code
exact_mappings:
- ECO:0000000
description: Class of evidence that supports an association
from_schema: https://w3id.org/biolink/biolink-model
is_a: information content entity
values_from:
- eco

```
</details>

### Induced

<details>
```yaml
name: evidence type
aliases:
- evidence code
exact_mappings:
- ECO:0000000
description: Class of evidence that supports an association
from_schema: https://w3id.org/biolink/biolink-model
is_a: information content entity
values_from:
- eco
attributes:
  license:
    name: license
    exact_mappings:
    - dct:license
    narrow_mappings:
    - WIKIDATA_PROPERTY:P275
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: information content entity
    alias: license
    owner: evidence type
    range: string
  rights:
    name: rights
    exact_mappings:
    - dct:rights
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: information content entity
    alias: rights
    owner: evidence type
    range: string
  format:
    name: format
    exact_mappings:
    - dct:format
    - WIKIDATA_PROPERTY:P2701
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: information content entity
    alias: format
    owner: evidence type
    range: string
  creation date:
    name: creation date
    aliases:
    - publication date
    exact_mappings:
    - dct:createdOn
    - WIKIDATA_PROPERTY:P577
    description: date on which an entity was created. This can be applied to nodes
      or edges
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    alias: creation_date
    owner: evidence type
    range: date
  id:
    name: id
    exact_mappings:
    - alliancegenome:primaryId
    - gff3:ID
    - gpi:DB_Object_ID
    description: A unique identifier for an entity. Must be either a CURIE shorthand
      for a URI or a complete URI
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    identifier: true
    alias: id
    owner: evidence type
    range: string
    required: true
  iri:
    name: iri
    exact_mappings:
    - WIKIDATA_PROPERTY:P854
    description: An IRI for an entity. This is determined by the id using expansion
      rules.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    alias: iri
    owner: evidence type
    range: iri type
  category:
    name: category
    description: "Name of the high level ontology class in which this entity is categorized.\
      \ Corresponds to the label for the biolink entity type class.\n * In a neo4j\
      \ database this MAY correspond to the neo4j label tag.\n * In an RDF database\
      \ it should be a biolink model class URI.\nThis field is multi-valued. It should\
      \ include values for ancestors of the biolink class; for example, a protein\
      \ such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`,\
      \ `biolink:MolecularEntity`, ...\nIn an RDF database, nodes will typically have\
      \ an rdf:type triples. This can be to the most specific biolink class, or potentially\
      \ to a class more specific than something in biolink. For example, a sequence\
      \ feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site,\
      \ which is more specific than anything in biolink. Here we would have categories\
      \ {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}"
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: type
    domain: entity
    multivalued: true
    designates_type: true
    alias: category
    owner: evidence type
    is_class_field: true
    range: named thing
    required: true
  type:
    name: type
    exact_mappings:
    - alliancegenome:soTermId
    - gff3:type
    - gpi:DB_Object_Type
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdf:type
    alias: type
    owner: evidence type
    range: string
  name:
    name: name
    aliases:
    - label
    - display name
    - title
    exact_mappings:
    - gff3:Name
    - gpi:DB_Object_Name
    narrow_mappings:
    - dct:title
    - WIKIDATA_PROPERTY:P1476
    description: A human-readable name for an attribute or entity.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdfs:label
    alias: name
    owner: evidence type
    range: label type
  description:
    name: description
    aliases:
    - definition
    exact_mappings:
    - IAO:0000115
    - skos:definitions
    narrow_mappings:
    - gff3:Description
    description: a human-readable description of an entity
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: dct:description
    alias: description
    owner: evidence type
    range: narrative text
  source:
    name: source
    description: a lightweight analog to the association class 'provided by' slot,
      which is the string name, or the authoritative (i.e. database) namespace, designating
      the origin of the entity to which the slot belongs.
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    alias: source
    owner: evidence type
    range: label type
  provided by:
    name: provided by
    exact_mappings:
    - pav:providedBy
    description: connects an association to the agent (person, organization or group)
      that provided it
    deprecated: This slot is deprecated and replaced by a set of more precise slots
      for describing the source retrieval provenance of an Association.  These include
      'knowledge source' and its descendants 'primary knowledge source', 'original
      knowledge source', and 'aggregator knowledge source'.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    multivalued: true
    alias: provided_by
    owner: evidence type
    range: agent
  has attribute:
    name: has attribute
    exact_mappings:
    - SIO:000008
    close_mappings:
    - OBI:0001927
    narrow_mappings:
    - OBAN:association_has_subject_property
    - OBAN:association_has_object_property
    - CPT:has_possibly_included_panel_element
    - DRUGBANK:category
    - EFO:is_executed_in
    - HANCESTRO:0301
    - LOINC:has_action_guidance
    - LOINC:has_adjustment
    - LOINC:has_aggregation_view
    - LOINC:has_approach_guidance
    - LOINC:has_divisor
    - LOINC:has_exam
    - LOINC:has_method
    - LOINC:has_modality_subtype
    - LOINC:has_object_guidance
    - LOINC:has_scale
    - LOINC:has_suffix
    - LOINC:has_time_aspect
    - LOINC:has_time_modifier
    - LOINC:has_timing_of
    - NCIT:R88
    - NCIT:eo_disease_has_property_or_attribute
    - NCIT:has_data_element
    - NCIT:has_pharmaceutical_administration_method
    - NCIT:has_pharmaceutical_basic_dose_form
    - NCIT:has_pharmaceutical_intended_site
    - NCIT:has_pharmaceutical_release_characteristics
    - NCIT:has_pharmaceutical_state_of_matter
    - NCIT:has_pharmaceutical_transformation
    - NCIT:is_qualified_by
    - NCIT:qualifier_applies_to
    - NCIT:role_has_domain
    - NCIT:role_has_range
    - INO:0000154
    - HANCESTRO:0308
    - OMIM:has_inheritance_type
    - ORPHA:C016
    - ORPHA:C017
    - RO:0000053
    - RO:0000086
    - RO:0000087
    - SNOMED:has_access
    - SNOMED:has_clinical_course
    - SNOMED:has_count_of_base_of_active_ingredient
    - SNOMED:has_dose_form_administration_method
    - SNOMED:has_dose_form_release_characteristic
    - SNOMED:has_dose_form_transformation
    - SNOMED:has_finding_context
    - SNOMED:has_finding_informer
    - SNOMED:has_inherent_attribute
    - SNOMED:has_intent
    - SNOMED:has_interpretation
    - SNOMED:has_laterality
    - SNOMED:has_measurement_method
    - SNOMED:has_method
    - SNOMED:has_priority
    - SNOMED:has_procedure_context
    - SNOMED:has_process_duration
    - SNOMED:has_property
    - SNOMED:has_revision_status
    - SNOMED:has_scale_type
    - SNOMED:has_severity
    - SNOMED:has_specimen
    - SNOMED:has_state_of_matter
    - SNOMED:has_subject_relationship_context
    - SNOMED:has_surgical_approach
    - SNOMED:has_technique
    - SNOMED:has_temporal_context
    - SNOMED:has_time_aspect
    - SNOMED:has_units
    - UMLS:has_structural_class
    - UMLS:has_supported_concept_property
    - UMLS:has_supported_concept_relationship
    - UMLS:may_be_qualified_by
    description: connects any entity to an attribute
    in_subset:
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    domain: entity
    multivalued: true
    alias: has_attribute
    owner: evidence type
    range: attribute

```
</details>