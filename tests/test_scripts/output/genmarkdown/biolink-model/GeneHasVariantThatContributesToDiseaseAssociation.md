# Class: gene has variant that contributes to disease association




URI: [http://bioentity.io/vocab/GeneHasVariantThatContributesToDiseaseAssociation](http://bioentity.io/vocab/GeneHasVariantThatContributesToDiseaseAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneToDiseaseAssociation]^-\[GeneHasVariantThatContributesToDiseaseAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;object(i):string;association_slot(i):string%20%3F;frequency_qualifier(i):frequency_value%20%3F],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20relation(i)>\[RelationshipType],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20publications(i)%20*>\[Publication],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20frequency%20qualifier(i)%20%3F>\[FrequencyValue],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20severity%20qualifier(i)%20%3F>\[SeverityValue],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20onset%20qualifier(i)%20%3F>\[Onset],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20sequence%20variant%20qualifier%20%3F>\[SequenceVariant],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20subject>\[GeneOrGeneProduct])
## Mappings

## Inheritance

 *  is_a: [gene to disease association](GeneToDiseaseAssociation.md)
## Children

## Used in

## Fields

 * _[sequence variant qualifier](sequence_variant_qualifier.md)_
    * _a qualifier used in an association where the variant_
    * range: [sequence variant](SequenceVariant.md)
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
 * _[frequency qualifier](frequency_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * range: [frequency value](FrequencyValue.md)
    * inherited from: None
 * _[severity qualifier](severity_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * range: [severity value](SeverityValue.md)
    * inherited from: None
 * _[onset qualifier](onset_qualifier.md)_
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * range: [onset](Onset.md)
    * inherited from: None
