# Class: ChemicalEntity
_A chemical entity is a physical entity that pertains to chemistry or biochemistry._





URI: [biolink:ChemicalEntity](https://w3id.org/biolink/vocab/ChemicalEntity)




## Inheritance

* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * **ChemicalEntity** [ physical essence chemical or drug or treatment chemical entity or gene or gene product chemical entity or protein or polypeptide]
            * [MolecularEntity](MolecularEntity.md)
            * [ChemicalMixture](ChemicalMixture.md)
            * [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md)
            * [FoodAdditive](FoodAdditive.md)
            * [Nutrient](Nutrient.md)




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [trade_name](trade_name.md) | [ChemicalEntity](ChemicalEntity.md) | 0..1 |   | . |
| [available_from](available_from.md) | [DrugAvailabilityEnum](DrugAvailabilityEnum.md) | 0..* |   | . |
| [max_tolerated_dose](max_tolerated_dose.md) | [string](string.md) | 0..1 | The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.  | . |
| [is_toxic](is_toxic.md) | [boolean](boolean.md) | 0..1 |   | . |
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
| [MolecularEntity](MolecularEntity.md) | [trade_name](trade_name.md) | range | chemical entity |
| [ChemicalEntity](ChemicalEntity.md) | [trade_name](trade_name.md) | range | chemical entity |
| [SmallMolecule](SmallMolecule.md) | [trade_name](trade_name.md) | range | chemical entity |
| [ChemicalMixture](ChemicalMixture.md) | [trade_name](trade_name.md) | range | chemical entity |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [trade_name](trade_name.md) | range | chemical entity |
| [MolecularMixture](MolecularMixture.md) | [trade_name](trade_name.md) | range | chemical entity |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [trade_name](trade_name.md) | range | chemical entity |
| [ProcessedMaterial](ProcessedMaterial.md) | [trade_name](trade_name.md) | range | chemical entity |
| [Drug](Drug.md) | [trade_name](trade_name.md) | range | chemical entity |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [trade_name](trade_name.md) | range | chemical entity |
| [FoodAdditive](FoodAdditive.md) | [trade_name](trade_name.md) | range | chemical entity |
| [Nutrient](Nutrient.md) | [trade_name](trade_name.md) | range | chemical entity |
| [Macronutrient](Macronutrient.md) | [trade_name](trade_name.md) | range | chemical entity |
| [Micronutrient](Micronutrient.md) | [trade_name](trade_name.md) | range | chemical entity |
| [Vitamin](Vitamin.md) | [trade_name](trade_name.md) | range | chemical entity |
| [Food](Food.md) | [trade_name](trade_name.md) | range | chemical entity |
| [Exon](Exon.md) | [trade_name](trade_name.md) | range | chemical entity |
| [Transcript](Transcript.md) | [trade_name](trade_name.md) | range | chemical entity |
| [CodingSequence](CodingSequence.md) | [trade_name](trade_name.md) | range | chemical entity |
| [RNAProduct](RNAProduct.md) | [trade_name](trade_name.md) | range | chemical entity |
| [RNAProductIsoform](RNAProductIsoform.md) | [trade_name](trade_name.md) | range | chemical entity |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [trade_name](trade_name.md) | range | chemical entity |
| [MicroRNA](MicroRNA.md) | [trade_name](trade_name.md) | range | chemical entity |
| [SiRNA](SiRNA.md) | [trade_name](trade_name.md) | range | chemical entity |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [object](object.md) | range | chemical entity |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object](object.md) | range | chemical entity |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [subject](subject.md) | range | chemical entity |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [object](object.md) | range | chemical entity |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object](object.md) | range | chemical entity |



## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* UNII

* MESH

* CAS

* UMLS










## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: chemical entity
id_prefixes:
- UNII
- MESH
- CAS
- UMLS
exact_mappings:
- CHEBI:24431
- SIO:010004
- WIKIDATA:Q79529
- STY:T103
narrow_mappings:
- WIKIDATA:Q43460564
description: A chemical entity is a physical entity that pertains to chemistry or
  biochemistry.
in_subset:
- translator_minimal
from_schema: https://w3id.org/biolink/biolink-model
is_a: named thing
mixins:
- physical essence
- chemical or drug or treatment
- chemical entity or gene or gene product
- chemical entity or protein or polypeptide
slots:
- trade name
- available from
- max tolerated dose
- is toxic

```
</details>

### Induced

<details>
```yaml
name: chemical entity
id_prefixes:
- UNII
- MESH
- CAS
- UMLS
exact_mappings:
- CHEBI:24431
- SIO:010004
- WIKIDATA:Q79529
- STY:T103
narrow_mappings:
- WIKIDATA:Q43460564
description: A chemical entity is a physical entity that pertains to chemistry or
  biochemistry.
in_subset:
- translator_minimal
from_schema: https://w3id.org/biolink/biolink-model
is_a: named thing
mixins:
- physical essence
- chemical or drug or treatment
- chemical entity or gene or gene product
- chemical entity or protein or polypeptide
attributes:
  trade name:
    name: trade name
    description: ''
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    alias: trade_name
    owner: chemical entity
    range: chemical entity
  available from:
    name: available from
    description: ''
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    multivalued: true
    alias: available_from
    owner: chemical entity
    range: drug_availability_enum
  max tolerated dose:
    name: max tolerated dose
    description: The highest dose of a drug or treatment that does not cause unacceptable
      side effects. The maximum tolerated dose is determined in clinical trials by
      testing increasing doses on different groups of people until the highest dose
      with acceptable side effects is found. Also called MTD.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    multivalued: false
    alias: max_tolerated_dose
    owner: chemical entity
    range: string
  is toxic:
    name: is toxic
    description: ''
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    multivalued: false
    alias: is_toxic
    owner: chemical entity
    range: boolean
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
    owner: chemical entity
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
    owner: chemical entity
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
    owner: chemical entity
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
    owner: chemical entity
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
    owner: chemical entity
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
    owner: chemical entity
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
    owner: chemical entity
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
    owner: chemical entity
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
    owner: chemical entity
    range: attribute

```
</details>