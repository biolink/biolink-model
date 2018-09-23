# Class: disease or phenotypic feature


Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.

URI: [http://bioentity.io/vocab/DiseaseOrPhenotypicFeature](http://bioentity.io/vocab/DiseaseOrPhenotypicFeature)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[DiseaseOrPhenotypicFeature|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20*;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F]-%20related%20to(i)%20%3F>\[NamedThing],%20\[DiseaseOrPhenotypicFeature]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[DiseaseOrPhenotypicFeature]-%20treated%20by%20%3F>\[NamedThing],%20\[DiseaseOrPhenotypicFeature]-%20has%20biomarker%20%3F>\[MolecularEntity],%20\[DiseaseOrPhenotypicFeature]-%20correlated%20with%20%3F>\[MolecularEntity],%20\[MolecularEntity]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[CellLineToDiseaseOrPhenotypicFeatureAssociation]-%20subject(i)>\[DiseaseOrPhenotypicFeature],%20\[ChemicalToDiseaseOrPhenotypicFeatureAssociation]-%20object(i)>\[DiseaseOrPhenotypicFeature],%20\[DiseaseOrPhenotypicFeatureAssociationToThingAssociation]-%20subject(i)>\[DiseaseOrPhenotypicFeature],%20\[Gene]-%20gene%20associated%20with%20condition(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[ThingToDiseaseOrPhenotypicFeatureAssociation]-%20object(i)>\[DiseaseOrPhenotypicFeature],%20\[Treatment]-%20treats(i)>\[DiseaseOrPhenotypicFeature],%20\[Treatment]-%20treats(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[DiseaseOrPhenotypicFeature]uses%20-.->\[ThingWithTaxon],%20\[DiseaseOrPhenotypicFeature]^-\[PhenotypicFeature],%20\[DiseaseOrPhenotypicFeature]^-\[Disease],%20\[BiologicalEntity]^-\[DiseaseOrPhenotypicFeature])
## Mappings

## Inheritance

 *  is_a: [BiologicalEntity](BiologicalEntity.md)
 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
## Children

 * [Disease](Disease.md)
 * [PhenotypicFeature](PhenotypicFeature.md)
## Used in

 *  class: **[MolecularEntity](MolecularEntity.md)** *[biomarker for](biomarker_for.md)* **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  class: **[CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)** *[cell line to disease or phenotypic feature association.subject](cell_line_to_disease_or_phenotypic_feature_association_subject.md)* **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  class: **[ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)** *[chemical to disease or phenotypic feature association.object](chemical_to_disease_or_phenotypic_feature_association_object.md)* **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  class: **[DiseaseOrPhenotypicFeatureAssociationToThingAssociation](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)** *[disease or phenotypic feature association to thing association.subject](disease_or_phenotypic_feature_association_to_thing_association_subject.md)* **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  class: **[Gene](Gene.md)** *[gene associated with condition](gene_associated_with_condition.md)* **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  class: **[ThingToDiseaseOrPhenotypicFeatureAssociation](ThingToDiseaseOrPhenotypicFeatureAssociation.md)** *[thing to disease or phenotypic feature association.object](thing_to_disease_or_phenotypic_feature_association_object.md)* **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  class: **[Treatment](Treatment.md)** *[treatment.treats](treatment_treats.md)* **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  class: **[Treatment](Treatment.md)** *[treats](treats.md)* **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
## Fields

 * [correlated with](correlated_with.md) *subsets*: (translator_minimal)
    * Description: holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
    * range: [MolecularEntity](MolecularEntity.md)
    * __Local__
 * [has biomarker](has_biomarker.md) *subsets*: (translator_minimal)
    * Description: holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
    * range: [MolecularEntity](MolecularEntity.md)
    * __Local__
 * [treated by](treated_by.md) *subsets*: (translator_minimal)
    * Description: holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition 
    * range: [NamedThing](NamedThing.md)
    * __Local__
 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [LabelType](LabelType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [has alternate identifier](has_alternate_identifier.md)
    * Description: An alternate identifier for the entity, provided by the source database
    * range: identifier*
    * inherited from: [NamedThing](NamedThing.md)
 * [has phenotype](has_phenotype.md) *subsets*: (translator_minimal)
    * Description: holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). 
    * range: [Phenotype](Phenotype.md)
    * inherited from: [BiologicalEntity](BiologicalEntity.md)
 * [has synonym](has_synonym.md)
    * Description: Alternate labels for an entity
    * range: [name](name.md) *subsets*: (translator_minimal)*
    * inherited from: [NamedThing](NamedThing.md)
 * [has xref](has_xref.md)
    * Description: A database cross-reference for the entity, provided by a separate database
    * range: identifier*
    * inherited from: [NamedThing](NamedThing.md)
 * [id](id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [in taxon](in_taxon.md) *subsets*: (translator_minimal)
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
 * [iri](iri.md) *subsets*: (translator_minimal)
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [name](name.md) *subsets*: (translator_minimal)
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [node property](node_property.md)
    * Description: A grouping for any property that holds between a node and a value
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
