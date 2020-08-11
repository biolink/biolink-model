---
parent: Classes
title: biolink:MaterialSampleDerivationAssociation
grand_parent: Browse Biolink Model
layout: default
---

# Type: MaterialSampleDerivationAssociation


An association between a material sample and the material entity it is derived from

URI: [biolink:MaterialSampleDerivationAssociation](https://w3id.org/biolink/vocab/MaterialSampleDerivationAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[OntologyClass],[NamedThing],[NamedThing]%3Cobject%201..1-%20[MaterialSampleDerivationAssociation|relation:uriorcurie;id(i):string;negated(i):boolean%20%3F],[MaterialSample]%3Csubject%201..1-%20[MaterialSampleDerivationAssociation],[Association]%5E-[MaterialSampleDerivationAssociation],[MaterialSample],[Association])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [material sample derivation association➞object](material_sample_derivation_association_object.md)  <sub>REQ</sub>
    * Description: the material entity the sample was derived from. This may be another material sample, or any other material entity, including for example an organism, a geographic feature, or some environmental material.
    * range: [NamedThing](NamedThing.md)
 * [material sample derivation association➞relation](material_sample_derivation_association_relation.md)  <sub>REQ</sub>
    * Description: derivation relationship
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [material sample derivation association➞subject](material_sample_derivation_association_subject.md)  <sub>REQ</sub>
    * Description: the material sample being described
    * range: [MaterialSample](MaterialSample.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)

### Domain for slot:

 * [material sample derivation association➞object](material_sample_derivation_association_object.md)  <sub>REQ</sub>
    * Description: the material entity the sample was derived from. This may be another material sample, or any other material entity, including for example an organism, a geographic feature, or some environmental material.
    * range: [NamedThing](NamedThing.md)
 * [material sample derivation association➞relation](material_sample_derivation_association_relation.md)  <sub>REQ</sub>
    * Description: derivation relationship
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [material sample derivation association➞subject](material_sample_derivation_association_subject.md)  <sub>REQ</sub>
    * Description: the material sample being described
    * range: [MaterialSample](MaterialSample.md)
