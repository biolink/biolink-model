# Class: gene to gene homology association


A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)

URI: http://bioentity.io/vocab/GeneToGeneHomologyAssociation

![img](http://yuml.me/diagram/nofunky/class/\[GeneToGeneAssociation]^-\[GeneToGeneHomologyAssociation],%20\[GeneToGeneHomologyAssociation]-%20relation>\[RelationshipType],%20)
## Mappings

## Inheritance

 *  is_a: [gene to gene association](GeneToGeneAssociation.md)
## Children

## Used in

## Fields

 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * edge label: [homologous to](homologous_to.md) *subsets: translator_minimal*
    * inherited from: [relation](relation.md)
