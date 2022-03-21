# Class: NamedThing
_a databased entity or concept/class_





URI: [biolink:NamedThing](https://w3id.org/biolink/vocab/NamedThing)




## Inheritance

* [Entity](Entity.md)
    * **NamedThing**
        * [OrganismTaxon](OrganismTaxon.md)
        * [Event](Event.md)
        * [AdministrativeEntity](AdministrativeEntity.md)
        * [InformationContentEntity](InformationContentEntity.md)
        * [PhysicalEntity](PhysicalEntity.md) [ physical essence]
        * [Activity](Activity.md) [ activity and behavior]
        * [Procedure](Procedure.md) [ activity and behavior]
        * [Phenomenon](Phenomenon.md) [ occurrent]
        * [Device](Device.md)
        * [PlanetaryEntity](PlanetaryEntity.md)
        * [BiologicalEntity](BiologicalEntity.md)
        * [ChemicalEntity](ChemicalEntity.md) [ physical essence chemical or drug or treatment chemical entity or gene or gene product chemical entity or protein or polypeptide]
        * [ClinicalEntity](ClinicalEntity.md)
        * [Treatment](Treatment.md) [ exposure event chemical or drug or treatment]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [provided_by](provided_by.md) | [string](string.md) | 0..* | The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.  | . |
| [id](id.md) | [string](string.md) | 1..1 | A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI  | . |
| [iri](iri.md) | [iri_type](iri_type.md) | 0..1 | An IRI for an entity. This is determined by the id using expansion rules.  | . |
| [category](category.md) | [NamedThing](NamedThing.md) | 1..* | Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}  | . |
| [type](type.md) | [string](string.md) | 0..1 | None  | . |
| [name](name.md) | [label_type](label_type.md) | 0..1 | A human-readable name for an attribute or entity.  | . |
| [description](description.md) | [narrative_text](narrative_text.md) | 0..1 | a human-readable description of an entity  | . |
| [source](source.md) | [string](string.md) | 0..1 | None  | . |
| [has_attribute](has_attribute.md) | [Attribute](Attribute.md) | 0..* | connects any entity to an attribute  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Attribute](Attribute.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [BiologicalSex](BiologicalSex.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [PhenotypicSex](PhenotypicSex.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [GenotypicSex](GenotypicSex.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [SeverityValue](SeverityValue.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [FrequencyQuantifier](FrequencyQuantifier.md) | [has_count](has_count.md) | domain | named thing |
| [FrequencyQuantifier](FrequencyQuantifier.md) | [has_total](has_total.md) | domain | named thing |
| [FrequencyQuantifier](FrequencyQuantifier.md) | [has_quotient](has_quotient.md) | domain | named thing |
| [FrequencyQuantifier](FrequencyQuantifier.md) | [has_percentage](has_percentage.md) | domain | named thing |
| [NamedThing](NamedThing.md) | [provided_by](provided_by.md) | domain | named thing |
| [NamedThing](NamedThing.md) | [category](category.md) | range | named thing |
| [OrganismTaxon](OrganismTaxon.md) | [provided_by](provided_by.md) | domain | named thing |
| [OrganismTaxon](OrganismTaxon.md) | [category](category.md) | range | named thing |
| [Event](Event.md) | [provided_by](provided_by.md) | domain | named thing |
| [Event](Event.md) | [category](category.md) | range | named thing |
| [AdministrativeEntity](AdministrativeEntity.md) | [provided_by](provided_by.md) | domain | named thing |
| [AdministrativeEntity](AdministrativeEntity.md) | [category](category.md) | range | named thing |
| [Agent](Agent.md) | [address](address.md) | domain | named thing |
| [Agent](Agent.md) | [provided_by](provided_by.md) | domain | named thing |
| [Agent](Agent.md) | [category](category.md) | range | named thing |
| [InformationContentEntity](InformationContentEntity.md) | [creation_date](creation_date.md) | domain | named thing |
| [InformationContentEntity](InformationContentEntity.md) | [provided_by](provided_by.md) | domain | named thing |
| [InformationContentEntity](InformationContentEntity.md) | [category](category.md) | range | named thing |
| [Dataset](Dataset.md) | [creation_date](creation_date.md) | domain | named thing |
| [Dataset](Dataset.md) | [provided_by](provided_by.md) | domain | named thing |
| [Dataset](Dataset.md) | [category](category.md) | range | named thing |
| [DatasetDistribution](DatasetDistribution.md) | [creation_date](creation_date.md) | domain | named thing |
| [DatasetDistribution](DatasetDistribution.md) | [provided_by](provided_by.md) | domain | named thing |
| [DatasetDistribution](DatasetDistribution.md) | [category](category.md) | range | named thing |
| [DatasetVersion](DatasetVersion.md) | [creation_date](creation_date.md) | domain | named thing |
| [DatasetVersion](DatasetVersion.md) | [provided_by](provided_by.md) | domain | named thing |
| [DatasetVersion](DatasetVersion.md) | [category](category.md) | range | named thing |
| [DatasetSummary](DatasetSummary.md) | [creation_date](creation_date.md) | domain | named thing |
| [DatasetSummary](DatasetSummary.md) | [provided_by](provided_by.md) | domain | named thing |
| [DatasetSummary](DatasetSummary.md) | [category](category.md) | range | named thing |
| [ConfidenceLevel](ConfidenceLevel.md) | [creation_date](creation_date.md) | domain | named thing |
| [ConfidenceLevel](ConfidenceLevel.md) | [provided_by](provided_by.md) | domain | named thing |
| [ConfidenceLevel](ConfidenceLevel.md) | [category](category.md) | range | named thing |
| [EvidenceType](EvidenceType.md) | [creation_date](creation_date.md) | domain | named thing |
| [EvidenceType](EvidenceType.md) | [provided_by](provided_by.md) | domain | named thing |
| [EvidenceType](EvidenceType.md) | [category](category.md) | range | named thing |
| [InformationResource](InformationResource.md) | [creation_date](creation_date.md) | domain | named thing |
| [InformationResource](InformationResource.md) | [provided_by](provided_by.md) | domain | named thing |
| [InformationResource](InformationResource.md) | [category](category.md) | range | named thing |
| [Publication](Publication.md) | [xref](xref.md) | domain | named thing |
| [Publication](Publication.md) | [creation_date](creation_date.md) | domain | named thing |
| [Publication](Publication.md) | [provided_by](provided_by.md) | domain | named thing |
| [Publication](Publication.md) | [category](category.md) | range | named thing |
| [Book](Book.md) | [xref](xref.md) | domain | named thing |
| [Book](Book.md) | [creation_date](creation_date.md) | domain | named thing |
| [Book](Book.md) | [provided_by](provided_by.md) | domain | named thing |
| [Book](Book.md) | [category](category.md) | range | named thing |
| [BookChapter](BookChapter.md) | [xref](xref.md) | domain | named thing |
| [BookChapter](BookChapter.md) | [creation_date](creation_date.md) | domain | named thing |
| [BookChapter](BookChapter.md) | [provided_by](provided_by.md) | domain | named thing |
| [BookChapter](BookChapter.md) | [category](category.md) | range | named thing |
| [Serial](Serial.md) | [xref](xref.md) | domain | named thing |
| [Serial](Serial.md) | [creation_date](creation_date.md) | domain | named thing |
| [Serial](Serial.md) | [provided_by](provided_by.md) | domain | named thing |
| [Serial](Serial.md) | [category](category.md) | range | named thing |
| [Article](Article.md) | [xref](xref.md) | domain | named thing |
| [Article](Article.md) | [creation_date](creation_date.md) | domain | named thing |
| [Article](Article.md) | [provided_by](provided_by.md) | domain | named thing |
| [Article](Article.md) | [category](category.md) | range | named thing |
| [PhysicalEntity](PhysicalEntity.md) | [provided_by](provided_by.md) | domain | named thing |
| [PhysicalEntity](PhysicalEntity.md) | [category](category.md) | range | named thing |
| [Activity](Activity.md) | [provided_by](provided_by.md) | domain | named thing |
| [Activity](Activity.md) | [category](category.md) | range | named thing |
| [Procedure](Procedure.md) | [provided_by](provided_by.md) | domain | named thing |
| [Procedure](Procedure.md) | [category](category.md) | range | named thing |
| [Phenomenon](Phenomenon.md) | [provided_by](provided_by.md) | domain | named thing |
| [Phenomenon](Phenomenon.md) | [category](category.md) | range | named thing |
| [Device](Device.md) | [provided_by](provided_by.md) | domain | named thing |
| [Device](Device.md) | [category](category.md) | range | named thing |
| [StudyPopulation](StudyPopulation.md) | [provided_by](provided_by.md) | domain | named thing |
| [StudyPopulation](StudyPopulation.md) | [category](category.md) | range | named thing |
| [MaterialSample](MaterialSample.md) | [provided_by](provided_by.md) | domain | named thing |
| [MaterialSample](MaterialSample.md) | [category](category.md) | range | named thing |
| [PlanetaryEntity](PlanetaryEntity.md) | [provided_by](provided_by.md) | domain | named thing |
| [PlanetaryEntity](PlanetaryEntity.md) | [category](category.md) | range | named thing |
| [EnvironmentalProcess](EnvironmentalProcess.md) | [provided_by](provided_by.md) | domain | named thing |
| [EnvironmentalProcess](EnvironmentalProcess.md) | [category](category.md) | range | named thing |
| [EnvironmentalFeature](EnvironmentalFeature.md) | [provided_by](provided_by.md) | domain | named thing |
| [EnvironmentalFeature](EnvironmentalFeature.md) | [category](category.md) | range | named thing |
| [GeographicLocation](GeographicLocation.md) | [latitude](latitude.md) | domain | named thing |
| [GeographicLocation](GeographicLocation.md) | [longitude](longitude.md) | domain | named thing |
| [GeographicLocation](GeographicLocation.md) | [provided_by](provided_by.md) | domain | named thing |
| [GeographicLocation](GeographicLocation.md) | [category](category.md) | range | named thing |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [timepoint](timepoint.md) | domain | named thing |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [latitude](latitude.md) | domain | named thing |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [longitude](longitude.md) | domain | named thing |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [provided_by](provided_by.md) | domain | named thing |
| [GeographicLocationAtTime](GeographicLocationAtTime.md) | [category](category.md) | range | named thing |
| [BiologicalEntity](BiologicalEntity.md) | [provided_by](provided_by.md) | domain | named thing |
| [BiologicalEntity](BiologicalEntity.md) | [category](category.md) | range | named thing |
| [GenomicEntity](GenomicEntity.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [MolecularEntity](MolecularEntity.md) | [trade_name](trade_name.md) | domain | named thing |
| [MolecularEntity](MolecularEntity.md) | [available_from](available_from.md) | domain | named thing |
| [MolecularEntity](MolecularEntity.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [MolecularEntity](MolecularEntity.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [MolecularEntity](MolecularEntity.md) | [provided_by](provided_by.md) | domain | named thing |
| [MolecularEntity](MolecularEntity.md) | [category](category.md) | range | named thing |
| [ChemicalEntity](ChemicalEntity.md) | [trade_name](trade_name.md) | domain | named thing |
| [ChemicalEntity](ChemicalEntity.md) | [available_from](available_from.md) | domain | named thing |
| [ChemicalEntity](ChemicalEntity.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [ChemicalEntity](ChemicalEntity.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [ChemicalEntity](ChemicalEntity.md) | [provided_by](provided_by.md) | domain | named thing |
| [ChemicalEntity](ChemicalEntity.md) | [category](category.md) | range | named thing |
| [SmallMolecule](SmallMolecule.md) | [trade_name](trade_name.md) | domain | named thing |
| [SmallMolecule](SmallMolecule.md) | [available_from](available_from.md) | domain | named thing |
| [SmallMolecule](SmallMolecule.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [SmallMolecule](SmallMolecule.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [SmallMolecule](SmallMolecule.md) | [provided_by](provided_by.md) | domain | named thing |
| [SmallMolecule](SmallMolecule.md) | [category](category.md) | range | named thing |
| [ChemicalMixture](ChemicalMixture.md) | [is_supplement](is_supplement.md) | domain | named thing |
| [ChemicalMixture](ChemicalMixture.md) | [trade_name](trade_name.md) | domain | named thing |
| [ChemicalMixture](ChemicalMixture.md) | [available_from](available_from.md) | domain | named thing |
| [ChemicalMixture](ChemicalMixture.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [ChemicalMixture](ChemicalMixture.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [ChemicalMixture](ChemicalMixture.md) | [provided_by](provided_by.md) | domain | named thing |
| [ChemicalMixture](ChemicalMixture.md) | [category](category.md) | range | named thing |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [trade_name](trade_name.md) | domain | named thing |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [available_from](available_from.md) | domain | named thing |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [provided_by](provided_by.md) | domain | named thing |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [category](category.md) | range | named thing |
| [MolecularMixture](MolecularMixture.md) | [is_supplement](is_supplement.md) | domain | named thing |
| [MolecularMixture](MolecularMixture.md) | [trade_name](trade_name.md) | domain | named thing |
| [MolecularMixture](MolecularMixture.md) | [available_from](available_from.md) | domain | named thing |
| [MolecularMixture](MolecularMixture.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [MolecularMixture](MolecularMixture.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [MolecularMixture](MolecularMixture.md) | [provided_by](provided_by.md) | domain | named thing |
| [MolecularMixture](MolecularMixture.md) | [category](category.md) | range | named thing |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [is_supplement](is_supplement.md) | domain | named thing |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [trade_name](trade_name.md) | domain | named thing |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [available_from](available_from.md) | domain | named thing |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [provided_by](provided_by.md) | domain | named thing |
| [ComplexMolecularMixture](ComplexMolecularMixture.md) | [category](category.md) | range | named thing |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [provided_by](provided_by.md) | domain | named thing |
| [BiologicalProcessOrActivity](BiologicalProcessOrActivity.md) | [category](category.md) | range | named thing |
| [MolecularActivity](MolecularActivity.md) | [provided_by](provided_by.md) | domain | named thing |
| [MolecularActivity](MolecularActivity.md) | [category](category.md) | range | named thing |
| [BiologicalProcess](BiologicalProcess.md) | [provided_by](provided_by.md) | domain | named thing |
| [BiologicalProcess](BiologicalProcess.md) | [category](category.md) | range | named thing |
| [Pathway](Pathway.md) | [provided_by](provided_by.md) | domain | named thing |
| [Pathway](Pathway.md) | [category](category.md) | range | named thing |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [provided_by](provided_by.md) | domain | named thing |
| [PhysiologicalProcess](PhysiologicalProcess.md) | [category](category.md) | range | named thing |
| [Behavior](Behavior.md) | [provided_by](provided_by.md) | domain | named thing |
| [Behavior](Behavior.md) | [category](category.md) | range | named thing |
| [ProcessedMaterial](ProcessedMaterial.md) | [is_supplement](is_supplement.md) | domain | named thing |
| [ProcessedMaterial](ProcessedMaterial.md) | [trade_name](trade_name.md) | domain | named thing |
| [ProcessedMaterial](ProcessedMaterial.md) | [available_from](available_from.md) | domain | named thing |
| [ProcessedMaterial](ProcessedMaterial.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [ProcessedMaterial](ProcessedMaterial.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [ProcessedMaterial](ProcessedMaterial.md) | [provided_by](provided_by.md) | domain | named thing |
| [ProcessedMaterial](ProcessedMaterial.md) | [category](category.md) | range | named thing |
| [Drug](Drug.md) | [is_supplement](is_supplement.md) | domain | named thing |
| [Drug](Drug.md) | [trade_name](trade_name.md) | domain | named thing |
| [Drug](Drug.md) | [available_from](available_from.md) | domain | named thing |
| [Drug](Drug.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [Drug](Drug.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [Drug](Drug.md) | [provided_by](provided_by.md) | domain | named thing |
| [Drug](Drug.md) | [category](category.md) | range | named thing |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [trade_name](trade_name.md) | domain | named thing |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [available_from](available_from.md) | domain | named thing |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [provided_by](provided_by.md) | domain | named thing |
| [EnvironmentalFoodContaminant](EnvironmentalFoodContaminant.md) | [category](category.md) | range | named thing |
| [FoodAdditive](FoodAdditive.md) | [trade_name](trade_name.md) | domain | named thing |
| [FoodAdditive](FoodAdditive.md) | [available_from](available_from.md) | domain | named thing |
| [FoodAdditive](FoodAdditive.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [FoodAdditive](FoodAdditive.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [FoodAdditive](FoodAdditive.md) | [provided_by](provided_by.md) | domain | named thing |
| [FoodAdditive](FoodAdditive.md) | [category](category.md) | range | named thing |
| [Nutrient](Nutrient.md) | [trade_name](trade_name.md) | domain | named thing |
| [Nutrient](Nutrient.md) | [available_from](available_from.md) | domain | named thing |
| [Nutrient](Nutrient.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [Nutrient](Nutrient.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [Nutrient](Nutrient.md) | [provided_by](provided_by.md) | domain | named thing |
| [Nutrient](Nutrient.md) | [category](category.md) | range | named thing |
| [Macronutrient](Macronutrient.md) | [trade_name](trade_name.md) | domain | named thing |
| [Macronutrient](Macronutrient.md) | [available_from](available_from.md) | domain | named thing |
| [Macronutrient](Macronutrient.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [Macronutrient](Macronutrient.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [Macronutrient](Macronutrient.md) | [provided_by](provided_by.md) | domain | named thing |
| [Macronutrient](Macronutrient.md) | [category](category.md) | range | named thing |
| [Micronutrient](Micronutrient.md) | [trade_name](trade_name.md) | domain | named thing |
| [Micronutrient](Micronutrient.md) | [available_from](available_from.md) | domain | named thing |
| [Micronutrient](Micronutrient.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [Micronutrient](Micronutrient.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [Micronutrient](Micronutrient.md) | [provided_by](provided_by.md) | domain | named thing |
| [Micronutrient](Micronutrient.md) | [category](category.md) | range | named thing |
| [Vitamin](Vitamin.md) | [trade_name](trade_name.md) | domain | named thing |
| [Vitamin](Vitamin.md) | [available_from](available_from.md) | domain | named thing |
| [Vitamin](Vitamin.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [Vitamin](Vitamin.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [Vitamin](Vitamin.md) | [provided_by](provided_by.md) | domain | named thing |
| [Vitamin](Vitamin.md) | [category](category.md) | range | named thing |
| [Food](Food.md) | [is_supplement](is_supplement.md) | domain | named thing |
| [Food](Food.md) | [trade_name](trade_name.md) | domain | named thing |
| [Food](Food.md) | [available_from](available_from.md) | domain | named thing |
| [Food](Food.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [Food](Food.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [Food](Food.md) | [provided_by](provided_by.md) | domain | named thing |
| [Food](Food.md) | [category](category.md) | range | named thing |
| [OrganismAttribute](OrganismAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [PhenotypicQuality](PhenotypicQuality.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [Inheritance](Inheritance.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [OrganismalEntity](OrganismalEntity.md) | [provided_by](provided_by.md) | domain | named thing |
| [OrganismalEntity](OrganismalEntity.md) | [category](category.md) | range | named thing |
| [LifeStage](LifeStage.md) | [provided_by](provided_by.md) | domain | named thing |
| [LifeStage](LifeStage.md) | [category](category.md) | range | named thing |
| [IndividualOrganism](IndividualOrganism.md) | [provided_by](provided_by.md) | domain | named thing |
| [IndividualOrganism](IndividualOrganism.md) | [category](category.md) | range | named thing |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | [provided_by](provided_by.md) | domain | named thing |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | [category](category.md) | range | named thing |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | [provided_by](provided_by.md) | domain | named thing |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | [category](category.md) | range | named thing |
| [Disease](Disease.md) | [provided_by](provided_by.md) | domain | named thing |
| [Disease](Disease.md) | [category](category.md) | range | named thing |
| [PhenotypicFeature](PhenotypicFeature.md) | [provided_by](provided_by.md) | domain | named thing |
| [PhenotypicFeature](PhenotypicFeature.md) | [category](category.md) | range | named thing |
| [BehavioralFeature](BehavioralFeature.md) | [provided_by](provided_by.md) | domain | named thing |
| [BehavioralFeature](BehavioralFeature.md) | [category](category.md) | range | named thing |
| [AnatomicalEntity](AnatomicalEntity.md) | [provided_by](provided_by.md) | domain | named thing |
| [AnatomicalEntity](AnatomicalEntity.md) | [category](category.md) | range | named thing |
| [CellularComponent](CellularComponent.md) | [provided_by](provided_by.md) | domain | named thing |
| [CellularComponent](CellularComponent.md) | [category](category.md) | range | named thing |
| [Cell](Cell.md) | [provided_by](provided_by.md) | domain | named thing |
| [Cell](Cell.md) | [category](category.md) | range | named thing |
| [CellLine](CellLine.md) | [provided_by](provided_by.md) | domain | named thing |
| [CellLine](CellLine.md) | [category](category.md) | range | named thing |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | [provided_by](provided_by.md) | domain | named thing |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | [category](category.md) | range | named thing |
| [Gene](Gene.md) | [symbol](symbol.md) | domain | named thing |
| [Gene](Gene.md) | [synonym](synonym.md) | domain | named thing |
| [Gene](Gene.md) | [xref](xref.md) | domain | named thing |
| [Gene](Gene.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [Gene](Gene.md) | [provided_by](provided_by.md) | domain | named thing |
| [Gene](Gene.md) | [category](category.md) | range | named thing |
| [GeneProductMixin](GeneProductMixin.md) | [synonym](synonym.md) | domain | named thing |
| [GeneProductMixin](GeneProductMixin.md) | [xref](xref.md) | domain | named thing |
| [GeneProductIsoformMixin](GeneProductIsoformMixin.md) | [synonym](synonym.md) | domain | named thing |
| [GeneProductIsoformMixin](GeneProductIsoformMixin.md) | [xref](xref.md) | domain | named thing |
| [Genome](Genome.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [Genome](Genome.md) | [provided_by](provided_by.md) | domain | named thing |
| [Genome](Genome.md) | [category](category.md) | range | named thing |
| [Exon](Exon.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [Exon](Exon.md) | [trade_name](trade_name.md) | domain | named thing |
| [Exon](Exon.md) | [available_from](available_from.md) | domain | named thing |
| [Exon](Exon.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [Exon](Exon.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [Exon](Exon.md) | [provided_by](provided_by.md) | domain | named thing |
| [Exon](Exon.md) | [category](category.md) | range | named thing |
| [Transcript](Transcript.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [Transcript](Transcript.md) | [trade_name](trade_name.md) | domain | named thing |
| [Transcript](Transcript.md) | [available_from](available_from.md) | domain | named thing |
| [Transcript](Transcript.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [Transcript](Transcript.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [Transcript](Transcript.md) | [provided_by](provided_by.md) | domain | named thing |
| [Transcript](Transcript.md) | [category](category.md) | range | named thing |
| [CodingSequence](CodingSequence.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [CodingSequence](CodingSequence.md) | [trade_name](trade_name.md) | domain | named thing |
| [CodingSequence](CodingSequence.md) | [available_from](available_from.md) | domain | named thing |
| [CodingSequence](CodingSequence.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [CodingSequence](CodingSequence.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [CodingSequence](CodingSequence.md) | [provided_by](provided_by.md) | domain | named thing |
| [CodingSequence](CodingSequence.md) | [category](category.md) | range | named thing |
| [Polypeptide](Polypeptide.md) | [provided_by](provided_by.md) | domain | named thing |
| [Polypeptide](Polypeptide.md) | [category](category.md) | range | named thing |
| [Protein](Protein.md) | [synonym](synonym.md) | domain | named thing |
| [Protein](Protein.md) | [xref](xref.md) | domain | named thing |
| [Protein](Protein.md) | [provided_by](provided_by.md) | domain | named thing |
| [Protein](Protein.md) | [category](category.md) | range | named thing |
| [ProteinIsoform](ProteinIsoform.md) | [synonym](synonym.md) | domain | named thing |
| [ProteinIsoform](ProteinIsoform.md) | [xref](xref.md) | domain | named thing |
| [ProteinIsoform](ProteinIsoform.md) | [provided_by](provided_by.md) | domain | named thing |
| [ProteinIsoform](ProteinIsoform.md) | [category](category.md) | range | named thing |
| [ProteinDomain](ProteinDomain.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | domain | named thing |
| [ProteinDomain](ProteinDomain.md) | [provided_by](provided_by.md) | domain | named thing |
| [ProteinDomain](ProteinDomain.md) | [category](category.md) | range | named thing |
| [ProteinFamily](ProteinFamily.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | domain | named thing |
| [ProteinFamily](ProteinFamily.md) | [provided_by](provided_by.md) | domain | named thing |
| [ProteinFamily](ProteinFamily.md) | [category](category.md) | range | named thing |
| [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | [provided_by](provided_by.md) | domain | named thing |
| [NucleicAcidSequenceMotif](NucleicAcidSequenceMotif.md) | [category](category.md) | range | named thing |
| [RNAProduct](RNAProduct.md) | [synonym](synonym.md) | domain | named thing |
| [RNAProduct](RNAProduct.md) | [xref](xref.md) | domain | named thing |
| [RNAProduct](RNAProduct.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [RNAProduct](RNAProduct.md) | [trade_name](trade_name.md) | domain | named thing |
| [RNAProduct](RNAProduct.md) | [available_from](available_from.md) | domain | named thing |
| [RNAProduct](RNAProduct.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [RNAProduct](RNAProduct.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [RNAProduct](RNAProduct.md) | [provided_by](provided_by.md) | domain | named thing |
| [RNAProduct](RNAProduct.md) | [category](category.md) | range | named thing |
| [RNAProductIsoform](RNAProductIsoform.md) | [synonym](synonym.md) | domain | named thing |
| [RNAProductIsoform](RNAProductIsoform.md) | [xref](xref.md) | domain | named thing |
| [RNAProductIsoform](RNAProductIsoform.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [RNAProductIsoform](RNAProductIsoform.md) | [trade_name](trade_name.md) | domain | named thing |
| [RNAProductIsoform](RNAProductIsoform.md) | [available_from](available_from.md) | domain | named thing |
| [RNAProductIsoform](RNAProductIsoform.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [RNAProductIsoform](RNAProductIsoform.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [RNAProductIsoform](RNAProductIsoform.md) | [provided_by](provided_by.md) | domain | named thing |
| [RNAProductIsoform](RNAProductIsoform.md) | [category](category.md) | range | named thing |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [synonym](synonym.md) | domain | named thing |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [xref](xref.md) | domain | named thing |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [trade_name](trade_name.md) | domain | named thing |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [available_from](available_from.md) | domain | named thing |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [provided_by](provided_by.md) | domain | named thing |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [category](category.md) | range | named thing |
| [MicroRNA](MicroRNA.md) | [synonym](synonym.md) | domain | named thing |
| [MicroRNA](MicroRNA.md) | [xref](xref.md) | domain | named thing |
| [MicroRNA](MicroRNA.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [MicroRNA](MicroRNA.md) | [trade_name](trade_name.md) | domain | named thing |
| [MicroRNA](MicroRNA.md) | [available_from](available_from.md) | domain | named thing |
| [MicroRNA](MicroRNA.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [MicroRNA](MicroRNA.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [MicroRNA](MicroRNA.md) | [provided_by](provided_by.md) | domain | named thing |
| [MicroRNA](MicroRNA.md) | [category](category.md) | range | named thing |
| [SiRNA](SiRNA.md) | [synonym](synonym.md) | domain | named thing |
| [SiRNA](SiRNA.md) | [xref](xref.md) | domain | named thing |
| [SiRNA](SiRNA.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [SiRNA](SiRNA.md) | [trade_name](trade_name.md) | domain | named thing |
| [SiRNA](SiRNA.md) | [available_from](available_from.md) | domain | named thing |
| [SiRNA](SiRNA.md) | [max_tolerated_dose](max_tolerated_dose.md) | domain | named thing |
| [SiRNA](SiRNA.md) | [is_toxic](is_toxic.md) | domain | named thing |
| [SiRNA](SiRNA.md) | [provided_by](provided_by.md) | domain | named thing |
| [SiRNA](SiRNA.md) | [category](category.md) | range | named thing |
| [GeneGroupingMixin](GeneGroupingMixin.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | domain | named thing |
| [GeneFamily](GeneFamily.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | domain | named thing |
| [GeneFamily](GeneFamily.md) | [provided_by](provided_by.md) | domain | named thing |
| [GeneFamily](GeneFamily.md) | [category](category.md) | range | named thing |
| [Zygosity](Zygosity.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [Genotype](Genotype.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [Genotype](Genotype.md) | [provided_by](provided_by.md) | domain | named thing |
| [Genotype](Genotype.md) | [category](category.md) | range | named thing |
| [Haplotype](Haplotype.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [Haplotype](Haplotype.md) | [provided_by](provided_by.md) | domain | named thing |
| [Haplotype](Haplotype.md) | [category](category.md) | range | named thing |
| [SequenceVariant](SequenceVariant.md) | [has_gene](has_gene.md) | domain | named thing |
| [SequenceVariant](SequenceVariant.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [SequenceVariant](SequenceVariant.md) | [provided_by](provided_by.md) | domain | named thing |
| [SequenceVariant](SequenceVariant.md) | [category](category.md) | range | named thing |
| [Snv](Snv.md) | [has_gene](has_gene.md) | domain | named thing |
| [Snv](Snv.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [Snv](Snv.md) | [provided_by](provided_by.md) | domain | named thing |
| [Snv](Snv.md) | [category](category.md) | range | named thing |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [provided_by](provided_by.md) | domain | named thing |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [category](category.md) | range | named thing |
| [ClinicalAttribute](ClinicalAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [ClinicalMeasurement](ClinicalMeasurement.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [ClinicalModifier](ClinicalModifier.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [ClinicalCourse](ClinicalCourse.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [Onset](Onset.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [ClinicalEntity](ClinicalEntity.md) | [provided_by](provided_by.md) | domain | named thing |
| [ClinicalEntity](ClinicalEntity.md) | [category](category.md) | range | named thing |
| [ClinicalTrial](ClinicalTrial.md) | [provided_by](provided_by.md) | domain | named thing |
| [ClinicalTrial](ClinicalTrial.md) | [category](category.md) | range | named thing |
| [ClinicalIntervention](ClinicalIntervention.md) | [provided_by](provided_by.md) | domain | named thing |
| [ClinicalIntervention](ClinicalIntervention.md) | [category](category.md) | range | named thing |
| [ClinicalFinding](ClinicalFinding.md) | [provided_by](provided_by.md) | domain | named thing |
| [ClinicalFinding](ClinicalFinding.md) | [category](category.md) | range | named thing |
| [Hospitalization](Hospitalization.md) | [provided_by](provided_by.md) | domain | named thing |
| [Hospitalization](Hospitalization.md) | [category](category.md) | range | named thing |
| [SocioeconomicAttribute](SocioeconomicAttribute.md) | [has_qualitative_value](has_qualitative_value.md) | range | named thing |
| [Case](Case.md) | [provided_by](provided_by.md) | domain | named thing |
| [Case](Case.md) | [category](category.md) | range | named thing |
| [Cohort](Cohort.md) | [provided_by](provided_by.md) | domain | named thing |
| [Cohort](Cohort.md) | [category](category.md) | range | named thing |
| [ExposureEvent](ExposureEvent.md) | [timepoint](timepoint.md) | domain | named thing |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [timepoint](timepoint.md) | domain | named thing |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | domain | named thing |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [has_biological_sequence](has_biological_sequence.md) | domain | named thing |
| [PathologicalProcess](PathologicalProcess.md) | [provided_by](provided_by.md) | domain | named thing |
| [PathologicalProcess](PathologicalProcess.md) | [category](category.md) | range | named thing |
| [PathologicalProcessExposure](PathologicalProcessExposure.md) | [timepoint](timepoint.md) | domain | named thing |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | [provided_by](provided_by.md) | domain | named thing |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | [category](category.md) | range | named thing |
| [PathologicalAnatomicalExposure](PathologicalAnatomicalExposure.md) | [timepoint](timepoint.md) | domain | named thing |
| [DiseaseOrPhenotypicFeatureExposure](DiseaseOrPhenotypicFeatureExposure.md) | [timepoint](timepoint.md) | domain | named thing |
| [ChemicalExposure](ChemicalExposure.md) | [timepoint](timepoint.md) | domain | named thing |
| [DrugExposure](DrugExposure.md) | [timepoint](timepoint.md) | domain | named thing |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [has_gene_or_gene_product](has_gene_or_gene_product.md) | domain | named thing |
| [DrugToGeneInteractionExposure](DrugToGeneInteractionExposure.md) | [timepoint](timepoint.md) | domain | named thing |
| [Treatment](Treatment.md) | [has_drug](has_drug.md) | domain | named thing |
| [Treatment](Treatment.md) | [has_device](has_device.md) | domain | named thing |
| [Treatment](Treatment.md) | [has_procedure](has_procedure.md) | domain | named thing |
| [Treatment](Treatment.md) | [timepoint](timepoint.md) | domain | named thing |
| [Treatment](Treatment.md) | [provided_by](provided_by.md) | domain | named thing |
| [Treatment](Treatment.md) | [category](category.md) | range | named thing |
| [BioticExposure](BioticExposure.md) | [timepoint](timepoint.md) | domain | named thing |
| [GeographicExposure](GeographicExposure.md) | [timepoint](timepoint.md) | domain | named thing |
| [EnvironmentalExposure](EnvironmentalExposure.md) | [timepoint](timepoint.md) | domain | named thing |
| [BehavioralExposure](BehavioralExposure.md) | [timepoint](timepoint.md) | domain | named thing |
| [SocioeconomicExposure](SocioeconomicExposure.md) | [timepoint](timepoint.md) | domain | named thing |
| [Association](Association.md) | [subject](subject.md) | range | named thing |
| [Association](Association.md) | [object](object.md) | range | named thing |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object](object.md) | range | named thing |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject](subject.md) | range | named thing |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [subject](subject.md) | range | named thing |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object](object.md) | range | named thing |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_count](has_count.md) | domain | named thing |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_total](has_total.md) | domain | named thing |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_quotient](has_quotient.md) | domain | named thing |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_percentage](has_percentage.md) | domain | named thing |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject](subject.md) | range | named thing |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object](object.md) | range | named thing |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject](subject.md) | range | named thing |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object](object.md) | range | named thing |
| [SequenceAssociation](SequenceAssociation.md) | [subject](subject.md) | range | named thing |
| [SequenceAssociation](SequenceAssociation.md) | [object](object.md) | range | named thing |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object](object.md) | range | named thing |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: named thing
exact_mappings:
- BFO:0000001
- WIKIDATA:Q35120
- UMLSSG:OBJC
- STY:T071
- dcid:Thing
description: a databased entity or concept/class
from_schema: https://w3id.org/biolink/biolink-model
is_a: entity
slots:
- provided by
slot_usage:
  category:
    name: category
    range: named thing
    required: true

```
</details>

### Induced

<details>
```yaml
name: named thing
exact_mappings:
- BFO:0000001
- WIKIDATA:Q35120
- UMLSSG:OBJC
- STY:T071
- dcid:Thing
description: a databased entity or concept/class
from_schema: https://w3id.org/biolink/biolink-model
is_a: entity
slot_usage:
  category:
    name: category
    range: named thing
    required: true
attributes:
  provided by:
    name: provided by
    description: The value in this node property represents the knowledge provider
      that created or assembled the node and all of its attributes.  Used internally
      to represent how a particular node made its way into a knowledge provider or
      graph.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    multivalued: true
    alias: provided_by
    owner: named thing
    range: string
  id:
    name: id
    exact_mappings:
    - alliancegenome:primaryId
    - gff3:ID
    - gpi:DB_Object_ID
    description: A unique identifier for an entity. Must be either a CURIE shorthand
      for a URI or a complete URI
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    identifier: true
    alias: id
    owner: named thing
    range: string
    required: true
  iri:
    name: iri
    exact_mappings:
    - WIKIDATA_PROPERTY:P854
    description: An IRI for an entity. This is determined by the id using expansion
      rules.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    alias: iri
    owner: named thing
    range: iri type
  category:
    name: category
    description: "Name of the high level ontology class in which this entity is categorized.\
      \ Corresponds to the label for the biolink entity type class.\n * In a neo4j\
      \ database this MAY correspond to the neo4j label tag.\n * In an RDF database\
      \ it should be a biolink model class URI.\nThis field is multi-valued. It should\
      \ include values for ancestors of the biolink class; for example, a protein\
      \ such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`,\
      \ `biolink:MolecularEntity`, ...\nIn an RDF database, nodes will typically have\
      \ an rdf:type triples. This can be to the most specific biolink class, or potentially\
      \ to a class more specific than something in biolink. For example, a sequence\
      \ feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site,\
      \ which is more specific than anything in biolink. Here we would have categories\
      \ {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}"
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: type
    domain: entity
    multivalued: true
    designates_type: true
    alias: category
    owner: named thing
    is_class_field: true
    range: named thing
    required: true
  type:
    name: type
    exact_mappings:
    - alliancegenome:soTermId
    - gff3:type
    - gpi:DB_Object_Type
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdf:type
    alias: type
    owner: named thing
    range: string
  name:
    name: name
    aliases:
    - label
    - display name
    - title
    exact_mappings:
    - gff3:Name
    - gpi:DB_Object_Name
    narrow_mappings:
    - dct:title
    - WIKIDATA_PROPERTY:P1476
    description: A human-readable name for an attribute or entity.
    in_subset:
    - translator_minimal
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdfs:label
    alias: name
    owner: named thing
    range: label type
  description:
    name: description
    aliases:
    - definition
    exact_mappings:
    - IAO:0000115
    - skos:definitions
    narrow_mappings:
    - gff3:Description
    description: a human-readable description of an entity
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: dct:description
    alias: description
    owner: named thing
    range: narrative text
  source:
    name: source
    deprecated: 'True'
    from_schema: https://w3id.org/biolink/biolink-model
    alias: source
    owner: named thing
    range: string
  has attribute:
    name: has attribute
    exact_mappings:
    - SIO:000008
    close_mappings:
    - OBI:0001927
    narrow_mappings:
    - OBAN:association_has_subject_property
    - OBAN:association_has_object_property
    - CPT:has_possibly_included_panel_element
    - DRUGBANK:category
    - EFO:is_executed_in
    - HANCESTRO:0301
    - LOINC:has_action_guidance
    - LOINC:has_adjustment
    - LOINC:has_aggregation_view
    - LOINC:has_approach_guidance
    - LOINC:has_divisor
    - LOINC:has_exam
    - LOINC:has_method
    - LOINC:has_modality_subtype
    - LOINC:has_object_guidance
    - LOINC:has_scale
    - LOINC:has_suffix
    - LOINC:has_time_aspect
    - LOINC:has_time_modifier
    - LOINC:has_timing_of
    - NCIT:R88
    - NCIT:eo_disease_has_property_or_attribute
    - NCIT:has_data_element
    - NCIT:has_pharmaceutical_administration_method
    - NCIT:has_pharmaceutical_basic_dose_form
    - NCIT:has_pharmaceutical_intended_site
    - NCIT:has_pharmaceutical_release_characteristics
    - NCIT:has_pharmaceutical_state_of_matter
    - NCIT:has_pharmaceutical_transformation
    - NCIT:is_qualified_by
    - NCIT:qualifier_applies_to
    - NCIT:role_has_domain
    - NCIT:role_has_range
    - INO:0000154
    - HANCESTRO:0308
    - OMIM:has_inheritance_type
    - ORPHA:C016
    - ORPHA:C017
    - RO:0000053
    - RO:0000086
    - RO:0000087
    - SNOMED:has_access
    - SNOMED:has_clinical_course
    - SNOMED:has_count_of_base_of_active_ingredient
    - SNOMED:has_dose_form_administration_method
    - SNOMED:has_dose_form_release_characteristic
    - SNOMED:has_dose_form_transformation
    - SNOMED:has_finding_context
    - SNOMED:has_finding_informer
    - SNOMED:has_inherent_attribute
    - SNOMED:has_intent
    - SNOMED:has_interpretation
    - SNOMED:has_laterality
    - SNOMED:has_measurement_method
    - SNOMED:has_method
    - SNOMED:has_priority
    - SNOMED:has_procedure_context
    - SNOMED:has_process_duration
    - SNOMED:has_property
    - SNOMED:has_revision_status
    - SNOMED:has_scale_type
    - SNOMED:has_severity
    - SNOMED:has_specimen
    - SNOMED:has_state_of_matter
    - SNOMED:has_subject_relationship_context
    - SNOMED:has_surgical_approach
    - SNOMED:has_technique
    - SNOMED:has_temporal_context
    - SNOMED:has_time_aspect
    - SNOMED:has_units
    - UMLS:has_structural_class
    - UMLS:has_supported_concept_property
    - UMLS:has_supported_concept_relationship
    - UMLS:may_be_qualified_by
    description: connects any entity to an attribute
    in_subset:
    - samples
    from_schema: https://w3id.org/biolink/biolink-model
    domain: entity
    multivalued: true
    alias: has_attribute
    owner: named thing
    range: attribute

```
</details>