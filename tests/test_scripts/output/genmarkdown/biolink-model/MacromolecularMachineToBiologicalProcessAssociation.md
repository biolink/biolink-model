# Class: macromolecular machine to biological process association


A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it

URI: [http://bioentity.io/vocab/MacromolecularMachineToBiologicalProcessAssociation](http://bioentity.io/vocab/MacromolecularMachineToBiologicalProcessAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[FunctionalAssociation]^-\[MacromolecularMachineToBiologicalProcessAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20relation(i)>\[RelationshipType],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20publications(i)%20*>\[Publication],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20subject(i)>\[MacromolecularMachine],%20\[MacromolecularMachineToBiologicalProcessAssociation]-%20object>\[BiologicalProcess])
## Mappings

## Inheritance

 *  is_a: [functional association](FunctionalAssociation.md) - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed
## Children

## Used in

## Fields

 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [biological process](BiologicalProcess.md) [required]
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
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [macromolecular machine](MacromolecularMachine.md) [required]
    * Example: [ZFIN:ZDB-GENE-050417-357](http://purl.obolibrary.org/obo/ZFIN_ZDB-GENE-050417-357) twist1b
    * inherited from: [functional association](FunctionalAssociation.md)
