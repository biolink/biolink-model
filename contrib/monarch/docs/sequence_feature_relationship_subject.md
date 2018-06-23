# Slot: subject


connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.

URI: [http://bioentity.io/vocab/sequence_feature_relationship_subject](slot_uri)
## Mappings

 * [rdf:subject](http://purl.obolibrary.org/obo/rdf_subject)
 * [owl:annotatedSource](http://purl.obolibrary.org/obo/owl_annotatedSource)
 * [oban:association_has_subject](http://purl.obolibrary.org/obo/oban_association_has_subject)
## Domain and Range

[SequenceFeatureRelationship](SequenceFeatureRelationship.md) -> [GenomicEntity](GenomicEntity.md)
## Inheritance

 *  is_a: [subject](subject.md)
## Children

 *  child: [gene to gene product relationship.subject](gene_to_gene_product_relationship_subject.md)
 *  child: [transcript to gene relationship.subject](transcript_to_gene_relationship_subject.md)
 *  child: [exon to transcript relationship.subject](exon_to_transcript_relationship_subject.md)
## Used in

 *  usage: [SequenceFeatureRelationship](SequenceFeatureRelationship.md)
