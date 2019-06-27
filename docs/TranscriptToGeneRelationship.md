# Class: transcript to gene relationship


A gene is a collection of transcripts

URI: [biolink:TranscriptToGeneRelationship](https://w3id.org/biolink/vocab/TranscriptToGeneRelationship)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[TranscriptToGeneRelationship|id(i):identifier_type;relation(i):iri_type;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[TranscriptToGeneRelationship],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[TranscriptToGeneRelationship],%20\[OntologyClass]<association%20type(i)%200..1-%20\[TranscriptToGeneRelationship],%20\[Gene]<object%201..1-%20\[TranscriptToGeneRelationship],%20\[Transcript]<subject%201..1-%20\[TranscriptToGeneRelationship],%20\[SequenceFeatureRelationship]^-\[TranscriptToGeneRelationship])
## Parents

 *  is_a: [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene
## Referenced by class

## Attributes

### Own

 * [object](transcript_to_gene_relationship_object.md)  <sub>REQ</sub>
    * range: [Gene](Gene.md)
 * [subject](transcript_to_gene_relationship_subject.md)  <sub>REQ</sub>
    * range: [Transcript](Transcript.md)
### Inherited from association:

 * [id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [Association](Association.md)
    * in subsets: (translator_minimal)
 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [IriType](IriType.md)
    * inherited from: [Association](Association.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [IriType](IriType.md)
    * inherited from: [Association](Association.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [IriType](IriType.md)
    * inherited from: [Association](Association.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](Boolean.md)
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
    * inherited from: [Association](Association.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)
### Inherited from transcript to gene relationship:

 * [subject](transcript_to_gene_relationship_subject.md)  <sub>REQ</sub>
    * range: [Transcript](Transcript.md)
 * [object](transcript_to_gene_relationship_object.md)  <sub>REQ</sub>
    * range: [Gene](Gene.md)
### Domain for slot:

 * [object](transcript_to_gene_relationship_object.md)  <sub>REQ</sub>
    * range: [Gene](Gene.md)
 * [subject](transcript_to_gene_relationship_subject.md)  <sub>REQ</sub>
    * range: [Transcript](Transcript.md)
