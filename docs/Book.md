# Class: Book
_This class may rarely be instantiated except if use cases of a given knowledge graph support its utility._





URI: [biolink:Book](https://w3id.org/biolink/vocab/Book)




## Inheritance

* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * [InformationContentEntity](InformationContentEntity.md)
            * [Publication](Publication.md)
                * **Book**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [authors](authors.md) | [string](string.md) | 0..* | connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.  | . |
| [pages](pages.md) | [string](string.md) | 0..* | page number of source referenced for statement or publication  | . |
| [summary](summary.md) | [string](string.md) | 0..1 | executive  summary of a publication  | . |
| [keywords](keywords.md) | [string](string.md) | 0..* | keywords tagging a publication  | . |
| [mesh_terms](mesh_terms.md) | [uriorcurie](uriorcurie.md) | 0..* | mesh terms tagging a publication  | . |
| [xref](xref.md) | [uriorcurie](uriorcurie.md) | 0..* | Alternate CURIEs for a thing  | . |
| [license](license.md) | [string](string.md) | 0..1 | None  | . |
| [rights](rights.md) | [string](string.md) | 0..1 | None  | . |
| [format](format.md) | [string](string.md) | 0..1 | None  | . |
| [creation_date](creation_date.md) | [date](date.md) | 0..1 | date on which an entity was created. This can be applied to nodes or edges  | . |
| [provided_by](provided_by.md) | [string](string.md) | 0..* | The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.  | . |
| [id](id.md) | [string](string.md) | 1..1 | Books should have industry-standard identifier such as from ISBN.  | . |
| [iri](iri.md) | [iri_type](iri_type.md) | 0..1 | An IRI for an entity. This is determined by the id using expansion rules.  | . |
| [category](category.md) | [NamedThing](NamedThing.md) | 1..* | Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}  | . |
| [type](type.md) | [string](string.md) | 1..1 | Should generally be set to an ontology class defined term for 'book'.  | . |
| [name](name.md) | [label_type](label_type.md) | 0..1 | A human-readable name for an attribute or entity.  | . |
| [description](description.md) | [narrative_text](narrative_text.md) | 0..1 | a human-readable description of an entity  | . |
| [source](source.md) | [string](string.md) | 0..1 | None  | . |
| [has_attribute](has_attribute.md) | [Attribute](Attribute.md) | 0..* | connects any entity to an attribute  | . |


## Usages



## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* isbn

* NLMID










## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: book
id_prefixes:
- isbn
- NLMID
description: This class may rarely be instantiated except if use cases of a given
  knowledge graph support its utility.
in_subset:
- model_organism_database
from_schema: https://w3id.org/biolink/biolink-model
is_a: publication
slot_usage:
  id:
    name: id
    description: Books should have industry-standard identifier such as from ISBN.
    required: true
  type:
    name: type
    description: Should generally be set to an ontology class defined term for 'book'.

```
</details>

### Induced

<details>
```yaml
name: book
id_prefixes:
- isbn
- NLMID
description: This class may rarely be instantiated except if use cases of a given
  knowledge graph support its utility.
in_subset:
- model_organism_database
from_schema: https://w3id.org/biolink/biolink-model
is_a: publication
slot_usage:
  id:
    name: id
    description: Books should have industry-standard identifier such as from ISBN.
    required: true
  type:
    name: type
    description: Should generally be set to an ontology class defined term for 'book'.
attributes:
  authors:
    name: authors
    description: connects an publication to the list of authors who contributed to
      the publication. This property should be a comma-delimited list of author names.
      It is recommended that an author's name be formatted as "surname, firstname
      initial.".   Note that this property is a node annotation expressing the citation
      list of authorship which might typically otherwise be more completely documented
      in biolink:PublicationToProviderAssociation defined edges which point to full
      details about an author and possibly, some qualifiers which clarify the specific
      status of a given author in the publication.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    singular_name: author
    domain: publication
    multivalued: true
    alias: authors
    owner: book
    range: string
  pages:
    name: pages
    exact_mappings:
    - WIKIDATA_PROPERTY:P304
    description: page number of source referenced for statement or publication
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: publication
    multivalued: true
    alias: pages
    owner: book
    range: string
  summary:
    name: summary
    aliases:
    - abstract
    exact_mappings:
    - dct:abstract
    - WIKIDATA:Q333291
    description: executive  summary of a publication
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: publication
    alias: summary
    owner: book
    range: string
  keywords:
    name: keywords
    description: keywords tagging a publication
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: publication
    multivalued: true
    alias: keywords
    owner: book
    range: string
  mesh terms:
    name: mesh terms
    exact_mappings:
    - dcid:MeSHTerm
    description: mesh terms tagging a publication
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    values_from:
    - MESH
    domain: publication
    multivalued: true
    alias: mesh_terms
    owner: book
    range: uriorcurie
  xref:
    name: xref
    aliases:
    - dbxref
    - Dbxref
    - DbXref
    narrow_mappings:
    - gff3:Dbxref
    - gpi:DB_Xrefs
    description: Alternate CURIEs for a thing
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    multivalued: true
    alias: xref
    owner: book
    range: uriorcurie
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
    owner: book
    range: string
  rights:
    name: rights
    exact_mappings:
    - dct:rights
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: information content entity
    alias: rights
    owner: book
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
    owner: book
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
    owner: book
    range: date
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
    owner: book
    range: string
  id:
    name: id
    description: Books should have industry-standard identifier such as from ISBN.
    from_schema: https://w3id.org/biolink/biolink-model
    identifier: true
    alias: id
    owner: book
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
    owner: book
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
    owner: book
    is_class_field: true
    range: named thing
    required: true
  type:
    name: type
    description: Should generally be set to an ontology class defined term for 'book'.
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdf:type
    alias: type
    owner: book
    range: string
    required: true
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
    owner: book
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
    owner: book
    range: narrative text
  source:
    name: source
    deprecated: 'True'
    from_schema: https://w3id.org/biolink/biolink-model
    alias: source
    owner: book
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
    owner: book
    range: attribute

```
</details>