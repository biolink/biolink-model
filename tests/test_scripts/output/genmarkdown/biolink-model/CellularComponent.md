# Class: cellular component


A location in or around a cell

URI: [http://bioentity.io/vocab/CellularComponent](http://bioentity.io/vocab/CellularComponent)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[CellularComponent|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20*;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F]-%20expresses(i)%20%3F>\[GeneOrGeneProduct],%20\[CellularComponent]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[CellularComponent]-%20related%20to(i)%20%3F>\[NamedThing],%20\[MacromolecularMachineToCellularComponentAssociation]-%20object(i)>\[CellularComponent],%20\[AnatomicalEntity]^-\[CellularComponent])
## Mappings

 * [GO:0005575](http://purl.obolibrary.org/obo/GO_0005575)
 * [SIO:001400](http://semanticscience.org/resource/SIO_001400)
 * [WD:Q5058355](http://purl.obolibrary.org/obo/WD_Q5058355)
## Inheritance

 *  is_a: [AnatomicalEntity](AnatomicalEntity.md) - A subcellular location, cell type or gross anatomical part
## Children

## Used in

 *  class: **[MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md)** *[macromolecular machine to cellular component association.object](macromolecular_machine_to_cellular_component_association_object.md)* **[CellularComponent](CellularComponent.md)**
## Fields

 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [LabelType](LabelType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [expresses](expresses.md) *subsets*: (translator_minimal)
    * Description: holds between an anatomical entity and gene or gene product that is expressed there
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * inherited from: [AnatomicalEntity](AnatomicalEntity.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
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
