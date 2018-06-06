# Class: biological entity




URI: [http://bioentity.io/vocab/BiologicalEntity](http://bioentity.io/vocab/BiologicalEntity)

![img](images/BiologicalEntity.png)
## Mappings

 * [WD:Q28845870](http://purl.obolibrary.org/obo/WD_Q28845870)
## Inheritance

 *  is_a: [named thing](NamedThing.md) - a databased entity or concept/class
## Children

 *  child: [biological process or activity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities
 *  child: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
 *  child: [organismal entity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
 *  child: [environment](Environment.md) - A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
 *  child: [molecular entity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)
## Used in

 *  class: [biological entity](BiologicalEntity.md) references: [biological process or activity](BiologicalProcessOrActivity.md)
 *  class: [biological entity](BiologicalEntity.md) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 *  class: [biological entity](BiologicalEntity.md) references: [organismal entity](OrganismalEntity.md)
 *  class: [biological entity](BiologicalEntity.md) references: [environment](Environment.md)
 *  class: [biological entity](BiologicalEntity.md) references: [molecular entity](MolecularEntity.md)
## Fields

 * _[has phenotype](has_phenotype.md) *subsets: translator_minimal*_
    * _holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). _
    * range: [phenotype](Phenotype.md)
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
