
# Class: genotype to genotype part association


Any association between one genotype and a genotypic entity that is a sub-component of it

URI: [biolink:GenotypeToGenotypePartAssociation](https://w3id.org/biolink/vocab/GenotypeToGenotypePartAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[GenotypeToGenotypePartAssociation|relation:iri_type;id(i):identifier_type;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[GenotypeToGenotypePartAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[GenotypeToGenotypePartAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[GenotypeToGenotypePartAssociation],%20\[Genotype]<object%201..1-%20\[GenotypeToGenotypePartAssociation],%20\[Genotype]<subject%201..1-%20\[GenotypeToGenotypePartAssociation],%20\[Association]^-\[GenotypeToGenotypePartAssociation])

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [object](genotype_to_genotype_part_association_object.md)  <sub>REQ</sub>
    * range: [Genotype](Genotype.md)
 * [relation](genotype_to_genotype_part_association_relation.md)  <sub>REQ</sub>
    * range: [IriType](IriType.md)
 * [subject](genotype_to_genotype_part_association_subject.md)  <sub>REQ</sub>
    * range: [Genotype](Genotype.md)

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

### Domain for slot:

 * [object](genotype_to_genotype_part_association_object.md)  <sub>REQ</sub>
    * range: [Genotype](Genotype.md)
 * [relation](genotype_to_genotype_part_association_relation.md)  <sub>REQ</sub>
    * range: [IriType](IriType.md)
 * [subject](genotype_to_genotype_part_association_subject.md)  <sub>REQ</sub>
    * range: [Genotype](Genotype.md)
