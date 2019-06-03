# Class: genotype to genotype part association


Any association between one genotype and a genotypic entity that is a sub-component of it

URI: [biolink:GenotypeToGenotypePartAssociation](https://w3id.org/biolink/vocab/GenotypeToGenotypePartAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ClinicalModifier]<clinical%20modifier%20qualifier(i)%200..1-%20\[GenotypeToGenotypePartAssociation|relation:iri_type;id(i):identifier_type;negated(i):boolean%20%3F;association_slot(i):string%20%3F;edge_label(i):label_type%20%3F],%20\[EvidenceType]<has%20evidence(i)%200..1-%20\[GenotypeToGenotypePartAssociation],%20\[ConfidenceLevel]<has%20confidence%20level(i)%200..1-%20\[GenotypeToGenotypePartAssociation],%20\[Provider]<provided%20by(i)%200..1-%20\[GenotypeToGenotypePartAssociation],%20\[Publication]<publications(i)%200..*-%20\[GenotypeToGenotypePartAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[GenotypeToGenotypePartAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[GenotypeToGenotypePartAssociation],%20\[Genotype]<object%201..1-%20\[GenotypeToGenotypePartAssociation],%20\[Genotype]<subject%201..1-%20\[GenotypeToGenotypePartAssociation],%20\[Association]^-\[GenotypeToGenotypePartAssociation])
## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
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
 * [genotype to genotype part association.object](genotype_to_genotype_part_association_object.md)  <sub>REQ</sub>
    * range: [Genotype](Genotype.md)
 * [genotype to genotype part association.relation](genotype_to_genotype_part_association_relation.md)  <sub>REQ</sub>
    * range: [IriType](IriType.md)
 * [genotype to genotype part association.subject](genotype_to_genotype_part_association_subject.md)  <sub>REQ</sub>
    * range: [Genotype](Genotype.md)
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
