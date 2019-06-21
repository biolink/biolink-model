# Class: variant to population association


An association between a variant and a population, where the variant has particular frequency in the population

URI: [biolink:VariantToPopulationAssociation](https://w3id.org/biolink/vocab/VariantToPopulationAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[VariantToPopulationAssociation|has_count:integer%20%3F;has_total:integer%20%3F;has_quotient:double%20%3F;has_percentage:double%20%3F;id(i):identifier_type;relation(i):iri_type;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[VariantToPopulationAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[VariantToPopulationAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[VariantToPopulationAssociation],%20\[FrequencyValue]<frequency%20qualifier%200..1-%20\[VariantToPopulationAssociation],%20\[PopulationOfIndividualOrganisms]<object%201..1-%20\[VariantToPopulationAssociation],%20\[SequenceVariant]<subject%201..1-%20\[VariantToPopulationAssociation],%20\[VariantToPopulationAssociation]uses%20-.->\[VariantToThingAssociation],%20\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQuantifier],%20\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQualifierMixin],%20\[Association]^-\[VariantToPopulationAssociation])
## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Uses Mixins

 *  mixin: [VariantToThingAssociation](VariantToThingAssociation.md)
 *  mixin: [FrequencyQuantifier](FrequencyQuantifier.md)
 *  mixin: [FrequencyQualifierMixin](FrequencyQualifierMixin.md) - Qualifier for freqency type associations
## Referenced by class

## Attributes

### Own

 * [has count](variant_to_population_association_has_count.md)  <sub>OPT</sub>
    * range: [Integer](Integer.md)
 * [has quotient](variant_to_population_association_has_quotient.md)  <sub>OPT</sub>
    * range: [Double](Double.md)
 * [has total](variant_to_population_association_has_total.md)  <sub>OPT</sub>
    * range: [Integer](Integer.md)
 * [object](variant_to_population_association_object.md)  <sub>REQ</sub>
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)
 * [subject](variant_to_population_association_subject.md)  <sub>REQ</sub>
    * range: [SequenceVariant](SequenceVariant.md)
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
### Inherited from frequency qualifier mixin:

 * [frequency qualifier](frequency_qualifier.md)  <sub>OPT</sub>
    * Description: a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
    * range: [FrequencyValue](FrequencyValue.md)
### Inherited from frequency quantifier:

 * [has count](has_count.md)  <sub>OPT</sub>
    * Description: number of things with a particular property
    * range: [Integer](Integer.md)
    * inherited from: [FrequencyQuantifier](FrequencyQuantifier.md)
 * [has total](has_total.md)  <sub>OPT</sub>
    * Description: total number of things in a particular reference set
    * range: [Integer](Integer.md)
    * inherited from: [FrequencyQuantifier](FrequencyQuantifier.md)
 * [has quotient](has_quotient.md)  <sub>OPT</sub>
    * range: [Double](Double.md)
    * inherited from: [FrequencyQuantifier](FrequencyQuantifier.md)
 * [has percentage](has_percentage.md)  <sub>OPT</sub>
    * Description: equivalent to has quotient multiplied by 100
    * range: [Double](Double.md)
### Inherited from variant to population association:

 * [subject](variant_to_population_association_subject.md)  <sub>REQ</sub>
    * range: [SequenceVariant](SequenceVariant.md)
 * [object](variant_to_population_association_object.md)  <sub>REQ</sub>
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)
 * [has count](variant_to_population_association_has_count.md)  <sub>OPT</sub>
    * range: [Integer](Integer.md)
 * [has total](variant_to_population_association_has_total.md)  <sub>OPT</sub>
    * range: [Integer](Integer.md)
 * [has quotient](variant_to_population_association_has_quotient.md)  <sub>OPT</sub>
    * range: [Double](Double.md)
### Domain for slot:

 * [has count](variant_to_population_association_has_count.md)  <sub>OPT</sub>
    * range: [Integer](Integer.md)
 * [has quotient](variant_to_population_association_has_quotient.md)  <sub>OPT</sub>
    * range: [Double](Double.md)
 * [has total](variant_to_population_association_has_total.md)  <sub>OPT</sub>
    * range: [Integer](Integer.md)
 * [object](variant_to_population_association_object.md)  <sub>REQ</sub>
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md)
 * [subject](variant_to_population_association_subject.md)  <sub>REQ</sub>
    * range: [SequenceVariant](SequenceVariant.md)
