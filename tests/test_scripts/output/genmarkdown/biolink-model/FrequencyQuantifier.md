# Class: frequency quantifier




URI: [http://bioentity.io/vocab/FrequencyQuantifier](http://bioentity.io/vocab/FrequencyQuantifier)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQuantifier|has_count:integer%20%3F;has_total:integer%20%3F;has_quotient:double%20%3F;has_percentage:double%20%3F],%20\[RelationshipQuantifier]^-\[FrequencyQuantifier])
## Mappings

## Inheritance

 *  is_a: relationship quantifier
## Children

 * variant to population association
## Used in

## Fields

 * _has count_
    * _number of things with a particular property_
    * range: **integer**
    * __Local__
 * _has percentage_
    * _equivalent to has quotient multiplied by 100_
    * range: **double**
    * __Local__
 * _has quotient_
    * _A grouping for any property that holds between a node and a value_
    * range: **double**
    * __Local__
 * _has total_
    * _total number of things in a particular reference set_
    * range: **integer**
    * __Local__
