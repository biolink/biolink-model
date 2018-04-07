---
layout: default
---

## transcript to gene relationship


A gene is a collection of transcripts

URI: [http://bioentity.io/vocab/TranscriptToGeneRelationship](http://bioentity.io/vocab/TranscriptToGeneRelationship)


![img](http://yuml.me/diagram/nofunky/class/[sequence feature relationship]^-[transcript to gene relationship], [transcript to gene relationship]-association type >[ontology class], [transcript to gene relationship]-subject >[transcript], [genomic entity]^-[transcript], [transcript]-in taxon >[organism taxon], [ontology class]^-[organism taxon], [transcript to gene relationship]-relation >[relationship type], [transcript to gene relationship]-object >[gene], [gene or gene product]^-[gene], [gene]-in taxon >[organism taxon], [transcript to gene relationship]-qualifiers >[ontology class], [transcript to gene relationship]-publications >[publication], [information content entity]^-[publication], [transcript to gene relationship]-provided by >[provider], [administrative entity]^-[provider])
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
    * __range__: [transcript](Transcript.html) [required]
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
    * __range__: [gene](Gene.html) [required]
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
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
