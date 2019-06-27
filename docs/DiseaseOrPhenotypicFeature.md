
# Class: disease or phenotypic feature


Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.

URI: [biolink:DiseaseOrPhenotypicFeature](https://w3id.org/biolink/vocab/DiseaseOrPhenotypicFeature)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon%200..*-%20\[DiseaseOrPhenotypicFeature|id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation]-%20subject%201..1>\[DiseaseOrPhenotypicFeature],%20\[ChemicalToDiseaseOrPhenotypicFeatureAssociation]-%20object%201..1>\[DiseaseOrPhenotypicFeature],%20\[DiseaseOrPhenotypicFeatureAssociationToThingAssociation]-%20subject%201..1>\[DiseaseOrPhenotypicFeature],%20\[ThingToDiseaseOrPhenotypicFeatureAssociation]-%20object%201..1>\[DiseaseOrPhenotypicFeature],%20\[DiseaseOrPhenotypicFeature]uses%20-.->\[ThingWithTaxon],%20\[DiseaseOrPhenotypicFeature]^-\[PhenotypicFeature],%20\[DiseaseOrPhenotypicFeature]^-\[Disease],%20\[BiologicalEntity]^-\[DiseaseOrPhenotypicFeature])

## Parents

 *  is_a: [BiologicalEntity](BiologicalEntity.md)

## Uses Mixins

 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon

## Children

 * [Disease](Disease.md)
 * [PhenotypicFeature](PhenotypicFeature.md)

## Referenced by class

 *  **[MolecularEntity](MolecularEntity.md)** *[biomarker for](biomarker_for.md)*  <sub>0..*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)** *[subject](cell_line_to_disease_or_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)** *[object](chemical_to_disease_or_phenotypic_feature_association_object.md)*  <sub>REQ</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[DiseaseOrPhenotypicFeatureAssociationToThingAssociation](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)** *[subject](disease_or_phenotypic_feature_association_to_thing_association_subject.md)*  <sub>REQ</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[Gene](Gene.md)** *[gene associated with condition](gene_associated_with_condition.md)*  <sub>0..*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[ThingToDiseaseOrPhenotypicFeatureAssociation](ThingToDiseaseOrPhenotypicFeatureAssociation.md)** *[object](thing_to_disease_or_phenotypic_feature_association_object.md)*  <sub>REQ</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[Treatment](Treatment.md)** *[treats](treats.md)*  <sub>1..*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**

## Attributes


### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [correlated with](correlated_with.md)  <sub>0..*</sub>
    * Description: holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
    * range: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [has biomarker](has_biomarker.md)  <sub>0..*</sub>
    * Description: holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
    * range: [MolecularEntity](MolecularEntity.md)
    * in subsets: (translator_minimal)
 * [treated by](treated_by.md)  <sub>0..*</sub>
    * Description: holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
