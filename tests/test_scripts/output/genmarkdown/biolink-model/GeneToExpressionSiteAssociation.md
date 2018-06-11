# Class: gene to expression site association


An association between a gene and an expression site, possibly qualified by stage/timing info.

URI: [http://bioentity.io/vocab/GeneToExpressionSiteAssociation](http://bioentity.io/vocab/GeneToExpressionSiteAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneToExpressionSiteAssociation|quantifier_qualifier:string%20%3F;id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[GeneToExpressionSiteAssociation]-%20publications(i)%20*>\[Publication],%20\[GeneToExpressionSiteAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GeneToExpressionSiteAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GeneToExpressionSiteAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[GeneToExpressionSiteAssociation]-%20relation>\[RelationshipType],%20\[GeneToExpressionSiteAssociation]-%20object>\[AnatomicalEntity],%20\[GeneToExpressionSiteAssociation]-%20subject>\[GeneOrGeneProduct],%20\[GeneToExpressionSiteAssociation]-%20stage%20qualifier%20%3F>\[LifeStage],%20\[Association]^-\[GeneToExpressionSiteAssociation])
## Mappings

## Inheritance

 *  is_a: association
## Children

## Used in

## Fields

 * _gene to expression site association object_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: anatomical entity [required]
    * __Local__
 * _gene to expression site association quantifier qualifier_
    * _can be used to indicate magnitude, or also ranking_
    * range: **string**
    * __Local__
 * _gene to expression site association relation_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: relationship type [required]
    * edge label: expressed in
    * __Local__
 * _gene to expression site association stage qualifier_
    * _stage at which the gene is expressed in the site_
    * range: life stage
    * __Local__
 * _gene to expression site association subject_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: gene or gene product [required]
    * __Local__
 * _association slot_
    * _any slot that relates an association to another entity_
    * range: **string**
    * inherited from: association
 * _association type_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: ontology class
    * inherited from: association
 * _category_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: label type
    * inherited from: named thing
 * _description_
    * _a human-readable description of a thing_
    * range: narrative text
    * inherited from: named thing
 * _full name_
    * _a long-form human readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _id_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: identifier type
    * inherited from: named thing
 * _iri_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: iri type
    * inherited from: named thing
 * _name_
    * _A human-readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _negated_
    * _if set to true, then the association is negated i.e. is not true_
    * range: **boolean**
    * inherited from: association
 * _node property_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * inherited from: named thing
 * _provided by_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: provider
    * inherited from: association
 * _publications_
    * _connects an association to publications supporting the association_
    * range: publication*
    * inherited from: association
 * _qualifiers_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: ontology class*
    * inherited from: association
 * _related to_
    * _A grouping for any relationship type that holds between any two things_
    * range: named thing
    * inherited from: named thing
 * _systematic synonym_
    * _more commonly used for gene symbols in yeast_
    * range: label type
    * inherited from: named thing
