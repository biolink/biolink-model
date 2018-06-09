# Class: disease or phenotypic feature


Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.

URI: [http://bioentity.io/vocab/DiseaseOrPhenotypicFeature](http://bioentity.io/vocab/DiseaseOrPhenotypicFeature)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[BiologicalEntity]^-\[DiseaseOrPhenotypicFeature|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F;treated_by:string%20%3F],%20\[DiseaseOrPhenotypicFeature]^-\[Disease],%20\[DiseaseOrPhenotypicFeature]^-\[PhenotypicFeature],%20\[DiseaseOrPhenotypicFeature]-%20related%20to(i)%20%3F>\[NamedThing],%20\[DiseaseOrPhenotypicFeature]-%20correlated%20with%20%3F>\[MolecularEntity],%20\[DiseaseOrPhenotypicFeature]-%20has%20biomarker%20%3F>\[MolecularEntity],%20\[DiseaseOrPhenotypicFeature]-%20in%20taxon%20%3F>\[OrganismTaxon],%20\[DiseaseOrPhenotypicFeature]uses%20-.->\[ThingWithTaxon])
## Mappings

## Inheritance

 *  is_a: [biological entity](BiologicalEntity.md)
 *  mixin: [thing with taxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
## Children

 *  child: [disease](Disease.md)
 *  child: [phenotypic feature](PhenotypicFeature.md)
## Used in

 *  class: [molecular entity](MolecularEntity.md) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 *  class: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 *  class: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 *  class: [disease or phenotypic feature association to thing association](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 *  class: [gene](Gene.md) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 *  class: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 *  class: [treatment](Treatment.md) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
 *  class: [treatment](Treatment.md) references: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
## Fields

 * _[correlated with](correlated_with.md) *subsets*: (translator_minimal)_
    * _holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature._
    * range: [molecular entity](MolecularEntity.md)
    * __Local__
 * _[has biomarker](has_biomarker.md) *subsets*: (translator_minimal)_
    * _holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature._
    * range: [molecular entity](MolecularEntity.md)
    * __Local__
 * _[in taxon](in_taxon.md) *subsets*: (translator_minimal)_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * __Local__
 * _[treated by](treated_by.md) *subsets*: (translator_minimal)_
    * _holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition _
    * range: string
    * __Local__
 * _[category](category.md) *subsets*: (translator_minimal)_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[description](description.md) *subsets*: (translator_minimal)_
    * _a human-readable description of a thing_
    * range: [narrative text](NarrativeText.md)
    * inherited from: [named thing](NamedThing.md)
 * _[full name](full_name.md)_
    * _a long-form human readable name for a thing_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[has phenotype](has_phenotype.md) *subsets*: (translator_minimal)_
    * _holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). _
    * range: [phenotype](Phenotype.md)
    * inherited from: [biological entity](BiologicalEntity.md)
 * _[id](id.md) *subsets*: (translator_minimal)_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: [identifier type](IdentifierType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[iri](iri.md) *subsets*: (translator_minimal)_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: [iri type](IriType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[name](name.md) *subsets*: (translator_minimal)_
    * _A human-readable name for a thing_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[node property](node_property.md)_
    * _A grouping for any property that holds between a node and a value_
    * range: string
    * inherited from: [named thing](NamedThing.md)
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[systematic synonym](systematic_synonym.md)_
    * _more commonly used for gene symbols in yeast_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
