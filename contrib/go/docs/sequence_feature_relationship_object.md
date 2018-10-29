# Slot: object


connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.

URI: [http://bioentity.io/vocab/sequence_feature_relationship_object](slot_uri)
## Mappings

 * [rdf:object](http://purl.obolibrary.org/obo/rdf_object)
 * [owl:annotatedTarget](http://purl.obolibrary.org/obo/owl_annotatedTarget)
 * [oban:association_has_object](http://purl.obolibrary.org/obo/oban_association_has_object)
## Domain and Range

[SequenceFeatureRelationship](SequenceFeatureRelationship.md) -> [GenomicEntity](GenomicEntity.md)
## Inheritance

 *  is_a: [object](object.md)
## Children

 *  child: [transcript to gene relationship.object](transcript_to_gene_relationship_object.md)
 *  child: [exon to transcript relationship.object](exon_to_transcript_relationship_object.md)
 *  child: [gene to gene product relationship.object](gene_to_gene_product_relationship_object.md)
## Used in

 *  usage: [SequenceFeatureRelationship](SequenceFeatureRelationship.md)
