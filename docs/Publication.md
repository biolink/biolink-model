# Class: Publication
_Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Biolink category subclasses._





URI: [biolink:Publication](https://w3id.org/biolink/vocab/Publication)




## Inheritance

* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * [InformationContentEntity](InformationContentEntity.md)
            * **Publication**
                * [Book](Book.md)
                * [BookChapter](BookChapter.md)
                * [Serial](Serial.md)
                * [Article](Article.md)




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [authors](authors.md) | [string](string.md) | 0..* | connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.  | . |
| [pages](pages.md) | [string](string.md) | 0..* | When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book.  | . |
| [summary](summary.md) | [string](string.md) | 0..1 | executive  summary of a publication  | . |
| [keywords](keywords.md) | [string](string.md) | 0..* | keywords tagging a publication  | . |
| [mesh_terms](mesh_terms.md) | [uriorcurie](uriorcurie.md) | 0..* | mesh terms tagging a publication  | . |
| [xref](xref.md) | [uriorcurie](uriorcurie.md) | 0..* | Alternate CURIEs for a thing  | . |
| [license](license.md) | [string](string.md) | 0..1 | None  | . |
| [rights](rights.md) | [string](string.md) | 0..1 | None  | . |
| [format](format.md) | [string](string.md) | 0..1 | None  | . |
| [creation_date](creation_date.md) | [date](date.md) | 0..1 | date on which an entity was created. This can be applied to nodes or edges  | . |
| [id](id.md) | [string](string.md) | 1..1 | Different kinds of publication subtypes will have different preferred identifiers (curies when feasible). Precedence of identifiers for scientific articles is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise. Enclosing publications (i.e. referenced by 'published in' node property) such as books and journals, should have industry-standard identifier such as from ISBN and ISSN.  | . |
| [iri](iri.md) | [iri_type](iri_type.md) | 0..1 | An IRI for an entity. This is determined by the id using expansion rules.  | . |
| [category](category.md) | [NamedThing](NamedThing.md) | 1..* | Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}  | . |
| [type](type.md) | [string](string.md) | 1..1 | Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html), the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of biolink:category biolink:OntologyClass.  | . |
| [name](name.md) | [label_type](label_type.md) | 0..1 | the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing). The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case).  | . |
| [description](description.md) | [narrative_text](narrative_text.md) | 0..1 | a human-readable description of an entity  | . |
| [source](source.md) | [label_type](label_type.md) | 0..1 | a lightweight analog to the association class 'provided by' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.  | . |
| [provided_by](provided_by.md) | [Agent](Agent.md) | 0..* | connects an association to the agent (person, organization or group) that provided it  | . |
| [has_attribute](has_attribute.md) | [Attribute](Attribute.md) | 0..* | connects any entity to an attribute  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Publication](Publication.md) | [authors](authors.md) | domain | publication |
| [Publication](Publication.md) | [pages](pages.md) | domain | publication |
| [Publication](Publication.md) | [summary](summary.md) | domain | publication |
| [Publication](Publication.md) | [keywords](keywords.md) | domain | publication |
| [Publication](Publication.md) | [mesh_terms](mesh_terms.md) | domain | publication |
| [Book](Book.md) | [authors](authors.md) | domain | publication |
| [Book](Book.md) | [pages](pages.md) | domain | publication |
| [Book](Book.md) | [summary](summary.md) | domain | publication |
| [Book](Book.md) | [keywords](keywords.md) | domain | publication |
| [Book](Book.md) | [mesh_terms](mesh_terms.md) | domain | publication |
| [BookChapter](BookChapter.md) | [published_in](published_in.md) | domain | publication |
| [BookChapter](BookChapter.md) | [volume](volume.md) | domain | publication |
| [BookChapter](BookChapter.md) | [authors](authors.md) | domain | publication |
| [BookChapter](BookChapter.md) | [pages](pages.md) | domain | publication |
| [BookChapter](BookChapter.md) | [summary](summary.md) | domain | publication |
| [BookChapter](BookChapter.md) | [keywords](keywords.md) | domain | publication |
| [BookChapter](BookChapter.md) | [mesh_terms](mesh_terms.md) | domain | publication |
| [Serial](Serial.md) | [iso_abbreviation](iso_abbreviation.md) | domain | publication |
| [Serial](Serial.md) | [volume](volume.md) | domain | publication |
| [Serial](Serial.md) | [issue](issue.md) | domain | publication |
| [Serial](Serial.md) | [authors](authors.md) | domain | publication |
| [Serial](Serial.md) | [pages](pages.md) | domain | publication |
| [Serial](Serial.md) | [summary](summary.md) | domain | publication |
| [Serial](Serial.md) | [keywords](keywords.md) | domain | publication |
| [Serial](Serial.md) | [mesh_terms](mesh_terms.md) | domain | publication |
| [Article](Article.md) | [published_in](published_in.md) | domain | publication |
| [Article](Article.md) | [iso_abbreviation](iso_abbreviation.md) | domain | publication |
| [Article](Article.md) | [volume](volume.md) | domain | publication |
| [Article](Article.md) | [issue](issue.md) | domain | publication |
| [Article](Article.md) | [authors](authors.md) | domain | publication |
| [Article](Article.md) | [pages](pages.md) | domain | publication |
| [Article](Article.md) | [summary](summary.md) | domain | publication |
| [Article](Article.md) | [keywords](keywords.md) | domain | publication |
| [Article](Article.md) | [mesh_terms](mesh_terms.md) | domain | publication |
| [Association](Association.md) | [publications](publications.md) | range | publication |
| [ContributorAssociation](ContributorAssociation.md) | [publications](publications.md) | range | publication |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [publications](publications.md) | range | publication |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [publications](publications.md) | range | publication |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [publications](publications.md) | range | publication |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [publications](publications.md) | range | publication |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [publications](publications.md) | range | publication |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [publications](publications.md) | range | publication |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [publications](publications.md) | range | publication |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [publications](publications.md) | range | publication |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | range | publication |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [publications](publications.md) | range | publication |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [publications](publications.md) | range | publication |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [publications](publications.md) | range | publication |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [publications](publications.md) | range | publication |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | range | publication |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [publications](publications.md) | range | publication |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [publications](publications.md) | range | publication |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [publications](publications.md) | range | publication |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [publications](publications.md) | range | publication |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | range | publication |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [publications](publications.md) | range | publication |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [publications](publications.md) | range | publication |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject](subject.md) | domain | publication |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [publications](publications.md) | range | publication |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [publications](publications.md) | range | publication |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [publications](publications.md) | range | publication |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [publications](publications.md) | range | publication |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [publications](publications.md) | range | publication |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [publications](publications.md) | range | publication |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [publications](publications.md) | range | publication |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [publications](publications.md) | range | publication |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [publications](publications.md) | range | publication |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [publications](publications.md) | range | publication |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [publications](publications.md) | range | publication |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [publications](publications.md) | range | publication |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [publications](publications.md) | range | publication |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [publications](publications.md) | range | publication |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [publications](publications.md) | range | publication |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [publications](publications.md) | range | publication |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | range | publication |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | range | publication |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | range | publication |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | range | publication |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | range | publication |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [publications](publications.md) | range | publication |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [publications](publications.md) | range | publication |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [publications](publications.md) | range | publication |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [publications](publications.md) | range | publication |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [publications](publications.md) | range | publication |
| [FunctionalAssociation](FunctionalAssociation.md) | [publications](publications.md) | range | publication |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [publications](publications.md) | range | publication |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [publications](publications.md) | range | publication |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [publications](publications.md) | range | publication |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [publications](publications.md) | range | publication |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [publications](publications.md) | range | publication |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [publications](publications.md) | range | publication |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [publications](publications.md) | range | publication |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [publications](publications.md) | range | publication |
| [SequenceAssociation](SequenceAssociation.md) | [publications](publications.md) | range | publication |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [publications](publications.md) | range | publication |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [publications](publications.md) | range | publication |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [publications](publications.md) | range | publication |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [publications](publications.md) | range | publication |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [publications](publications.md) | range | publication |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [publications](publications.md) | range | publication |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [publications](publications.md) | range | publication |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [publications](publications.md) | range | publication |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [publications](publications.md) | range | publication |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [publications](publications.md) | range | publication |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [publications](publications.md) | range | publication |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [publications](publications.md) | range | publication |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [publications](publications.md) | range | publication |



