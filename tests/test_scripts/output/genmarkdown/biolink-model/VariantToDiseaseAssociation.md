# Class: variant to disease association




URI: [http://w3id.org/biolink/vocab/VariantToDiseaseAssociation](http://w3id.org/biolink/vocab/VariantToDiseaseAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[VariantToDiseaseAssociation|subject:iri_type;relation:iri_type;object:iri_type;id(i):identifier_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20onset%20qualifier(i)%20%3F>\[Onset],%20\[VariantToDiseaseAssociation]-%20severity%20qualifier(i)%20%3F>\[SeverityValue],%20\[VariantToDiseaseAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[VariantToDiseaseAssociation]-%20publications(i)%20*>\[Publication],%20\[VariantToDiseaseAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[VariantToDiseaseAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[VariantToDiseaseAssociation]uses%20-.->\[VariantToThingAssociation],%20\[VariantToDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[Association]^-\[VariantToDiseaseAssociation])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
 *  mixin: [VariantToThingAssociation](VariantToThingAssociation.md)
 *  mixin: [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) - mixin class for any association whose object (target node) is a disease
## Children

## Used in

## Fields

 * [variant to disease association.object](variant_to_disease_association_object.md)
    * Description: a disease that is associated with that variant
    * range: [IriType](IriType.md) [required]
    * __Local__
 * [variant to disease association.relation](variant_to_disease_association_relation.md)
    * Description: E.g. is pathogenic for
    * range: [IriType](IriType.md) [required]
    * __Local__
 * [variant to disease association.subject](variant_to_disease_association_subject.md)
    * Description: a sequence variant in which the allele state is associated in some way with the disease state
    * range: [IriType](IriType.md) [required]
    * __Local__
 * [association slot](association_slot.md)
    * Description: any slot that relates an association to another entity
    * range: **string**
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [association.id](association_id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [Association](Association.md)
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * inherited from: [Association](Association.md)
 * [onset qualifier](onset_qualifier.md)
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)
    * inherited from: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md)
 * [provided by](provided_by.md)
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)*
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)*
    * inherited from: [Association](Association.md)
 * [severity qualifier](severity_qualifier.md)
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)
    * inherited from: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md)
