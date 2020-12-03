---
parent: Entities
title: biolink:OntologyClass
grand_parent: Classes
layout: default
---

# Class: OntologyClass


a concept or class in an ontology, vocabulary or thesaurus

URI: [biolink:OntologyClass](https://w3id.org/biolink/vocab/OntologyClass)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[TaxonomicRank],[RelationshipType],[OrganismTaxon],[ContributorAssociation]-%20qualifiers%200..%2A%3E[OntologyClass%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[GeneExpressionMixin]-%20quantifier%20qualifier%200..1%3E[OntologyClass],[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier%200..1%3E[OntologyClass],[Attribute]-%20has%20attribute%20type%201..1%3E[OntologyClass],[PairwiseMolecularInteraction]-%20interacting%20molecules%20category%200..1%3E[OntologyClass],[Association]-%20qualifiers%200..%2A%3E[OntologyClass],[GeneExpressionMixin]-%20quantifier%20qualifier(i)%200..1%3E[OntologyClass],[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier(i)%200..1%3E[OntologyClass],[OntologyClass]%5E-[TaxonomicRank],[OntologyClass]%5E-[RelationshipType],[OntologyClass]%5E-[OrganismTaxon],[OntologyClass]%5E-[GeneOntologyClass],[NamedThing]%5E-[OntologyClass],[PairwiseMolecularInteraction],[NamedThing],[GeneToExpressionSiteAssociation],[GeneOntologyClass],[GeneExpressionMixin],[ContributorAssociation],[Attribute],[Association],[Agent])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [GeneOntologyClass](GeneOntologyClass.md) - an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 * [OrganismTaxon](OrganismTaxon.md) - A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.
 * [RelationshipType](RelationshipType.md) - An OWL property used as an edge label
 * [TaxonomicRank](TaxonomicRank.md) - A descriptor for the rank within a taxonomic classification. Example instance: TAXRANK:0000017 (kingdom)

## Referenced by class

 *  **[Association](Association.md)** *[association type](association_type.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[ContributorAssociation](ContributorAssociation.md)** *[contributor association➞qualifiers](contributor_association_qualifiers.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[GeneExpressionMixin](GeneExpressionMixin.md)** *[gene expression mixin➞quantifier qualifier](gene_expression_mixin_quantifier_qualifier.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[gene to expression site association➞quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Attribute](Attribute.md)** *[has attribute type](has_attribute_type.md)*  <sub>REQ</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[NamedThing](NamedThing.md)** *[has molecular consequence](has_molecular_consequence.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[NamedThing](NamedThing.md)** *[has topic](has_topic.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[interacting molecules category](interacting_molecules_category.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[qualifiers](qualifiers.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[Association](Association.md)** *[quantifier qualifier](quantifier_qualifier.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[OntologyClass](OntologyClass.md)** *[subclass of](subclass_of.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[OntologyClass](OntologyClass.md)** *[superclass of](superclass_of.md)*  <sub>0..*</sub>  **[OntologyClass](OntologyClass.md)**

## Attributes


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

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)
