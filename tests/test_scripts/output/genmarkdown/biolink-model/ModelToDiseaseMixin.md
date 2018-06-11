# Class: model to disease mixin


This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease

URI: [http://bioentity.io/vocab/ModelToDiseaseMixin](http://bioentity.io/vocab/ModelToDiseaseMixin)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[ModelToDiseaseMixin|subject:string%20%3F;relation:string%20%3F])
## Mappings

## Inheritance

## Children

 * gene as a model of disease association
## Used in

## Fields

 * _model to disease mixin relation_
    * _The relationship to the disease
  _
    * range: **string**
    * edge label: model of
    * __Local__
 * _model to disease mixin subject_
    * _The entity that serves as the model of the disease. This may be an organism, a strain of organism, a genotype or variant that exhibits similar features, or a gene that when mutated exhibits features of the disease_
    * range: **string**
    * __Local__
