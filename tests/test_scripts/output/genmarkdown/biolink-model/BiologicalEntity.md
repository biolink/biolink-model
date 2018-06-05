# Class: biological entity




URI: http://bioentity.io/vocab/BiologicalEntity

![img](http://yuml.me/diagram/nofunky/class/\[NamedThing]^-\[BiologicalEntity|has_phenotype:phenotype%20%3F],%20\[BiologicalEntity]^-\[BiologicalProcessOrActivity],%20\[BiologicalEntity]^-\[DiseaseOrPhenotypicFeature],%20\[BiologicalEntity]^-\[Environment],%20\[BiologicalEntity]^-\[MolecularEntity],%20\[BiologicalEntity]^-\[OrganismalEntity],%20)
## Mappings

 * [WD:Q28845870](http://purl.obolibrary.org/obo/WD_Q28845870)
## Inheritance

 *  is_a: [named thing](NamedThing.md)
## Children

 *  child: [biological process or activity](BiologicalProcessOrActivity.md)
 *  child: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 *  child: [molecular entity](MolecularEntity.md)
 *  child: [environment](Environment.md)
 *  child: [organismal entity](OrganismalEntity.md)
## Used in

 *  class: [biological entity](BiologicalEntity.md) references: [biological process or activity](BiologicalProcessOrActivity.md)
 *  class: [biological entity](BiologicalEntity.md) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 *  class: [biological entity](BiologicalEntity.md) references: [molecular entity](MolecularEntity.md)
 *  class: [biological entity](BiologicalEntity.md) references: [environment](Environment.md)
 *  class: [biological entity](BiologicalEntity.md) references: [organismal entity](OrganismalEntity.md)
## Fields

 * _[has phenotype](has_phenotype.md) *subsets: translator_minimal*_
    * _holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). _
    * range: [phenotype](Phenotype.md)
    * inherited from: [related to](related_to.md)
