# Class: gene regulatory relationship


A regulatory relationship between two genes

URI: [http://w3id.org/biolink/vocab/GeneRegulatoryRelationship](http://w3id.org/biolink/vocab/GeneRegulatoryRelationship)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneRegulatoryRelationship|relation:iri_type;id(i):identifier_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[GeneRegulatoryRelationship]-%20publications(i)%20*>\[Publication],%20\[GeneRegulatoryRelationship]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GeneRegulatoryRelationship]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GeneRegulatoryRelationship]-%20object>\[GeneOrGeneProduct],%20\[GeneRegulatoryRelationship]-%20subject>\[GeneOrGeneProduct],%20\[Association]^-\[GeneRegulatoryRelationship])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

## Used in

## Fields

 * [gene regulatory relationship.object](gene_regulatory_relationship_object.md)
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md) [required]
    * __Local__
 * [gene regulatory relationship.relation](gene_regulatory_relationship_relation.md)
    * Description: the direction is always from regulator to regulated
    * range: [IriType](IriType.md) [required]
    * __Local__
 * [gene regulatory relationship.subject](gene_regulatory_relationship_subject.md)
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
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
