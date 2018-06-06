# Class: biosample to disease or phenotypic feature association


An association between a biosample and a disease or phenotype
  definitional: true

URI: [http://bioentity.io/vocab/BiosampleToDiseaseOrPhenotypicFeatureAssociation](http://bioentity.io/vocab/BiosampleToDiseaseOrPhenotypicFeatureAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Association]^-\[BiosampleToDiseaseOrPhenotypicFeatureAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;subject(i):string;negated(i):boolean%20%3F;object(i):string;association_slot(i):string%20%3F],%20\[BiosampleToDiseaseOrPhenotypicFeatureAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[BiosampleToDiseaseOrPhenotypicFeatureAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[BiosampleToDiseaseOrPhenotypicFeatureAssociation]-%20relation(i)>\[RelationshipType],%20\[BiosampleToDiseaseOrPhenotypicFeatureAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[BiosampleToDiseaseOrPhenotypicFeatureAssociation]-%20publications(i)%20*>\[Publication],%20\[BiosampleToDiseaseOrPhenotypicFeatureAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[BiosampleToDiseaseOrPhenotypicFeatureAssociation]uses%20-.->\[BiosampleToThingAssociation],%20\[BiosampleToDiseaseOrPhenotypicFeatureAssociation]uses%20-.->\[ThingToDiseaseOrPhenotypicFeatureAssociation])
## Mappings

## Inheritance

 *  is_a: [association](Association.md) - A typed association between two entities, supported by evidence
 *  mixin: [biosample to thing association](BiosampleToThingAssociation.md) - An association between a biosample and something
 *  mixin: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md)
## Children

## Fields

 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[association type](association_type.md)_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: [ontology class](OntologyClass.md)
    * inherited from: None
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
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
