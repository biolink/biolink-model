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

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Transcript],[PhysicalEssence],[Nutrient],[NucleicAcidEntity],[NamedThing],[MolecularEntity],[FoodAdditive],[EnvironmentalFoodContaminant],[DiseaseOrPhenotypicFeature],[ChemicalToEntityAssociationMixin],[ChemicalToChemicalDerivationAssociation],[ChemicalToChemicalAssociation],[ChemicalOrDrugOrTreatment],[ChemicalMixture],[ChemicalEntityToEntityAssociationMixin],[ChemicalEntityOrProteinOrPolypeptide],[ChemicalEntityOrGeneOrGeneProduct],[ChemicalEntity]%3Ctrade%20name%200..1-%20[ChemicalEntity%7Cavailable_from:drug_availability_enum%20%2A;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[ChemicalEntityToEntityAssociationMixin]-%20subject%201..1%3E[ChemicalEntity],[ChemicalToChemicalAssociation]-%20object%201..1%3E[ChemicalEntity],[ChemicalToChemicalDerivationAssociation]-%20object%201..1%3E[ChemicalEntity],[ChemicalToChemicalDerivationAssociation]-%20subject%201..1%3E[ChemicalEntity],[ChemicalToEntityAssociationMixin]-%20subject%201..1%3E[ChemicalEntity],[ChemicalEntity]uses%20-.-%3E[PhysicalEssence],[ChemicalEntity]uses%20-.-%3E[ChemicalOrDrugOrTreatment],[ChemicalEntity]uses%20-.-%3E[ChemicalEntityOrGeneOrGeneProduct],[ChemicalEntity]uses%20-.-%3E[ChemicalEntityOrProteinOrPolypeptide],[ChemicalEntity]%5E-[Nutrient],[ChemicalEntity]%5E-[MolecularEntity],[ChemicalEntity]%5E-[FoodAdditive],[ChemicalEntity]%5E-[EnvironmentalFoodContaminant],[ChemicalEntity]%5E-[ChemicalMixture],[NamedThing]%5E-[ChemicalEntity],[Attribute],[Agent])

---


## Identifier prefixes

 * UNII
 * MESH
 * CAS

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
 * [Nutrient](Nutrient.md)

