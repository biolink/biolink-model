# Class: frequency quantifier




URI: [http://bioentity.io/vocab/FrequencyQuantifier](http://bioentity.io/vocab/FrequencyQuantifier)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQuantifier|has_count:integer%20%3F;has_total:integer%20%3F;has_quotient:double%20%3F;has_percentage:double%20%3F],%20\[RelationshipQuantifier]^-\[FrequencyQuantifier])
## Mappings

## Inheritance

 *  is_a: [RelationshipQuantifier](RelationshipQuantifier.md)
## Children

 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) (mixin)  - An association between a variant and a population, where the variant has particular frequency in the population
## Used in

## Fields

 * _[has count](has_count.md)_
    * _number of things with a particular property_
    * range: **integer**
    * __Local__
 * _[has percentage](has_percentage.md)_
    * _equivalent to has quotient multiplied by 100_
    * range: **double**
    * __Local__
 * _[has quotient](has_quotient.md)_
    * _A grouping for any property that holds between a node and a value_
    * range: **double**
    * __Local__
 * _[has total](has_total.md)_
    * _total number of things in a particular reference set_
    * range: **integer**
    * __Local__
