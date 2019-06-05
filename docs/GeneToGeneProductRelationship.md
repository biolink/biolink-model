# Class: gene to gene product relationship


A gene is transcribed and potentially translated to a gene product

URI: [biolink:GeneToGeneProductRelationship](https://w3id.org/biolink/vocab/GeneToGeneProductRelationship)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ClinicalModifier]<clinical%20modifier%20qualifier(i)%200..1-%20\[GeneToGeneProductRelationship|relation:iri_type;id(i):identifier_type;negated(i):boolean%20%3F;association_slot(i):string%20%3F;edge_label(i):label_type%20%3F],%20\[EvidenceType]<has%20evidence(i)%200..1-%20\[GeneToGeneProductRelationship],%20\[ConfidenceLevel]<has%20confidence%20level(i)%200..1-%20\[GeneToGeneProductRelationship],%20\[Provider]<provided%20by(i)%200..1-%20\[GeneToGeneProductRelationship],%20\[Publication]<publications(i)%200..*-%20\[GeneToGeneProductRelationship],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[GeneToGeneProductRelationship],%20\[OntologyClass]<association%20type(i)%200..1-%20\[GeneToGeneProductRelationship],%20\[GeneProduct]<object%201..1-%20\[GeneToGeneProductRelationship],%20\[Gene]<subject%201..1-%20\[GeneToGeneProductRelationship],%20\[SequenceFeatureRelationship]^-\[GeneToGeneProductRelationship])
## Inheritance

 *  is_a: [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene
## Children

## Used by

## Fields

 * [association slot](association_slot.md)  <sub>OPT</sub>
    * Description: any slot that relates an association to another entity
    * range: [String](String.md)
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [association.id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [Association](Association.md)
    * in subsets: (translator_minimal)
 * [gene to gene product relationship.object](gene_to_gene_product_relationship_object.md)  <sub>REQ</sub>
    * range: [GeneProduct](GeneProduct.md)
 * [gene to gene product relationship.relation](gene_to_gene_product_relationship_relation.md)  <sub>REQ</sub>
    * range: [IriType](IriType.md)
 * [gene to gene product relationship.subject](gene_to_gene_product_relationship_subject.md)  <sub>REQ</sub>
    * range: [Gene](Gene.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](Boolean.md)
    * inherited from: [Association](Association.md)
 * [provided by](provided_by.md)  <sub>OPT</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