## Referenced by class

 *  **[ChemicalEntity](ChemicalEntity.md)** *[abundance affected by](abundance_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[abundance decreased by](abundance_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[abundance increased by](abundance_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[activity affected by](activity_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[activity affects](activity_affects.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[activity decreased by](activity_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[activity increased by](activity_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[affects abundance of](affects_abundance_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[affects activity of](affects_activity_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[affects degradation of](affects_degradation_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[affects localization of](affects_localization_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[affects metabolic processing of](affects_metabolic_processing_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[affects molecular modification of](affects_molecular_modification_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[affects response to](affects_response_to.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[affects secretion of](affects_secretion_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[affects stability of](affects_stability_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[affects synthesis of](affects_synthesis_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[affects transport of](affects_transport_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[affects uptake of](affects_uptake_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md)** *[chemical entity to entity association mixin➞subject](chemical_entity_to_entity_association_mixin_subject.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md)** *[chemical to chemical association➞object](chemical_to_chemical_association_object.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)** *[chemical to chemical derivation association➞object](chemical_to_chemical_derivation_association_object.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md)** *[chemical to chemical derivation association➞subject](chemical_to_chemical_derivation_association_subject.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md)** *[chemical to entity association mixin➞subject](chemical_to_entity_association_mixin_subject.md)*  <sub>1..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[chemically interacts with](chemically_interacts_with.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[decreases abundance of](decreases_abundance_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[decreases activity of](decreases_activity_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[decreases degradation of](decreases_degradation_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[decreases localization of](decreases_localization_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[decreases metabolic processing of](decreases_metabolic_processing_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[decreases molecular modification of](decreases_molecular_modification_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[decreases response to](decreases_response_to.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[decreases secretion of](decreases_secretion_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[decreases stability of](decreases_stability_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[decreases synthesis of](decreases_synthesis_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[decreases transport of](decreases_transport_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[decreases uptake of](decreases_uptake_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[degradation affected by](degradation_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[degradation decreased by](degradation_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[degradation increased by](degradation_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[directly interacts with](directly_interacts_with.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[entity negatively regulated by entity](entity_negatively_regulated_by_entity.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[entity negatively regulates entity](entity_negatively_regulates_entity.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[entity positively regulated by entity](entity_positively_regulated_by_entity.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[entity positively regulates entity](entity_positively_regulates_entity.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[entity regulated by entity](entity_regulated_by_entity.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[entity regulates entity](entity_regulates_entity.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[expression affected by](expression_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[expression decreased by](expression_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[expression increased by](expression_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[folding affected by](folding_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[folding decreased by](folding_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[folding increased by](folding_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[food component of](food_component_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)** *[has biomarker](has_biomarker.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[has food component](has_food_component.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[has nutrient](has_nutrient.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[increases abundance of](increases_abundance_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[increases activity of](increases_activity_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[increases degradation of](increases_degradation_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[increases localization of](increases_localization_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[increases metabolic processing of](increases_metabolic_processing_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[increases molecular modification of](increases_molecular_modification_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[increases response to](increases_response_to.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[increases secretion of](increases_secretion_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[increases stability of](increases_stability_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[increases synthesis of](increases_synthesis_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[increases transport of](increases_transport_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[increases uptake of](increases_uptake_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[localization affected by](localization_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[localization decreased by](localization_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[localization increased by](localization_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[metabolic processing affected by](metabolic_processing_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[metabolic processing decreased by](metabolic_processing_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[metabolic processing increased by](metabolic_processing_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[molecular modification affected by](molecular_modification_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[molecular modification decreased by](molecular_modification_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[molecular modification increased by](molecular_modification_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[mutation rate affected by](mutation_rate_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[mutation rate decreased by](mutation_rate_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[mutation rate increased by](mutation_rate_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[nutrient of](nutrient_of.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[response affected by](response_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[response decreased by](response_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[response increased by](response_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[secretion affected by](secretion_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[secretion decreased by](secretion_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[secretion increased by](secretion_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[Transcript](Transcript.md)** *[splicing affected by](splicing_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[Transcript](Transcript.md)** *[splicing decreased by](splicing_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[Transcript](Transcript.md)** *[splicing increased by](splicing_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[stability affected by](stability_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[stability decreased by](stability_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[stability increased by](stability_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[synthesis affected by](synthesis_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[synthesis decreased by](synthesis_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[synthesis increased by](synthesis_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[NamedThing](NamedThing.md)** *[trade name](trade_name.md)*  <sub>0..1</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[transport affected by](transport_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[transport decreased by](transport_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[transport increased by](transport_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[uptake affected by](uptake_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[uptake decreased by](uptake_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[uptake increased by](uptake_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntity](ChemicalEntity.md)**

## Attributes


### Own

 * [available from](available_from.md)  <sub>0..\*</sub>
     * Range: [drug_availability_enum](drug_availability_enum.md)
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
 * [type](type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [source](source.md)  <sub>0..1</sub>
     * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: connects an association to the agent (person, organization or group) that provided it
     * Range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from macromolecular machine mixin:

 * [macromolecular machine mixin➞name](macromolecular_machine_mixin_name.md)  <sub>0..1</sub>
     * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * Range: [SymbolType](types/SymbolType.md)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..\*</sub>
     * Range: [NamedThing](NamedThing.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | translator_minimal |
| **Exact Mappings:** | | CHEBI:24431 |
|  | | SIO:010004 |
|  | | WIKIDATA:Q79529 |
|  | | STY:T103 |
| **Narrow Mappings:** | | WIKIDATA:Q43460564 |

