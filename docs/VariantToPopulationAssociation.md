# Class: variant to population association


An association between a variant and a population, where the variant has particular frequency in the population

URI: http://bioentity.io/vocab/VariantToPopulationAssociation

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[VariantToPopulationAssociation|frequency_qualifier:frequency_value%20%3F;has_count:string%20%3F;has_total:string%20%3F;has_quotient:string%20%3F;has_percentage:double%20%3F],%20\[VariantToPopulationAssociation]-%20frequency_qualifier%20%3F>\[FrequencyValue],%20\[VariantToPopulationAssociation]-%20subject>\[SequenceVariant],%20\[VariantToPopulationAssociation]-%20object>\[PopulationOfIndividualOrganisms],%20\[VariantToPopulationAssociation]uses%20-.->\[VariantToThingAssociation],%20\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQuantifier],%20)
## Mappings

## Inheritance

 *  is_a: [association](Association.md)
 *  mixin: [variant to thing association](VariantToThingAssociation.md)
 *  mixin: [frequency quantifier](FrequencyQuantifier.md)
## Children

## Used in

## Fields

 * _[frequency qualifier](frequency_qualifier.md)_
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * range: [frequency value](FrequencyValue.md)
    * inherited from: [association slot](association_slot.md)
 * _[has count](has_count.md)_
    * _number in object population that carry a particular allele, aka allele count_
    * range: string
    * Example: [4](4) 4 individuals in gnomad set
 * _[has total](has_total.md)_
    * _number all populations that carry a particular allele, aka allele number_
    * range: string
    * Example: [24014](24014) 24014 individuals in gnomad set
 * _[has quotient](has_quotient.md)_
    * _frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency_
    * range: string
    * Example: [0.0001666](0.0001666) None
 * _[has percentage](has_percentage.md)_
    * _equivalent to has quotient multiplied by 100_
    * range: double
    * inherited from: [aggregate statistic](aggregate_statistic.md)
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [sequence variant](SequenceVariant.md) [required]
    * Example: [NC_000017.11:g.43051071A>T](http://purl.obolibrary.org/obo/NC_000017.11_g.43051071A>T) 17:41203088 A/C in gnomad
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [population of individual organisms](PopulationOfIndividualOrganisms.md) [required]
    * Example: [ANCESTRO:0010](http://purl.obolibrary.org/obo/ANCESTRO_0010) African
    * inherited from: [object](object.md)
