---
parent: Classes
title: biolink:GeneToExpressionSiteAssociation
grand_parent: Browse Biolink Model
layout: default
---

# Type: GeneToExpressionSiteAssociation


An association between a gene and an expression site, possibly qualified by stage/timing info.

URI: [biolink:GeneToExpressionSiteAssociation](https://w3id.org/biolink/vocab/GeneToExpressionSiteAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[OntologyClass],[LifeStage],[AnatomicalEntity]%3Cobject%201..1-%20[GeneToExpressionSiteAssociation%7Crelation:uriorcurie;id(i):string;negated(i):boolean%20%3F],[GeneOrGeneProduct]%3Csubject%201..1-%20[GeneToExpressionSiteAssociation],[OntologyClass]%3Cquantifier%20qualifier%200..1-%20[GeneToExpressionSiteAssociation],[LifeStage]%3Cstage%20qualifier%200..1-%20[GeneToExpressionSiteAssociation],[Association]%5E-[GeneToExpressionSiteAssociation],[GeneOrGeneProduct],[Association],[AnatomicalEntity])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [gene to expression site association➞object](gene_to_expression_site_association_object.md)  <sub>REQ</sub>
    * Description: location in which the gene is expressed
    * range: [AnatomicalEntity](AnatomicalEntity.md)
    * Example:    
 * [gene to expression site association➞quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)  <sub>OPT</sub>
    * Description: can be used to indicate magnitude, or also ranking
    * range: [OntologyClass](OntologyClass.md)
 * [gene to expression site association➞relation](gene_to_expression_site_association_relation.md)  <sub>REQ</sub>
    * Description: expression relationship
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [gene to expression site association➞stage qualifier](gene_to_expression_site_association_stage_qualifier.md)  <sub>OPT</sub>
    * Description: stage at which the gene is expressed in the site
    * range: [LifeStage](LifeStage.md)
    * Example:    
 * [gene to expression site association➞subject](gene_to_expression_site_association_subject.md)  <sub>REQ</sub>
    * Description: gene in which variation is correlated with the phenotypic feature
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)

### Domain for slot:

 * [gene to expression site association➞object](gene_to_expression_site_association_object.md)  <sub>REQ</sub>
    * Description: location in which the gene is expressed
    * range: [AnatomicalEntity](AnatomicalEntity.md)
    * Example:    
 * [gene to expression site association➞quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)  <sub>OPT</sub>
    * Description: can be used to indicate magnitude, or also ranking
    * range: [OntologyClass](OntologyClass.md)
 * [gene to expression site association➞relation](gene_to_expression_site_association_relation.md)  <sub>REQ</sub>
    * Description: expression relationship
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [gene to expression site association➞stage qualifier](gene_to_expression_site_association_stage_qualifier.md)  <sub>OPT</sub>
    * Description: stage at which the gene is expressed in the site
    * range: [LifeStage](LifeStage.md)
    * Example:    
 * [gene to expression site association➞subject](gene_to_expression_site_association_subject.md)  <sub>REQ</sub>
    * Description: gene in which variation is correlated with the phenotypic feature
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **See also:** | | https://github.com/monarch-initiative/ingest-artifacts/tree/master/sources/BGee |

