# Class: Association
_A typed association between two entities, supported by evidence_





URI: [biolink:Association](https://w3id.org/biolink/vocab/Association)




## Inheritance

* [Entity](Entity.md)
    * **Association**
        * [ContributorAssociation](ContributorAssociation.md)
        * [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md)
        * [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)
        * [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)
        * [GeneToGeneAssociation](GeneToGeneAssociation.md)
        * [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) [ cell line to entity association mixin entity to disease or phenotypic feature association mixin]
        * [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) [ chemical to entity association mixin]
        * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) [ chemical to entity association mixin entity to disease or phenotypic feature association mixin]
        * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) [ chemical to entity association mixin]
        * [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) [ chemical to entity association mixin]
        * [DrugToGeneAssociation](DrugToGeneAssociation.md) [ drug to entity association mixin]
        * [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md)
        * [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) [ material sample to entity association mixin entity to disease or phenotypic feature association mixin]
        * [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) [ disease to entity association mixin entity to exposure event association mixin]
        * [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) [ exposure event to entity association mixin entity to outcome association mixin]
        * [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md)
        * [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) [ disease or phenotypic feature to entity association mixin]
        * [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) [ entity to phenotypic feature association mixin genotype to entity association mixin]
        * [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) [ entity to phenotypic feature association mixin]
        * [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) [ entity to phenotypic feature association mixin disease to entity association mixin]
        * [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) [ entity to phenotypic feature association mixin case to entity association mixin]
        * [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) [ entity to phenotypic feature association mixin]
        * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) [ entity to phenotypic feature association mixin gene to entity association mixin]
        * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) [ entity to disease association mixin gene to entity association mixin]
        * [VariantToGeneAssociation](VariantToGeneAssociation.md) [ variant to entity association mixin]
        * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) [ variant to entity association mixin frequency quantifier frequency qualifier mixin]
        * [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md)
        * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) [ variant to entity association mixin entity to phenotypic feature association mixin]
        * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) [ variant to entity association mixin entity to disease association mixin]
        * [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) [ genotype to entity association mixin entity to disease association mixin]
        * [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) [ model to disease association mixin entity to disease association mixin]
        * [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md)
        * [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md)
        * [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)
        * [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md)
        * [FunctionalAssociation](FunctionalAssociation.md)
        * [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md)
        * [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md)
        * [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md)
        * [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md)
        * [SequenceAssociation](SequenceAssociation.md)
        * [SequenceFeatureRelationship](SequenceFeatureRelationship.md)
        * [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md)
        * [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
        * [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) [ organism taxon to entity association]
        * [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) [ organism taxon to entity association]




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [subject](subject.md) | [NamedThing](NamedThing.md) | 1..1 | connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.  | . |
| [predicate](predicate.md) | [predicate_type](predicate_type.md) | 1..1 | A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.  | . |
| [object](object.md) | [NamedThing](NamedThing.md) | 1..1 | connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.  | . |
| [relation](relation.md) | [string](string.md) | 0..1 | None  | . |
| [negated](negated.md) | [boolean](boolean.md) | 0..1 | if set to true, then the association is negated i.e. is not true  | . |
| [qualifiers](qualifiers.md) | [OntologyClass](OntologyClass.md) | 0..* | connects an association to qualifiers that modify or qualify the meaning of that association  | . |
| [publications](publications.md) | [Publication](Publication.md) | 0..* | connects an association to publications supporting the association  | . |
| [has_evidence](has_evidence.md) | [EvidenceType](EvidenceType.md) | 0..* | connects an association to an instance of supporting evidence  | . |
| [knowledge_source](knowledge_source.md) | [InformationResource](InformationResource.md) | 0..* | An Information Resource from which the knowledge expressed in an Association was retrieved, directly or indirectly. This can be any resource through which the knowledge passed on its way to its currently serialized form. In practice, implementers should use one of the more specific subtypes of this generic property.  | . |
| [original_knowledge_source](original_knowledge_source.md) | [InformationResource](InformationResource.md) | 0..* | The Information Resource that created the original record of the knowledge expressed in an Association (e.g. via curation of the knowledge from the literature, or generation of the knowledge de novo through computation, reasoning, inference over data).  | . |
| [primary_knowledge_source](primary_knowledge_source.md) | [InformationResource](InformationResource.md) | 0..* | The most upstream source of the knowledge expressed in an Association that an implementer can identify (may or may not be the 'original' source).  | . |
| [aggregator_knowledge_source](aggregator_knowledge_source.md) | [InformationResource](InformationResource.md) | 0..* | An intermediate aggregator resource from which knowledge expressed in an Association was retrieved downstream of the original source, on its path to its current serialized form.  | . |
| [id](id.md) | [string](string.md) | 1..1 | A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI  | . |
| [iri](iri.md) | [iri_type](iri_type.md) | 0..1 | An IRI for an entity. This is determined by the id using expansion rules.  | . |
| [category](category.md) | [category_type](category_type.md) | 0..* | Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}  | . |
| [type](type.md) | [string](string.md) | 0..1 | rdf:type of biolink:Association should be fixed at rdf:Statement  | . |
| [name](name.md) | [label_type](label_type.md) | 0..1 | A human-readable name for an attribute or entity.  | . |
| [description](description.md) | [narrative_text](narrative_text.md) | 0..1 | a human-readable description of an entity  | . |
| [source](source.md) | [string](string.md) | 0..1 | None  | . |
| [has_attribute](has_attribute.md) | [Attribute](Attribute.md) | 0..* | connects any entity to an attribute  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Association](Association.md) | [subject](subject.md) | domain | association |
| [Association](Association.md) | [predicate](predicate.md) | domain | association |
| [Association](Association.md) | [object](object.md) | domain | association |
| [Association](Association.md) | [negated](negated.md) | domain | association |
| [Association](Association.md) | [qualifiers](qualifiers.md) | domain | association |
| [Association](Association.md) | [publications](publications.md) | domain | association |
| [Association](Association.md) | [has_evidence](has_evidence.md) | domain | association |
| [Association](Association.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [Association](Association.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [Association](Association.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [Association](Association.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [ContributorAssociation](ContributorAssociation.md) | [subject](subject.md) | domain | association |
| [ContributorAssociation](ContributorAssociation.md) | [predicate](predicate.md) | domain | association |
| [ContributorAssociation](ContributorAssociation.md) | [object](object.md) | domain | association |
| [ContributorAssociation](ContributorAssociation.md) | [negated](negated.md) | domain | association |
| [ContributorAssociation](ContributorAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [ContributorAssociation](ContributorAssociation.md) | [publications](publications.md) | domain | association |
| [ContributorAssociation](ContributorAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [ContributorAssociation](ContributorAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [ContributorAssociation](ContributorAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [ContributorAssociation](ContributorAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [ContributorAssociation](ContributorAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [subject](subject.md) | domain | association |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [predicate](predicate.md) | domain | association |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [object](object.md) | domain | association |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [negated](negated.md) | domain | association |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [publications](publications.md) | domain | association |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [subject](subject.md) | domain | association |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [predicate](predicate.md) | domain | association |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [object](object.md) | domain | association |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [negated](negated.md) | domain | association |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [publications](publications.md) | domain | association |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GenotypeToGeneAssociation](GenotypeToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [subject](subject.md) | domain | association |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [predicate](predicate.md) | domain | association |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [object](object.md) | domain | association |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [negated](negated.md) | domain | association |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [publications](publications.md) | domain | association |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GenotypeToVariantAssociation](GenotypeToVariantAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [subject](subject.md) | domain | association |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [predicate](predicate.md) | domain | association |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [object](object.md) | domain | association |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [negated](negated.md) | domain | association |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [publications](publications.md) | domain | association |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GeneToGeneAssociation](GeneToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [subject](subject.md) | domain | association |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [predicate](predicate.md) | domain | association |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [object](object.md) | domain | association |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [negated](negated.md) | domain | association |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [publications](publications.md) | domain | association |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GeneToGeneHomologyAssociation](GeneToGeneHomologyAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GeneExpressionMixin](GeneExpressionMixin.md) | [quantifier_qualifier](quantifier_qualifier.md) | domain | association |
| [GeneExpressionMixin](GeneExpressionMixin.md) | [expression_site](expression_site.md) | domain | association |
| [GeneExpressionMixin](GeneExpressionMixin.md) | [stage_qualifier](stage_qualifier.md) | domain | association |
| [GeneExpressionMixin](GeneExpressionMixin.md) | [phenotypic_state](phenotypic_state.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [quantifier_qualifier](quantifier_qualifier.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [expression_site](expression_site.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [stage_qualifier](stage_qualifier.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [phenotypic_state](phenotypic_state.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [subject](subject.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [predicate](predicate.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [object](object.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [negated](negated.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [publications](publications.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GeneToGeneCoexpressionAssociation](GeneToGeneCoexpressionAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [subject](subject.md) | domain | association |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [predicate](predicate.md) | domain | association |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [object](object.md) | domain | association |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [negated](negated.md) | domain | association |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [qualifiers](qualifiers.md) | domain | association |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [publications](publications.md) | domain | association |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [has_evidence](has_evidence.md) | domain | association |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [PairwiseGeneToGeneInteraction](PairwiseGeneToGeneInteraction.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [interacting_molecules_category](interacting_molecules_category.md) | domain | association |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [subject](subject.md) | domain | association |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [predicate](predicate.md) | domain | association |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [object](object.md) | domain | association |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [negated](negated.md) | domain | association |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [qualifiers](qualifiers.md) | domain | association |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [publications](publications.md) | domain | association |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [has_evidence](has_evidence.md) | domain | association |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [PairwiseMolecularInteraction](PairwiseMolecularInteraction.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | association |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | association |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [object](object.md) | domain | association |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | association |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | association |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [subject](subject.md) | domain | association |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [predicate](predicate.md) | domain | association |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [object](object.md) | domain | association |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [negated](negated.md) | domain | association |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [publications](publications.md) | domain | association |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [ChemicalToChemicalAssociation](ChemicalToChemicalAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [stoichiometry](stoichiometry.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [reaction_direction](reaction_direction.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [reaction_side](reaction_side.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [subject](subject.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [predicate](predicate.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [object](object.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [negated](negated.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [publications](publications.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [ReactionToParticipantAssociation](ReactionToParticipantAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [stoichiometry](stoichiometry.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [reaction_direction](reaction_direction.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [reaction_side](reaction_side.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [subject](subject.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [predicate](predicate.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [object](object.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [negated](negated.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [publications](publications.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [ReactionToCatalystAssociation](ReactionToCatalystAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [catalyst_qualifier](catalyst_qualifier.md) | domain | association |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [subject](subject.md) | domain | association |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [predicate](predicate.md) | domain | association |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [object](object.md) | domain | association |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [negated](negated.md) | domain | association |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [publications](publications.md) | domain | association |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [ChemicalToChemicalDerivationAssociation](ChemicalToChemicalDerivationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | association |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | association |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [object](object.md) | domain | association |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | association |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | association |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [subject](subject.md) | domain | association |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [predicate](predicate.md) | domain | association |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [object](object.md) | domain | association |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [negated](negated.md) | domain | association |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [publications](publications.md) | domain | association |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [subject](subject.md) | domain | association |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [predicate](predicate.md) | domain | association |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [object](object.md) | domain | association |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [negated](negated.md) | domain | association |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [publications](publications.md) | domain | association |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [subject](subject.md) | domain | association |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [predicate](predicate.md) | domain | association |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [object](object.md) | domain | association |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [negated](negated.md) | domain | association |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [publications](publications.md) | domain | association |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [DrugToGeneAssociation](DrugToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [subject](subject.md) | domain | association |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [predicate](predicate.md) | domain | association |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [object](object.md) | domain | association |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [negated](negated.md) | domain | association |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [publications](publications.md) | domain | association |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | association |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | association |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [object](object.md) | domain | association |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | association |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | association |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [MaterialSampleToDiseaseOrPhenotypicFeatureAssociation](MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [subject](subject.md) | domain | association |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [predicate](predicate.md) | domain | association |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [object](object.md) | domain | association |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [negated](negated.md) | domain | association |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [publications](publications.md) | domain | association |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [DiseaseToExposureEventAssociation](DiseaseToExposureEventAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_population_context](has_population_context.md) | domain | association |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_temporal_context](has_temporal_context.md) | domain | association |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [subject](subject.md) | domain | association |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [predicate](predicate.md) | domain | association |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [object](object.md) | domain | association |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [negated](negated.md) | domain | association |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [publications](publications.md) | domain | association |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [ExposureEventToOutcomeAssociation](ExposureEventToOutcomeAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [FrequencyQualifierMixin](FrequencyQualifierMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [EntityToFeatureOrDiseaseQualifiersMixin](EntityToFeatureOrDiseaseQualifiersMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [sex_qualifier](sex_qualifier.md) | domain | association |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [EntityToPhenotypicFeatureAssociationMixin](EntityToPhenotypicFeatureAssociationMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [predicate](predicate.md) | domain | association |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [object](object.md) | domain | association |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [negated](negated.md) | domain | association |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [publications](publications.md) | domain | association |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [InformationContentEntityToNamedThingAssociation](InformationContentEntityToNamedThingAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [EntityToDiseaseAssociationMixin](EntityToDiseaseAssociationMixin.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [subject](subject.md) | domain | association |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [predicate](predicate.md) | domain | association |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [object](object.md) | domain | association |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [negated](negated.md) | domain | association |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [publications](publications.md) | domain | association |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [ExposureEventToPhenotypicFeatureAssociation](ExposureEventToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [DiseaseToPhenotypicFeatureAssociation](DiseaseToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [CaseToPhenotypicFeatureAssociation](CaseToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [subject](subject.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [predicate](predicate.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [object](object.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [negated](negated.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [publications](publications.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [BehaviorToBehavioralFeatureAssociation](BehaviorToBehavioralFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [subject](subject.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [predicate](predicate.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [object](object.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [negated](negated.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [publications](publications.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [subject](subject.md) | domain | association |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [predicate](predicate.md) | domain | association |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [object](object.md) | domain | association |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [negated](negated.md) | domain | association |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [publications](publications.md) | domain | association |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [VariantToGeneAssociation](VariantToGeneAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [quantifier_qualifier](quantifier_qualifier.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [expression_site](expression_site.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [stage_qualifier](stage_qualifier.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [phenotypic_state](phenotypic_state.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [subject](subject.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [predicate](predicate.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [object](object.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [negated](negated.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [publications](publications.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [VariantToGeneExpressionAssociation](VariantToGeneExpressionAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [subject](subject.md) | domain | association |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [predicate](predicate.md) | domain | association |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [object](object.md) | domain | association |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [negated](negated.md) | domain | association |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [publications](publications.md) | domain | association |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [VariantToPopulationAssociation](VariantToPopulationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [subject](subject.md) | domain | association |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [predicate](predicate.md) | domain | association |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [object](object.md) | domain | association |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [negated](negated.md) | domain | association |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [publications](publications.md) | domain | association |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [PopulationToPopulationAssociation](PopulationToPopulationAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [sex_qualifier](sex_qualifier.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [subject](subject.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [predicate](predicate.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [object](object.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [negated](negated.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [publications](publications.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [subject](subject.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [predicate](predicate.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [object](object.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [negated](negated.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [publications](publications.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [GenotypeToDiseaseAssociation](GenotypeToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [VariantAsAModelOfDiseaseAssociation](VariantAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [GenotypeAsAModelOfDiseaseAssociation](GenotypeAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [CellLineAsAModelOfDiseaseAssociation](CellLineAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [subject](subject.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [predicate](predicate.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [object](object.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [negated](negated.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [publications](publications.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [OrganismalEntityAsAModelOfDiseaseAssociation](OrganismalEntityAsAModelOfDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [subject](subject.md) | domain | association |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [predicate](predicate.md) | domain | association |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [object](object.md) | domain | association |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [negated](negated.md) | domain | association |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [publications](publications.md) | domain | association |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [OrganismToOrganismAssociation](OrganismToOrganismAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [subject](subject.md) | domain | association |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [predicate](predicate.md) | domain | association |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [object](object.md) | domain | association |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [negated](negated.md) | domain | association |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [publications](publications.md) | domain | association |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [TaxonToTaxonAssociation](TaxonToTaxonAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [sequence_variant_qualifier](sequence_variant_qualifier.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [subject](subject.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [predicate](predicate.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [object](object.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [negated](negated.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [publications](publications.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [severity_qualifier](severity_qualifier.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [onset_qualifier](onset_qualifier.md) | domain | association |
| [GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md) | [frequency_qualifier](frequency_qualifier.md) | domain | association |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [stage_qualifier](stage_qualifier.md) | domain | association |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [quantifier_qualifier](quantifier_qualifier.md) | domain | association |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [subject](subject.md) | domain | association |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [predicate](predicate.md) | domain | association |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [object](object.md) | domain | association |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [negated](negated.md) | domain | association |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [publications](publications.md) | domain | association |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [subject](subject.md) | domain | association |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [predicate](predicate.md) | domain | association |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [object](object.md) | domain | association |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [negated](negated.md) | domain | association |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [publications](publications.md) | domain | association |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [SequenceVariantModulatesTreatmentAssociation](SequenceVariantModulatesTreatmentAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [FunctionalAssociation](FunctionalAssociation.md) | [subject](subject.md) | domain | association |
| [FunctionalAssociation](FunctionalAssociation.md) | [predicate](predicate.md) | domain | association |
| [FunctionalAssociation](FunctionalAssociation.md) | [object](object.md) | domain | association |
| [FunctionalAssociation](FunctionalAssociation.md) | [negated](negated.md) | domain | association |
| [FunctionalAssociation](FunctionalAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [FunctionalAssociation](FunctionalAssociation.md) | [publications](publications.md) | domain | association |
| [FunctionalAssociation](FunctionalAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [FunctionalAssociation](FunctionalAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [FunctionalAssociation](FunctionalAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [FunctionalAssociation](FunctionalAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [FunctionalAssociation](FunctionalAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [predicate](predicate.md) | domain | association |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [object](object.md) | domain | association |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [negated](negated.md) | domain | association |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [publications](publications.md) | domain | association |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [predicate](predicate.md) | domain | association |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [object](object.md) | domain | association |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [negated](negated.md) | domain | association |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [publications](publications.md) | domain | association |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [predicate](predicate.md) | domain | association |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [object](object.md) | domain | association |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [negated](negated.md) | domain | association |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [publications](publications.md) | domain | association |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [subject](subject.md) | domain | association |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [predicate](predicate.md) | domain | association |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [object](object.md) | domain | association |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [negated](negated.md) | domain | association |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [publications](publications.md) | domain | association |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [MolecularActivityToChemicalEntityAssociation](MolecularActivityToChemicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [subject](subject.md) | domain | association |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [predicate](predicate.md) | domain | association |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [object](object.md) | domain | association |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [negated](negated.md) | domain | association |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [publications](publications.md) | domain | association |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [MolecularActivityToMolecularActivityAssociation](MolecularActivityToMolecularActivityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [subject](subject.md) | domain | association |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [predicate](predicate.md) | domain | association |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [object](object.md) | domain | association |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [negated](negated.md) | domain | association |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [publications](publications.md) | domain | association |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GeneToGoTermAssociation](GeneToGoTermAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [FDA_approval_status](FDA_approval_status.md) | domain | association |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [subject](subject.md) | domain | association |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [predicate](predicate.md) | domain | association |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [object](object.md) | domain | association |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [negated](negated.md) | domain | association |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [publications](publications.md) | domain | association |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [EntityToDiseaseAssociation](EntityToDiseaseAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [FDA_approval_status](FDA_approval_status.md) | domain | association |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [subject](subject.md) | domain | association |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [predicate](predicate.md) | domain | association |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [object](object.md) | domain | association |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [negated](negated.md) | domain | association |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [publications](publications.md) | domain | association |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [EntityToPhenotypicFeatureAssociation](EntityToPhenotypicFeatureAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [SequenceAssociation](SequenceAssociation.md) | [subject](subject.md) | domain | association |
| [SequenceAssociation](SequenceAssociation.md) | [predicate](predicate.md) | domain | association |
| [SequenceAssociation](SequenceAssociation.md) | [object](object.md) | domain | association |
| [SequenceAssociation](SequenceAssociation.md) | [negated](negated.md) | domain | association |
| [SequenceAssociation](SequenceAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [SequenceAssociation](SequenceAssociation.md) | [publications](publications.md) | domain | association |
| [SequenceAssociation](SequenceAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [SequenceAssociation](SequenceAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [SequenceAssociation](SequenceAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [SequenceAssociation](SequenceAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [SequenceAssociation](SequenceAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [subject](subject.md) | domain | association |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [predicate](predicate.md) | domain | association |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [object](object.md) | domain | association |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [negated](negated.md) | domain | association |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [qualifiers](qualifiers.md) | domain | association |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [publications](publications.md) | domain | association |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [has_evidence](has_evidence.md) | domain | association |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GenomicSequenceLocalization](GenomicSequenceLocalization.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [subject](subject.md) | domain | association |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [predicate](predicate.md) | domain | association |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [object](object.md) | domain | association |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [negated](negated.md) | domain | association |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [qualifiers](qualifiers.md) | domain | association |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [publications](publications.md) | domain | association |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [has_evidence](has_evidence.md) | domain | association |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [SequenceFeatureRelationship](SequenceFeatureRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [subject](subject.md) | domain | association |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [predicate](predicate.md) | domain | association |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [object](object.md) | domain | association |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [negated](negated.md) | domain | association |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [qualifiers](qualifiers.md) | domain | association |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [publications](publications.md) | domain | association |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [has_evidence](has_evidence.md) | domain | association |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [TranscriptToGeneRelationship](TranscriptToGeneRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [subject](subject.md) | domain | association |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [predicate](predicate.md) | domain | association |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [object](object.md) | domain | association |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [negated](negated.md) | domain | association |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [qualifiers](qualifiers.md) | domain | association |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [publications](publications.md) | domain | association |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [has_evidence](has_evidence.md) | domain | association |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GeneToGeneProductRelationship](GeneToGeneProductRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [subject](subject.md) | domain | association |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [predicate](predicate.md) | domain | association |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [object](object.md) | domain | association |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [negated](negated.md) | domain | association |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [qualifiers](qualifiers.md) | domain | association |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [publications](publications.md) | domain | association |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [has_evidence](has_evidence.md) | domain | association |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [ExonToTranscriptRelationship](ExonToTranscriptRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [subject](subject.md) | domain | association |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [predicate](predicate.md) | domain | association |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [object](object.md) | domain | association |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [negated](negated.md) | domain | association |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [qualifiers](qualifiers.md) | domain | association |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [publications](publications.md) | domain | association |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [has_evidence](has_evidence.md) | domain | association |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [GeneRegulatoryRelationship](GeneRegulatoryRelationship.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [subject](subject.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [predicate](predicate.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [object](object.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [negated](negated.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [publications](publications.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [subject](subject.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [predicate](predicate.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [object](object.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [negated](negated.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [publications](publications.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [subject](subject.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [predicate](predicate.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [object](object.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [negated](negated.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [publications](publications.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [subject](subject.md) | domain | association |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [predicate](predicate.md) | domain | association |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [object](object.md) | domain | association |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [negated](negated.md) | domain | association |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [publications](publications.md) | domain | association |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [OrganismTaxonToOrganismTaxonAssociation](OrganismTaxonToOrganismTaxonAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [subject](subject.md) | domain | association |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [predicate](predicate.md) | domain | association |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [object](object.md) | domain | association |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [negated](negated.md) | domain | association |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [qualifiers](qualifiers.md) | domain | association |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [publications](publications.md) | domain | association |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [has_evidence](has_evidence.md) | domain | association |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [OrganismTaxonToOrganismTaxonSpecialization](OrganismTaxonToOrganismTaxonSpecialization.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [associated_environmental_context](associated_environmental_context.md) | domain | association |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [subject](subject.md) | domain | association |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [predicate](predicate.md) | domain | association |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [object](object.md) | domain | association |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [negated](negated.md) | domain | association |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [qualifiers](qualifiers.md) | domain | association |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [publications](publications.md) | domain | association |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [has_evidence](has_evidence.md) | domain | association |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [OrganismTaxonToOrganismTaxonInteraction](OrganismTaxonToOrganismTaxonInteraction.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [subject](subject.md) | domain | association |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [predicate](predicate.md) | domain | association |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [object](object.md) | domain | association |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [negated](negated.md) | domain | association |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [qualifiers](qualifiers.md) | domain | association |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [publications](publications.md) | domain | association |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [has_evidence](has_evidence.md) | domain | association |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [knowledge_source](knowledge_source.md) | domain | association |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [original_knowledge_source](original_knowledge_source.md) | domain | association |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [primary_knowledge_source](primary_knowledge_source.md) | domain | association |
| [OrganismTaxonToEnvironmentAssociation](OrganismTaxonToEnvironmentAssociation.md) | [aggregator_knowledge_source](aggregator_knowledge_source.md) | domain | association |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: association
exact_mappings:
- OBAN:association
- rdf:Statement
- owl:Axiom
description: A typed association between two entities, supported by evidence
comments:
- This is roughly the model used by biolink and ontobio at the moment
from_schema: https://w3id.org/biolink/biolink-model
is_a: entity
slots:
- subject
- predicate
- object
- relation
- negated
- qualifiers
- publications
- has evidence
- knowledge source
- original knowledge source
- primary knowledge source
- aggregator knowledge source
slot_usage:
  type:
    name: type
    description: rdf:type of biolink:Association should be fixed at rdf:Statement
  category:
    name: category
    range: category type
    required: false

```
</details>

### Induced

<details>
```yaml
name: association
exact_mappings:
- OBAN:association
- rdf:Statement
- owl:Axiom
description: A typed association between two entities, supported by evidence
comments:
- This is roughly the model used by biolink and ontobio at the moment
from_schema: https://w3id.org/biolink/biolink-model
is_a: entity
slot_usage:
  type:
    name: type
    description: rdf:type of biolink:Association should be fixed at rdf:Statement
  category:
    name: category
    range: category type
    required: false
attributes:
  subject:
    name: subject
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: annotation subject
      neo4j:
        local_name_source: neo4j
        local_name_value: node with outgoing relationship
    exact_mappings:
    - owl:annotatedSource
    - OBAN:association_has_subject
    description: connects an association to the subject of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    slot_uri: rdf:subject
    alias: subject
    owner: association
    range: named thing
    required: true
  predicate:
    name: predicate
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: annotation predicate
      translator:
        local_name_source: translator
        local_name_value: predicate
    exact_mappings:
    - owl:annotatedProperty
    - OBAN:association_has_predicate
    description: A high-level grouping for the relationship type. AKA minimal predicate.
      This is analogous to category for nodes.
    notes:
    - Has a value from the Biolink related_to hierarchy. In RDF,  this corresponds
      to rdf:predicate and in Neo4j this corresponds to the relationship type. The
      convention is for an edge label in snake_case form. For example, biolink:related_to,
      biolink:causes, biolink:treats
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    slot_uri: rdf:predicate
    alias: predicate
    owner: association
    range: predicate type
    required: true
  object:
    name: object
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: descriptor
      neo4j:
        local_name_source: neo4j
        local_name_value: node with incoming relationship
    exact_mappings:
    - owl:annotatedTarget
    - OBAN:association_has_object
    description: connects an association to the object of the association. For example,
      in a gene-to-phenotype association, the gene is subject and phenotype is object.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    slot_uri: rdf:object
    alias: object
    owner: association
    range: named thing
    required: true
  relation:
    name: relation
    deprecated: 'True'
    from_schema: https://w3id.org/biolink/biolink-model
    alias: relation
    owner: association
    range: string
  negated:
    name: negated
    description: if set to true, then the association is negated i.e. is not true
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    alias: negated
    owner: association
    range: boolean
  qualifiers:
    name: qualifiers
    local_names:
      ga4gh:
        local_name_source: ga4gh
        local_name_value: annotation qualifier
    description: connects an association to qualifiers that modify or qualify the
      meaning of that association
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    singular_name: qualifier
    domain: association
    multivalued: true
    alias: qualifiers
    owner: association
    range: ontology class
  publications:
    name: publications
    description: connects an association to publications supporting the association
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    singular_name: publication
    domain: association
    multivalued: true
    alias: publications
    owner: association
    range: publication
  has evidence:
    name: has evidence
    exact_mappings:
    - RO:0002558
    description: connects an association to an instance of supporting evidence
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    multivalued: true
    alias: has_evidence
    owner: association
    range: evidence type
  knowledge source:
    name: knowledge source
    close_mappings:
    - pav:providedBy
    description: An Information Resource from which the knowledge expressed in an
      Association was retrieved, directly or indirectly. This can be any resource
      through which the knowledge passed on its way to its currently serialized form.
      In practice, implementers should use one of the more specific subtypes of this
      generic property.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: association slot
    domain: association
    multivalued: true
    alias: knowledge_source
    owner: association
    range: information resource
  original knowledge source:
    name: original knowledge source
    description: The Information Resource that created the original record of the
      knowledge expressed in an Association (e.g. via curation of the knowledge from
      the literature, or generation of the knowledge de novo through computation,
      reasoning, inference over data).
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: primary knowledge source
    domain: association
    multivalued: true
    alias: original_knowledge_source
    owner: association
    range: information resource
  primary knowledge source:
    name: primary knowledge source
    description: The most upstream source of the knowledge expressed in an Association
      that an implementer can identify (may or may not be the 'original' source).
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: knowledge source
    domain: association
    multivalued: true
    alias: primary_knowledge_source
    owner: association
    range: information resource
  aggregator knowledge source:
    name: aggregator knowledge source
    description: An intermediate aggregator resource from which knowledge expressed
      in an Association was retrieved downstream of the original source, on its path
      to its current serialized form.
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: knowledge source
    domain: association
    multivalued: true
    alias: aggregator_knowledge_source
    owner: association
    range: information resource
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
    owner: association
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
    owner: association
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
    owner: association
    is_class_field: true
    range: category type
    required: false
  type:
    name: type
    description: rdf:type of biolink:Association should be fixed at rdf:Statement
    from_schema: https://w3id.org/biolink/biolink-model
    slot_uri: rdf:type
    alias: type
    owner: association
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
    owner: association
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
    owner: association
    range: narrative text
  source:
    name: source
    deprecated: 'True'
    from_schema: https://w3id.org/biolink/biolink-model
    alias: source
    owner: association
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
    owner: association
    range: attribute

```
</details>