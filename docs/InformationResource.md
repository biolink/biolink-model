# Class: InformationResource
_A database or knowledgebase and its supporting ecosystem of interfaces  and services that deliver content to consumers (e.g. web portals, APIs,  query endpoints, streaming services, data downloads, etc.). A single Information Resource by this definition may span many different datasets or databases, and include many access endpoints and user interfaces. Information Resources include project-specific resources such as a Translator Knowledge Provider, and community knowledgebases like ChemBL, OMIM, or DGIdb._





URI: [biolink:InformationResource](https://w3id.org/biolink/vocab/InformationResource)




## Inheritance

* [Entity](Entity.md)
    * [NamedThing](NamedThing.md)
        * [InformationContentEntity](InformationContentEntity.md)
            * **InformationResource**




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [license](license.md) | [string](string.md) | 0..1 | None  | . |
| [rights](rights.md) | [string](string.md) | 0..1 | None  | . |
| [format](format.md) | [string](string.md) | 0..1 | None  | . |
| [creation_date](creation_date.md) | [date](date.md) | 0..1 | date on which an entity was created. This can be applied to nodes or edges  | . |
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
| [Association](Association.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [Association](Association.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [Association](Association.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [Association](Association.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [ContributorAssociation](ContributorAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [ContributorAssociation](ContributorAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [ContributorAssociation](ContributorAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [ContributorAssociation](ContributorAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [FunctionalAssociation](FunctionalAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [FunctionalAssociation](FunctionalAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [FunctionalAssociation](FunctionalAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [FunctionalAssociation](FunctionalAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [SequenceAssociation](SequenceAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [SequenceAssociation](SequenceAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [SequenceAssociation](SequenceAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [SequenceAssociation](SequenceAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [knowledge_source](knowledge_source.md) | range | information resource |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | range | information resource |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | range | information resource |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | range | information resource |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: information resource
aliases:
- knowledgebase
description: A database or knowledgebase and its supporting ecosystem of interfaces  and
  services that deliver content to consumers (e.g. web portals, APIs,  query endpoints,
  streaming services, data downloads, etc.). A single Information Resource by this
  definition may span many different datasets or databases, and include many access
  endpoints and user interfaces. Information Resources include project-specific resources
  such as a Translator Knowledge Provider, and community knowledgebases like ChemBL,
  OMIM, or DGIdb.
in_subset:
- translator_minimal
from_schema: https://w3id.org/biolink/biolink-model
is_a: information content entity

```
</details>

### Induced

<details>
```yaml
name: information resource
aliases:
- knowledgebase
description: A database or knowledgebase and its supporting ecosystem of interfaces  and
  services that deliver content to consumers (e.g. web portals, APIs,  query endpoints,
  streaming services, data downloads, etc.). A single Information Resource by this
  definition may span many different datasets or databases, and include many access
  endpoints and user interfaces. Information Resources include project-specific resources
  such as a Translator Knowledge Provider, and community knowledgebases like ChemBL,
  OMIM, or DGIdb.
in_subset:
- translator_minimal
from_schema: https://w3id.org/biolink/biolink-model
is_a: information content entity
attributes:
  license:
    name: license
    exact_mappings:
    - dct:license
    narrow_mappings:
    - WIKIDATA_PROPERTY:P275
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: information content entity
    alias: license
    owner: information resource
    range: string
  rights:
    name: rights
    exact_mappings:
    - dct:rights
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: information content entity
    alias: rights
    owner: information resource
    range: string
  format:
    name: format
    exact_mappings:
    - dct:format
    - WIKIDATA_PROPERTY:P2701
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: information content entity
    alias: format
    owner: information resource
    range: string
  creation date:
    name: creation date
    aliases:
    - publication date
    exact_mappings:
    - dct:createdOn
    - WIKIDATA_PROPERTY:P577
    description: date on which an entity was created. This can be applied to nodes
      or edges
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: node property
    domain: named thing
    alias: creation_date
    owner: information resource
    range: date
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
    owner: information resource
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
    owner: information resource
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
    owner: information resource
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
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: type
    domain: entity
    multivalued: true
    designates_type: true
    alias: category
    owner: information resource
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
    owner: information resource
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
    owner: information resource
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
    owner: information resource
    range: narrative text
  source:
    name: source
    deprecated: 'True'
    from_schema: https://w3id.org/biolink/biolink-model
    alias: source
    owner: information resource
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
    owner: information resource
    range: attribute

```
</details>