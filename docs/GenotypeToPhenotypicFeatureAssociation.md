# Class: genotype to phenotypic feature association


Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment

URI: [biolink:GenotypeToPhenotypicFeatureAssociation](https://w3id.org/biolink/vocab/GenotypeToPhenotypicFeatureAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[GenotypeToPhenotypicFeatureAssociation|relation:iri_type;id(i):identifier_type;object(i):iri_type;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[GenotypeToPhenotypicFeatureAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[GenotypeToPhenotypicFeatureAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[GenotypeToPhenotypicFeatureAssociation],%20\[Onset]<onset%20qualifier%200..1-%20\[GenotypeToPhenotypicFeatureAssociation],%20\[SeverityValue]<severity%20qualifier%200..1-%20\[GenotypeToPhenotypicFeatureAssociation],%20\[FrequencyValue]<frequency%20qualifier%200..1-%20\[GenotypeToPhenotypicFeatureAssociation],%20\[BiologicalSex]<sex%20qualifier%200..1-%20\[GenotypeToPhenotypicFeatureAssociation],%20\[Genotype]<subject%201..1-%20\[GenotypeToPhenotypicFeatureAssociation],%20\[GenotypeToPhenotypicFeatureAssociation]uses%20-.->\[EntityToPhenotypicFeatureAssociation],%20\[GenotypeToPhenotypicFeatureAssociation]uses%20-.->\[GenotypeToThingAssociation],%20\[Association]^-\[GenotypeToPhenotypicFeatureAssociation])
## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Uses Mixins

 *  mixin: [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
 *  mixin: [GenotypeToThingAssociation](GenotypeToThingAssociation.md)
## Referenced by class

## Attributes

### Own

 * [relation](genotype_to_phenotypic_feature_association_relation.md)  <sub>REQ</sub>
    * range: [IriType](IriType.md)
 * [subject](genotype_to_phenotypic_feature_association_subject.md)  <sub>REQ</sub>
    * range: [Genotype](Genotype.md)
### Inherited from association:

 * [id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [Association](Association.md)
    * in subsets: (translator_minimal)
 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [IriType](IriType.md)
    * inherited from: [Association](Association.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [IriType](IriType.md)
    * inherited from: [Association](Association.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [IriType](IriType.md)
    * inherited from: [Association](Association.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](Boolean.md)
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
### Inherited from entity to feature or disease qualifiers:

 * [severity qualifier](severity_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)
 * [onset qualifier](onset_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)
### Inherited from entity to phenotypic feature association:

 * [object](entity_to_phenotypic_feature_association_object.md)  <sub>REQ</sub>
    * range: [PhenotypicFeature](PhenotypicFeature.md)
    * inherited from: [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
 * [sex qualifier](sex_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
    * range: [BiologicalSex](BiologicalSex.md)
### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)
### Inherited from genotype to phenotypic feature association:

 * [subject](genotype_to_phenotypic_feature_association_subject.md)  <sub>REQ</sub>
    * range: [Genotype](Genotype.md)
 * [relation](genotype_to_phenotypic_feature_association_relation.md)  <sub>REQ</sub>
    * range: [IriType](IriType.md)
### Domain for slot:

 * [relation](genotype_to_phenotypic_feature_association_relation.md)  <sub>REQ</sub>
    * range: [IriType](IriType.md)
 * [subject](genotype_to_phenotypic_feature_association_subject.md)  <sub>REQ</sub>
    * range: [Genotype](Genotype.md)
