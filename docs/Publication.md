---
parent: Entities
title: biolink:Publication
grand_parent: Classes
layout: default
---

# Class: Publication


Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Biolink category subclasses.

URI: [biolink:Publication](https://w3id.org/biolink/vocab/Publication)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Serial],[Association]-%20publications%200..%2A%3E[Publication%7Cauthors:string%20%2A;pages:string%20%2A;summary:string%20%3F;keywords:string%20%2A;mesh_terms:uriorcurie%20%2A;xref:iri_type%20%2A;id:string;name:label_type%20%3F;type:string;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;iri(i):iri_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Publication]%5E-[Serial],[Publication]%5E-[BookChapter],[Publication]%5E-[Book],[Publication]%5E-[Article],[InformationContentEntity]%5E-[Publication],[NamedThing],[InformationContentEntity],[BookChapter],[Book],[Attribute],[Association],[Article],[Agent])

---


## Identifier prefixes

 * NLMID

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support.

## Children

 * [Article](Article.md)
 * [Book](Book.md) - This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
 * [BookChapter](BookChapter.md)
 * [Serial](Serial.md) - This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.

## Referenced by class

 *  **[Association](Association.md)** *[publications](publications.md)*  <sub>0..*</sub>  **[Publication](Publication.md)**

## Attributes


### Own

 * [authors](authors.md)  <sub>0..*</sub>
    * Description: connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
    * range: [String](types/String.md)
 * [keywords](keywords.md)  <sub>0..*</sub>
    * Description: keywords tagging a publication
    * range: [String](types/String.md)
 * [mesh terms](mesh_terms.md)  <sub>0..*</sub>
    * Description: mesh terms tagging a publication
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [publication➞id](publication_id.md)  <sub>REQ</sub>
    * Description: Different kinds of publication subtypes will have different preferred identifiers (curies when feasible). Precedence of identifiers for scientific articles is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise. Enclosing publications (i.e. referenced by 'published in' node property) such as books and journals, should have industry-standard identifier such as from ISBN and ISSN.
    * range: [String](types/String.md)
 * [publication➞name](publication_name.md)  <sub>OPT</sub>
    * Description: the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing) The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case).
    * range: [LabelType](types/LabelType.md)
 * [publication➞pages](publication_pages.md)  <sub>0..*</sub>
    * Description: When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book.
    * range: [String](types/String.md)
 * [publication➞type](publication_type.md)  <sub>REQ</sub>
    * Description: Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html), the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of biolink:category biolink:OntologyClass.
    * range: [String](types/String.md)
 * [summary](summary.md)  <sub>OPT</sub>
    * Description: executive  summary of a publication
    * range: [String](types/String.md)

### Inherited from entity:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for an entity. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for an attribute or entity.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of an entity
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (translator_minimal)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any entity to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from information content entity:

 * [license](license.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [rights](rights.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [format](format.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [creation date](creation_date.md)  <sub>OPT</sub>
    * Description: date on which an entity was created. This can be applied to nodes or edges
    * range: [Date](types/Date.md)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [authors](authors.md)  <sub>0..*</sub>
    * Description: connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
    * range: [String](types/String.md)
 * [keywords](keywords.md)  <sub>0..*</sub>
    * Description: keywords tagging a publication
    * range: [String](types/String.md)
 * [mesh terms](mesh_terms.md)  <sub>0..*</sub>
    * Description: mesh terms tagging a publication
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [publication➞id](publication_id.md)  <sub>REQ</sub>
    * Description: Different kinds of publication subtypes will have different preferred identifiers (curies when feasible). Precedence of identifiers for scientific articles is as follows: PMID if available; DOI if not; actual alternate CURIE otherwise. Enclosing publications (i.e. referenced by 'published in' node property) such as books and journals, should have industry-standard identifier such as from ISBN and ISSN.
    * range: [String](types/String.md)
 * [publication➞name](publication_name.md)  <sub>OPT</sub>
    * Description: the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing) The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case).
    * range: [LabelType](types/LabelType.md)
 * [publication➞pages](publication_pages.md)  <sub>0..*</sub>
    * Description: When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book.
    * range: [String](types/String.md)
 * [publication➞type](publication_type.md)  <sub>REQ</sub>
    * Description: Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html), the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of biolink:category biolink:OntologyClass.
    * range: [String](types/String.md)
 * [summary](summary.md)  <sub>OPT</sub>
    * Description: executive  summary of a publication
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | IAO:0000311 |
| **Narrow Mappings:** | | IAO:0000013 |
|  | | UMLSSC:T170 |
|  | | UMLSST:inpr |

