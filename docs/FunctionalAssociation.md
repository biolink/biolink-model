---
layout: default
---

## functional association


An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed

URI: [http://bioentity.io/vocab/FunctionalAssociation](http://bioentity.io/vocab/FunctionalAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[functional association|], [functional association|]-association type >[ontology class|], [functional association|]-subject >[macromolecular machine|], [genomic entity|has biological sequence]^-[macromolecular machine|], [macromolecular machine|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [functional association|]-relation >[relationship type|], [functional association|]-object >[gene ontology class|], [ontology class|]^-[gene ontology class|], [functional association|]-qualifiers >[ontology class|], [functional association|]-publications >[publication|], [information content entity|]^-[publication|], [functional association|]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings


## Inheritance

 *  is_a: [association](Association.html)

## Children

 *  child: [macromolecular machine to molecular activity association](MacromolecularMachineToMolecularActivityAssociation.html)
 *  child: [macromolecular machine to biological process association](MacromolecularMachineToBiologicalProcessAssociation.html)
 *  child: [macromolecular machine to cellular component association](MacromolecularMachineToCellularComponentAssociation.html)
 *  child: [gene to go term association](GeneToGoTermAssociation.html)


## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _gene, product or macromolecular complex that has the function associated with the GO term_
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
    * _class describing the activity, process or localization of the gene product_
    * __range__: [gene ontology class](GeneOntologyClass.html) [required]
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
