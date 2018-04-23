---
layout: default
---

## gene to go term association


None

URI: [http://bioentity.io/vocab/GeneToGoTermAssociation](http://bioentity.io/vocab/GeneToGoTermAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[gene to go term association|], [gene to go term association|]-association type >[ontology class|], [gene to go term association|]-subject >[molecular entity|in taxon], [biological entity|]^-[molecular entity|in taxon], [molecular entity|in taxon]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [gene to go term association|]-relation >[relationship type|], [gene to go term association|]-object >[gene ontology class|], [ontology class|]^-[gene ontology class|], [gene to go term association|]-qualifiers >[ontology class|], [gene to go term association|]-publications >[publication|], [information content entity|]^-[publication|], [gene to go term association|]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings

 * [http://bio2rdf.org/wormbase_vocabulary:Gene-GO-Association](http://purl.obolibrary.org/obo/http_//bio2rdf.org/wormbase_vocabulary_Gene-GO-Association)

## Inheritance

 *  is_a: [association](Association.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _gene, product or macromolecular complex that has the function associated with the GO term_
    * __range__: [molecular entity](MolecularEntity.html) [required]
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
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
