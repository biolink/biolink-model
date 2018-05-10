---
layout: default
---

## cell line to disease or phenotypic feature association


An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype

URI: [http://bioentity.io/vocab/CellLineToDiseaseOrPhenotypicFeatureAssociation](http://bioentity.io/vocab/CellLineToDiseaseOrPhenotypicFeatureAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[cell line to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category], [cell line to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-association type >[ontology class|], [cell line to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-subject >[cell line|], [biosample|in taxon]^-[cell line|], [cell line|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [cell line to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-relation >[relationship type|], [cell line to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-object >[disease or phenotypic feature|in taxon], [biological entity|]^-[disease or phenotypic feature|in taxon], [disease or phenotypic feature|in taxon]-in taxon >[organism taxon|], [cell line to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-qualifiers >[ontology class|], [cell line to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-publications >[publication|], [information content entity|]^-[publication|], [cell line to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings


## Inheritance

 *  is_a: [association](Association.html)
 *  mixin: [cell line to thing association](CellLineToThingAssociation.html)
 *  mixin: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: [cell line](CellLine.html) [required]
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _the relationship type by which a subject is connected to an object in an association_
    * __range__: [relationship type](RelationshipType.html) [required]
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html) [required]
    * inherited from: [association](Association.html)
 * [qualifiers](qualifiers.html)
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * __range__: [ontology class](OntologyClass.html)*
    * inherited from: [association](Association.html)
 * [publications](publications.html)
    * _connects an association to publications supporting the association_
    * __range__: [publication](Publication.html)*
    * inherited from: [association](Association.html)
 * [provided by](provided_by.html)
    * _connects an association to the agent (person, organization or group) that provided it_
    * __range__: [provider](Provider.html)
    * inherited from: [association](Association.html)
 * [id](id.html)
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
