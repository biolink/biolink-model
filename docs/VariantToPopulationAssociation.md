# Class: VariantToPopulationAssociation
_An association between a variant and a population, where the variant has particular frequency in the population_





URI: [biolink:VariantToPopulationAssociation](https://w3id.org/biolink/vocab/VariantToPopulationAssociation)




## Inheritance

* [Entity](Entity.md)
    * [Association](Association.md)
        * **VariantToPopulationAssociation** [ variant to entity association mixin frequency quantifier frequency qualifier mixin]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [has_count](has_count.md) | [integer](integer.md) | 0..1 | number in object population that carry a particular allele, aka allele count  | . |
| [has_total](has_total.md) | [integer](integer.md) | 0..1 | number all populations that carry a particular allele, aka allele number  | . |
| [has_quotient](has_quotient.md) | [double](double.md) | 0..1 | frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency  | . |
| [has_percentage](has_percentage.md) | [double](double.md) | 0..1 | equivalent to has quotient multiplied by 100  | . |
| [frequency_qualifier](frequency_qualifier.md) | [frequency_value](frequency_value.md) | 0..1 | a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject  | . |
| [subject](subject.md) | [SequenceVariant](SequenceVariant.md) | 1..1 | an allele that has a certain frequency in a given population  | . |
| [predicate](predicate.md) | [predicate_type](predicate_type.md) | 1..1 | A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.  | . |
| [object](object.md) | [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | 1..1 | the population that is observed to have the frequency  | . |
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
name: variant to population association
description: An association between a variant and a population, where the variant
  has particular frequency in the population
from_schema: https://w3id.org/biolink/biolink-model
is_a: association
mixins:
- variant to entity association mixin
- frequency quantifier
- frequency qualifier mixin
slot_usage:
  subject:
    name: subject
    description: an allele that has a certain frequency in a given population
    examples:
    - value: NC_000017.11:g.43051071A>T
      description: 17:41203088 A/C in gnomad
    range: sequence variant
  object:
    name: object
    description: the population that is observed to have the frequency
    examples:
    - value: HANCESTRO:0010
      description: African
    range: population of individual organisms
  has quotient:
    name: has quotient
    description: frequency of allele in population, expressed as a number with allele
      divided by number in reference population, aka allele frequency
    examples:
    - value: '0.0001666'
  has count:
    name: has count
    description: number in object population that carry a particular allele, aka allele
      count
    examples:
    - value: '4'
      description: 4 individuals in gnomad set
  has total:
    name: has total
    description: number all populations that carry a particular allele, aka allele
      number
    examples:
    - value: '24014'
      description: 24014 individuals in gnomad set
defining_slots:
- subject
- object

```
</details>

### Induced

<details>
```yaml
name: variant to population association
description: An association between a variant and a population, where the variant
  has particular frequency in the population
from_schema: https://w3id.org/biolink/biolink-model
is_a: association
mixins:
- variant to entity association mixin
- frequency quantifier
- frequency qualifier mixin
slot_usage:
  subject:
    name: subject
    description: an allele that has a certain frequency in a given population
    examples:
    - value: NC_000017.11:g.43051071A>T
      description: 17:41203088 A/C in gnomad
    range: sequence variant
  object:
    name: object
    description: the population that is observed to have the frequency
    examples:
    - value: HANCESTRO:0010
      description: African
    range: population of individual organisms
  has quotient:
    name: has quotient
    description: frequency of allele in population, expressed as a number with allele
      divided by number in reference population, aka allele frequency
    examples:
    - value: '0.0001666'
  has count:
    name: has count
    description: number in object population that carry a particular allele, aka allele
      count
    examples:
    - value: '4'
      description: 4 individuals in gnomad set
  has total:
    name: has total
    description: number all populations that carry a particular allele, aka allele
      number
    examples:
    - value: '24014'
      description: 24014 individuals in gnomad set
attributes:
  has count:
    name: has count
    description: number in object population that carry a particular allele, aka allele
      count
    examples:
    - value: '4'
      description: 4 individuals in gnomad set
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: aggregate statistic
    domain: named thing
    alias: has_count
    owner: variant to population association
    range: integer
  has total:
    name: has total
    description: number all populations that carry a particular allele, aka allele
      number
    examples:
    - value: '24014'
      description: 24014 individuals in gnomad set
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: aggregate statistic
    domain: named thing
    alias: has_total
    owner: variant to population association
    range: integer
  has quotient:
    name: has quotient
    description: frequency of allele in population, expressed as a number with allele
      divided by number in reference population, aka allele frequency
    examples:
    - value: '0.0001666'
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: aggregate statistic
    domain: named thing
    alias: has_quotient
    owner: variant to population association
    range: double
  has percentage:
    name: has percentage
    description: equivalent to has quotient multiplied by 100
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: aggregate statistic
    domain: named thing
    alias: has_percentage
    owner: variant to population association
    range: double
  frequency qualifier:
    name: frequency qualifier
    description: a qualifier used in a phenotypic association to state how frequent
      the phenotype is observed in the subject
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: frequency_qualifier
    owner: variant to population association
    range: frequency value
  subject:
    name: subject
    description: an allele that has a certain frequency in a given population
    examples:
    - value: NC_000017.11:g.43051071A>T
      description: 17:41203088 A/C in gnomad
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    slot_uri: rdf:subject
    alias: subject
    owner: variant to population association
    range: sequence variant
    required: true
  predicate:
    name: predicate
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: annotation predicate
      translator:
        local_name_source: translator
        local_name_value: predicate
    exact_mappings:
    - owl:annotatedProperty
    - OBAN:association_has_predicate
    description: A high-level grouping for the relationship type. AKA minimal predicate.
      This is analogous to category for nodes.
    notes:
    - Has a value from the Biolink related_to hierarchy. In RDF,  this corresponds
      to rdf:predicate and in Neo4j this corresponds to the relationship type. The
      convention is for an edge label in snake_case form. For example, biolink:related_to,
      biolink:causes, biolink:treats
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    slot_uri: rdf:predicate
    alias: predicate
    owner: variant to population association
    range: predicate type
    required: true
  object:
    name: object
    description: the population that is observed to have the frequency
    examples:
    - value: HANCESTRO:0010
      description: African
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    slot_uri: rdf:object
    alias: object
    owner: variant to population association
    range: population of individual organisms
    required: true
  relation:
    name: relation
    deprecated: 'True'
    from_schema: https://w3id.org/biolink/biolink-model
    alias: relation
    owner: variant to population association
    range: string
  negated:
    name: negated
    description: if set to true, then the association is negated i.e. is not true
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: negated
    owner: variant to population association
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
    owner: variant to population association
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
    owner: variant to population association
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
    owner: variant to population association
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
    owner: variant to population association
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
    owner: variant to population association
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
    owner: variant to population association
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
    owner: variant to population association
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
    owner: variant to population association
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
    owner: variant to population association
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
    owner: variant to population association
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
    owner: variant to population association
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
    owner: variant to population association
    range: attribute
defining_slots:
- subject
- object

```
</details>