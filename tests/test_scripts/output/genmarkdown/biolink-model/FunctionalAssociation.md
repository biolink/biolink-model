# Class: functional association


An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed

URI: [http://w3id.org/biolink/vocab/FunctionalAssociation](http://w3id.org/biolink/vocab/FunctionalAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[FunctionalAssociation|id(i):identifier_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[FunctionalAssociation]-%20publications(i)%20*>\[Publication],%20\[FunctionalAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[FunctionalAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[FunctionalAssociation]-%20relation(i)>\[RelationshipType],%20\[FunctionalAssociation]-%20object>\[GeneOntologyClass],%20\[FunctionalAssociation]-%20subject>\[MacromolecularMachine],%20\[FunctionalAssociation]^-\[MacromolecularMachineToMolecularActivityAssociation],%20\[FunctionalAssociation]^-\[MacromolecularMachineToCellularComponentAssociation],%20\[FunctionalAssociation]^-\[MacromolecularMachineToBiologicalProcessAssociation],%20\[FunctionalAssociation]^-\[GeneToGoTermAssociation],%20\[Association]^-\[FunctionalAssociation])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

 * [GeneToGoTermAssociation](GeneToGoTermAssociation.md)
 * [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it
 * [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component
 * [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution
## Used in

## Fields

 * [functional association.object](functional_association_object.md)
    * Description: class describing the activity, process or localization of the gene product
    * range: [GeneOntologyClass](GeneOntologyClass.md) [required]
    * __Local__
 * [functional association.subject](functional_association_subject.md)
    * Description: gene, product or macromolecular complex that has the function associated with the GO term
    * range: [MacromolecularMachine](MacromolecularMachine.md) [required]
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
 * [relation](relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [RelationshipType](RelationshipType.md) [required]
    * inherited from: [Association](Association.md)
