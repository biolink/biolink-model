---
parent: Entities
title: biolink:Publication
grand_parent: Classes
layout: default
---

# Class: Publication


Any ‘published’ piece of information. Publications are considered broadly  to include any document or document part made available in print or on the  web - which may include scientific journal issues, individual articles, and  books - as well as things like pre-prints, white papers, patents, drug  labels, web pages, protocol documents,  and even a part of a publication if  of significant knowledge scope (e.g. a figure, figure legend, or section  highlighted by NLP).

URI: [biolink:Publication](https://w3id.org/biolink/vocab/Publication)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[WebPage],[Serial],[Agent]%3Cauthors%200..%2A-%20[Publication%7Cpages:string%20%2A;summary:string%20%3F;keywords:string%20%2A;mesh_terms:uriorcurie%20%2A;id:string;name:label_type%20%3F;publication_type:string%20%2B;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;provided_by(i):string%20%2A;xref(i):uriorcurie%20%2A;full_name(i):label_type%20%3F;synonym(i):label_type%20%2A;category(i):category_type%20%2B;iri(i):iri_type%20%3F;type(i):string%20%2A;description(i):narrative_text%20%3F;deprecated(i):boolean%20%3F],[Association]-%20publications%200..%2A%3E[Publication],[Publication]%5E-[WebPage],[Publication]%5E-[Serial],[Publication]%5E-[PreprintPublication],[Publication]%5E-[Patent],[Publication]%5E-[DrugLabel],[Publication]%5E-[BookChapter],[Publication]%5E-[Book],[Publication]%5E-[Article],[InformationContentEntity]%5E-[Publication],[PreprintPublication],[Patent],[InformationContentEntity],[DrugLabel],[BookChapter],[Book],[Attribute],[Association],[Article],[Agent])

---


## Identifier prefixes

 * PMID
 * PMC
 * doi
 * NLMID

## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support.

## Children

 * [Article](Article.md) - a piece of writing on a particular topic presented as a stand-alone  section of a larger publication	  
 * [Book](Book.md) - This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
 * [BookChapter](BookChapter.md)
 * [DrugLabel](DrugLabel.md) - a document accompanying a drug or its container that provides written, printed or graphic information about the drug, including drug contents, specific instructions  or warnings for administration, storage and disposal instructions, etc. 
 * [Patent](Patent.md) - a legal document granted by a patent issuing authority which confers upon  the patenter the sole right to make, use and sell an invention for a set period of time. 
 * [PreprintPublication](PreprintPublication.md) - a document reresenting an early version of an author's original scholarly work,  such as a research paper or a review, prior to formal peer review and publication  in a peer-reviewed scholarly or scientific journal.
 * [Serial](Serial.md) - This class may rarely be instantiated except if use cases of a given knowledge graph support its utility.
 * [WebPage](WebPage.md) - a document that is published according to World Wide Web standards, which  may incorporate text, graphics, sound, and/or other features.

## Referenced by class

 *  **[Agent](Agent.md)** *[author](author.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**
 *  **[Agent](Agent.md)** *[editor](editor.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**
 *  **[Association](Association.md)** *[publications](publications.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**
 *  **[Agent](Agent.md)** *[publisher](publisher.md)*  <sub>0..\*</sub>  **[Publication](Publication.md)**

## Attributes


### Own

 * [authors](authors.md)  <sub>0..\*</sub>
     * Description: connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
     * Range: [Agent](Agent.md)
 * [keywords](keywords.md)  <sub>0..\*</sub>
     * Description: keywords tagging a publication
     * Range: [String](types/String.md)
 * [mesh terms](mesh_terms.md)  <sub>0..\*</sub>
     * Description: mesh terms tagging a publication
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)
 * [pages](pages.md)  <sub>0..\*</sub>
     * Description: page number of source referenced for statement or publication
     * Range: [String](types/String.md)
 * [publication type](publication_type.md)  <sub>0..\*</sub>
     * Description: Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html), the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of biolink:category biolink:OntologyClass.
     * Range: [String](types/String.md)
 * [summary](summary.md)  <sub>0..1</sub>
     * Description: executive  summary of a publication
     * Range: [String](types/String.md)

### Inherited from entity:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>0..1</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * Range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)
 * [type](type.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)
 * [deprecated](deprecated.md)  <sub>0..1</sub>
     * Description: A boolean flag indicating that an entity is no longer considered current or valid.
     * Range: [Boolean](types/Boolean.md)

### Inherited from gene product mixin:

 * [synonym](synonym.md)  <sub>0..\*</sub>
     * Description: Alternate human-readable names for a thing
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)
 * [xref](xref.md)  <sub>0..\*</sub>
     * Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (translator_minimal)

### Inherited from information content entity:

 * [license](license.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [rights](rights.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [format](format.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [creation date](creation_date.md)  <sub>0..1</sub>
     * Description: date on which an entity was created. This can be applied to nodes or edges
     * Range: [Date](types/Date.md)

### Inherited from named thing:

 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     * Range: [String](types/String.md)
 * [full name](full_name.md)  <sub>0..1</sub>
     * Description: a long-form human readable name for a thing
     * Range: [LabelType](types/LabelType.md)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)

### Domain for slot:

 * [authors](authors.md)  <sub>0..\*</sub>
     * Description: connects an publication to the list of authors who contributed to the publication. This property should be a comma-delimited list of author names. It is recommended that an author's name be formatted as "surname, firstname initial.".   Note that this property is a node annotation expressing the citation list of authorship which might typically otherwise be more completely documented in biolink:PublicationToProviderAssociation defined edges which point to full details about an author and possibly, some qualifiers which clarify the specific status of a given author in the publication.
     * Range: [Agent](Agent.md)
 * [keywords](keywords.md)  <sub>0..\*</sub>
     * Description: keywords tagging a publication
     * Range: [String](types/String.md)
 * [mesh terms](mesh_terms.md)  <sub>0..\*</sub>
     * Description: mesh terms tagging a publication
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)
 * [pages](pages.md)  <sub>0..\*</sub>
     * Description: page number of source referenced for statement or publication
     * Range: [String](types/String.md)
 * [publication type](publication_type.md)  <sub>0..\*</sub>
     * Description: Ontology term for publication type may be drawn from Dublin Core types (https://www.dublincore.org/specifications/dublin-core/dcmi-type-vocabulary/), FRBR-aligned Bibliographic Ontology (https://sparontologies.github.io/fabio/current/fabio.html), the MESH publication types (https://www.nlm.nih.gov/mesh/pubtypes.html), the Confederation of Open Access Repositories (COAR) Controlled Vocabulary for Resource Type Genres (http://vocabularies.coar-repositories.org/documentation/resource_types/), Wikidata (https://www.wikidata.org/wiki/Wikidata:Publication_types), or equivalent publication type ontology. When a given publication type ontology term is used within a given knowledge graph, then the CURIE identified term must be documented in the graph as a concept node of biolink:category biolink:OntologyClass.
     * Range: [String](types/String.md)
 * [summary](summary.md)  <sub>0..1</sub>
     * Description: executive  summary of a publication
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | IAO:0000311 |
| **Narrow Mappings:** | | IAO:0000013 |
|  | | STY:T170 |

