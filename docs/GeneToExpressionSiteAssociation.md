
# Type: gene to expression site association


An association between a gene and an expression site, possibly qualified by stage/timing info.

URI: [biolink:GeneToExpressionSiteAssociation](https://w3id.org/biolink/vocab/GeneToExpressionSiteAssociation)


![img](images/GeneToExpressionSiteAssociation.svg)

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

 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **See also:** | | https://github.com/monarch-initiative/ingest-artifacts/tree/master/sources/BGee |

