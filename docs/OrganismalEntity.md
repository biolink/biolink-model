---
layout: default
---

## organismal entity


A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

URI: [http://bioentity.io/vocab/OrganismalEntity](http://bioentity.io/vocab/OrganismalEntity)


![img](http://yuml.me/diagram/nofunky/class/[biological entity|]^-[organismal entity|])
## Mappings

 * [WD:Q7239](http://purl.obolibrary.org/obo/WD_Q7239)

## Inheritance

 *  is_a: [biological entity](BiologicalEntity.html)

## Children

 *  child: [individual organism](IndividualOrganism.html)
 *  child: [population of individual organisms](PopulationOfIndividualOrganisms.html)
 *  child: [biosample](Biosample.html)
 *  child: [anatomical entity](AnatomicalEntity.html)
 *  child: [life stage](LifeStage.html)

## Used in

 *  class: [cell line to thing association](CellLineToThingAssociation.html) references: [cell line](CellLine.html)
 *  class: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.html) references: [cell line](CellLine.html)
 *  class: [case to thing association](CaseToThingAssociation.html) references: [case](Case.html)
 *  class: [biosample to thing association](BiosampleToThingAssociation.html) references: [biosample](Biosample.html)
 *  class: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.html) references: [biosample](Biosample.html)
 *  class: [disease or phenotypic feature association to location association](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.html) references: [anatomical entity](AnatomicalEntity.html)
 *  class: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html) references: [case](Case.html)
 *  class: [variant to population association](VariantToPopulationAssociation.html) references: [population of individual organisms](PopulationOfIndividualOrganisms.html)
 *  class: [population to population association](PopulationToPopulationAssociation.html) references: [population of individual organisms](PopulationOfIndividualOrganisms.html)
 *  class: [gene to expression site association](GeneToExpressionSiteAssociation.html) references: [life stage](LifeStage.html)
 *  class: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.html) references: [anatomical entity](AnatomicalEntity.html)
 *  class: [anatomical entity part of anatomical entity association](AnatomicalEntityPartOfAnatomicalEntityAssociation.html) references: [anatomical entity](AnatomicalEntity.html)

## Fields

 * [id](id.html)
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
