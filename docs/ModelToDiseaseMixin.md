# Class: model to disease mixin


This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease

URI: [http://bioentity.io/vocab/ModelToDiseaseMixin](http://bioentity.io/vocab/ModelToDiseaseMixin)

![img](images/ModelToDiseaseMixin.png)
## Mappings

## Inheritance

## Children

 * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) (mixin) 
## Used in

## Fields

 * _[relation](relation.md)_
    * _The relationship to the disease
  _
    * range: **string**
    * edge label: [model of](model_of.md) *subsets*: (translator_minimal)
    * __Local__
 * _[subject](subject.md)_
    * _The entity that serves as the model of the disease. This may be an organism, a strain of organism, a genotype or variant that exhibits similar features, or a gene that when mutated exhibits features of the disease_
    * range: **string**
    * __Local__
