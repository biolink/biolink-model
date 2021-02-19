---
parent: Other Classes
title: biolink:Attribute
grand_parent: Classes
layout: default
---

# Class: Attribute


A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.

URI: [biolink:Attribute](https://w3id.org/biolink/vocab/Attribute)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Zygosity],[SocioeconomicAttribute],[SeverityValue],[QuantityValue],[OrganismalEntity],[OrganismAttribute],[OntologyClass],[NamedThing],[FrequencyValue],[Entity],[ClinicalAttribute],[BiologicalSex],[NamedThing]%3Chas%20qualitative%20value%200..1-%20[Attribute%7Cname:label_type%20%3F;iri:iri_type%20%3F;source:label_type%20%3F],[QuantityValue]%3Chas%20quantitative%20value%200..%2A-++[Attribute],[OntologyClass]%3Chas%20attribute%20type%201..1-++[Attribute],[Entity]++-%20has%20attribute%200..%2A%3E[Attribute],[OrganismalEntity]++-%20has%20attribute%200..%2A%3E[Attribute],[Attribute]uses%20-.-%3E[OntologyClass],[Attribute]%5E-[Zygosity],[Attribute]%5E-[SocioeconomicAttribute],[Attribute]%5E-[SeverityValue],[Attribute]%5E-[OrganismAttribute],[Attribute]%5E-[FrequencyValue],[Attribute]%5E-[ClinicalAttribute],[Attribute]%5E-[BiologicalSex],[Annotation]%5E-[Attribute],[Annotation])

---


## Identifier prefixes

 * EDAM-DATA
 * EDAM-FORMAT
 * EDAM-OPERATION
 * EDAM-TOPIC

## Parents

 *  is_a: [Annotation](Annotation.md) - Biolink Model root class for entity annotations.

## Uses Mixins

 *  mixin: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.

## Children

 * [BiologicalSex](BiologicalSex.md)
 * [ClinicalAttribute](ClinicalAttribute.md) - Attributes relating to a clinical manifestation
 * [FrequencyValue](FrequencyValue.md) - describes the frequency of occurrence of an event or condition
 * [OrganismAttribute](OrganismAttribute.md) - describes a characteristic of an organismal entity.
 * [SeverityValue](SeverityValue.md) - describes the severity of a phenotypic feature or disease
 * [SocioeconomicAttribute](SocioeconomicAttribute.md) - Attributes relating to a socioeconomic manifestation
 * [Zygosity](Zygosity.md)

## Referenced by class

 *  **[Entity](Entity.md)** *[has attribute](has_attribute.md)*  <sub>0..*</sub>  **[Attribute](Attribute.md)**
 *  **[OrganismalEntity](OrganismalEntity.md)** *[organismal entity➞has attribute](organismal_entity_has_attribute.md)*  <sub>0..*</sub>  **[Attribute](Attribute.md)**

## Attributes


### Own

 * [attribute➞name](attribute_name.md)  <sub>OPT</sub>
    * Description: The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.
    * range: [LabelType](types/LabelType.md)
 * [has attribute type](has_attribute_type.md)  <sub>REQ</sub>
    * Description: connects an attribute to a class that describes it
    * range: [OntologyClass](OntologyClass.md)
    * in subsets: (samples)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [NamedThing](NamedThing.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (samples)

### Inherited from entity:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for an entity. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>0..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
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

### Domain for slot:

 * [attribute➞name](attribute_name.md)  <sub>OPT</sub>
    * Description: The human-readable 'attribute name' can be set to a string which reflects its context of interpretation, e.g. SEPIO evidence/provenance/confidence annotation or it can default to the name associated with the 'has attribute type' slot ontology term.
    * range: [LabelType](types/LabelType.md)
 * [has attribute type](has_attribute_type.md)  <sub>REQ</sub>
    * Description: connects an attribute to a class that describes it
    * range: [OntologyClass](OntologyClass.md)
    * in subsets: (samples)
 * [has qualitative value](has_qualitative_value.md)  <sub>OPT</sub>
    * Description: connects an attribute to a value
    * range: [NamedThing](NamedThing.md)
    * in subsets: (samples)
 * [has quantitative value](has_quantitative_value.md)  <sub>0..*</sub>
    * Description: connects an attribute to a value
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (samples)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | samples |
| **Exact Mappings:** | | SIO:000614 |

