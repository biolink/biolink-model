# Class: variant to population association


An association between a variant and a population, where the variant has particular frequency in the population

URI: [http://w3id.org/biolink/vocab/VariantToPopulationAssociation](http://w3id.org/biolink/vocab/VariantToPopulationAssociation)

![img](images/VariantToPopulationAssociation.png)
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
 *  mixin: [VariantToThingAssociation](VariantToThingAssociation.md)
 *  mixin: [FrequencyQuantifier](FrequencyQuantifier.md)
 *  mixin: [FrequencyQualifier](FrequencyQualifier.md) - Qualifier for freqency type associations
## Children

## Used in

## Fields

 * [variant to population association.has count](variant_to_population_association_has_count.md)
    * Description: number in object population that carry a particular allele, aka allele count
    * range: **integer**
    * __Local__
 * [variant to population association.has quotient](variant_to_population_association_has_quotient.md)
    * Description: frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency
    * range: **double**
    * __Local__
 * [variant to population association.has total](variant_to_population_association_has_total.md)
    * Description: number all populations that carry a particular allele, aka allele number
    * range: **integer**
    * __Local__
 * [variant to population association.object](variant_to_population_association_object.md)
    * Description: the population that is observed to have the frequency
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) [required]
    * __Local__
 * [variant to population association.subject](variant_to_population_association_subject.md)
    * Description: an allele that has a certain frequency in a given population
    * range: [SequenceVariant](SequenceVariant.md) [required]
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
 * [has percentage](has_percentage.md)
    * Description: equivalent to has quotient multiplied by 100
    * range: **double**
    * inherited from: [FrequencyQuantifier](FrequencyQuantifier.md)
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * inherited from: [Association](Association.md)
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
    * range: [IriType](IriType.md) [required]
    * inherited from: [Association](Association.md)
