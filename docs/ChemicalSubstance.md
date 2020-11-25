---
parent: Entities
title: biolink:ChemicalSubstance
grand_parent: Classes
layout: default
---

# Class: ChemicalSubstance


May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part

URI: [biolink:ChemicalSubstance](https://w3id.org/biolink/vocab/ChemicalSubstance)

SIO:010004
{: .mapping-label }

WIKIDATA:Q79529
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

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ProcessedMaterial],[OrganismTaxon],[NamedThing],[MolecularEntity],[MolecularActivity],[Metabolite],[Food],[DrugExposure],[Drug],[ChemicalToThingAssociation],[ChemicalToChemicalDerivationAssociation],[ChemicalToChemicalAssociation],[ChemicalToChemicalAssociation]-%20object%201..1%3E[ChemicalSubstance%7Cid(i):string;category(i):category_type%20%2B;iri(i):iri_type%20%3F;name(i):label_type%20%3F;source(i):label_type%20%3F],[ChemicalToChemicalDerivationAssociation]-%20object%201..1%3E[ChemicalSubstance],[ChemicalToChemicalDerivationAssociation]-%20subject%201..1%3E[ChemicalSubstance],[ChemicalToThingAssociation]-%20subject%201..1%3E[ChemicalSubstance],[DrugExposure]-%20has%20drug%201..%2A%3E[ChemicalSubstance],[Drug]-%20has%20active%20ingredient%200..%2A%3E[ChemicalSubstance],[Mixture]-%20has%20constituent%200..%2A%3E[ChemicalSubstance],[Drug]-%20has%20excipient%200..%2A%3E[ChemicalSubstance],[Food]-%20has%20nutrient%200..%2A%3E[ChemicalSubstance],[MolecularActivity]-%20has%20input%200..%2A%3E[ChemicalSubstance],[MolecularActivity]-%20has%20output%200..%2A%3E[ChemicalSubstance],[ChemicalSubstance]%5E-[ProcessedMaterial],[ChemicalSubstance]%5E-[Metabolite],[ChemicalSubstance]%5E-[Carbohydrate],[MolecularEntity]%5E-[ChemicalSubstance],[Mixture],[Carbohydrate],[Attribute])

---


## Identifier prefixes

 * CHEBI
 * CHEMBL.COMPOUND
 * DRUGBANK
 * PUBCHEM.COMPOUND
 * MESH
 * HMDB
 * INCHI
 * INCHIKEY
 * UNII
 * KEGG
 * gtpo

## Parents

 *  is_a: [MolecularEntity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)

## Children

 * [Carbohydrate](Carbohydrate.md)
 * [Metabolite](Metabolite.md) - Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
 * [ProcessedMaterial](ProcessedMaterial.md) - A chemical substance (often a mixture) processed for consumption for nutritional, medical or technical use.

## Referenced by class

 *  **[ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md)** *[chemical to chemical association➞object](chemical_to_chemical_association_object.md)*  <sub>REQ</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)** *[chemical to chemical derivation association➞object](chemical_to_chemical_derivation_association_object.md)*  <sub>REQ</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)** *[chemical to chemical derivation association➞subject](chemical_to_chemical_derivation_association_subject.md)*  <sub>REQ</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[ChemicalToThingAssociation](ChemicalToThingAssociation.md)** *[chemical to thing association➞subject](chemical_to_thing_association_subject.md)*  <sub>REQ</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[DrugExposure](DrugExposure.md)** *[drug exposure➞has drug](drug_exposure_has_drug.md)*  <sub>1..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[Drug](Drug.md)** *[has active ingredient](has_active_ingredient.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[NamedThing](NamedThing.md)** *[has constituent](has_constituent.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[Drug](Drug.md)** *[has excipient](has_excipient.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[Food](Food.md)** *[has nutrient](has_nutrient.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[molecular activity➞has input](molecular_activity_has_input.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[molecular activity➞has output](molecular_activity_has_output.md)*  <sub>0..*</sub>  **[ChemicalSubstance](ChemicalSubstance.md)**

## Attributes


### Inherited from attribute mixin:

 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any named thing to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

### Inherited from resource mixin:

 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | SIO:010004 |
|  | | WIKIDATA:Q79529 |
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

