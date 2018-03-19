---
layout: default
---

## gene to disease association


None

URI: [http://bioentity.io/vocab/GeneToDiseaseAssociation](http://bioentity.io/vocab/GeneToDiseaseAssociation)
## Mappings

 * [SIO:000983](http://semanticscience.org/resource/SIO_000983)

## Inheritance

 *  is_a: [association](Association.html)
 *  mixin: [entity to disease association](EntityToDiseaseAssociation.html)
 *  mixin: [gene to thing association](GeneToThingAssociation.html)

## Children

 *  child: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.html)
 *  child: [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.html)


## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _gene in which variation is correlated with the disease - may be protective or causative or associative, or as a model
  _
    * __range__: [gene or gene product](GeneOrGeneProduct.html) [required]
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _the relationship type by which a subject is connected to an object in an association_
    * __range__: [relationship type](RelationshipType.html) [required]
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _disease_
    * __range__: [disease](Disease.html) [required]
    * Example: [MONDO:0020066](http://purl.obolibrary.org/obo/MONDO_0020066) Ehlers-Danlos syndrome
    * inherited from: [association](Association.html)
 * [qualifiers](qualifiers.html)
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * __range__: [ontology class](OntologyClass.html)*
    * inherited from: [association](Association.html)
 * [publications](publications.html)
    * _connects an association to publications supporting the association_
    * __range__: [publication](Publication.html)*
    * inherited from: [association](Association.html)
 * [provided by](provided_by.html)
    * _connects an association to the agent (person, organization or group) that provided it_
    * __range__: [provider](Provider.html)
    * inherited from: [association](Association.html)
 * [id](id.html)
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [frequency qualifier](frequency_qualifier.html)
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * __range__: [frequency value](FrequencyValue.html)
    * inherited from: [entity to disease association](EntityToDiseaseAssociation.html)
 * [severity qualifier](severity_qualifier.html)
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * __range__: [severity value](SeverityValue.html)
    * inherited from: [entity to disease association](EntityToDiseaseAssociation.html)
 * [onset qualifier](onset_qualifier.html)
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * __range__: [onset](Onset.html)
    * inherited from: [entity to disease association](EntityToDiseaseAssociation.html)
