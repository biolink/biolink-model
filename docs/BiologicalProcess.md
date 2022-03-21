# Class: BiologicalProcess
_One or more causally connected executions of molecular functions_





URI: [biolink:BiologicalProcess](https://w3id.org/biolink/vocab/BiologicalProcess)




## Inheritance

* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * [BiologicalEntity](BiologicalEntity.md)
            * [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) [ occurrent ontology class]
                * **BiologicalProcess** [ occurrent ontology class]
                    * [Pathway](Pathway.md) [ ontology class]
                    * [PhysiologicalProcess](PhysiologicalProcess.md) [ ontology class]
                    * [Behavior](Behavior.md) [ ontology class activity and behavior]
                    * [PathologicalProcess](PathologicalProcess.md) [ pathological entity mixin]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [has_input](has_input.md) | [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | 0..* | holds between a process and a continuant, where the continuant is an input into the process  | . |
| [has_output](has_output.md) | [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | 0..* | holds between a process and a continuant, where the continuant is an output of the process  | . |
| [enabled_by](enabled_by.md) | [PhysicalEntity](PhysicalEntity.md) | 0..* | holds between a process and a physical entity, where the physical entity executes the process  | . |
| [provided_by](provided_by.md) | [string](string.md) | 0..* | The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.  | . |
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
| [source](source.md) | [string](string.md) | 0..1 | None  | . |
| [has_attribute](has_attribute.md) | [Attribute](Attribute.md) | 0..* | connects any entity to an attribute  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object](object.md) | range | biological process |



## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* GO

* REACT

* metacyc.reaction

* KEGG.MODULE










## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: biological process
id_prefixes:
- GO
- REACT
- metacyc.reaction
- KEGG.MODULE
exact_mappings:
- GO:0008150
- SIO:000006
- WIKIDATA:Q2996394
broad_mappings:
- WIKIDATA:P682
description: One or more causally connected executions of molecular functions
from_schema: https://w3id.org/biolink/biolink-model
is_a: biological process or activity
mixins:
- occurrent
- ontology class

```
</details>

### Induced

<details>
```yaml
name: biological process
id_prefixes:
- GO
- REACT
- metacyc.reaction
- KEGG.MODULE
exact_mappings:
- GO:0008150
- SIO:000006
- WIKIDATA:Q2996394
broad_mappings:
- WIKIDATA:P682
description: One or more causally connected executions of molecular functions
from_schema: https://w3id.org/biolink/biolink-model
is_a: biological process or activity
mixins:
- occurrent
- ontology class
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
    owner: biological process
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
    owner: biological process
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
    owner: biological process
    inverse: enables
    range: physical entity
  provided by:
    name: provided by
    description: The value in this node property represents the knowledge provider
      that created or assembled the node and all of its attributes.  Used internally
      to represent how a particular node made its way into a knowledge provider or
      graph.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    multivalued: true
    alias: provided_by
    owner: biological process
    range: string
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
    owner: biological process
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
    owner: biological process
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
    owner: biological process
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
    owner: biological process
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
    owner: biological process
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
    owner: biological process
    range: narrative text
  source:
    name: source
    deprecated: 'True'
    from_schema: https://w3id.org/biolink/biolink-model
    alias: source
    owner: biological process
    range: string
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
    owner: biological process
    range: attribute

```
</details>