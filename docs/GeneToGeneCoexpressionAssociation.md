# Class: GeneToGeneCoexpressionAssociation
_Indicates that two genes are co-expressed, generally under the same conditions._





URI: [biolink:GeneToGeneCoexpressionAssociation](https://w3id.org/biolink/vocab/GeneToGeneCoexpressionAssociation)




## Inheritance

* [Entity](Entity.md)
    * [Association](Association.md)
        * [GeneToGeneAssociation](GeneToGeneAssociation.md)
            * **GeneToGeneCoexpressionAssociation** [ gene expression mixin]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [quantifier_qualifier](quantifier_qualifier.md) | [OntologyClass](OntologyClass.md) | 0..1 | A measurable quantity for the object of the association  | . |
| [expression_site](expression_site.md) | [AnatomicalEntity](AnatomicalEntity.md) | 0..1 | location in which gene or protein expression takes place. May be cell, tissue, or organ.  | . |
| [stage_qualifier](stage_qualifier.md) | [LifeStage](LifeStage.md) | 0..1 | stage during which gene or protein expression of takes place.  | . |
| [phenotypic_state](phenotypic_state.md) | [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | 0..1 | in experiments (e.g. gene expression) assaying diseased or unhealthy tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues, use XXX.  | . |
| [subject](subject.md) | [GeneOrGeneProduct](GeneOrGeneProduct.md) | 1..1 | connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.  | . |
| [predicate](predicate.md) | [predicate_type](predicate_type.md) | 1..1 | A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.  | . |
| [object](object.md) | [GeneOrGeneProduct](GeneOrGeneProduct.md) | 1..1 | connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.  | . |
| [relation](relation.md) | [string](string.md) | 0..1 | None  | . |
| [negated](negated.md) | [boolean](boolean.md) | 0..1 | if set to true, then the association is negated i.e. is not true  | . |
| [qualifiers](qualifiers.md) | [OntologyClass](OntologyClass.md) | 0..* | connects an association to qualifiers that modify or qualify the meaning of that association  | . |
| [publications](publications.md) | [Publication](Publication.md) | 0..* | connects an association to publications supporting the association  | . |
| [has_evidence](has_evidence.md) | [EvidenceType](EvidenceType.md) | 0..* | connects an association to an instance of supporting evidence  | . |
| [id](id.md) | [string](string.md) | 1..1 | A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI  | . |
| [iri](iri.md) | [iri_type](iri_type.md) | 0..1 | An IRI for an entity. This is determined by the id using expansion rules.  | . |
| [category](category.md) | [category_type](category_type.md) | 0..* | Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
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



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: gene to gene coexpression association
description: Indicates that two genes are co-expressed, generally under the same conditions.
from_schema: https://w3id.org/biolink/biolink-model
is_a: gene to gene association
mixins:
- gene expression mixin
slot_usage:
  predicate:
    name: predicate
    subproperty_of: coexpressed with
    symmetric: true
defining_slots:
- subject
- predicate
- object

```
</details>

### Induced

<details>
```yaml
name: gene to gene coexpression association
description: Indicates that two genes are co-expressed, generally under the same conditions.
from_schema: https://w3id.org/biolink/biolink-model
is_a: gene to gene association
mixins:
- gene expression mixin
slot_usage:
  predicate:
    name: predicate
    subproperty_of: coexpressed with
    symmetric: true
attributes:
  quantifier qualifier:
    name: quantifier qualifier
    narrow_mappings:
    - LOINC:analyzes
    - LOINC:measured_by
    - LOINC:property_of
    - SEMMEDDB:measures
    - UMLS:measures
    description: A measurable quantity for the object of the association
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: quantifier_qualifier
    owner: gene to gene coexpression association
    range: ontology class
  expression site:
    name: expression site
    description: location in which gene or protein expression takes place. May be
      cell, tissue, or organ.
    examples:
    - value: UBERON:0002037
      description: cerebellum
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: expression_site
    owner: gene to gene coexpression association
    range: anatomical entity
  stage qualifier:
    name: stage qualifier
    description: stage during which gene or protein expression of takes place.
    examples:
    - value: UBERON:0000069
      description: larval stage
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: stage_qualifier
    owner: gene to gene coexpression association
    range: life stage
  phenotypic state:
    name: phenotypic state
    description: in experiments (e.g. gene expression) assaying diseased or unhealthy
      tissue, the phenotypic state can be put here, e.g. MONDO ID. For healthy tissues,
      use XXX.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: phenotypic_state
    owner: gene to gene coexpression association
    range: disease or phenotypic feature
  subject:
    name: subject
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: annotation subject
      neo4j:
        local_name_source: neo4j
        local_name_value: node with outgoing relationship
    exact_mappings:
    - owl:annotatedSource
    - OBAN:association_has_subject
    description: connects an association to the subject of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    slot_uri: rdf:subject
    alias: subject
    owner: gene to gene coexpression association
    range: gene or gene product
    required: true
  predicate:
    name: predicate
    description: A high-level grouping for the relationship type. AKA minimal predicate.
      This is analogous to category for nodes.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    slot_uri: rdf:predicate
    alias: predicate
    owner: gene to gene coexpression association
    subproperty_of: coexpressed with
    symmetric: true
    range: predicate type
    required: true
  object:
    name: object
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: descriptor
      neo4j:
        local_name_source: neo4j
        local_name_value: node with incoming relationship
    exact_mappings:
    - owl:annotatedTarget
    - OBAN:association_has_object
    description: connects an association to the object of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    slot_uri: rdf:object
    alias: object
    owner: gene to gene coexpression association
    range: gene or gene product
    required: true
  relation:
    name: relation
    deprecated: 'True'
    from_schema: https://w3id.org/biolink/biolink-model
    alias: relation
    owner: gene to gene coexpression association
    range: string
  negated:
    name: negated
    description: if set to true, then the association is negated i.e. is not true
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: negated
    owner: gene to gene coexpression association
    range: boolean
  qualifiers:
    name: qualifiers
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: annotation qualifier
    description: connects an association to qualifiers that modify or qualify the
      meaning of that association
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    singular_name: qualifier
    domain: association
    multivalued: true
    alias: qualifiers
    owner: gene to gene coexpression association
    range: ontology class
  publications:
    name: publications
    description: connects an association to publications supporting the association
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    singular_name: publication
    domain: association
    multivalued: true
    alias: publications
    owner: gene to gene coexpression association
    range: publication
  has evidence:
    name: has evidence
    exact_mappings:
    - RO:0002558
    description: connects an association to an instance of supporting evidence
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    multivalued: true
    alias: has_evidence
    owner: gene to gene coexpression association
    range: evidence type
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
    owner: gene to gene coexpression association
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
    owner: gene to gene coexpression association
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
    owner: gene to gene coexpression association
    is_class_field: true
    range: category type
    required: false
  type:
    name: type
    exact_mappings:
    - alliancegenome:soTermId
    - gff3:type
    - gpi:DB_Object_Type
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdf:type
    alias: type
    owner: gene to gene coexpression association
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
    owner: gene to gene coexpression association
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
    owner: gene to gene coexpression association
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
    owner: gene to gene coexpression association
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
    owner: gene to gene coexpression association
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
    owner: gene to gene coexpression association
    range: attribute
defining_slots:
- subject
- predicate
- object

```
</details>