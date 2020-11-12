---
parent: Entities
title: biolink:Article
grand_parent: Classes
layout: default
---

# Class: Article




URI: [biolink:Article](https://w3id.org/biolink/vocab/Article)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Publication]%5E-[Article%7Cpublished_in:uriorcurie;iso_abbreviation:string%20%3F;volume:string%20%3F;issue:string%20%3F;type(i):string;authors(i):string%20%2A;pages(i):string%20%2A;abstract(i):string%20%3F;keywords(i):string%20%2A;mesh_terms(i):uriorcurie%20%2A;xref(i):iri_type%20%2A;id(i):string;name(i):label_type;description(i):narrative_text%20%3F;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;category(i):category_type%20%2B])

---


## Identifier prefixes

 * PMID

## Parents

 *  is_a: [Publication](Publication.md) - Any published piece of information. Can refer to a whole publication, its encompassing publication (i.e. journal or book) or to a part of a publication, if of significant knowledge scope (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web, as well as printed materials, either directly or in one of the Publication Biolink category subclasses.

## Referenced by class


## Attributes


### Own

 * [article➞iso abbreviation](article_iso_abbreviation.md)  <sub>OPT</sub>
    * Description: Optional value, if used locally as a convenience, is set to the iso abbreviation of the 'published in' parent.
    * range: [String](types/String.md)
 * [article➞published in](article_published_in.md)  <sub>REQ</sub>
    * Description: The enclosing parent serial containing the article should have industry-standard identifier from ISSN.
    * range: [Uriorcurie](types/Uriorcurie.md)

### Inherited from information content entity:

 * [license](license.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [rights](rights.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [format](format.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [creation date](creation_date.md)  <sub>OPT</sub>
    * Description: date on which thing was created. This can be applied to nodes or edges
    * range: [Date](types/Date.md)

### Inherited from named thing:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

### Inherited from publication:

 * [publication➞type](publication_type.md)  <sub>REQ</sub>
    * Description: Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html), the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of biolink:category biolink:OntologyClass.
    * range: [String](types/String.md)
 * [authors](authors.md)  <sub>0..*</sub>
    * Description: connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
    * range: [String](types/String.md)
 * [publication➞pages](publication_pages.md)  <sub>0..*</sub>
    * Description: When a 2-tuple of page numbers are provided, they represent the start and end page of the publication within its parent publication context. For books, this may be set to the total number of pages of the book.
    * range: [String](types/String.md)
 * [abstract](abstract.md)  <sub>OPT</sub>
    * Description: summary of a publication
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
 * [publication➞name](publication_name.md)  <sub>REQ</sub>
    * Description: the 'title' of the publication is generally recorded in the 'name' property (inherited from NamedThing) The field name 'title' is now also tagged as an acceptable alias for the node property 'name' (just in case).
    * range: [LabelType](types/LabelType.md)

### Domain for slot:

 * [article➞iso abbreviation](article_iso_abbreviation.md)  <sub>OPT</sub>
    * Description: Optional value, if used locally as a convenience, is set to the iso abbreviation of the 'published in' parent.
    * range: [String](types/String.md)
 * [article➞published in](article_published_in.md)  <sub>REQ</sub>
    * Description: The enclosing parent serial containing the article should have industry-standard identifier from ISSN.
    * range: [Uriorcurie](types/Uriorcurie.md)
