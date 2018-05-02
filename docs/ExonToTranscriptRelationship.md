---
layout: default
---

## exon to transcript relationship


A transcript is formed from multiple exons

URI: [http://bioentity.io/vocab/ExonToTranscriptRelationship](http://bioentity.io/vocab/ExonToTranscriptRelationship)


![img](http://yuml.me/diagram/nofunky/class/[sequence feature relationship|]^-[exon to transcript relationship|], [exon to transcript relationship|]-association type >[ontology class|], [exon to transcript relationship|]-subject >[exon|], [genomic entity|has biological sequence]^-[exon|], [exon|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [exon to transcript relationship|]-relation >[relationship type|], [exon to transcript relationship|]-object >[transcript|], [genomic entity|has biological sequence]^-[transcript|], [transcript|]-in taxon >[organism taxon|], [exon to transcript relationship|]-qualifiers >[ontology class|], [exon to transcript relationship|]-publications >[publication|], [information content entity|]^-[publication|], [exon to transcript relationship|]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings


## Inheritance

 *  is_a: [sequence feature relationship](SequenceFeatureRelationship.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: [exon](Exon.html) [required]
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
    * __range__: [transcript](Transcript.html) [required]
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
