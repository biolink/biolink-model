---
layout: default
---

## macromolecular machine to biological process association


A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it

URI: [http://bioentity.io/vocab/MacromolecularMachineToBiologicalProcessAssociation](http://bioentity.io/vocab/MacromolecularMachineToBiologicalProcessAssociation)


![img](http://yuml.me/diagram/nofunky/class/[functional association|]^-[macromolecular machine to biological process association|], [macromolecular machine to biological process association|]-association type >[ontology class|], [macromolecular machine to biological process association|]-subject >[macromolecular machine|], [genomic entity|has biological sequence]^-[macromolecular machine|], [macromolecular machine|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [macromolecular machine to biological process association|]-relation >[relationship type|], [macromolecular machine to biological process association|]-object >[biological process|], [biological process or activity|]^-[biological process|], [macromolecular machine to biological process association|]-qualifiers >[ontology class|], [macromolecular machine to biological process association|]-publications >[publication|], [information content entity|]^-[publication|], [macromolecular machine to biological process association|]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings


## Inheritance

 *  is_a: [functional association](FunctionalAssociation.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: [macromolecular machine](MacromolecularMachine.html) [required]
    * Example: [ZFIN:ZDB-GENE-050417-357](http://purl.obolibrary.org/obo/ZFIN_ZDB-GENE-050417-357) twist1b
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
    * __range__: [biological process](BiologicalProcess.html) [required]
    * Example: [GO:0016301](http://purl.obolibrary.org/obo/GO_0016301) kinase activity
    * Example: [GO:0045211](http://purl.obolibrary.org/obo/GO_0045211) postsynaptic membrane
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
 * [id](id.html) *subsets: translator_minimal*
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html) *subsets: translator_minimal*
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html) *subsets: translator_minimal*
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
