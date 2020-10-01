
# Type: frequency quantifier




URI: [biolink:FrequencyQuantifier](https://w3id.org/biolink/vocab/FrequencyQuantifier)


![img](images/FrequencyQuantifier.svg)

## Parents

 *  is_a: [RelationshipQuantifier](RelationshipQuantifier.md)

## Mixin for

 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) (mixin)  - An association between a variant and a population, where the variant has particular frequency in the population

## Referenced by class


## Attributes


### Own

 * [has count](has_count.md)  <sub>OPT</sub>
    * Description: number of things with a particular property
    * range: [Integer](types/Integer.md)
 * [has percentage](has_percentage.md)  <sub>OPT</sub>
    * Description: equivalent to has quotient multiplied by 100
    * range: [Double](types/Double.md)
 * [has quotient](has_quotient.md)  <sub>OPT</sub>
    * range: [Double](types/Double.md)
 * [has total](has_total.md)  <sub>OPT</sub>
    * Description: total number of things in a particular reference set
    * range: [Integer](types/Integer.md)
