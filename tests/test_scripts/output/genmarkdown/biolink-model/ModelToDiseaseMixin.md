# Class: model to disease mixin


This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease

URI: [http://w3id.org/biolink/vocab/ModelToDiseaseMixin](http://w3id.org/biolink/vocab/ModelToDiseaseMixin)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[ModelToDiseaseMixin|subject:iri_type;relation:iri_type])
## Mappings

## Inheritance

## Children

 * [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) (mixin) 
## Used in

## Fields

 * [model to disease mixin.relation](model_to_disease_mixin_relation.md)
    * Description: The relationship to the disease
  
    * range: [IriType](IriType.md) [required]
    * edge label: [model of](model_of.md) *subsets*: (translator_minimal)
    * __Local__
 * [model to disease mixin.subject](model_to_disease_mixin_subject.md)
    * Description: The entity that serves as the model of the disease. This may be an organism, a strain of organism, a genotype or variant that exhibits similar features, or a gene that when mutated exhibits features of the disease
    * range: [IriType](IriType.md) [required]
    * __Local__
