# Class: disease




URI: [http://bioentity.io/vocab/Disease](http://bioentity.io/vocab/Disease)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Disease|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20*;uri(i):uri%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F]-%20treated%20by(i)%20%3F>\[NamedThing],%20\[Disease]-%20has%20biomarker(i)%20%3F>\[MolecularEntity],%20\[Disease]-%20correlated%20with(i)%20%3F>\[MolecularEntity],%20\[Disease]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[Disease]-%20related%20to(i)%20%3F>\[NamedThing],%20\[DiseaseToThingAssociation]-%20subject(i)>\[Disease],%20\[EntityToDiseaseAssociation]-%20object(i)>\[Disease],%20\[NamedThing]-%20manifestation%20of(i)%20%3F>\[Disease],%20\[DiseaseOrPhenotypicFeature]^-\[Disease])
## Mappings

 * [MONDO:0000001](http://purl.obolibrary.org/obo/MONDO_0000001)
 * [WD:Q12136](http://purl.obolibrary.org/obo/WD_Q12136)
 * [SIO:010299](http://semanticscience.org/resource/SIO_010299)
 * [UMLSSG:DISO](http://purl.obolibrary.org/obo/UMLSSG_DISO)
## Inheritance

 *  is_a: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
## Children

## Used in

 *  class: **[DiseaseToThingAssociation](DiseaseToThingAssociation.md)** *[disease to thing association.subject](disease_to_thing_association_subject.md)* **[Disease](Disease.md)**
 *  class: **[EntityToDiseaseAssociation](EntityToDiseaseAssociation.md)** *[entity to disease association.object](entity_to_disease_association_object.md)* **[Disease](Disease.md)**
 *  class: **[NamedThing](NamedThing.md)** *[manifestation of](manifestation_of.md)* **[Disease](Disease.md)**
## Fields

 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [LabelType](LabelType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [correlated with](correlated_with.md) *subsets*: (translator_minimal)
    * Description: holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [has biomarker](has_biomarker.md) *subsets*: (translator_minimal)
    * Description: holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
 * [has phenotype](has_phenotype.md) *subsets*: (translator_minimal)
    * Description: holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). 
    * range: [Phenotype](Phenotype.md)
    * inherited from: [BiologicalEntity](BiologicalEntity.md)
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
 * [treated by](treated_by.md) *subsets*: (translator_minimal)
    * Description: holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition 
    * range: [NamedThing](NamedThing.md)
    * inherited from: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
 * [uri](uri.md)
    * Description: URI expansion of CURIE
    * range: [uri](uri.md)
    * inherited from: [NamedThing](NamedThing.md)