## Identifier and Mapping Information


### Valid ID Prefixes

Instances of this class *should* have identifiers with one of the following prefixes:

* NLMID










## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: publication
id_prefixes:
- NLMID
exact_mappings:
- IAO:0000311
narrow_mappings:
- IAO:0000013
- STY:T170
description: Any published piece of information. Can refer to a whole publication,
  its encompassing publication (i.e. journal or book) or to a part of a publication,
  if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted
  by NLP). The scope is intended to be general and include information published on
  the web, as well as printed materials, either directly or in one of the Publication
  Biolink category subclasses.
in_subset:
- model_organism_database
from_schema: https://w3id.org/biolink/biolink-model
is_a: information content entity
slots:
- authors
- pages
- summary
- keywords
- mesh terms
- xref
slot_usage:
  id:
    name: id
    description: 'Different kinds of publication subtypes will have different preferred
      identifiers (curies when feasible). Precedence of identifiers for scientific
      articles is as follows: PMID if available; DOI if not; actual alternate CURIE
      otherwise. Enclosing publications (i.e. referenced by ''published in'' node
      property) such as books and journals, should have industry-standard identifier
      such as from ISBN and ISSN.'
  name:
    name: name
    description: the 'title' of the publication is generally recorded in the 'name'
      property (inherited from NamedThing). The field name 'title' is now also tagged
      as an acceptable alias for the node property 'name' (just in case).
  type:
    name: type
    description: Ontology term for publication type may be drawn from Dublin Core
      types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/),
      FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html),
      the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the
      Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource
      Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/),
      Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent
      publication type ontology. When a given publication type ontology term is used
      within a given knowledge graph, then the CURIE identified term must be documented
      in the graph as a concept node of biolink:category biolink:OntologyClass.
    values_from:
    - dctypes
    - fabio
    - MESH_PUB
    - COAR_RESOURCE
    - WIKIDATA
    slot_uri: dct:type
    required: true
  pages:
    name: pages
    description: When a 2-tuple of page numbers are provided, they represent the start
      and end page of the publication within its parent publication context. For books,
      this may be set to the total number of pages of the book.
    multivalued: true

