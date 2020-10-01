
# Type: genotype to genotype part association


Any association between one genotype and a genotypic entity that is a sub-component of it

URI: [biolink:GenotypeToGenotypePartAssociation](https://w3id.org/biolink/vocab/GenotypeToGenotypePartAssociation)


![img](images/GenotypeToGenotypePartAssociation.svg)

## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Referenced by class


## Attributes


### Own

 * [genotype to genotype part association➞object](genotype_to_genotype_part_association_object.md)  <sub>REQ</sub>
    * Description: child genotype
    * range: [Genotype](Genotype.md)
 * [genotype to genotype part association➞relation](genotype_to_genotype_part_association_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [genotype to genotype part association➞subject](genotype_to_genotype_part_association_subject.md)  <sub>REQ</sub>
    * Description: parent genotype
    * range: [Genotype](Genotype.md)

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
