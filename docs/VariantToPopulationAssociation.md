---
parent: Classes
title: biolink:VariantToPopulationAssociation
grand_parent: Browse Biolink Model
---

# Type: VariantToPopulationAssociation


An association between a variant and a population, where the variant has particular frequency in the population

URI: [biolink:VariantToPopulationAssociation](https://w3id.org/biolink/vocab/VariantToPopulationAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[VariantToPopulationAssociation&#124;has_count:integer%20%3F;has_total:integer%20%3F;has_quotient:double%20%3F;relation(i):uriorcurie;id(i):nodeidentifier;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[VariantToPopulationAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[VariantToPopulationAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[VariantToPopulationAssociation],%20\[PopulationOfIndividualOrganisms]<object%201..1-%20\[VariantToPopulationAssociation],%20\[SequenceVariant]<subject%201..1-%20\[VariantToPopulationAssociation],%20\[VariantToPopulationAssociation]uses%20-.->\[VariantToThingAssociation],%20\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQuantifier],%20\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQualifierMixin],%20\[Association]^-\[VariantToPopulationAssociation])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Uses Mixins

 *  mixin: [VariantToThingAssociation](VariantToThingAssociation.md)
 *  mixin: [FrequencyQuantifier](FrequencyQuantifier.md)
 *  mixin: [FrequencyQualifierMixin](FrequencyQualifierMixin.md) - Qualifier for frequency type associations

## Referenced by class


## Attributes


### Own

 * [variant to population association➞has count](variant_to_population_association_has_count.md)  <sub>OPT</sub>
    * range: [Integer](types/Integer.md)
 * [variant to population association➞has quotient](variant_to_population_association_has_quotient.md)  <sub>OPT</sub>
    * range: [Double](types/Double.md)
 * [variant to population association➞has total](variant_to_population_association_has_total.md)  <sub>OPT</sub>
    * range: [Integer](types/Integer.md)
 * [variant to population association➞object](variant_to_population_association_object.md)  <sub>REQ</sub>
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)
 * [variant to population association➞subject](variant_to_population_association_subject.md)  <sub>REQ</sub>
    * range: [SequenceVariant](SequenceVariant.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Association](Association.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: [Association](Association.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Association](Association.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [Nodeidentifier](types/Nodeidentifier.md)
    * inherited from: [Association](Association.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
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

### Domain for slot:

 * [variant to population association➞has count](variant_to_population_association_has_count.md)  <sub>OPT</sub>
    * range: [Integer](types/Integer.md)
 * [variant to population association➞has quotient](variant_to_population_association_has_quotient.md)  <sub>OPT</sub>
    * range: [Double](types/Double.md)
 * [variant to population association➞has total](variant_to_population_association_has_total.md)  <sub>OPT</sub>
    * range: [Integer](types/Integer.md)
 * [variant to population association➞object](variant_to_population_association_object.md)  <sub>REQ</sub>
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)
 * [variant to population association➞subject](variant_to_population_association_subject.md)  <sub>REQ</sub>
    * range: [SequenceVariant](SequenceVariant.md)
