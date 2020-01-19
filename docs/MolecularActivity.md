---
parent: Classes
title: biolink:MolecularActivity
grand_parent: Browse Biolink Model
---

# Type: MolecularActivity


An execution of a molecular function carried out by a gene product or macromolecular complex.

URI: [biolink:MolecularActivity](https://w3id.org/biolink/vocab/MolecularActivity)

GO:0003674
{: .mapping-label }

UMLSSC:T044
{: .mapping-label }

UMLSST:moft
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[MacromolecularMachine]<enabled%20by%200..*-%20\[MolecularActivity&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[ChemicalSubstance]<has%20output%200..*-%20\[MolecularActivity],%20\[ChemicalSubstance]<has%20input%200..*-%20\[MolecularActivity],%20\[MacromolecularMachineToMolecularActivityAssociation]-%20object%201..1>\[MolecularActivity],%20\[MolecularActivity]uses%20-.->\[Occurrent],%20\[BiologicalProcessOrActivity]^-\[MolecularActivity])

---


## Parents

 *  is_a: [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity

## Referenced by class

 *  **[MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md)** *[macromolecular machine to molecular activity association➞object](macromolecular_machine_to_molecular_activity_association_object.md)*  <sub>REQ</sub>  **[MolecularActivity](MolecularActivity.md)**

## Attributes


### Own

 * [molecular activity➞enabled by](molecular_activity_enabled_by.md)  <sub>0..*</sub>
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [molecular activity➞has input](molecular_activity_has_input.md)  <sub>0..*</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [molecular activity➞has output](molecular_activity_has_output.md)  <sub>0..*</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [molecular activity➞enabled by](molecular_activity_enabled_by.md)  <sub>0..*</sub>
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [molecular activity➞has input](molecular_activity_has_input.md)  <sub>0..*</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [molecular activity➞has output](molecular_activity_has_output.md)  <sub>0..*</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | molecular function |
|  | | molecular event |
|  | | reaction |
| **Mappings:** | | GO:0003674 |
|  | | UMLSSC:T044 |
|  | | UMLSST:moft |

