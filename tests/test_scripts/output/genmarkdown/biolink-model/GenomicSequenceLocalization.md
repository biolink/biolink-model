# Class: genomic sequence localization


A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig

URI: http://bioentity.io/vocab/GenomicSequenceLocalization

![img](http://yuml.me/diagram/nofunky/class/\[Association]^-\[GenomicSequenceLocalization|start_interbase_coordinate:string%20%3F;end_interbase_coordinate:string%20%3F;genome_build:string%20%3F;phase:string%20%3F],%20\[GenomicSequenceLocalization]-%20subject>\[GenomicEntity],%20\[GenomicSequenceLocalization]-%20object>\[GenomicEntity],%20)
## Mappings

 * [faldo:location](http://purl.obolibrary.org/obo/faldo_location)
## Inheritance

 *  is_a: [association](Association.md)
## Children

## Used in

## Fields

 * _[start interbase coordinate](start_interbase_coordinate.md)_
    * range: string
    * inherited from: [interbase coordinate](interbase_coordinate.md)
 * _[end interbase coordinate](end_interbase_coordinate.md)_
    * range: string
    * inherited from: [interbase coordinate](interbase_coordinate.md)
 * _[genome build](genome_build.md)_
    * _TODO_
    * range: string
    * inherited from: [node property](node_property.md)
 * _[phase](phase.md)_
    * _TODO_
    * range: string
    * inherited from: [node property](node_property.md)
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [genomic entity](GenomicEntity.md) [required]
    * inherited from: [subject](subject.md)
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [genomic entity](GenomicEntity.md) [required]
    * inherited from: [object](object.md)
