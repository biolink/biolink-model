# Class: functional association


An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed

URI: [http://bioentity.io/vocab/FunctionalAssociation](http://bioentity.io/vocab/FunctionalAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Association]^-\[FunctionalAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F],%20\[FunctionalAssociation]^-\[GeneToGoTermAssociation],%20\[FunctionalAssociation]^-\[MacromolecularMachineToBiologicalProcessAssociation],%20\[FunctionalAssociation]^-\[MacromolecularMachineToCellularComponentAssociation],%20\[FunctionalAssociation]^-\[MacromolecularMachineToMolecularActivityAssociation],%20\[FunctionalAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[FunctionalAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[FunctionalAssociation]-%20relation(i)>\[RelationshipType],%20\[FunctionalAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[FunctionalAssociation]-%20publications(i)%20*>\[Publication],%20\[FunctionalAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[FunctionalAssociation]-%20subject>\[MacromolecularMachine],%20\[FunctionalAssociation]-%20object>\[GeneOntologyClass])
## Mappings

## Inheritance

 *  is_a: [association](Association.md) - A typed association between two entities, supported by evidence
## Children

 *  child: [gene to go term association](GeneToGoTermAssociation.md)
 *  child: [macromolecular machine to cellular component association](MacromolecularMachineToCellularComponentAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component
 *  child: [macromolecular machine to molecular activity association](MacromolecularMachineToMolecularActivityAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution
 *  child: [macromolecular machine to biological process association](MacromolecularMachineToBiologicalProcessAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it
## Used in

 *  class: [functional association](FunctionalAssociation.md) references: [gene to go term association](GeneToGoTermAssociation.md)
 *  class: [functional association](FunctionalAssociation.md) references: [macromolecular machine to cellular component association](MacromolecularMachineToCellularComponentAssociation.md)
 *  class: [functional association](FunctionalAssociation.md) references: [macromolecular machine to molecular activity association](MacromolecularMachineToMolecularActivityAssociation.md)
 *  class: [functional association](FunctionalAssociation.md) references: [macromolecular machine to biological process association](MacromolecularMachineToBiologicalProcessAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [macromolecular machine](MacromolecularMachine.md) [required]
    * Example: [ZFIN:ZDB-GENE-050417-357](http://purl.obolibrary.org/obo/ZFIN_ZDB-GENE-050417-357) twist1b
    * __Local__
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [gene ontology class](GeneOntologyClass.md) [required]
    * Example: [GO:0016301](http://purl.obolibrary.org/obo/GO_0016301) kinase activity
    * Example: [GO:0045211](http://purl.obolibrary.org/obo/GO_0045211) postsynaptic membrane
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[association type](association_type.md)_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: [ontology class](OntologyClass.md)
    * inherited from: None
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * inherited from: None
 * _[qualifiers](qualifiers.md)_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: [ontology class](OntologyClass.md)*
    * inherited from: None
 * _[publications](publications.md)_
    * _connects an association to publications supporting the association_
    * range: [publication](Publication.md)*
    * inherited from: None
 * _[provided by](provided_by.md)_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: [provider](Provider.md)
    * inherited from: None