```
</details>

### Induced

<details>
```yaml
name: publication
id_prefixes:
- NLMID
exact_mappings:
- IAO:0000311
narrow_mappings:
- IAO:0000013
- STY:T170
description: Any published piece of information. Can refer to a whole publication,
  its encompassing publication (i.e. journal or book) or to a part of a publication,
  if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted
  by NLP). The scope is intended to be general and include information published on
  the web, as well as printed materials, either directly or in one of the Publication
  Biolink category subclasses.
in_subset:
- model_organism_database
from_schema: https://w3id.org/biolink/biolink-model
is_a: information content entity
slot_usage:
  id:
    name: id
    description: 'Different kinds of publication subtypes will have different preferred
      identifiers (curies when feasible). Precedence of identifiers for scientific
      articles is as follows: PMID if available; DOI if not; actual alternate CURIE
      otherwise. Enclosing publications (i.e. referenced by ''published in'' node
      property) such as books and journals, should have industry-standard identifier
      such as from ISBN and ISSN.'
  name:
    name: name
    description: the 'title' of the publication is generally recorded in the 'name'
      property (inherited from NamedThing). The field name 'title' is now also tagged
      as an acceptable alias for the node property 'name' (just in case).
  type:
    name: type
    description: Ontology term for publication type may be drawn from Dublin Core
      types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/),
      FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html),
      the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the
      Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource
      Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/),
      Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent
      publication type ontology. When a given publication type ontology term is used
      within a given knowledge graph, then the CURIE identified term must be documented
      in the graph as a concept node of biolink:category biolink:OntologyClass.
    values_from:
    - dctypes
    - fabio
    - MESH_PUB
    - COAR_RESOURCE
    - WIKIDATA
    slot_uri: dct:type
    required: true
  pages:
    name: pages
    description: When a 2-tuple of page numbers are provided, they represent the start
      and end page of the publication within its parent publication context. For books,
      this may be set to the total number of pages of the book.
    multivalued: true
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
    owner: publication
    range: string
  pages:
    name: pages
    description: When a 2-tuple of page numbers are provided, they represent the start
      and end page of the publication within its parent publication context. For books,
      this may be set to the total number of pages of the book.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: publication
    multivalued: true
    alias: pages
    owner: publication
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
    owner: publication
    range: string
  keywords:
    name: keywords
    description: keywords tagging a publication
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: publication
    multivalued: true
    alias: keywords
    owner: publication
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
    owner: publication
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
    owner: publication
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
    owner: publication
    range: string
  rights:
    name: rights
    exact_mappings:
    - dct:rights
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: information content entity
    alias: rights
    owner: publication
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
    owner: publication
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
    owner: publication
    range: date
  id:
    name: id
    description: 'Different kinds of publication subtypes will have different preferred
      identifiers (curies when feasible). Precedence of identifiers for scientific
      articles is as follows: PMID if available; DOI if not; actual alternate CURIE
      otherwise. Enclosing publications (i.e. referenced by ''published in'' node
      property) such as books and journals, should have industry-standard identifier
      such as from ISBN and ISSN.'
    from_schema: https://w3id.org/biolink/biolink-model
    identifier: true
    alias: id
    owner: publication
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
    owner: publication
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
    owner: publication
    is_class_field: true
    range: named thing
    required: true
  type:
    name: type
    description: Ontology term for publication type may be drawn from Dublin Core
      types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/),
      FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html),
      the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the
      Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource
      Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/),
      Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent
      publication type ontology. When a given publication type ontology term is used
      within a given knowledge graph, then the CURIE identified term must be documented
      in the graph as a concept node of biolink:category biolink:OntologyClass.
    from_schema: https://w3id.org/biolink/biolink-model
    values_from:
    - dctypes
    - fabio
    - MESH_PUB
    - COAR_RESOURCE
    - WIKIDATA
    slot_uri: dct:type
    alias: type
    owner: publication
    range: string
    required: true
  name:
    name: name
    description: the 'title' of the publication is generally recorded in the 'name'
      property (inherited from NamedThing). The field name 'title' is now also tagged
      as an acceptable alias for the node property 'name' (just in case).
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdfs:label
    alias: name
    owner: publication
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
    owner: publication
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
    owner: publication
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
    owner: publication
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
    owner: publication
    range: attribute

```
</details>