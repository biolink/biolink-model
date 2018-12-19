# Class: macromolecular machine to biological process association


A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it

URI: [http://w3id.org/biolink/vocab/MacromolecularMachineToBiologicalProcessAssociation](http://w3id.org/biolink/vocab/MacromolecularMachineToBiologicalProcessAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[MacromolecularMachineToBiologicalProcessAssociation|id(i):identifier_type%20%3F;relation(i):iri_type;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20subject(i)>\[MacromolecularMachine],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20publications(i)%20*>\[Publication],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20object>\[BiologicalProcess],%20\[FunctionalAssociation]^-\[MacromolecularMachineToBiologicalProcessAssociation])
## Mappings

## Inheritance

 *  is_a: [FunctionalAssociation](FunctionalAssociation.md) - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed
## Children

## Used in

## Fields

 * [macromolecular machine to biological process association.object](macromolecular_machine_to_biological_process_association_object.md)
    * Description: class describing the activity, process or localization of the gene product
    * range: [BiologicalProcess](BiologicalProcess.md) [required]
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
 * [functional association.subject](functional_association_subject.md)
    * Description: gene, product or macromolecular complex that has the function associated with the GO term
    * range: [MacromolecularMachine](MacromolecularMachine.md) [required]
    * inherited from: [FunctionalAssociation](FunctionalAssociation.md)
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
 * [relation](relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [IriType](IriType.md) [required]
    * inherited from: [Association](Association.md)
