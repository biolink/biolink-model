---
parent: Classes
title: biolink:GeneToExpressionSiteAssociation
grand_parent: Browse Biolink Model
---

# Type: GeneToExpressionSiteAssociation


An association between a gene and an expression site, possibly qualified by stage/timing info.

URI: [biolink:GeneToExpressionSiteAssociation](https://w3id.org/biolink/vocab/GeneToExpressionSiteAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[GeneToExpressionSiteAssociation&#124;relation:uriorcurie;id(i):nodeidentifier;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[GeneToExpressionSiteAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[GeneToExpressionSiteAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[GeneToExpressionSiteAssociation],%20\[OntologyClass]<quantifier%20qualifier%200..1-%20\[GeneToExpressionSiteAssociation],%20\[LifeStage]<stage%20qualifier%200..1-%20\[GeneToExpressionSiteAssociation],%20\[AnatomicalEntity]<object%201..1-%20\[GeneToExpressionSiteAssociation],%20\[GeneOrGeneProduct]<subject%201..1-%20\[GeneToExpressionSiteAssociation],%20\[Association]^-\[GeneToExpressionSiteAssociation])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [gene to expression site association➞object](gene_to_expression_site_association_object.md)  <sub>REQ</sub>
    * range: [AnatomicalEntity](AnatomicalEntity.md)
 * [gene to expression site association➞quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)  <sub>OPT</sub>
    * range: [OntologyClass](OntologyClass.md)
 * [gene to expression site association➞relation](gene_to_expression_site_association_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [gene to expression site association➞stage qualifier](gene_to_expression_site_association_stage_qualifier.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [gene to expression site association➞subject](gene_to_expression_site_association_subject.md)  <sub>REQ</sub>
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)

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

 * [gene to expression site association➞object](gene_to_expression_site_association_object.md)  <sub>REQ</sub>
    * range: [AnatomicalEntity](AnatomicalEntity.md)
 * [gene to expression site association➞quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)  <sub>OPT</sub>
    * range: [OntologyClass](OntologyClass.md)
 * [gene to expression site association➞relation](gene_to_expression_site_association_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [gene to expression site association➞stage qualifier](gene_to_expression_site_association_stage_qualifier.md)  <sub>OPT</sub>
    * range: [LifeStage](LifeStage.md)
 * [gene to expression site association➞subject](gene_to_expression_site_association_subject.md)  <sub>REQ</sub>
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **See also:** | | h |
|  | | t |
|  | | t |
|  | | p |
|  | | s |
|  | | : |
|  | | / |
|  | | / |
|  | | g |
|  | | i |
|  | | t |
|  | | h |
|  | | u |
|  | | b |
|  | | . |
|  | | c |
|  | | o |
|  | | m |
|  | | / |
|  | | m |
|  | | o |
|  | | n |
|  | | a |
|  | | r |
|  | | c |
|  | | h |
|  | | - |
|  | | i |
|  | | n |
|  | | i |
|  | | t |
|  | | i |
|  | | a |
|  | | t |
|  | | i |
|  | | v |
|  | | e |
|  | | / |
|  | | i |
|  | | n |
|  | | g |
|  | | e |
|  | | s |
|  | | t |
|  | | - |
|  | | a |
|  | | r |
|  | | t |
|  | | i |
|  | | f |
|  | | a |
|  | | c |
|  | | t |
|  | | s |
|  | | / |
|  | | t |
|  | | r |
|  | | e |
|  | | e |
|  | | / |
|  | | m |
|  | | a |
|  | | s |
|  | | t |
|  | | e |
|  | | r |
|  | | / |
|  | | s |
|  | | o |
|  | | u |
|  | | r |
|  | | c |
|  | | e |
|  | | s |
|  | | / |
|  | | B |
|  | | G |
|  | | e |
|  | | e |

