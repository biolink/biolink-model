---
parent: Classes
title: biolink:SequenceVariantModulatesTreatmentAssociation
grand_parent: Browse Biolink Model
layout: default
---

# Type: SequenceVariantModulatesTreatmentAssociation


An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.

URI: [biolink:SequenceVariantModulatesTreatmentAssociation](https://w3id.org/biolink/vocab/SequenceVariantModulatesTreatmentAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Treatment],[Treatment]%3Cobject%201..1-%20[SequenceVariantModulatesTreatmentAssociation%7Crelation(i):uriorcurie;id(i):string;negated(i):boolean%20%3F],[SequenceVariant]%3Csubject%201..1-%20[SequenceVariantModulatesTreatmentAssociation],[Association]%5E-[SequenceVariantModulatesTreatmentAssociation],[SequenceVariant],[Publication],[Provider],[OntologyClass],[Association])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [sequence variant modulates treatment association➞object](sequence_variant_modulates_treatment_association_object.md)  <sub>REQ</sub>
    * Description: treatment whose efficacy is modulated by the subject variant
    * range: [Treatment](Treatment.md)
 * [sequence variant modulates treatment association➞subject](sequence_variant_modulates_treatment_association_subject.md)  <sub>REQ</sub>
    * Description: variant that modulates the treatment of some disease
    * range: [SequenceVariant](SequenceVariant.md)

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

 * [sequence variant modulates treatment association➞object](sequence_variant_modulates_treatment_association_object.md)  <sub>REQ</sub>
    * Description: treatment whose efficacy is modulated by the subject variant
    * range: [Treatment](Treatment.md)
 * [sequence variant modulates treatment association➞subject](sequence_variant_modulates_treatment_association_subject.md)  <sub>REQ</sub>
    * Description: variant that modulates the treatment of some disease
    * range: [SequenceVariant](SequenceVariant.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | An alternate way to model the same information could be via a qualifier |

