---
parent: Classes
title: biolink:NamedThing
grand_parent: Browse Biolink Model
layout: default
---

# Type: NamedThing


a databased entity or concept/class

URI: [biolink:NamedThing](https://w3id.org/biolink/vocab/NamedThing)

WIKIDATA:Q35120
{: .mapping-label }

UMLSSG:OBJC
{: .mapping-label }

UMLSSC:T071
{: .mapping-label }

UMLSST:enty
{: .mapping-label }

UMLSSC:T072
{: .mapping-label }

UMLSST:phob
{: .mapping-label }

UMLSSC:T073
{: .mapping-label }

UMLSST:mnob
{: .mapping-label }

UMLSSC:T168
{: .mapping-label }

UMLSST:food
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[VariantToDiseaseAssociation],[PlanetaryEntity],[PhysicalEntity],[OntologyClass],[Occurrent],[BiologicalProcessOrActivity]-%20enabled%20by%200..*%3E[NamedThing|id:string;name:label_type;category:category_type%20%2B],[GenotypeToDiseaseAssociation]-%20object%201..1%3E[NamedThing],[GenotypeToDiseaseAssociation]-%20subject%201..1%3E[NamedThing],[BiologicalProcessOrActivity]-%20has%20input%200..*%3E[NamedThing],[BiologicalProcessOrActivity]-%20has%20output%200..*%3E[NamedThing],[Attribute]-%20has%20qualitative%20value%200..1%3E[NamedThing],[MaterialSampleDerivationAssociation]-%20object%201..1%3E[NamedThing],[ModelToDiseaseMixin]-%20subject(i)%201..1%3E[NamedThing],[Association]-%20object%201..1%3E[NamedThing],[Association]-%20subject%201..1%3E[NamedThing],[VariantToDiseaseAssociation]-%20object%201..1%3E[NamedThing],[VariantToDiseaseAssociation]-%20subject%201..1%3E[NamedThing],[NamedThing]%5E-[PlanetaryEntity],[NamedThing]%5E-[PhysicalEntity],[NamedThing]%5E-[OntologyClass],[NamedThing]%5E-[Occurrent],[NamedThing]%5E-[MaterialSample],[NamedThing]%5E-[InformationContentEntity],[NamedThing]%5E-[Device],[NamedThing]%5E-[DataSet],[NamedThing]%5E-[DataFile],[NamedThing]%5E-[ClinicalEntity],[NamedThing]%5E-[BiologicalEntity],[NamedThing]%5E-[AdministrativeEntity],[ModelToDiseaseMixin],[MaterialSampleDerivationAssociation],[MaterialSample],[InformationContentEntity],[GenotypeToDiseaseAssociation],[DiseaseOrPhenotypicFeature],[Device],[DataSet],[DataFile],[ClinicalEntity],[BiologicalProcessOrActivity],[BiologicalEntity],[Attribute],[Association],[AdministrativeEntity])

---


## Children

 * [AdministrativeEntity](AdministrativeEntity.md)
 * [BiologicalEntity](BiologicalEntity.md)
 * [ClinicalEntity](ClinicalEntity.md) - Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
 * [DataFile](DataFile.md)
 * [DataSet](DataSet.md)
 * [Device](Device.md) - A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
 * [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.
 * [MaterialSample](MaterialSample.md) - A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
 * [Occurrent](Occurrent.md) - A processual entity
 * [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus
 * [PhysicalEntity](PhysicalEntity.md) - An entity that has physical properties such as mass, volume, or charge
 * [PlanetaryEntity](PlanetaryEntity.md) - Any entity or process that exists at the level of the whole planet

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[affects](affects.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[affects expression in](affects_expression_in.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[affects risk for](affects_risk_for.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[caused by](caused_by.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[causes](causes.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[causes adverse event](causes_adverse_event.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[coexists with](coexists_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[colocalizes with](colocalizes_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[contraindicated for](contraindicated_for.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[contributes to](contributes_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[correlated with](correlated_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[derives from](derives_from.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[derives into](derives_into.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[directly interacts with](directly_interacts_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[disease has basis in](disease_has_basis_in.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[disrupts](disrupts.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[BiologicalProcessOrActivity](BiologicalProcessOrActivity.md)** *[enabled by](enabled_by.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[filler](filler.md)*  <sub>OPT</sub>  **[NamedThing](NamedThing.md)**
 *  **[GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md)** *[genotype to disease association➞object](genotype_to_disease_association_object.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md)** *[genotype to disease association➞subject](genotype_to_disease_association_subject.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[has completed](has_completed.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[has decreased amount](has_decreased_amount.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[has increased amount](has_increased_amount.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Occurrent](Occurrent.md)** *[has input](has_input.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[has not completed](has_not_completed.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Occurrent](Occurrent.md)** *[has output](has_output.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[has part](has_part.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Occurrent](Occurrent.md)** *[has participant](has_participant.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Attribute](Attribute.md)** *[has qualitative value](has_qualitative_value.md)*  <sub>OPT</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[homologous to](homologous_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[in linkage disequilibrium with](in_linkage_disequilibrium_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[interacts with](interacts_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[is missense variant of](is_missense_variant_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[is nearby variant of](is_nearby_variant_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[is non coding variant of](is_non_coding_variant_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[is nonsense variant of](is_nonsense_variant_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[is splice site variant of](is_splice_site_variant_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[is synonymous variant of](is_synonymous_variant_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[lacks part](lacks_part.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[located in](located_in.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[location of](location_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md)** *[material sample derivation association➞object](material_sample_derivation_association_object.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[model of](model_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[ModelToDiseaseMixin](ModelToDiseaseMixin.md)** *[model to disease mixin➞subject](model_to_disease_mixin_subject.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[negatively regulates](negatively_regulates.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Association](Association.md)** *[object](object.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[occurs in](occurs_in.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[orthologous to](orthologous_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[overlaps](overlaps.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[paralogous to](paralogous_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[part of](part_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[physically interacts with](physically_interacts_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[positively regulates](positively_regulates.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[predisposes](predisposes.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[prevents](prevents.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[produced by](produced_by.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[produces](produces.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[regulates](regulates.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[related to](related_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[same as](same_as.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Association](Association.md)** *[subject](subject.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)** *[treated by](treated_by.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[VariantToDiseaseAssociation](VariantToDiseaseAssociation.md)** *[variant to disease association➞object](variant_to_disease_association_object.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[VariantToDiseaseAssociation](VariantToDiseaseAssociation.md)** *[variant to disease association➞subject](variant_to_disease_association_subject.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[xenologous to](xenologous_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**

## Attributes


### Own

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | WIKIDATA:Q35120 |
|  | | UMLSSG:OBJC |
|  | | UMLSSC:T071 |
|  | | UMLSST:enty |
|  | | UMLSSC:T072 |
|  | | UMLSST:phob |
|  | | UMLSSC:T073 |
|  | | UMLSST:mnob |
|  | | UMLSSC:T168 |
|  | | UMLSST:food |

