---
parent: Classes
title: biolink:ChemicalSubstance
grand_parent: Browse Biolink Model
---

# Type: ChemicalSubstance


May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part

URI: [biolink:ChemicalSubstance](https://w3id.org/biolink/vocab/ChemicalSubstance)

SIO:010004
{: .mapping-label }

WD:Q79529
{: .mapping-label }

UMLSSC:T167
{: .mapping-label }

UMLSST:sbst
{: .mapping-label }

UMLSSG:CHEM
{: .mapping-label }

UMLSSC:T103
{: .mapping-label }

UMLSST:chem
{: .mapping-label }

UMLSSC:T104
{: .mapping-label }

UMLSST:chvs
{: .mapping-label }

UMLSSC:T109
{: .mapping-label }

UMLSST:orch
{: .mapping-label }

UMLSSC:T114
{: .mapping-label }

UMLSST:nnon
{: .mapping-label }

UMLSSC:T120
{: .mapping-label }

UMLSST:chvf
{: .mapping-label }

UMLSSC:T121
{: .mapping-label }

UMLSST:phsu
{: .mapping-label }

UMLSSC:T122
{: .mapping-label }

UMLSST:bodm
{: .mapping-label }

UMLSSC:T123
{: .mapping-label }

UMLSST:bacs
{: .mapping-label }

UMLSSC:T125
{: .mapping-label }

UMLSST:horm
{: .mapping-label }

UMLSSC:T126
{: .mapping-label }

UMLSST:enzy
{: .mapping-label }

UMLSSC:T127
{: .mapping-label }

UMLSST:vita
{: .mapping-label }

UMLSSC:T129
{: .mapping-label }

UMLSST:imft
{: .mapping-label }

UMLSSC:T130
{: .mapping-label }

UMLSST:irda
{: .mapping-label }

UMLSSC:T131
{: .mapping-label }

UMLSST:hops
{: .mapping-label }

UMLSSC:T192
{: .mapping-label }

UMLSST:rcpt
{: .mapping-label }

UMLSSC:T195
{: .mapping-label }

UMLSST:antb
{: .mapping-label }

UMLSSC:T196
{: .mapping-label }

UMLSST:elii
{: .mapping-label }

UMLSSC:T197
{: .mapping-label }

UMLSST:inch
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[ChemicalSubstance&#124;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[ChemicalToChemicalAssociation]-%20object%201..1>\[ChemicalSubstance],%20\[ChemicalToChemicalDerivationAssociation]-%20object%201..1>\[ChemicalSubstance],%20\[ChemicalToChemicalDerivationAssociation]-%20subject%201..1>\[ChemicalSubstance],%20\[ChemicalToThingAssociation]-%20subject%201..1>\[ChemicalSubstance],%20\[MolecularActivity]-%20has%20input%200..*>\[ChemicalSubstance],%20\[MolecularActivity]-%20has%20output%200..*>\[ChemicalSubstance],%20\[ChemicalSubstance]^-\[Metabolite],%20\[ChemicalSubstance]^-\[Drug],%20\[ChemicalSubstance]^-\[Carbohydrate],%20\[MolecularEntity]^-\[ChemicalSubstance])

---


## Parents

 *  is_a: [MolecularEntity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)

## Children

 * [Carbohydrate](Carbohydrate.md)
 * [Drug](Drug.md) - A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
 * [Metabolite](Metabolite.md) - Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.

## Referenced by class

 *  **[ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md)** *[chemical to chemical association➞object](chemical_to_chemical_association_object.md)*  <sub>REQ</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)** *[chemical to chemical derivation association➞object](chemical_to_chemical_derivation_association_object.md)*  <sub>REQ</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)** *[chemical to chemical derivation association➞subject](chemical_to_chemical_derivation_association_subject.md)*  <sub>REQ</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[ChemicalToThingAssociation](ChemicalToThingAssociation.md)** *[chemical to thing association➞subject](chemical_to_thing_association_subject.md)*  <sub>REQ</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[DrugExposure](DrugExposure.md)** *[drug exposure➞has drug](drug_exposure_has_drug.md)*  <sub>1..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[molecular activity➞has input](molecular_activity_has_input.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[molecular activity➞has output](molecular_activity_has_output.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**

## Attributes


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

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SIO:010004 |
|  | | WD:Q79529 |
|  | | UMLSSC:T167 |
|  | | UMLSST:sbst |
|  | | UMLSSG:CHEM |
|  | | UMLSSC:T103 |
|  | | UMLSST:chem |
|  | | UMLSSC:T104 |
|  | | UMLSST:chvs |
|  | | UMLSSC:T109 |
|  | | UMLSST:orch |
|  | | UMLSSC:T114 |
|  | | UMLSST:nnon |
|  | | UMLSSC:T120 |
|  | | UMLSST:chvf |
|  | | UMLSSC:T121 |
|  | | UMLSST:phsu |
|  | | UMLSSC:T122 |
|  | | UMLSST:bodm |
|  | | UMLSSC:T123 |
|  | | UMLSST:bacs |
|  | | UMLSSC:T125 |
|  | | UMLSST:horm |
|  | | UMLSSC:T126 |
|  | | UMLSST:enzy |
|  | | UMLSSC:T127 |
|  | | UMLSST:vita |
|  | | UMLSSC:T129 |
|  | | UMLSST:imft |
|  | | UMLSSC:T130 |
|  | | UMLSST:irda |
|  | | UMLSSC:T131 |
|  | | UMLSST:hops |
|  | | UMLSSC:T192 |
|  | | UMLSST:rcpt |
|  | | UMLSSC:T195 |
|  | | UMLSST:antb |
|  | | UMLSSC:T196 |
|  | | UMLSST:elii |
|  | | UMLSSC:T197 |
|  | | UMLSST:inch |

