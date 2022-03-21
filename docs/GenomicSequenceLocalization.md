# Class: GenomicSequenceLocalization
_A relationship between a sequence feature and a nucleic acid entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig._





URI: [biolink:GenomicSequenceLocalization](https://w3id.org/biolink/vocab/GenomicSequenceLocalization)




## Inheritance

* [Entity](Entity.md)
    * [Association](Association.md)
        * [SequenceAssociation](SequenceAssociation.md)
            * **GenomicSequenceLocalization**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [start_interbase_coordinate](start_interbase_coordinate.md) | [integer](integer.md) | 0..1 | The position at which the subject nucleic acid entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 0).  | . |
| [end_interbase_coordinate](end_interbase_coordinate.md) | [integer](integer.md) | 0..1 | The position at which the subject nucleic acid entity ends on the chromosome or other entity to which it is located on.  | . |
| [genome_build](genome_build.md) | [StrandEnum](StrandEnum.md) | 0..1 | The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens.  | . |
| [strand](strand.md) | [StrandEnum](StrandEnum.md) | 0..1 | The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand).  | . |
| [phase](phase.md) | [PhaseEnum](PhaseEnum.md) | 0..1 | The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2.  | . |
| [subject](subject.md) | [NucleicAcidEntity](NucleicAcidEntity.md) | 1..1 | connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.  | . |
| [predicate](predicate.md) | [predicate_type](predicate_type.md) | 1..1 | A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.  | . |
| [object](object.md) | [NucleicAcidEntity](NucleicAcidEntity.md) | 1..1 | connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.  | . |
| [relation](relation.md) | [string](string.md) | 0..1 | None  | . |
| [negated](negated.md) | [boolean](boolean.md) | 0..1 | if set to true, then the association is negated i.e. is not true  | . |
| [qualifiers](qualifiers.md) | [OntologyClass](OntologyClass.md) | 0..* | connects an association to qualifiers that modify or qualify the meaning of that association  | . |
| [publications](publications.md) | [Publication](Publication.md) | 0..* | connects an association to publications supporting the association  | . |
| [has_evidence](has_evidence.md) | [EvidenceType](EvidenceType.md) | 0..* | connects an association to an instance of supporting evidence  | . |
| [knowledge_source](knowledge_source.md) | [InformationResource](InformationResource.md) | 0..* | An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.  | . |
| [original_knowledge_source](original_knowledge_source.md) | [InformationResource](InformationResource.md) | 0..* | The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).  | . |
| [primary_knowledge_source](primary_knowledge_source.md) | [InformationResource](InformationResource.md) | 0..* | The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).  | . |
| [aggregator_knowledge_source](aggregator_knowledge_source.md) | [InformationResource](InformationResource.md) | 0..* | An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.  | . |
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
| [source](source.md) | [string](string.md) | 0..1 | None  | . |
| [has_attribute](has_attribute.md) | [Attribute](Attribute.md) | 0..* | connects any entity to an attribute  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [start_interbase_coordinate](start_interbase_coordinate.md) | domain | genomic sequence localization |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [end_interbase_coordinate](end_interbase_coordinate.md) | domain | genomic sequence localization |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [genome_build](genome_build.md) | domain | genomic sequence localization |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [strand](strand.md) | domain | genomic sequence localization |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: genomic sequence localization
exact_mappings:
- dcid:GenomeAnnotation
broad_mappings:
- dcid:Chromosome
description: A relationship between a sequence feature and a nucleic acid entity it
  is localized to. The reference entity may be a chromosome, chromosome region or
  information entity such as a contig.
from_schema: https://w3id.org/biolink/biolink-model
is_a: sequence association
slots:
- start interbase coordinate
- end interbase coordinate
- genome build
- strand
- phase
slot_usage:
  subject:
    name: subject
    aliases:
    - sequence feature
    range: nucleic acid entity
  object:
    name: object
    aliases:
    - reference
    range: nucleic acid entity
  predicate:
    name: predicate
    subproperty_of: has sequence location

```
</details>

### Induced

<details>
```yaml
name: genomic sequence localization
exact_mappings:
- dcid:GenomeAnnotation
broad_mappings:
- dcid:Chromosome
description: A relationship between a sequence feature and a nucleic acid entity it
  is localized to. The reference entity may be a chromosome, chromosome region or
  information entity such as a contig.
from_schema: https://w3id.org/biolink/biolink-model
is_a: sequence association
slot_usage:
  subject:
    name: subject
    aliases:
    - sequence feature
    range: nucleic acid entity
  object:
    name: object
    aliases:
    - reference
    range: nucleic acid entity
  predicate:
    name: predicate
    subproperty_of: has sequence location
