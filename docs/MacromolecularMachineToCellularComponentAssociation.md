# Class: macromolecular machine to cellular component association


A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component

URI: [biolink:MacromolecularMachineToCellularComponentAssociation](https://w3id.org/biolink/vocab/MacromolecularMachineToCellularComponentAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ClinicalModifier]<clinical%20modifier%20qualifier(i)%200..1-%20\[MacromolecularMachineToCellularComponentAssociation|id(i):identifier_type;relation(i):iri_type;negated(i):boolean%20%3F;association_slot(i):string%20%3F;edge_label(i):label_type%20%3F],%20\[EvidenceType]<has%20evidence(i)%200..1-%20\[MacromolecularMachineToCellularComponentAssociation],%20\[ConfidenceLevel]<has%20confidence%20level(i)%200..1-%20\[MacromolecularMachineToCellularComponentAssociation],%20\[Provider]<provided%20by(i)%200..1-%20\[MacromolecularMachineToCellularComponentAssociation],%20\[Publication]<publications(i)%200..*-%20\[MacromolecularMachineToCellularComponentAssociation],%20\[OntologyClass]<qualifiers(i)%200..*-%20\[MacromolecularMachineToCellularComponentAssociation],%20\[OntologyClass]<association%20type(i)%200..1-%20\[MacromolecularMachineToCellularComponentAssociation],%20\[MacromolecularMachine]<subject(i)%201..1-%20\[MacromolecularMachineToCellularComponentAssociation],%20\[CellularComponent]<object%201..1-%20\[MacromolecularMachineToCellularComponentAssociation],%20\[FunctionalAssociation]^-\[MacromolecularMachineToCellularComponentAssociation])
## Inheritance

 *  is_a: [FunctionalAssociation](FunctionalAssociation.md) - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed
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
 * [functional association.subject](functional_association_subject.md)  <sub>REQ</sub>
    * range: [MacromolecularMachine](MacromolecularMachine.md)
    * inherited from: [FunctionalAssociation](FunctionalAssociation.md)
 * [macromolecular machine to cellular component association.object](macromolecular_machine_to_cellular_component_association_object.md)  <sub>REQ</sub>
    * range: [CellularComponent](CellularComponent.md)
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
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [IriType](IriType.md)
    * inherited from: [Association](Association.md)
