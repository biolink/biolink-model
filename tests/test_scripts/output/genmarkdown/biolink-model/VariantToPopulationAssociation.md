# Class: variant to population association


An association between a variant and a population, where the variant has particular frequency in the population

URI: [http://bioentity.io/vocab/VariantToPopulationAssociation](http://bioentity.io/vocab/VariantToPopulationAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[VariantToPopulationAssociation|has_quotient:string%20%3F;has_count:string%20%3F;has_total:string%20%3F;id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F;has_percentage(i):double%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[VariantToPopulationAssociation]-%20publications(i)%20*>\[Publication],%20\[VariantToPopulationAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[VariantToPopulationAssociation]-%20relation(i)>\[RelationshipType],%20\[VariantToPopulationAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[VariantToPopulationAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[VariantToPopulationAssociation]-%20object>\[PopulationOfIndividualOrganisms],%20\[VariantToPopulationAssociation]-%20subject>\[SequenceVariant],%20\[VariantToPopulationAssociation]uses%20-.->\[VariantToThingAssociation],%20\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQuantifier],%20\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQualifier],%20\[Association]^-\[VariantToPopulationAssociation])
## Mappings

## Inheritance

 *  is_a: association
 *  mixin: variant to thing association
 *  mixin: frequency quantifier
 *  mixin: frequency qualifier
## Children

## Used in

## Fields

 * _variant to population association has count_
    * _number in object population that carry a particular allele, aka allele count_
    * range: **string**
    * __Local__
 * _variant to population association has quotient_
    * _frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency_
    * range: **string**
    * __Local__
 * _variant to population association has total_
    * _number all populations that carry a particular allele, aka allele number_
    * range: **string**
    * __Local__
 * _variant to population association object_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: population of individual organisms [required]
    * __Local__
 * _variant to population association subject_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: sequence variant [required]
    * __Local__
 * _association slot_
    * _any slot that relates an association to another entity_
    * range: **string**
    * inherited from: association
 * _association type_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: ontology class
    * inherited from: association
 * _category_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: label type
    * inherited from: named thing
 * _description_
    * _a human-readable description of a thing_
    * range: narrative text
    * inherited from: named thing
 * _full name_
    * _a long-form human readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _has percentage_
    * _equivalent to has quotient multiplied by 100_
    * range: **double**
    * inherited from: frequency quantifier
 * _id_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: identifier type
    * inherited from: named thing
 * _iri_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: iri type
    * inherited from: named thing
 * _name_
    * _A human-readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _negated_
    * _if set to true, then the association is negated i.e. is not true_
    * range: **boolean**
    * inherited from: association
 * _node property_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * inherited from: named thing
 * _provided by_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: provider
    * inherited from: association
 * _publications_
    * _connects an association to publications supporting the association_
    * range: publication*
    * inherited from: association
 * _qualifiers_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: ontology class*
    * inherited from: association
 * _related to_
    * _A grouping for any relationship type that holds between any two things_
    * range: named thing
    * inherited from: named thing
 * _relation_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: relationship type [required]
    * inherited from: association
 * _systematic synonym_
    * _more commonly used for gene symbols in yeast_
    * range: label type
    * inherited from: named thing
