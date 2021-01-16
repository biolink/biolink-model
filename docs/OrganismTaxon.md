---
parent: Entities
title: biolink:OrganismTaxon
grand_parent: Classes
layout: default
---

# Class: OrganismTaxon


A classification of a set of organisms. Example instances: NCBITaxon:9606 (Homo sapiens), NCBITaxon:2 (Bacteria). Can also be used to represent strains or subspecies.

URI: [biolink:OrganismTaxon](https://w3id.org/biolink/vocab/OrganismTaxon)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ThingWithTaxon],[TaxonomicRank],[OrganismTaxonToOrganismTaxonSpecialization],[OrganismTaxonToOrganismTaxonInteraction],[OrganismTaxonToOrganismTaxonAssociation],[OrganismTaxon]%3Csubclass%20of%200..%2A-%20[OrganismTaxon%7Cid(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[TaxonomicRank]%3Chas%20taxonomic%20rank%200..1-%20[OrganismTaxon],[ThingWithTaxon]-%20in%20taxon%200..%2A%3E[OrganismTaxon],[OrganismTaxonToOrganismTaxonAssociation]-%20object%201..1%3E[OrganismTaxon],[OrganismTaxonToOrganismTaxonAssociation]-%20subject%201..1%3E[OrganismTaxon],[OrganismTaxonToOrganismTaxonInteraction]-%20object%201..1%3E[OrganismTaxon],[OrganismTaxonToOrganismTaxonInteraction]-%20subject%201..1%3E[OrganismTaxon],[OrganismTaxonToOrganismTaxonSpecialization]-%20object%201..1%3E[OrganismTaxon],[OrganismTaxonToOrganismTaxonSpecialization]-%20subject%201..1%3E[OrganismTaxon],[OrganismTaxon]%5E-[BioticExposure],[OntologyClass]%5E-[OrganismTaxon],[OntologyClass],[NamedThing],[BioticExposure],[Attribute],[Agent])

---


## Identifier prefixes

 * NCBITaxon
 * MESH

## Parents

 *  is_a: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus

## Children

 * [BioticExposure](BioticExposure.md) - An external biotic exposure is an intake of (sometimes pathological) biological organisms (including viruses).

## Referenced by class

 *  **[ThingWithTaxon](ThingWithTaxon.md)** *[in taxon](in_taxon.md)*  <sub>0..*</sub>  **[OrganismTaxon](OrganismTaxon.md)**
 *  **[OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md)** *[organism taxon to organism taxon association➞object](organism_taxon_to_organism_taxon_association_object.md)*  <sub>REQ</sub>  **[OrganismTaxon](OrganismTaxon.md)**
 *  **[OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md)** *[organism taxon to organism taxon association➞subject](organism_taxon_to_organism_taxon_association_subject.md)*  <sub>REQ</sub>  **[OrganismTaxon](OrganismTaxon.md)**
 *  **[OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md)** *[organism taxon to organism taxon interaction➞object](organism_taxon_to_organism_taxon_interaction_object.md)*  <sub>REQ</sub>  **[OrganismTaxon](OrganismTaxon.md)**
 *  **[OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md)** *[organism taxon to organism taxon interaction➞subject](organism_taxon_to_organism_taxon_interaction_subject.md)*  <sub>REQ</sub>  **[OrganismTaxon](OrganismTaxon.md)**
 *  **[OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md)** *[organism taxon to organism taxon specialization➞object](organism_taxon_to_organism_taxon_specialization_object.md)*  <sub>REQ</sub>  **[OrganismTaxon](OrganismTaxon.md)**
 *  **[OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md)** *[organism taxon to organism taxon specialization➞subject](organism_taxon_to_organism_taxon_specialization_subject.md)*  <sub>REQ</sub>  **[OrganismTaxon](OrganismTaxon.md)**
 *  **[OrganismTaxon](OrganismTaxon.md)** *[organism taxon➞subclass of](organism_taxon_subclass_of.md)*  <sub>0..*</sub>  **[OrganismTaxon](OrganismTaxon.md)**

## Attributes


### Own

 * [organism taxon➞has taxonomic rank](organism_taxon_has_taxonomic_rank.md)  <sub>OPT</sub>
    * range: [TaxonomicRank](TaxonomicRank.md)
 * [organism taxon➞subclass of](organism_taxon_subclass_of.md)  <sub>0..*</sub>
    * Description: subclass of holds between two taxa, e.g. human subclass of mammal
    * range: [OrganismTaxon](OrganismTaxon.md)

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

### Inherited from macromolecular machine mixin:

 * [macromolecular machine mixin➞name](macromolecular_machine_mixin_name.md)  <sub>OPT</sub>
    * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [organism taxon➞has taxonomic rank](organism_taxon_has_taxonomic_rank.md)  <sub>OPT</sub>
    * range: [TaxonomicRank](TaxonomicRank.md)
 * [organism taxon➞subclass of](organism_taxon_subclass_of.md)  <sub>0..*</sub>
    * Description: subclass of holds between two taxa, e.g. human subclass of mammal
    * range: [OrganismTaxon](OrganismTaxon.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | taxon |
|  | | taxonomic classification |
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | WIKIDATA:Q16521 |
| **Narrow Mappings:** | | UMLSSC:T005 |
|  | | UMLSST:virs |
|  | | UMLSSC:T007 |
|  | | UMLSST:bact |
|  | | UMLSSC:T194 |
|  | | UMLSST:arch |
|  | | UMLSSC:T204 |
|  | | UMLSST:euka |
|  | | UMLSSC:T002 |
|  | | UMLSST:plnt |
|  | | UMLSSC:T004 |
|  | | UMLSST:fngs |
|  | | UMLSSC:T008 |
|  | | UMLSST:anim |
|  | | UMLSSC:T010 |
|  | | UMLSST:vtbt |
|  | | UMLSSC:T011 |
|  | | UMLSST:amph |
|  | | UMLSSC:T012 |
|  | | UMLSST:bird |
|  | | UMLSSC:T013 |
|  | | UMLSST:fish |
|  | | UMLSSC:T014 |
|  | | UMLSST:rept |
|  | | UMLSSC:T015 |
|  | | UMLSST:mamm |
|  | | UMLSSC:T016 |
|  | | UMLSST:humn |

