---
parent: Classes
title: biolink:GeneToGeneProductRelationship
grand_parent: Browse Biolink Model
---

# Type: GeneToGeneProductRelationship


A gene is transcribed and potentially translated to a gene product

URI: [biolink:GeneToGeneProductRelationship](https://w3id.org/biolink/vocab/GeneToGeneProductRelationship)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[GeneToGeneProductRelationship&#124;relation:uriorcurie;id(i):nodeidentifier;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[GeneToGeneProductRelationship],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[GeneToGeneProductRelationship],%20\[OntologyClass]<association%20type(i)%200..1-%20\[GeneToGeneProductRelationship],%20\[GeneProduct]<object%201..1-%20\[GeneToGeneProductRelationship],%20\[Gene]<subject%201..1-%20\[GeneToGeneProductRelationship],%20\[SequenceFeatureRelationship]^-\[GeneToGeneProductRelationship])

---


## Parents

 *  is_a: [SequenceFeatureRelationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene

## Referenced by class


## Attributes


### Own

 * [gene to gene product relationship➞object](gene_to_gene_product_relationship_object.md)  <sub>REQ</sub>
    * range: [GeneProduct](GeneProduct.md)
 * [gene to gene product relationship➞relation](gene_to_gene_product_relationship_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [gene to gene product relationship➞subject](gene_to_gene_product_relationship_subject.md)  <sub>REQ</sub>
    * range: [Gene](Gene.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Association](Association.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [Uriorcurie](types/Uriorcurie.md)
    * inherited from: [Association](Association.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Association](Association.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [Nodeidentifier](types/Nodeidentifier.md)
    * inherited from: [Association](Association.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
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

### Domain for slot:

 * [gene to gene product relationship➞object](gene_to_gene_product_relationship_object.md)  <sub>REQ</sub>
    * range: [GeneProduct](GeneProduct.md)
 * [gene to gene product relationship➞relation](gene_to_gene_product_relationship_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [gene to gene product relationship➞subject](gene_to_gene_product_relationship_subject.md)  <sub>REQ</sub>
    * range: [Gene](Gene.md)
