---
parent: Classes
title: biolink:AnatomicalEntity
grand_parent: Browse Biolink Model
---

# Type: AnatomicalEntity


A subcellular location, cell type or gross anatomical part

URI: [biolink:AnatomicalEntity](https://w3id.org/biolink/vocab/AnatomicalEntity)

SIO:010046
{: .mapping-label }

WD:Q4936952
{: .mapping-label }

UMLSSG:ANAT
{: .mapping-label }

UMLSSC:T022
{: .mapping-label }

UMLSST:bdsy
{: .mapping-label }

UMLSSC:T029
{: .mapping-label }

UMLSST:blor
{: .mapping-label }

UMLSSC:T030
{: .mapping-label }

UMLSST:bsoj
{: .mapping-label }

UMLSSC:T031
{: .mapping-label }

UMLSST:bdsu
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon%200..*-%20\[AnatomicalEntity&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20object%201..1>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20subject%201..1>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20object%201..1>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20subject%201..1>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20object%201..1>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20subject%201..1>\[AnatomicalEntity],%20\[DiseaseOrPhenotypicFeatureAssociationToLocationAssociation]-%20object%201..1>\[AnatomicalEntity],%20\[GeneToExpressionSiteAssociation]-%20object%201..1>\[AnatomicalEntity],%20\[AnatomicalEntity]uses%20-.->\[ThingWithTaxon],%20\[AnatomicalEntity]uses%20-.->\[PhysicalEntity],%20\[AnatomicalEntity]^-\[GrossAnatomicalStructure],%20\[AnatomicalEntity]^-\[CellularComponent],%20\[AnatomicalEntity]^-\[Cell],%20\[OrganismalEntity]^-\[AnatomicalEntity])

---


## Parents

 *  is_a: [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
 *  mixin: [PhysicalEntity](PhysicalEntity.md) - An entity that has physical properties such as mass, volume, or charge

## Children

 * [Cell](Cell.md)
 * [CellularComponent](CellularComponent.md) - A location in or around a cell
 * [GrossAnatomicalStructure](GrossAnatomicalStructure.md)

## Referenced by class

 *  **[AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)** *[anatomical entity to anatomical entity association➞object](anatomical_entity_to_anatomical_entity_association_object.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)** *[anatomical entity to anatomical entity association➞subject](anatomical_entity_to_anatomical_entity_association_subject.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md)** *[anatomical entity to anatomical entity ontogenic association➞object](anatomical_entity_to_anatomical_entity_ontogenic_association_object.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md)** *[anatomical entity to anatomical entity ontogenic association➞subject](anatomical_entity_to_anatomical_entity_ontogenic_association_subject.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md)** *[anatomical entity to anatomical entity part of association➞object](anatomical_entity_to_anatomical_entity_part_of_association_object.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md)** *[anatomical entity to anatomical entity part of association➞subject](anatomical_entity_to_anatomical_entity_part_of_association_subject.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[DiseaseOrPhenotypicFeatureAssociationToLocationAssociation](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.md)** *[disease or phenotypic feature association to location association➞object](disease_or_phenotypic_feature_association_to_location_association_object.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[expressed in](expressed_in.md)*  <sub>0..*</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[gene to expression site association➞object](gene_to_expression_site_association_object.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [expresses](expresses.md)  <sub>0..*</sub>
    * Description: holds between an anatomical entity and gene or gene product that is expressed there
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SIO:010046 |
|  | | WD:Q4936952 |
|  | | UMLSSG:ANAT |
|  | | UMLSSC:T022 |
|  | | UMLSST:bdsy |
|  | | UMLSSC:T029 |
|  | | UMLSST:blor |
|  | | UMLSSC:T030 |
|  | | UMLSST:bsoj |
|  | | UMLSSC:T031 |
|  | | UMLSST:bdsu |

