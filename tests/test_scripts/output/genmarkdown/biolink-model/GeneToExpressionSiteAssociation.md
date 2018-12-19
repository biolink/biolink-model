# Class: gene to expression site association


An association between a gene and an expression site, possibly qualified by stage/timing info.

URI: [http://w3id.org/biolink/vocab/GeneToExpressionSiteAssociation](http://w3id.org/biolink/vocab/GeneToExpressionSiteAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneToExpressionSiteAssociation|id(i):identifier_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[GeneToExpressionSiteAssociation]-%20publications(i)%20*>\[Publication],%20\[GeneToExpressionSiteAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GeneToExpressionSiteAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GeneToExpressionSiteAssociation]-%20relation>\[RelationshipType],%20\[GeneToExpressionSiteAssociation]-%20object>\[AnatomicalEntity],%20\[GeneToExpressionSiteAssociation]-%20subject>\[GeneOrGeneProduct],%20\[GeneToExpressionSiteAssociation]-%20quantifier%20qualifier%20%3F>\[OntologyClass],%20\[GeneToExpressionSiteAssociation]-%20stage%20qualifier%20%3F>\[LifeStage],%20\[Association]^-\[GeneToExpressionSiteAssociation])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

## Used in

## Fields

 * [gene to expression site association.object](gene_to_expression_site_association_object.md)
    * Description: location in which the gene is expressed
    * range: [AnatomicalEntity](AnatomicalEntity.md) [required]
    * __Local__
 * [gene to expression site association.quantifier qualifier](gene_to_expression_site_association_quantifier_qualifier.md)
    * Description: can be used to indicate magnitude, or also ranking
    * range: [OntologyClass](OntologyClass.md)
    * __Local__
 * [gene to expression site association.relation](gene_to_expression_site_association_relation.md)
    * Description: expression relationship
    * range: [RelationshipType](RelationshipType.md) [required]
    * edge label: [expressed in](expressed_in.md) *subsets*: (translator_minimal)
    * __Local__
 * [gene to expression site association.stage qualifier](gene_to_expression_site_association_stage_qualifier.md)
    * Description: stage at which the gene is expressed in the site
    * range: [LifeStage](LifeStage.md)
    * __Local__
 * [gene to expression site association.subject](gene_to_expression_site_association_subject.md)
    * Description: gene in which variation is correlated with the phenotypic feature
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md) [required]
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
