---
parent: Classes
title: biolink:MacromolecularMachineToCellularComponentAssociation
grand_parent: Browse Biolink Model
---

# Type: MacromolecularMachineToCellularComponentAssociation


A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component

URI: [biolink:MacromolecularMachineToCellularComponentAssociation](https://w3id.org/biolink/vocab/MacromolecularMachineToCellularComponentAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Provider]<provided%20by(i)%200..1-%20\[MacromolecularMachineToCellularComponentAssociation&#124;relation(i):uriorcurie;id(i):nodeidentifier;negated(i):boolean%20%3F],%20\[Publication]<publications(i)%200..*-%20\[MacromolecularMachineToCellularComponentAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[MacromolecularMachineToCellularComponentAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[MacromolecularMachineToCellularComponentAssociation],%20\[MacromolecularMachine]<subject(i)%201..1-%20\[MacromolecularMachineToCellularComponentAssociation],%20\[CellularComponent]<object%201..1-%20\[MacromolecularMachineToCellularComponentAssociation],%20\[FunctionalAssociation]^-\[MacromolecularMachineToCellularComponentAssociation])

---


## Parents

 *  is_a: [FunctionalAssociation](FunctionalAssociation.md) - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed

## Referenced by class


## Attributes


### Own

 * [macromolecular machine to cellular component association➞object](macromolecular_machine_to_cellular_component_association_object.md)  <sub>REQ</sub>
    * range: [CellularComponent](CellularComponent.md)

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

### Inherited from functional association:

 * [functional association➞subject](functional_association_subject.md)  <sub>REQ</sub>
    * range: [MacromolecularMachine](MacromolecularMachine.md)
    * inherited from: [FunctionalAssociation](FunctionalAssociation.md)
 * [functional association➞object](functional_association_object.md)  <sub>REQ</sub>
    * range: [GeneOntologyClass](GeneOntologyClass.md)
    * inherited from: [FunctionalAssociation](FunctionalAssociation.md)

### Domain for slot:

 * [macromolecular machine to cellular component association➞object](macromolecular_machine_to_cellular_component_association_object.md)  <sub>REQ</sub>
    * range: [CellularComponent](CellularComponent.md)
