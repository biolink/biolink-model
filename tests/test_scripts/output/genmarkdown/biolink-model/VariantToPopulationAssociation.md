# Class: variant to population association


An association between a variant and a population, where the variant has particular frequency in the population

URI: [http://bioentity.io/vocab/VariantToPopulationAssociation](http://bioentity.io/vocab/VariantToPopulationAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[VariantToPopulationAssociation|has_quotient:double%20%3F;has_count:integer%20%3F;has_total:integer%20%3F;id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F;has_percentage(i):double%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[VariantToPopulationAssociation]-%20publications(i)%20*>\[Publication],%20\[VariantToPopulationAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[VariantToPopulationAssociation]-%20relation(i)>\[RelationshipType],%20\[VariantToPopulationAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[VariantToPopulationAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[VariantToPopulationAssociation]-%20object>\[PopulationOfIndividualOrganisms],%20\[VariantToPopulationAssociation]-%20subject>\[SequenceVariant],%20\[VariantToPopulationAssociation]uses%20-.->\[VariantToThingAssociation],%20\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQuantifier],%20\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQualifier],%20\[Association]^-\[VariantToPopulationAssociation])
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
 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [has percentage](has_percentage.md)
    * Description: equivalent to has quotient multiplied by 100
    * range: **double**
    * inherited from: [FrequencyQuantifier](FrequencyQuantifier.md)
 * [id](id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [iri](iri.md) *subsets*: (translator_minimal)
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [name](name.md) *subsets*: (translator_minimal)
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * inherited from: [Association](Association.md)
 * [node property](node_property.md)
    * Description: A grouping for any property that holds between a node and a value
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
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
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [relation](relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [RelationshipType](RelationshipType.md) [required]
    * inherited from: [Association](Association.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
