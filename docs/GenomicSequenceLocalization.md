# Class: genomic sequence localization


A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig

URI: [http://w3id.org/biolink/vocab/GenomicSequenceLocalization](http://w3id.org/biolink/vocab/GenomicSequenceLocalization)

![img](images/GenomicSequenceLocalization.png)
## Mappings

 * [faldo:location](http://purl.obolibrary.org/obo/faldo_location)
## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

## Used in

## Fields

 * [end interbase coordinate](end_interbase_coordinate.md)
    * Description: TODO
    * range: **string**
    * __Local__
 * [genome build](genome_build.md)
    * Description: TODO
    * range: **string**
    * __Local__
 * [genomic sequence localization.object](genomic_sequence_localization_object.md)
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [GenomicEntity](GenomicEntity.md) [required]
    * __Local__
 * [genomic sequence localization.subject](genomic_sequence_localization_subject.md)
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [GenomicEntity](GenomicEntity.md) [required]
    * __Local__
 * [phase](phase.md)
    * Description: TODO
    * range: **string**
    * __Local__
 * [start interbase coordinate](start_interbase_coordinate.md)
    * Description: TODO
    * range: **string**
    * __Local__
 * [association slot](association_slot.md)
    * Description: any slot that relates an association to another entity
    * range: **string**
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [association.id](association_id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [Association](Association.md)
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * inherited from: [Association](Association.md)
 * [provided by](provided_by.md)
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)*
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)*
    * inherited from: [Association](Association.md)
 * [relation](relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [IriType](IriType.md) [required]
    * inherited from: [Association](Association.md)
