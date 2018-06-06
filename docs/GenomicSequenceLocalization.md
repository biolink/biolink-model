# Class: genomic sequence localization


A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig

URI: [http://bioentity.io/vocab/GenomicSequenceLocalization](http://bioentity.io/vocab/GenomicSequenceLocalization)

![img](images/GenomicSequenceLocalization.png)
## Mappings

 * [faldo:location](http://purl.obolibrary.org/obo/faldo_location)
## Inheritance

 *  is_a: [association](Association.md) - A typed association between two entities, supported by evidence
## Children

## Used in

## Fields

 * _[start interbase coordinate](start_interbase_coordinate.md)_
    * range: string
    * __Local__
 * _[end interbase coordinate](end_interbase_coordinate.md)_
    * range: string
    * __Local__
 * _[genome build](genome_build.md)_
    * _TODO_
    * range: string
    * __Local__
 * _[phase](phase.md)_
    * _TODO_
    * range: string
    * __Local__
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [genomic entity](GenomicEntity.md) [required]
    * __Local__
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [genomic entity](GenomicEntity.md) [required]
    * __Local__
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
