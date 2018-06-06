# Class: variant to population association


An association between a variant and a population, where the variant has particular frequency in the population

URI: [http://bioentity.io/vocab/VariantToPopulationAssociation](http://bioentity.io/vocab/VariantToPopulationAssociation)

![img](images/VariantToPopulationAssociation.png)
## Mappings

## Inheritance

 *  is_a: [association](Association.md) - A typed association between two entities, supported by evidence
 *  mixin: [variant to thing association](VariantToThingAssociation.md)
 *  mixin: [frequency quantifier](FrequencyQuantifier.md)
## Children

## Used in

## Fields

 * _[frequency qualifier](frequency_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * range: [frequency value](FrequencyValue.md)
    * __Local__
 * _[has count](has_count.md)_
    * _number in object population that carry a particular allele, aka allele count_
    * range: string
    * Example: [4](4) 4 individuals in gnomad set
    * __Local__
 * _[has total](has_total.md)_
    * _number all populations that carry a particular allele, aka allele number_
    * range: string
    * Example: [24014](24014) 24014 individuals in gnomad set
    * __Local__
 * _[has quotient](has_quotient.md)_
    * _frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency_
    * range: string
    * Example: [0.0001666](0.0001666) None
    * __Local__
 * _[has percentage](has_percentage.md)_
    * _equivalent to has quotient multiplied by 100_
    * range: double
    * __Local__
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [sequence variant](SequenceVariant.md) [required]
    * Example: [NC_000017.11:g.43051071A>T](http://purl.obolibrary.org/obo/NC_000017.11_g.43051071A>T) 17:41203088 A/C in gnomad
    * __Local__
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [population of individual organisms](PopulationOfIndividualOrganisms.md) [required]
    * Example: [ANCESTRO:0010](http://purl.obolibrary.org/obo/ANCESTRO_0010) African
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
