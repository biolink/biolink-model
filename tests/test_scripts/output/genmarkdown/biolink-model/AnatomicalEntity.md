# Class: anatomical entity


A subcellular location, cell type or gross anatomical part

URI: [http://bioentity.io/vocab/AnatomicalEntity](http://bioentity.io/vocab/AnatomicalEntity)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismalEntity]^-\[AnatomicalEntity|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F],%20\[AnatomicalEntity]^-\[Cell],%20\[AnatomicalEntity]^-\[CellularComponent],%20\[AnatomicalEntity]^-\[GrossAnatomicalStructure],%20\[AnatomicalEntity]-%20related%20to(i)%20%3F>\[NamedThing],%20\[AnatomicalEntity]-%20expresses%20%3F>\[GeneOrGeneProduct],%20\[AnatomicalEntity]-%20in%20taxon%20%3F>\[OrganismTaxon],%20\[AnatomicalEntity]uses%20-.->\[ThingWithTaxon])
## Mappings

 * [UMLSSG:ANAT](http://purl.obolibrary.org/obo/UMLSSG_ANAT)
 * [SIO:010046](http://semanticscience.org/resource/SIO_010046)
 * [WD:Q4936952](http://purl.obolibrary.org/obo/WD_Q4936952)
 * [UBERON:0001062](http://purl.obolibrary.org/obo/UBERON_0001062)
## Inheritance

 *  is_a: [organismal entity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
 *  mixin: [thing with taxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
## Children

 *  child: [cell](Cell.md)
 *  child: [cellular component](CellularComponent.md) - A location in or around a cell
 *  child: [gross anatomical structure](GrossAnatomicalStructure.md)
## Used in

 *  class: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.md) references: [anatomical entity](AnatomicalEntity.md)
 *  class: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.md) references: [anatomical entity](AnatomicalEntity.md)
 *  class: [anatomical entity to anatomical entity ontogenic association](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) references: [anatomical entity](AnatomicalEntity.md)
 *  class: [anatomical entity to anatomical entity ontogenic association](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) references: [anatomical entity](AnatomicalEntity.md)
 *  class: [anatomical entity to anatomical entity part of association](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) references: [anatomical entity](AnatomicalEntity.md)
 *  class: [anatomical entity to anatomical entity part of association](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) references: [anatomical entity](AnatomicalEntity.md)
 *  class: [disease or phenotypic feature association to location association](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.md) references: [anatomical entity](AnatomicalEntity.md)
 *  class: [gene or gene product](GeneOrGeneProduct.md) references: [anatomical entity](AnatomicalEntity.md)
 *  class: [gene to expression site association](GeneToExpressionSiteAssociation.md) references: [anatomical entity](AnatomicalEntity.md)
## Fields

 * _[expresses](expresses.md) *subsets*: (translator_minimal)_
    * _holds between an anatomical entity and gene or gene product that is expressed there_
    * range: [gene or gene product](GeneOrGeneProduct.md)
    * __Local__
 * _[in taxon](in_taxon.md) *subsets*: (translator_minimal)_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
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
