---
parent: Entities
title: biolink:ChemicalEntity
grand_parent: Classes
layout: default
---

# Class: ChemicalEntity


A chemical entity is a physical entity that pertains to chemistry or biochemistry.

URI: [biolink:ChemicalEntity](https://w3id.org/biolink/vocab/ChemicalEntity)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PhysicalEssence],[NamedThing],[MolecularEntity],[MolecularActivityToChemicalEntityAssociation],[GeneAffectsChemicalAssociation],[FoodAdditive],[EnvironmentalFoodContaminant],[ChemicalToPathwayAssociation],[ChemicalToChemicalDerivationAssociation],[ChemicalToChemicalAssociation],[ChemicalRole],[ChemicalOrDrugOrTreatment],[ChemicalMixture],[ChemicalGeneInteractionAssociation],[ChemicalEntityOrProteinOrPolypeptide],[ChemicalEntityOrGeneOrGeneProduct],[ChemicalEntityAssessesNamedThingAssociation],[ChemicalRole]%3Chas%20chemical%20role%200..%2A-%20[ChemicalEntity%7Cavailable_from:DrugAvailabilityEnum%20%2A;max_tolerated_dose:string%20%3F;is_toxic:boolean%20%3F;provided_by(i):string%20%2A;xref(i):uriorcurie%20%2A;full_name(i):label_type%20%3F;synonym(i):label_type%20%2A;category(i):category_type%20%2B;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%2A;name(i):label_type%20%3F;description(i):narrative_text%20%3F],[ChemicalEntity]%3Ctrade%20name%200..1-%20[ChemicalEntity],[ChemicalAffectsGeneAssociation]-%20subject%201..1%3E[ChemicalEntity],[ChemicalEntityAssessesNamedThingAssociation]-%20subject%201..1%3E[ChemicalEntity],[ChemicalGeneInteractionAssociation]-%20subject%201..1%3E[ChemicalEntity],[ChemicalToChemicalAssociation]-%20object%201..1%3E[ChemicalEntity],[ChemicalToChemicalDerivationAssociation]-%20object%201..1%3E[ChemicalEntity],[ChemicalToChemicalDerivationAssociation]-%20subject%201..1%3E[ChemicalEntity],[ChemicalToPathwayAssociation]-%20subject%201..1%3E[ChemicalEntity],[GeneAffectsChemicalAssociation]-%20object%201..1%3E[ChemicalEntity],[MolecularActivityToChemicalEntityAssociation]-%20object%201..1%3E[ChemicalEntity],[ChemicalEntity]uses%20-.-%3E[PhysicalEssence],[ChemicalEntity]uses%20-.-%3E[ChemicalOrDrugOrTreatment],[ChemicalEntity]uses%20-.-%3E[ChemicalEntityOrGeneOrGeneProduct],[ChemicalEntity]uses%20-.-%3E[ChemicalEntityOrProteinOrPolypeptide],[ChemicalEntity]%5E-[MolecularEntity],[ChemicalEntity]%5E-[FoodAdditive],[ChemicalEntity]%5E-[EnvironmentalFoodContaminant],[ChemicalEntity]%5E-[ChemicalMixture],[NamedThing]%5E-[ChemicalEntity],[ChemicalAffectsGeneAssociation],[Attribute])

---


## Identifier prefixes

 * UNII
 * CHEBI
 * MESH
 * CAS
 * UMLS
 * ncats.drug
 * PHARMGKB.CHEMICAL
 * PUBCHEM.COMPOUND
 * CHEMBL.COMPOUND
 * DrugCentral
 * GTOPDB
 * HMDB
 * KEGG.COMPOUND
 * ChemBank
 * PUBCHEM.SUBSTANCE
 * SIDER.DRUG
 * INCHI
 * INCHIKEY
 * KEGG.GLYCAN
 * KEGG.DRUG
 * KEGG.ENVIRON
 * KEGG

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Uses Mixins

 *  mixin: [PhysicalEssence](PhysicalEssence.md) - Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.
 *  mixin: [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md)
 *  mixin: [ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md) - A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.
 *  mixin: [ChemicalEntityOrProteinOrPolypeptide](ChemicalEntityOrProteinOrPolypeptide.md) - A union of chemical entities and children, and protein and polypeptide. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.

## Children

 * [ChemicalMixture](ChemicalMixture.md) - A chemical mixture is a chemical entity composed of two or more molecular entities.
 * [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md)
 * [FoodAdditive](FoodAdditive.md)
 * [MolecularEntity](MolecularEntity.md) - A molecular entity is a chemical entity composed of individual or covalently bonded atoms.

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[associated with resistance to](associated_with_resistance_to.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[NamedThing](NamedThing.md)** *[associated with sensitivity to](associated_with_sensitivity_to.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntityAssessesNamedThingAssociation](ChemicalEntityAssessesNamedThingAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[food component of](food_component_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[has food component](has_food_component.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[has nutrient](has_nutrient.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[nutrient of](nutrient_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[NamedThing](NamedThing.md)** *[trade name](trade_name.md)*  <sub>0..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**

## Attributes


### Own

 * [available from](available_from.md)  <sub>0..\*</sub>
     * Range: [DrugAvailabilityEnum](DrugAvailabilityEnum.md)
 * [has chemical role](has_chemical_role.md)  <sub>0..\*</sub>
     * Description: A role is particular behaviour which a chemical entity may exhibit.
     * Range: [ChemicalRole](ChemicalRole.md)
 * [is toxic](is_toxic.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [max tolerated dose](max_tolerated_dose.md)  <sub>0..1</sub>
     * Description: The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.
     * Range: [String](types/String.md)
 * [trade name](trade_name.md)  <sub>0..1</sub>
     * Range: [ChemicalEntity](ChemicalEntity.md)

### Inherited from entity:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>0..1</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * Range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)
 * [type](type.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from gene product mixin:

 * [synonym](synonym.md)  <sub>0..\*</sub>
     * Description: Alternate human-readable names for a thing
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)
 * [xref](xref.md)  <sub>0..\*</sub>
     * Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (translator_minimal)

### Inherited from macromolecular machine mixin:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)

### Inherited from named thing:

 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     * Range: [String](types/String.md)
 * [full name](full_name.md)  <sub>0..1</sub>
     * Description: a long-form human readable name for a thing
     * Range: [LabelType](types/LabelType.md)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | translator_minimal |
| **Exact Mappings:** | | CHEBI:24431 |
|  | | SIO:010004 |
|  | | WIKIDATA:Q79529 |
|  | | STY:T103 |
| **Narrow Mappings:** | | WIKIDATA:Q43460564 |

