---
parent: Classes
title: biolink:SequenceVariantModulatesTreatmentAssociation
grand_parent: Browse Biolink Model
---

# Type: SequenceVariantModulatesTreatmentAssociation


An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.

URI: [biolink:SequenceVariantModulatesTreatmentAssociation](https://w3id.org/biolink/vocab/SequenceVariantModulatesTreatmentAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[SequenceVariantModulatesTreatmentAssociation&#124;relation(i):uriorcurie;id(i):nodeidentifier;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[SequenceVariantModulatesTreatmentAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[SequenceVariantModulatesTreatmentAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[SequenceVariantModulatesTreatmentAssociation],%20\[Treatment]<object%201..1-%20\[SequenceVariantModulatesTreatmentAssociation],%20\[SequenceVariant]<subject%201..1-%20\[SequenceVariantModulatesTreatmentAssociation],%20\[Association]^-\[SequenceVariantModulatesTreatmentAssociation])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [sequence variant modulates treatment association➞object](sequence_variant_modulates_treatment_association_object.md)  <sub>REQ</sub>
    * range: [Treatment](Treatment.md)
 * [sequence variant modulates treatment association➞subject](sequence_variant_modulates_treatment_association_subject.md)  <sub>REQ</sub>
    * range: [SequenceVariant](SequenceVariant.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Association](Association.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: [Association](Association.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Association](Association.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [Nodeidentifier](types/Nodeidentifier.md)
    * inherited from: [Association](Association.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
    * inherited from: [Association](Association.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)

### Domain for slot:

 * [sequence variant modulates treatment association➞object](sequence_variant_modulates_treatment_association_object.md)  <sub>REQ</sub>
    * range: [Treatment](Treatment.md)
 * [sequence variant modulates treatment association➞subject](sequence_variant_modulates_treatment_association_subject.md)  <sub>REQ</sub>
    * range: [SequenceVariant](SequenceVariant.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | An alternate way to model the same information could be via a qualifier |

