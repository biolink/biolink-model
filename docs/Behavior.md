# Class: Behavior




URI: [biolink:Behavior](https://w3id.org/biolink/vocab/Behavior)




## Inheritance

* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * [BiologicalEntity](BiologicalEntity.md)
            * [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) [ occurrent ontology class]
                * [BiologicalProcess](BiologicalProcess.md) [ occurrent ontology class]
                    * **Behavior** [ ontology class activity and behavior]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [has_input](has_input.md) | [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | 0..* | holds between a process and a continuant, where the continuant is an input into the process  | . |
| [has_output](has_output.md) | [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | 0..* | holds between a process and a continuant, where the continuant is an output of the process  | . |
| [enabled_by](enabled_by.md) | [PhysicalEntity](PhysicalEntity.md) | 0..* | holds between a process and a physical entity, where the physical entity executes the process  | . |
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
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject](subject.md) | range | behavior |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: behavior
exact_mappings:
- GO:0007610
- STY:T053
narrow_mappings:
- STY:T041
- STY:T054
- STY:T055
from_schema: https://w3id.org/biolink/biolink-model
is_a: biological process
mixins:
- ontology class
- activity and behavior

```
</details>

### Induced

<details>
```yaml
name: behavior
exact_mappings:
- GO:0007610
- STY:T053
narrow_mappings:
- STY:T041
- STY:T054
- STY:T055
from_schema: https://w3id.org/biolink/biolink-model
is_a: biological process
mixins:
- ontology class
- activity and behavior
attributes:
  has input:
    name: has input
    exact_mappings:
    - RO:0002233
    - SEMMEDDB:USES
    - SEMMEDDB:uses
    close_mappings:
    - RO:0002352
    narrow_mappings:
    - LOINC:has_fragments_for_synonyms
    - LOINC:has_system
    - PathWhiz:has_left_element
    - RO:0002590
    - RO:0004009
    - SNOMED:has_finding_method
    - SNOMED:has_precondition
    - SNOMED:has_specimen_source_identity
    - SNOMED:has_specimen_substance
    - SNOMED:uses_access_device
    - SNOMED:uses_device
    - SNOMED:uses_energy
    - SNOMED:uses_substance
    annotations:
      biolink:canonical_predicate:
        tag: biolink:canonical_predicate
        value: 'True'
      biolink:opposite_of:
        tag: biolink:opposite_of
        value: biolink:has output
    description: holds between a process and a continuant, where the continuant is
      an input into the process
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: has participant
    domain: occurrent
    multivalued: true
    inherited: true
    alias: has_input
    owner: behavior
    range: biological process or activity
  has output:
    name: has output
    exact_mappings:
    - RO:0002234
    close_mappings:
    - RO:0002353
    - RO:0002354
    narrow_mappings:
    - NCIT:R31
    - OBI:0000299
    - PathWhiz:has_right_element
    - RO:0002296
    - RO:0002297
    - RO:0002298
    - RO:0002299
    - RO:0002588
    - RO:0004008
    annotations:
      biolink:canonical_predicate:
        tag: biolink:canonical_predicate
        value: 'True'
      biolink:opposite_of:
        tag: biolink:opposite_of
        value: biolink:has input
    description: holds between a process and a continuant, where the continuant is
      an output of the process
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: has participant
    domain: occurrent
    multivalued: true
    inherited: true
    alias: has_output
    owner: behavior
    range: biological process or activity
  enabled by:
    name: enabled by
    exact_mappings:
    - RO:0002333
    annotations:
      biolink:opposite_of:
        tag: biolink:opposite_of
        value: biolink:prevented by
    description: holds between a process and a physical entity, where the physical
      entity executes the process
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: has participant
    domain: biological process or activity
    multivalued: true
    inherited: true
    alias: enabled_by
    owner: behavior
    inverse: enables
    range: physical entity
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
    owner: behavior
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
    owner: behavior
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
    owner: behavior
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
    owner: behavior
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
    owner: behavior
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
    owner: behavior
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
    owner: behavior
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
    owner: behavior
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
    owner: behavior
    range: attribute

```
</details>