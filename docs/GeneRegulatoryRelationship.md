---
layout: default
---

## gene regulatory relationship


A regulatory relationship between two genes

URI: [http://bioentity.io/vocab/GeneRegulatoryRelationship](http://bioentity.io/vocab/GeneRegulatoryRelationship)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[gene regulatory relationship|], [gene regulatory relationship|]-association type >[ontology class|], [gene regulatory relationship|]-subject >[gene or gene product|], [genomic entity|has biological sequence]^-[gene or gene product|], [gene or gene product|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [gene regulatory relationship|]-relation >[relationship type|], [gene regulatory relationship|]-object >[gene or gene product|], [gene regulatory relationship|]-qualifiers >[ontology class|], [gene regulatory relationship|]-publications >[publication|], [information content entity|]^-[publication|], [gene regulatory relationship|]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings


## Inheritance

 *  is_a: [association](Association.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: [gene or gene product](GeneOrGeneProduct.html) [required]
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _the direction is always from regulator to regulated_
    * __range__: [relationship type](RelationshipType.html) [required]
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: [gene or gene product](GeneOrGeneProduct.html) [required]
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
