---
parent: Classes
title: biolink:ChemicalToChemicalDerivationAssociation
grand_parent: Browse Biolink Model
---

# Type: ChemicalToChemicalDerivationAssociation


A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:
  IF
  R has-input C1 AND
  R has-output C2 AND
  R enabled-by P AND
  R type Reaction
  THEN
  C1 derives-into C2 <<change is catalyzed by P>>

URI: [biolink:ChemicalToChemicalDerivationAssociation](https://w3id.org/biolink/vocab/ChemicalToChemicalDerivationAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[ChemicalToChemicalDerivationAssociation&#124;relation:uriorcurie;id(i):nodeidentifier;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[ChemicalToChemicalDerivationAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[ChemicalToChemicalDerivationAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[ChemicalToChemicalDerivationAssociation],%20\[MacromolecularMachine]<change%20is%20catalyzed%20by%200..*-%20\[ChemicalToChemicalDerivationAssociation],%20\[ChemicalSubstance]<object%201..1-%20\[ChemicalToChemicalDerivationAssociation],%20\[ChemicalSubstance]<subject%201..1-%20\[ChemicalToChemicalDerivationAssociation],%20\[ChemicalToChemicalAssociation]^-\[ChemicalToChemicalDerivationAssociation])

---


## Parents

 *  is_a: [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) - A relationship between two chemical entities. This can encompass actual interactions as well as temporal causal edges, e.g. one chemical converted to another.

## Referenced by class


## Attributes


### Own

 * [chemical to chemical derivation association➞change is catalyzed by](chemical_to_chemical_derivation_association_change_is_catalyzed_by.md)  <sub>0..*</sub>
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [chemical to chemical derivation association➞object](chemical_to_chemical_derivation_association_object.md)  <sub>REQ</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [chemical to chemical derivation association➞relation](chemical_to_chemical_derivation_association_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [chemical to chemical derivation association➞subject](chemical_to_chemical_derivation_association_subject.md)  <sub>REQ</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)

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

 * [chemical to chemical derivation association➞change is catalyzed by](chemical_to_chemical_derivation_association_change_is_catalyzed_by.md)  <sub>0..*</sub>
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [chemical to chemical derivation association➞object](chemical_to_chemical_derivation_association_object.md)  <sub>REQ</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [chemical to chemical derivation association➞relation](chemical_to_chemical_derivation_association_relation.md)  <sub>REQ</sub>
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [chemical to chemical derivation association➞subject](chemical_to_chemical_derivation_association_subject.md)  <sub>REQ</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)
