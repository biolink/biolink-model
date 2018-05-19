---
layout: default
---

## variant to population association


An association between a variant and a population, where the variant has particular frequency in the population

URI: [http://bioentity.io/vocab/VariantToPopulationAssociation](http://bioentity.io/vocab/VariantToPopulationAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[variant to population association|frequency qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;has count;has total;has quotient;has percentage], [variant to population association|frequency qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;has count;has total;has quotient;has percentage]-frequency qualifier >[frequency value|], [attribute|]^-[frequency value|], [variant to population association|frequency qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;has count;has total;has quotient;has percentage]-association type >[ontology class|], [variant to population association|frequency qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;has count;has total;has quotient;has percentage]-subject >[sequence variant|has gene], [genomic entity|has biological sequence]^-[sequence variant|has gene], [sequence variant|has gene]-has gene >[gene|], [gene or gene product|]^-[gene|], [gene|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [sequence variant|has gene]-in taxon >[organism taxon|], [variant to population association|frequency qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;has count;has total;has quotient;has percentage]-relation >[relationship type|], [variant to population association|frequency qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;has count;has total;has quotient;has percentage]-object >[population of individual organisms|in taxon], [organismal entity|]^-[population of individual organisms|in taxon], [population of individual organisms|in taxon]-in taxon >[organism taxon|], [variant to population association|frequency qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;has count;has total;has quotient;has percentage]-qualifiers >[ontology class|], [variant to population association|frequency qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;has count;has total;has quotient;has percentage]-publications >[publication|], [information content entity|]^-[publication|], [variant to population association|frequency qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;has count;has total;has quotient;has percentage]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings


## Inheritance

 *  is_a: [association](Association.html)
 *  mixin: [variant to thing association](VariantToThingAssociation.html)
 *  mixin: [frequency quantifier](FrequencyQuantifier.html)

## Children



## Fields

 * [frequency qualifier](frequency_qualifier.html)
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * __range__: [frequency value](FrequencyValue.html)
    * __Local__
 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _an allele that has a certain frequency in a given population_
    * __range__: [sequence variant](SequenceVariant.html) [required]
    * Example: [NC_000017.11:g.43051071A>T](http://purl.obolibrary.org/obo/NC_000017.11_g.43051071A>T) 17:41203088 A/C in gnomad
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _the relationship type by which a subject is connected to an object in an association_
    * __range__: [relationship type](RelationshipType.html) [required]
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _the population that is observed to have the frequency_
    * __range__: [population of individual organisms](PopulationOfIndividualOrganisms.html) [required]
    * Example: [ANCESTRO:0010](http://purl.obolibrary.org/obo/ANCESTRO_0010) African
    * inherited from: [association](Association.html)
 * [qualifiers](qualifiers.html)
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * __range__: [ontology class](OntologyClass.html)*
    * inherited from: [association](Association.html)
 * [publications](publications.html)
    * _connects an association to publications supporting the association_
    * __range__: [publication](Publication.html)*
    * inherited from: [association](Association.html)
 * [provided by](provided_by.html)
    * _connects an association to the agent (person, organization or group) that provided it_
    * __range__: [provider](Provider.html)
    * inherited from: [association](Association.html)
 * [id](id.html) *subsets: translator_minimal*
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html) *subsets: translator_minimal*
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html) *subsets: translator_minimal*
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [has count](has_count.html)
    * _number in object population that carry a particular allele, aka allele count_
    * __range__: integer
    * Example: [4](4) 4 individuals in gnomad set
    * inherited from: [frequency quantifier](FrequencyQuantifier.html)
 * [has total](has_total.html)
    * _number all populations that carry a particular allele, aka allele number_
    * __range__: integer
    * Example: [24014](24014) 24014 individuals in gnomad set
    * inherited from: [frequency quantifier](FrequencyQuantifier.html)
 * [has quotient](has_quotient.html)
    * _frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency_
    * __range__: double
    * Example: [0.0001666](0.0001666) None
    * inherited from: [frequency quantifier](FrequencyQuantifier.html)
 * [has percentage](has_percentage.html)
    * _equivalent to has quotient multiplied by 100_
    * __range__: double
    * inherited from: [frequency quantifier](FrequencyQuantifier.html)