attributes:
  start interbase coordinate:
    name: start interbase coordinate
    close_mappings:
    - faldo:begin
    annotations:
      biolink:opposite_of:
        tag: biolink:opposite_of
        value: biolink:end interbase coordinate
    description: 'The position at which the subject nucleic acid entity starts on
      the chromosome or other entity to which it is located on. (ie: the start of
      the sequence being referenced is 0).'
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: interbase coordinate
    domain: genomic sequence localization
    alias: start_interbase_coordinate
    owner: genomic sequence localization
    range: integer
  end interbase coordinate:
    name: end interbase coordinate
    close_mappings:
    - faldo:end
    annotations:
      biolink:opposite_of:
        tag: biolink:opposite_of
        value: biolink:start interbase coordinate
    description: The position at which the subject nucleic acid entity ends on the
      chromosome or other entity to which it is located on.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: interbase coordinate
    domain: genomic sequence localization
    alias: end_interbase_coordinate
    owner: genomic sequence localization
    range: integer
  genome build:
    name: genome build
    exact_mappings:
    - gff3:strand
    description: The version of the genome on which a feature is located. For example,
      GRCh38 for Homo sapiens.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: sequence localization attribute
    domain: genomic sequence localization
    alias: genome_build
    owner: genomic sequence localization
    range: strand_enum
  strand:
    name: strand
    exact_mappings:
    - gff3:strand
    description: The strand on which a feature is located. Has a value of '+' (sense
      strand or forward strand) or '-' (anti-sense strand or reverse strand).
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: sequence localization attribute
    domain: genomic sequence localization
    alias: strand
    owner: genomic sequence localization
    range: strand_enum
  phase:
    name: phase
    exact_mappings:
    - gff3:phase
    description: The phase for a coding sequence entity. For example, phase of a CDS
      as represented in a GFF3 with a value of 0, 1 or 2.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: sequence localization attribute
    domain: coding sequence
    alias: phase
    owner: genomic sequence localization
    range: phase_enum
  subject:
    name: subject
    aliases:
    - sequence feature
    description: connects an association to the subject of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    slot_uri: rdf:subject
    alias: subject
    owner: genomic sequence localization
    range: nucleic acid entity
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
    owner: genomic sequence localization
    subproperty_of: has sequence location
    range: predicate type
    required: true
  object:
    name: object
    aliases:
    - reference
    description: connects an association to the object of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    slot_uri: rdf:object
    alias: object
    owner: genomic sequence localization
    range: nucleic acid entity
    required: true
  relation:
    name: relation
    deprecated: 'True'
    from_schema: https://w3id.org/biolink/biolink-model
    alias: relation
    owner: genomic sequence localization
    range: string
  negated:
    name: negated
    description: if set to true, then the association is negated i.e. is not true
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: negated
    owner: genomic sequence localization
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
    owner: genomic sequence localization
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
    owner: genomic sequence localization
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
    owner: genomic sequence localization
    range: evidence type
  knowledge source:
    name: knowledge source
    close_mappings:
    - pav:providedBy
    description: An Information Resource from which the knowledge expressed in an
      Association was retrieved, directly or indirectly. This can be any resource
      through which the knowledge passed on its way to its currently serialized form.
      In practice, implementers should use one of the more specific subtypes of this
      generic property.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    multivalued: true
    alias: knowledge_source
    owner: genomic sequence localization
    range: information resource
  original knowledge source:
    name: original knowledge source
    description: The Information Resource that created the original record of the
      knowledge expressed in an Association (e.g. via curation of the knowledge from
      the literature, or generation of the knowledge de novo through computation,
      reasoning, inference over data).
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: primary knowledge source
    domain: association
    multivalued: true
    alias: original_knowledge_source
    owner: genomic sequence localization
    range: information resource
  primary knowledge source:
    name: primary knowledge source
    description: The most upstream source of the knowledge expressed in an Association
      that an implementer can identify (may or may not be the 'original' source).
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: knowledge source
    domain: association
    multivalued: true
    alias: primary_knowledge_source
    owner: genomic sequence localization
    range: information resource
  aggregator knowledge source:
    name: aggregator knowledge source
    description: An intermediate aggregator resource from which knowledge expressed
      in an Association was retrieved downstream of the original source, on its path
      to its current serialized form.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: knowledge source
    domain: association
    multivalued: true
    alias: aggregator_knowledge_source
    owner: genomic sequence localization
    range: information resource
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
    owner: genomic sequence localization
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
    owner: genomic sequence localization
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
    owner: genomic sequence localization
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
    owner: genomic sequence localization
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
    owner: genomic sequence localization
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
    owner: genomic sequence localization
    range: narrative text
  source:
    name: source
    deprecated: 'True'
    from_schema: https://w3id.org/biolink/biolink-model
    alias: source
    owner: genomic sequence localization
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
    owner: genomic sequence localization
    range: attribute

```
</details>