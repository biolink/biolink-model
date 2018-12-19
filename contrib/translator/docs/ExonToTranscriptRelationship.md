# Class: exon to transcript relationship


A transcript is formed from multiple exons

URI: [http://w3id.org/biolink/vocab/ExonToTranscriptRelationship](http://w3id.org/biolink/vocab/ExonToTranscriptRelationship)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ExonToTranscriptRelationship|id(i):identifier_type%20%3F;relation(i):iri_type;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[ExonToTranscriptRelationship]-%20publications(i)%20*>\[Publication],%20\[ExonToTranscriptRelationship]-%20qualifiers(i)%20*>\[OntologyClass],%20\[ExonToTranscriptRelationship]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[ExonToTranscriptRelationship]-%20object>\[Transcript],%20\[ExonToTranscriptRelationship]-%20subject>\[Exon],%20\[SequenceFeatureRelationship]^-\[ExonToTranscriptRelationship])
## Mappings

## Inheritance

 *  is_a: [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene
## Children

## Used in

## Fields

 * [exon to transcript relationship.object](exon_to_transcript_relationship_object.md)
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [Transcript](Transcript.md) [required]
    * __Local__
 * [exon to transcript relationship.subject](exon_to_transcript_relationship_subject.md)
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [Exon](Exon.md) [required]
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
