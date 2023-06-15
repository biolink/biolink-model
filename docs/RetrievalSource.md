---
parent: Entities
title: biolink:RetrievalSource
grand_parent: Classes
layout: default
---

# Class: RetrievalSource


Provides information about how a particular InformationResource served as a source from which knowledge expressed in an Edge, or data used to generate this knowledge, was retrieved.

URI: [biolink:RetrievalSource](https://w3id.org/biolink/vocab/RetrievalSource)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Association]-%20retrieval%20source%20ids%200..%2A%3E[RetrievalSource%7Cresource_id:uriorcurie;resource_role:ResourceRoleEnum;upstream_resource_ids:uriorcurie%20%3F;license(i):string%20%3F;rights(i):string%20%3F;format(i):string%20%3F;creation_date(i):date%20%3F;provided_by(i):string%20%2A;xref(i):uriorcurie%20%2A;full_name(i):label_type%20%3F;category(i):category_type%20%2B;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%2A;name(i):label_type%20%3F;description(i):narrative_text%20%3F],[InformationContentEntity]%5E-[RetrievalSource],[InformationContentEntity],[Attribute],[Association])

---


## Parents

 *  is_a: [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some topic of discourse or is used as support.

## Referenced by class

 *  **None** *[retrieval source ids](retrieval_source_ids.md)*  <sub>0..\*</sub>  **[RetrievalSource](RetrievalSource.md)**

## Attributes


### Own

 * [resource id](resource_id.md)  <sub>0..1</sub>
     * Description: The CURIE for an Information Resource that served as a source of knowledge expressed in an Edge, or a source of data used to generate this knowledge.
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (translator_minimal)
 * [resource role](resource_role.md)  <sub>0..1</sub>
     * Description: The role played by the InformationResource in serving as a source for an Edge. Note that a given Edge should have one and only one 'primary' source, and may have any number of 'aggregator' or 'supporting data' sources.
     * Range: [ResourceRoleEnum](ResourceRoleEnum.md)
     * in subsets: (translator_minimal)
 * [upstream resource ids](upstream_resource_ids.md)  <sub>0..1</sub>
     * Description: An upstream InformationResource from which the resource being described directly retrieved a record of the knowledge expressed in the Edge, or data used to generate this knowledge. This is an array because there are cases where a merged Edge holds knowledge that was retrieved from multiple sources. e.g. an Edge provided by the ARAGORN ARA can expressing knowledge it retrieved from both the automat-mychem-info and molepro KPs, which both provided it with records of this single fact.
     * Range: [Uriorcurie](types/Uriorcurie.md)

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

### Inherited from gene product mixin:

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

### Inherited from macromolecular machine mixin:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)

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

 * [resource id](resource_id.md)  <sub>0..1</sub>
     * Description: The CURIE for an Information Resource that served as a source of knowledge expressed in an Edge, or a source of data used to generate this knowledge.
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (translator_minimal)
 * [resource role](resource_role.md)  <sub>0..1</sub>
     * Description: The role played by the InformationResource in serving as a source for an Edge. Note that a given Edge should have one and only one 'primary' source, and may have any number of 'aggregator' or 'supporting data' sources.
     * Range: [ResourceRoleEnum](ResourceRoleEnum.md)
     * in subsets: (translator_minimal)
 * [upstream resource ids](upstream_resource_ids.md)  <sub>0..1</sub>
     * Description: An upstream InformationResource from which the resource being described directly retrieved a record of the knowledge expressed in the Edge, or data used to generate this knowledge. This is an array because there are cases where a merged Edge holds knowledge that was retrieved from multiple sources. e.g. an Edge provided by the ARAGORN ARA can expressing knowledge it retrieved from both the automat-mychem-info and molepro KPs, which both provided it with records of this single fact.
     * Range: [Uriorcurie](types/Uriorcurie.md)
