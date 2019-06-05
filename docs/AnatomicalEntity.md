# Class: anatomical entity


A subcellular location, cell type or gross anatomical part

URI: [biolink:AnatomicalEntity](https://w3id.org/biolink/vocab/AnatomicalEntity)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]<filler(i)%200..1-%20\[AnatomicalEntity|id(i):identifier_type;name(i):label_type%20%3F;category(i):iri_type%20*;node_property(i):string%20%3F;iri(i):iri_type%20%3F;synonym(i):label_type%20*;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;creation_date(i):date%20%3F;update_date(i):date%20%3F;has_chemical_formula(i):chemical_formula_value%20%3F;aggregate_statistic(i):string%20%3F;interbase_coordinate(i):string%20%3F],%20\[OntologyClass]<has%20molecular%20consequence(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<same%20as(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<produces(i)%200..*-%20\[AnatomicalEntity],%20\[Disease]<manifestation%20of(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<derives%20from(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<derives%20into(i)%200..*-%20\[AnatomicalEntity],%20\[Occurrent]<capable%20of(i)%200..*-%20\[AnatomicalEntity],%20\[Occurrent]<actively%20involved%20in(i)%200..*-%20\[AnatomicalEntity],%20\[Occurrent]<participates%20in(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<part%20of(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<has%20part(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<overlaps(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<model%20of(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<location%20of(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<located%20in(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<occurs%20in(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<prevents(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<causes(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<contributes%20to(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<predisposes(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<affects%20risk%20for(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<colocalizes%20with(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<coexists%20with(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<xenologous%20to(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<orthologous%20to(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<paralogous%20to(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<homologous%20to(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<disrupts(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<negatively%20regulates(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<positively%20regulates(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<regulates(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<affects(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<physically%20interacts%20with(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<interacts%20with(i)%200..*-%20\[AnatomicalEntity],%20\[NamedThing]<related%20to(i)%200..*-%20\[AnatomicalEntity],%20\[PhenotypicFeature]<has%20phenotype(i)%200..*-%20\[AnatomicalEntity],%20\[OrganismTaxon]<in%20taxon%200..*-%20\[AnatomicalEntity],%20\[GeneOrGeneProduct]<expresses%200..*-%20\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20object%201..1>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityAssociation]-%20subject%201..1>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20object%201..1>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20subject%201..1>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20object%201..1>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20subject%201..1>\[AnatomicalEntity],%20\[DiseaseOrPhenotypicFeatureAssociationToLocationAssociation]-%20object%201..1>\[AnatomicalEntity],%20\[GeneOrGeneProduct]-%20expressed%20in%200..*>\[AnatomicalEntity],%20\[GeneToExpressionSiteAssociation]-%20object%201..1>\[AnatomicalEntity],%20\[AnatomicalEntity]uses%20-.->\[ThingWithTaxon],%20\[AnatomicalEntity]^-\[GrossAnatomicalStructure],%20\[AnatomicalEntity]^-\[CellularComponent],%20\[AnatomicalEntity]^-\[Cell],%20\[OrganismalEntity]^-\[AnatomicalEntity])
## Inheritance

 *  is_a: [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
## Children

 * [Cell](Cell.md)
 * [CellularComponent](CellularComponent.md) - A location in or around a cell
 * [GrossAnatomicalStructure](GrossAnatomicalStructure.md)
## Used by

 *  **[AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)** *[anatomical entity to anatomical entity association.object](anatomical_entity_to_anatomical_entity_association_object.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)** *[anatomical entity to anatomical entity association.subject](anatomical_entity_to_anatomical_entity_association_subject.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md)** *[anatomical entity to anatomical entity ontogenic association.object](anatomical_entity_to_anatomical_entity_ontogenic_association_object.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md)** *[anatomical entity to anatomical entity ontogenic association.subject](anatomical_entity_to_anatomical_entity_ontogenic_association_subject.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md)** *[anatomical entity to anatomical entity part of association.object](anatomical_entity_to_anatomical_entity_part_of_association_object.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md)** *[anatomical entity to anatomical entity part of association.subject](anatomical_entity_to_anatomical_entity_part_of_association_subject.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[DiseaseOrPhenotypicFeatureAssociationToLocationAssociation](DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.md)** *[disease or phenotypic feature association to location association.object](disease_or_phenotypic_feature_association_to_location_association_object.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[expressed in](expressed_in.md)*  <sub>0..*</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[gene to expression site association.object](gene_to_expression_site_association_object.md)*  <sub>REQ</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
## Fields

 * [category](category.md)  <sub>0..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [expresses](expresses.md)  <sub>0..*</sub>
    * Description: holds between an anatomical entity and gene or gene product that is expressed there
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * in subsets: (translator_minimal)
 * [full name](full_name.md)  <sub>OPT</sub>
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [has phenotype](has_phenotype.md)  <sub>0..*</sub>
    * Description: holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature).
    * range: [PhenotypicFeature](PhenotypicFeature.md)
    * inherited from: [BiologicalEntity](BiologicalEntity.md)
    * in subsets: (translator_minimal)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)
 * [interacts with](interacts_with.md)  <sub>0..*</sub>
    * Description: holds between any two entities that directly or indirectly interact with each other
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [node property](node_property.md)  <sub>OPT</sub>
    * Description: A grouping for any property that holds between a node and a value
    * range: [String](String.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [related to](related_to.md)  <sub>0..*</sub>
    * Description: A relationship that is asserted between two named things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [synonym](synonym.md)  <sub>0..*</sub>
    * Description: Alternate human-readable names for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [systematic synonym](systematic_synonym.md)  <sub>OPT</sub>
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
