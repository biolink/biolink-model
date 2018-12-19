# Class: genotype to genotype part association


Any association between one genotype and a genotypic entity that is a sub-component of it

URI: [http://w3id.org/biolink/vocab/GenotypeToGenotypePartAssociation](http://w3id.org/biolink/vocab/GenotypeToGenotypePartAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GenotypeToGenotypePartAssociation|relation:iri_type;id(i):identifier_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[GenotypeToGenotypePartAssociation]-%20publications(i)%20*>\[Publication],%20\[GenotypeToGenotypePartAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GenotypeToGenotypePartAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GenotypeToGenotypePartAssociation]-%20object>\[Genotype],%20\[GenotypeToGenotypePartAssociation]-%20subject>\[Genotype],%20\[Association]^-\[GenotypeToGenotypePartAssociation])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

## Used in

## Fields

 * [genotype to genotype part association.object](genotype_to_genotype_part_association_object.md)
    * Description: child genotype
    * range: [Genotype](Genotype.md) [required]
    * __Local__
 * [genotype to genotype part association.relation](genotype_to_genotype_part_association_relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [IriType](IriType.md) [required]
    * __Local__
 * [genotype to genotype part association.subject](genotype_to_genotype_part_association_subject.md)
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
