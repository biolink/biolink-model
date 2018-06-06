# Class: organismal entity


A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

URI: [http://bioentity.io/vocab/OrganismalEntity](http://bioentity.io/vocab/OrganismalEntity)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[BiologicalEntity]^-\[OrganismalEntity|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F],%20\[OrganismalEntity]^-\[AnatomicalEntity],%20\[OrganismalEntity]^-\[Biosample],%20\[OrganismalEntity]^-\[IndividualOrganism],%20\[OrganismalEntity]^-\[LifeStage],%20\[OrganismalEntity]^-\[PopulationOfIndividualOrganisms],%20\[OrganismalEntity]-%20related%20to(i)%20%3F>\[NamedThing])
## Mappings

 * [WD:Q7239](http://purl.obolibrary.org/obo/WD_Q7239)
## Inheritance

 *  is_a: [biological entity](BiologicalEntity.md)
## Children

 *  child: [biosample](Biosample.md)
 *  child: [individual organism](IndividualOrganism.md)
 *  child: [population of individual organisms](PopulationOfIndividualOrganisms.md)
 *  child: [life stage](LifeStage.md) - A stage of development or growth of an organism, including post-natal adult stages
 *  child: [anatomical entity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part
## Used in

 *  class: [organismal entity](OrganismalEntity.md) references: [biosample](Biosample.md)
 *  class: [organismal entity](OrganismalEntity.md) references: [individual organism](IndividualOrganism.md)
 *  class: [organismal entity](OrganismalEntity.md) references: [population of individual organisms](PopulationOfIndividualOrganisms.md)
 *  class: [organismal entity](OrganismalEntity.md) references: [life stage](LifeStage.md)
 *  class: [organismal entity](OrganismalEntity.md) references: [anatomical entity](AnatomicalEntity.md)
## Fields

 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
