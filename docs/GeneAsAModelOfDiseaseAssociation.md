---
parent: Classes
title: biolink:GeneAsAModelOfDiseaseAssociation
grand_parent: Browse Biolink Model
---

# Type: GeneAsAModelOfDiseaseAssociation




URI: [biolink:GeneAsAModelOfDiseaseAssociation](https://w3id.org/biolink/vocab/GeneAsAModelOfDiseaseAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[GeneAsAModelOfDiseaseAssociation&#124;relation(i):uriorcurie;id(i):nodeidentifier;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[GeneAsAModelOfDiseaseAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[GeneAsAModelOfDiseaseAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[GeneAsAModelOfDiseaseAssociation],%20\[NamedThing]<object(i)%201..1-%20\[GeneAsAModelOfDiseaseAssociation],%20\[GeneOrGeneProduct]<subject%201..1-%20\[GeneAsAModelOfDiseaseAssociation],%20\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[ModelToDiseaseMixin],%20\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[GeneToDiseaseAssociation]^-\[GeneAsAModelOfDiseaseAssociation])

---


## Parents

 *  is_a: [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)

## Uses Mixins

 *  mixin: [ModelToDiseaseMixin](ModelToDiseaseMixin.md) - This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease
 *  mixin: [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) - mixin class for any association whose object (target node) is a disease

## Referenced by class


## Attributes


### Own

 * [gene as a model of disease association➞subject](gene_as_a_model_of_disease_association_subject.md)  <sub>REQ</sub>
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)

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

 * [gene as a model of disease association➞subject](gene_as_a_model_of_disease_association_subject.md)  <sub>REQ</sub>
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
