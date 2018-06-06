# Class: gene as a model of disease association




URI: [http://bioentity.io/vocab/GeneAsAModelOfDiseaseAssociation](http://bioentity.io/vocab/GeneAsAModelOfDiseaseAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneToDiseaseAssociation]^-\[GeneAsAModelOfDiseaseAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;object(i):string;association_slot(i):string%20%3F;frequency_qualifier:frequency_value%20%3F],%20\[GeneAsAModelOfDiseaseAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[GeneAsAModelOfDiseaseAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GeneAsAModelOfDiseaseAssociation]-%20relation(i)>\[RelationshipType],%20\[GeneAsAModelOfDiseaseAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GeneAsAModelOfDiseaseAssociation]-%20publications(i)%20*>\[Publication],%20\[GeneAsAModelOfDiseaseAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[GeneAsAModelOfDiseaseAssociation]-%20frequency%20qualifier%20%3F>\[FrequencyValue],%20\[GeneAsAModelOfDiseaseAssociation]-%20severity%20qualifier%20%3F>\[SeverityValue],%20\[GeneAsAModelOfDiseaseAssociation]-%20onset%20qualifier%20%3F>\[Onset],%20\[GeneAsAModelOfDiseaseAssociation]-%20subject>\[GeneOrGeneProduct],%20\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[ModelToDiseaseMixin],%20\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation])
## Mappings

## Inheritance

 *  is_a: [gene to disease association](GeneToDiseaseAssociation.md)
 *  mixin: [model to disease mixin](ModelToDiseaseMixin.md) - This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease
 *  mixin: [entity to disease association](EntityToDiseaseAssociation.md) - mixin class for any association whose object (target node) is a disease
## Children

## Used in

## Fields

 * _[frequency qualifier](frequency_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * range: [frequency value](FrequencyValue.md)
    * __Local__
 * _[severity qualifier](severity_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * range: [severity value](SeverityValue.md)
    * __Local__
 * _[onset qualifier](onset_qualifier.md)_
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * range: [onset](Onset.md)
    * __Local__
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene or gene product](GeneOrGeneProduct.md) [required]
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[association type](association_type.md)_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: [ontology class](OntologyClass.md)
    * inherited from: None
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * inherited from: None
 * _[qualifiers](qualifiers.md)_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: [ontology class](OntologyClass.md)*
    * inherited from: None
 * _[publications](publications.md)_
    * _connects an association to publications supporting the association_
    * range: [publication](Publication.md)*
    * inherited from: None
 * _[provided by](provided_by.md)_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: [provider](Provider.md)
    * inherited from: None
