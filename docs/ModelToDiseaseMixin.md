---
parent: Mixins
title: biolink:ModelToDiseaseMixin
grand_parent: Browse Biolink Model
---

# Type: ModelToDiseaseMixin


This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease

URI: [biolink:ModelToDiseaseMixin](https://w3id.org/biolink/vocab/ModelToDiseaseMixin)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[ModelToDiseaseMixin])

---


## Mixin for

 * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) (mixin) 

## Referenced by class


## Attributes


### Domain for slot:

 * [model to disease mixin➞relation](model_to_disease_mixin_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [model to disease mixin➞subject](model_to_disease_mixin_subject.md)  <sub>REQ</sub>
    * range: [NamedThing](NamedThing.md)
