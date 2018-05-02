---
layout: default
---

## frequency quantifier


None

URI: [http://bioentity.io/vocab/FrequencyQuantifier](http://bioentity.io/vocab/FrequencyQuantifier)


![img](http://yuml.me/diagram/nofunky/class/[relationship quantifier|]^-[frequency quantifier|has count;has total;has quotient;has percentage])
## Mappings


## Inheritance

 *  is_a: [relationship quantifier](RelationshipQuantifier.html)

## Children

 *  mixin: [variant to population association](VariantToPopulationAssociation.html)


## Fields

 * [has count](has_count.html)
    * _number of things with a particular property_
    * __range__: integer
    * __Local__
 * [has total](has_total.html)
    * _total number of things in a particular reference set_
    * __range__: integer
    * __Local__
 * [has quotient](has_quotient.html)
    * __range__: double
    * __Local__
 * [has percentage](has_percentage.html)
    * _equivalent to has quotient multiplied by 100_
    * __range__: double
    * __Local__
