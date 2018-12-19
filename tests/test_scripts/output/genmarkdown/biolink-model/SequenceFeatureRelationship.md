# Class: sequence feature relationship


For example, a particular exon is part of a particular transcript or gene

URI: [http://w3id.org/biolink/vocab/SequenceFeatureRelationship](http://w3id.org/biolink/vocab/SequenceFeatureRelationship)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[SequenceFeatureRelationship|id(i):identifier_type%20%3F;relation(i):iri_type;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[SequenceFeatureRelationship]-%20publications(i)%20*>\[Publication],%20\[SequenceFeatureRelationship]-%20qualifiers(i)%20*>\[OntologyClass],%20\[SequenceFeatureRelationship]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[SequenceFeatureRelationship]-%20object>\[GenomicEntity],%20\[SequenceFeatureRelationship]-%20subject>\[GenomicEntity],%20\[SequenceFeatureRelationship]^-\[TranscriptToGeneRelationship],%20\[SequenceFeatureRelationship]^-\[GeneToGeneProductRelationship],%20\[SequenceFeatureRelationship]^-\[ExonToTranscriptRelationship],%20\[Association]^-\[SequenceFeatureRelationship])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

 * [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) - A transcript is formed from multiple exons
 * [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) - A gene is transcribed and potentially translated to a gene product
 * [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) - A gene is a collection of transcripts
## Used in

## Fields

 * [sequence feature relationship.object](sequence_feature_relationship_object.md)
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [GenomicEntity](GenomicEntity.md) [required]
    * __Local__
 * [sequence feature relationship.subject](sequence_feature_relationship_subject.md)
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [GenomicEntity](GenomicEntity.md) [required]
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
