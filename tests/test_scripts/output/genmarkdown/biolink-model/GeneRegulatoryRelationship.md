# Class: gene regulatory relationship


A regulatory relationship between two genes

URI: [http://bioentity.io/vocab/GeneRegulatoryRelationship](http://bioentity.io/vocab/GeneRegulatoryRelationship)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Association]^-\[GeneRegulatoryRelationship|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F],%20\[GeneRegulatoryRelationship]-%20related%20to(i)%20%3F>\[NamedThing],%20\[GeneRegulatoryRelationship]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GeneRegulatoryRelationship]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GeneRegulatoryRelationship]-%20publications(i)%20*>\[Publication],%20\[GeneRegulatoryRelationship]-%20provided%20by(i)%20%3F>\[Provider],%20\[GeneRegulatoryRelationship]-%20relation>\[RelationshipType],%20\[GeneRegulatoryRelationship]-%20subject>\[GeneOrGeneProduct],%20\[GeneRegulatoryRelationship]-%20object>\[GeneOrGeneProduct])
## Mappings

## Inheritance

 *  is_a: [association](Association.md) - A typed association between two entities, supported by evidence
## Children

## Used in

## Fields

 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * __Local__
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene or gene product](GeneOrGeneProduct.md) [required]
    * __Local__
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene or gene product](GeneOrGeneProduct.md) [required]
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[association type](association_type.md)_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: [ontology class](OntologyClass.md)
    * inherited from: None
 * _[qualifiers](qualifiers.md)_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: [ontology class](OntologyClass.md)*
    * inherited from: None
 * _[publications](publications.md)_
    * _connects an association to publications supporting the association_
    * range: [publication](Publication.md)*
    * inherited from: None
 * _[provided by](provided_by.md)_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: [provider](Provider.md)
    * inherited from: None
