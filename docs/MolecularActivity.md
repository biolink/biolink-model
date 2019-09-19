
# Class: molecular activity


An execution of a molecular function carried out by a gene product or macromolecular complex.

URI: [biolink:MolecularActivity](https://w3id.org/biolink/vocab/MolecularActivity)

![img](images/MolecularActivity.png)

## Parents

 *  is_a: [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) - Either an individual molecular activity, or a collection of causally connected molecular activities

## Uses Mixins

 *  mixin: [Occurrent](Occurrent.md) - A processual entity

## Referenced by class

 *  **[MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md)** *[object](macromolecular_machine_to_molecular_activity_association_object.md)*  <sub>REQ</sub>  **[MolecularActivity](MolecularActivity.md)**

## Attributes


### Own

 * [enabled by](molecular_activity_enabled_by.md)  <sub>0..*</sub>
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [has input](molecular_activity_has_input.md)  <sub>0..*</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [has output](molecular_activity_has_output.md)  <sub>0..*</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [enabled by](molecular_activity_enabled_by.md)  <sub>0..*</sub>
    * range: [MacromolecularMachine](MacromolecularMachine.md)
 * [has input](molecular_activity_has_input.md)  <sub>0..*</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)
 * [has output](molecular_activity_has_output.md)  <sub>0..*</sub>
    * range: [ChemicalSubstance](ChemicalSubstance.md)
