# Class: genotype to variant association


Any association between a genotype and a sequence variant.

URI: [http://w3id.org/biolink/vocab/GenotypeToVariantAssociation](http://w3id.org/biolink/vocab/GenotypeToVariantAssociation)

![img](images/GenotypeToVariantAssociation.png)
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

## Used in

## Fields

 * [genotype to variant association.object](genotype_to_variant_association_object.md)
    * Description: gene implicated in genotype
    * range: [SequenceVariant](SequenceVariant.md) [required]
    * __Local__
 * [genotype to variant association.relation](genotype_to_variant_association_relation.md)
    * Description: the relationship type used to connect genotype to gene
    * range: [RelationshipType](RelationshipType.md) [required]
    * __Local__
 * [genotype to variant association.subject](genotype_to_variant_association_subject.md)
    * Description: parent genotype
    * range: [Genotype](Genotype.md) [required]
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
