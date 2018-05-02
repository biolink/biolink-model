---
layout: default
---

## genomic sequence localization


A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig

URI: [http://bioentity.io/vocab/GenomicSequenceLocalization](http://bioentity.io/vocab/GenomicSequenceLocalization)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[genomic sequence localization|start interbase coordinate;end interbase coordinate;genome build;phase], [genomic sequence localization|start interbase coordinate;end interbase coordinate;genome build;phase]-association type >[ontology class|], [genomic sequence localization|start interbase coordinate;end interbase coordinate;genome build;phase]-subject >[genomic entity|has biological sequence], [molecular entity|in taxon]^-[genomic entity|has biological sequence], [genomic entity|has biological sequence]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [genomic sequence localization|start interbase coordinate;end interbase coordinate;genome build;phase]-relation >[relationship type|], [genomic sequence localization|start interbase coordinate;end interbase coordinate;genome build;phase]-object >[genomic entity|has biological sequence], [genomic sequence localization|start interbase coordinate;end interbase coordinate;genome build;phase]-qualifiers >[ontology class|], [genomic sequence localization|start interbase coordinate;end interbase coordinate;genome build;phase]-publications >[publication|], [information content entity|]^-[publication|], [genomic sequence localization|start interbase coordinate;end interbase coordinate;genome build;phase]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings


## Inheritance

 *  is_a: [association](Association.html)

## Children



## Fields

 * [start interbase coordinate](start_interbase_coordinate.html)
    * _TODO_
    * __range__: None
    * __Local__
 * [end interbase coordinate](end_interbase_coordinate.html)
    * _TODO_
    * __range__: None
    * __Local__
 * [genome build](genome_build.html)
    * _TODO_
    * __range__: None
    * __Local__
 * [phase](phase.html)
    * _TODO_
    * __range__: None
    * __Local__
 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: [genomic entity](GenomicEntity.html) [required]
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
    * __range__: [genomic entity](GenomicEntity.html) [required]
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
