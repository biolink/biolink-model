---
parent: Classes
title: biolink:MacromolecularMachineToBiologicalProcessAssociation
grand_parent: Browse Biolink Model
layout: default
---

# Class: MacromolecularMachineToBiologicalProcessAssociation


A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it

URI: [biolink:MacromolecularMachineToBiologicalProcessAssociation](https://w3id.org/biolink/vocab/MacromolecularMachineToBiologicalProcessAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[Provider],[OntologyClass],[BiologicalProcess]%3Cobject%201..1-%20[MacromolecularMachineToBiologicalProcessAssociation%7Crelation(i):uriorcurie;id(i):string;negated(i):boolean%20%3F],[FunctionalAssociation]%5E-[MacromolecularMachineToBiologicalProcessAssociation],[MacromolecularMachine],[FunctionalAssociation],[BiologicalProcess])

---


## Parents

 *  is_a: [FunctionalAssociation](FunctionalAssociation.md) - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed

## Referenced by class


## Attributes


### Own

 * [macromolecular machine to biological process association➞object](macromolecular_machine_to_biological_process_association_object.md)  <sub>REQ</sub>
    * range: [BiologicalProcess](BiologicalProcess.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [association➞id](association_id.md)  <sub>REQ</sub>
    * Description: A unique identifier for an association
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [association type](association_type.md)  <sub>OPT</sub>
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)

### Inherited from functional association:

 * [functional association➞subject](functional_association_subject.md)  <sub>REQ</sub>
    * Description: gene, product or macromolecular complex that has the function associated with the GO term
    * range: [MacromolecularMachine](MacromolecularMachine.md)
    * Example:    
 * [functional association➞object](functional_association_object.md)  <sub>REQ</sub>
    * Description: class describing the activity, process or localization of the gene product
    * range: [GeneOntologyClass](GeneOntologyClass.md)
    * Example:    
    * Example:    

### Domain for slot:

 * [macromolecular machine to biological process association➞object](macromolecular_machine_to_biological_process_association_object.md)  <sub>REQ</sub>
    * range: [BiologicalProcess](BiologicalProcess.md)
