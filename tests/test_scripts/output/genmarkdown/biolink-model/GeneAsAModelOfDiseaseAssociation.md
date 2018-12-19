# Class: gene as a model of disease association




URI: [http://w3id.org/biolink/vocab/GeneAsAModelOfDiseaseAssociation](http://w3id.org/biolink/vocab/GeneAsAModelOfDiseaseAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneAsAModelOfDiseaseAssociation|id(i):identifier_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[GeneAsAModelOfDiseaseAssociation]-%20publications(i)%20*>\[Publication],%20\[GeneAsAModelOfDiseaseAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GeneAsAModelOfDiseaseAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GeneAsAModelOfDiseaseAssociation]-%20object(i)>\[Disease],%20\[GeneAsAModelOfDiseaseAssociation]-%20onset%20qualifier(i)%20%3F>\[Onset],%20\[GeneAsAModelOfDiseaseAssociation]-%20severity%20qualifier(i)%20%3F>\[SeverityValue],%20\[GeneAsAModelOfDiseaseAssociation]-%20relation(i)>\[RelationshipType],%20\[GeneAsAModelOfDiseaseAssociation]-%20subject>\[GeneOrGeneProduct],%20\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[ModelToDiseaseMixin],%20\[GeneAsAModelOfDiseaseAssociation]uses%20-.->\[EntityToDiseaseAssociation],%20\[GeneToDiseaseAssociation]^-\[GeneAsAModelOfDiseaseAssociation])
## Mappings

## Inheritance

 *  is_a: [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)
 *  mixin: [ModelToDiseaseMixin](ModelToDiseaseMixin.md) - This mixin is used for any association class for which the subject (source node) plays the role of a 'model', in that it recapitulates some features of the disease in a way that is useful for studying the disease outside a patient carrying the disease
 *  mixin: [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) - mixin class for any association whose object (target node) is a disease
## Children

## Used in

## Fields

 * [gene as a model of disease association.subject](gene_as_a_model_of_disease_association_subject.md)
    * Description: A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.
  
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md) [required]
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
 * [object](object.md)
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: **string** [required]
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
 * [relation](relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [RelationshipType](RelationshipType.md) [required]
    * inherited from: [Association](Association.md)
 * [severity qualifier](severity_qualifier.md)
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)
    * inherited from: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md)
