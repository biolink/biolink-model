---
parent: Class Mixins
title: biolink:ChemicalEntityOrGeneOrGeneProduct
grand_parent: Classes
layout: default
---

# Class: ChemicalEntityOrGeneOrGeneProduct


A union of chemical entities and children, and gene or gene product. This mixin is helpful to use when searching across chemical entities that must include genes and their children as chemical entities.

URI: [biolink:ChemicalEntityOrGeneOrGeneProduct](https://w3id.org/biolink/vocab/ChemicalEntityOrGeneOrGeneProduct)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Transcript],[NucleicAcidEntity],[DiseaseOrPhenotypicFeature],[ChemicalToEntityAssociationMixin],[ChemicalEntityToEntityAssociationMixin],[ChemicalEntityToEntityAssociationMixin]++-%20subject%201..1%3E[ChemicalEntityOrGeneOrGeneProduct],[ChemicalToEntityAssociationMixin]++-%20subject%201..1%3E[ChemicalEntityOrGeneOrGeneProduct],[ProteinFamily]uses%20-.-%3E[ChemicalEntityOrGeneOrGeneProduct],[ProteinDomain]uses%20-.-%3E[ChemicalEntityOrGeneOrGeneProduct],[Polypeptide]uses%20-.-%3E[ChemicalEntityOrGeneOrGeneProduct],[GeneFamily]uses%20-.-%3E[ChemicalEntityOrGeneOrGeneProduct],[Gene]uses%20-.-%3E[ChemicalEntityOrGeneOrGeneProduct],[ChemicalEntity]uses%20-.-%3E[ChemicalEntityOrGeneOrGeneProduct],[ProteinFamily],[ProteinDomain],[Polypeptide],[GeneFamily],[Gene],[ChemicalEntity])

---


## Mixin for

 * [ChemicalEntity](ChemicalEntity.md) (mixin)  - A chemical entity is a physical entity that pertains to chemistry or biochemistry.
 * [Gene](Gene.md) (mixin)  - A region (or regions) that includes all of the sequence elements necessary to encode a functional transcript. A gene locus may include regulatory regions, transcribed regions and/or other functional sequence regions.
 * [GeneFamily](GeneFamily.md) (mixin)  - any grouping of multiple genes or gene products related by common descent
 * [Polypeptide](Polypeptide.md) (mixin)  - A polypeptide is a molecular entity characterized by availability in protein databases of amino-acid-based sequence representations of its precise primary structure; for convenience of representation, partial sequences of various kinds are included, even if they do not represent a physical molecule.
 * [ProteinDomain](ProteinDomain.md) (mixin)  - A conserved part of protein sequence and (tertiary) structure that can evolve, function, and exist independently of the rest of the protein chain. Protein domains maintain their structure and function independently of the proteins in which they are found. e.g. an SH3 domain.
 * [ProteinFamily](ProteinFamily.md) (mixin) 

## Referenced by class

 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[abundance affected by](abundance_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[abundance decreased by](abundance_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[abundance increased by](abundance_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[activity affected by](activity_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[activity decreased by](activity_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[activity increased by](activity_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[affects abundance of](affects_abundance_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[affects activity of](affects_activity_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[affects degradation of](affects_degradation_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[affects localization of](affects_localization_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[affects metabolic processing of](affects_metabolic_processing_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[affects molecular modification of](affects_molecular_modification_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[affects response to](affects_response_to.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[affects secretion of](affects_secretion_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[affects stability of](affects_stability_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[affects synthesis of](affects_synthesis_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[affects transport of](affects_transport_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[affects uptake of](affects_uptake_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityToEntityAssociationMixin](ChemicalEntityToEntityAssociationMixin.md)** *[chemical entity to entity association mixin➞subject](chemical_entity_to_entity_association_mixin_subject.md)*  <sub>1..1</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalToEntityAssociationMixin](ChemicalToEntityAssociationMixin.md)** *[chemical to entity association mixin➞subject](chemical_to_entity_association_mixin_subject.md)*  <sub>1..1</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[decreases abundance of](decreases_abundance_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[decreases activity of](decreases_activity_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[decreases degradation of](decreases_degradation_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[decreases localization of](decreases_localization_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[decreases metabolic processing of](decreases_metabolic_processing_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[decreases molecular modification of](decreases_molecular_modification_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[decreases response to](decreases_response_to.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[decreases secretion of](decreases_secretion_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[decreases stability of](decreases_stability_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[decreases synthesis of](decreases_synthesis_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[decreases transport of](decreases_transport_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[decreases uptake of](decreases_uptake_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[degradation affected by](degradation_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[degradation decreased by](degradation_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[degradation increased by](degradation_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntity](ChemicalEntity.md)** *[directly interacts with](directly_interacts_with.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[entity negatively regulated by entity](entity_negatively_regulated_by_entity.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[entity negatively regulates entity](entity_negatively_regulates_entity.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[entity positively regulated by entity](entity_positively_regulated_by_entity.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[entity positively regulates entity](entity_positively_regulates_entity.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[entity regulated by entity](entity_regulated_by_entity.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[entity regulates entity](entity_regulates_entity.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[expression affected by](expression_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[expression decreased by](expression_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[expression increased by](expression_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[folding affected by](folding_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[folding decreased by](folding_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[folding increased by](folding_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)** *[has biomarker](has_biomarker.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[increases abundance of](increases_abundance_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[increases activity of](increases_activity_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[increases degradation of](increases_degradation_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[increases localization of](increases_localization_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[increases metabolic processing of](increases_metabolic_processing_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[increases molecular modification of](increases_molecular_modification_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[increases response to](increases_response_to.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[increases secretion of](increases_secretion_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[increases stability of](increases_stability_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[increases synthesis of](increases_synthesis_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[increases transport of](increases_transport_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[increases uptake of](increases_uptake_of.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[localization affected by](localization_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[localization decreased by](localization_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[localization increased by](localization_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[metabolic processing affected by](metabolic_processing_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[metabolic processing decreased by](metabolic_processing_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[metabolic processing increased by](metabolic_processing_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[molecular modification affected by](molecular_modification_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[molecular modification decreased by](molecular_modification_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[molecular modification increased by](molecular_modification_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[NucleicAcidEntity](NucleicAcidEntity.md)** *[mutation rate affected by](mutation_rate_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[response affected by](response_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[response decreased by](response_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[response increased by](response_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[secretion affected by](secretion_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[secretion decreased by](secretion_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[secretion increased by](secretion_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[Transcript](Transcript.md)** *[splicing affected by](splicing_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[Transcript](Transcript.md)** *[splicing decreased by](splicing_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[Transcript](Transcript.md)** *[splicing increased by](splicing_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[stability affected by](stability_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[stability decreased by](stability_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[stability increased by](stability_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[synthesis affected by](synthesis_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[synthesis decreased by](synthesis_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[synthesis increased by](synthesis_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[transport affected by](transport_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[transport decreased by](transport_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[transport increased by](transport_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[uptake affected by](uptake_affected_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[uptake decreased by](uptake_decreased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[uptake increased by](uptake_increased_by.md)*  <sub>0..\*</sub>  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)**

## Attributes

