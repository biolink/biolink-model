# Class: gene or gene product


a union of genes or gene products. Frequently an identifier for one will be used as proxy for another

URI: [http://bioentity.io/vocab/GeneOrGeneProduct](http://bioentity.io/vocab/GeneOrGeneProduct)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneOrGeneProduct|id(i):identifier_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F;isa_partof_closure_label(i):string%20*;regulates_closure_label(i):string%20*;has_biological_sequence(i):biological_sequence%20%3F;name(i):symbol_type%20%3F]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[GeneOrGeneProduct]-%20regulates,%20entity%20to%20entity(i)%20%3F>\[MolecularEntity],%20\[GeneOrGeneProduct]-%20molecularly%20interacts%20with(i)%20%3F>\[MolecularEntity],%20\[GeneOrGeneProduct]-%20regulates%20closure(i)%20*>\[RelationshipType],%20\[GeneOrGeneProduct]-%20isa%20partof%20closure(i)%20*>\[OntologyClass],%20\[GeneOrGeneProduct]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[GeneOrGeneProduct]-%20related%20to(i)%20%3F>\[NamedThing],%20\[GeneOrGeneProduct]-%20expressed%20in%20%3F>\[AnatomicalEntity],%20\[GeneOrGeneProduct]-%20in%20cell%20population%20with%20%3F>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]-%20in%20complex%20with%20%3F>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]-%20in%20pathway%20with%20%3F>\[GeneOrGeneProduct],%20\[ChemicalToGeneAssociation]-%20object(i)>\[GeneOrGeneProduct],%20\[MolecularActivity]-%20enabled%20by(i)%20%3F>\[GeneOrGeneProduct],%20\[AnatomicalEntity]-%20expresses(i)%20%3F>\[GeneOrGeneProduct],%20\[GeneAsAModelOfDiseaseAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneRegulatoryRelationship]-%20object(i)>\[GeneOrGeneProduct],%20\[GeneRegulatoryRelationship]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneToDiseaseAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneToExpressionSiteAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneToGeneAssociation]-%20object(i)>\[GeneOrGeneProduct],%20\[GeneToGeneAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneToPhenotypicFeatureAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneToThingAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]-%20in%20cell%20population%20with%20%3F>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]-%20in%20complex%20with%20%3F>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]-%20in%20pathway%20with%20%3F>\[GeneOrGeneProduct],%20\[MolecularActivityToGeneProductAssociation]-%20object(i)>\[GeneOrGeneProduct],%20\[GeneOrGeneProduct]^-\[GeneProduct],%20\[GeneOrGeneProduct]^-\[Gene],%20\[MacromolecularMachine]^-\[GeneOrGeneProduct])
## Mappings

## Inheritance

 *  is_a: [MacromolecularMachine](MacromolecularMachine.md) - A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
## Children

 * [Gene](Gene.md)
 * [GeneProduct](GeneProduct.md) - The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
## Used in

 *  class: **[ChemicalToGeneAssociation](ChemicalToGeneAssociation.md)** *[chemical to gene association.object](chemical_to_gene_association_object.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[MolecularActivity](MolecularActivity.md)** *[enabled by](enabled_by.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[AnatomicalEntity](AnatomicalEntity.md)** *[expresses](expresses.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md)** *[gene as a model of disease association.subject](gene_as_a_model_of_disease_association_subject.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md)** *[gene has variant that contributes to disease association.subject](gene_has_variant_that_contributes_to_disease_association_subject.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[GeneRegulatoryRelationship](GeneRegulatoryRelationship.md)** *[gene regulatory relationship.object](gene_regulatory_relationship_object.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[GeneRegulatoryRelationship](GeneRegulatoryRelationship.md)** *[gene regulatory relationship.subject](gene_regulatory_relationship_subject.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)** *[gene to disease association.subject](gene_to_disease_association_subject.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[gene to expression site association.subject](gene_to_expression_site_association_subject.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[GeneToGeneAssociation](GeneToGeneAssociation.md)** *[gene to gene association.object](gene_to_gene_association_object.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[GeneToGeneAssociation](GeneToGeneAssociation.md)** *[gene to gene association.subject](gene_to_gene_association_subject.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md)** *[gene to phenotypic feature association.subject](gene_to_phenotypic_feature_association_subject.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[GeneToThingAssociation](GeneToThingAssociation.md)** *[gene to thing association.subject](gene_to_thing_association_subject.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[in cell population with](in_cell_population_with.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[in complex with](in_complex_with.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[in pathway with](in_pathway_with.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  class: **[MolecularActivityToGeneProductAssociation](MolecularActivityToGeneProductAssociation.md)** *[molecular activity to gene product association.object](molecular_activity_to_gene_product_association_object.md)* **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
## Fields

 * [expressed in](expressed_in.md) *subsets*: (translator_minimal)
    * Description: holds between a gene or gene product and an anatomical entity in which it is expressed
    * range: [AnatomicalEntity](AnatomicalEntity.md)
    * __Local__
 * [in cell population with](in_cell_population_with.md) *subsets*: (translator_minimal)
    * Description: holds between two genes or gene products that are expressed in the same cell type or population 
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * __Local__
 * [in complex with](in_complex_with.md) *subsets*: (translator_minimal)
    * Description: holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * __Local__
 * [in pathway with](in_pathway_with.md) *subsets*: (translator_minimal)
    * Description: holds between two genes or gene products that are part of in the same biological pathway
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * __Local__
 * [biomarker for](biomarker_for.md) *subsets*: (translator_minimal)
    * Description: holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
    * range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [has biological sequence](has_biological_sequence.md)
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](BiologicalSequence.md)
    * inherited from: [GenomicEntity](GenomicEntity.md)
 * [has phenotype](has_phenotype.md) *subsets*: (translator_minimal)
    * Description: holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). 
    * range: [Phenotype](Phenotype.md)
    * inherited from: [BiologicalEntity](BiologicalEntity.md)
 * [id](id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [in taxon](in_taxon.md) *subsets*: (translator_minimal)
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
 * [iri](iri.md) *subsets*: (translator_minimal)
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [isa partof closure](isa_partof_closure.md)
    * Description: Ancestors (reflexive) of the object field following is_a (subClassOf) and part-of links. This is typically used as a query constraint and for faceting. The combination of is_a and part of is a common pattern, and can be used in gene expression queries (finding genes that are expressed in a structure, a subtype, or a part of that structure) or in GO queries (in any of the three branches of GO)
    * range: [OntologyClass](OntologyClass.md)*
    * inherited from: [GoTermBioentityMixin](GoTermBioentityMixin.md)
 * [isa partof closure label](isa_partof_closure_label.md)
    * Description: parent field for fields used for storing the label of the closure concept. See also: closure concept field
    * range: **string***
    * inherited from: [GoTermBioentityMixin](GoTermBioentityMixin.md)
 * [macromolecular machine.name](macromolecular_machine_name.md) *subsets*: (translator_minimal)
    * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](SymbolType.md)
    * inherited from: [MacromolecularMachine](MacromolecularMachine.md)
 * [molecularly interacts with](molecularly_interacts_with.md) *subsets*: (translator_minimal)
    * Description: holds between two entities that make physical contact as part of some interaction
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
 * [node property](node_property.md)
    * Description: A grouping for any property that holds between a node and a value
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * [regulates closure](regulates_closure.md)
    * Description: Ancestors (reflexive) of the object field following is_a (subClassOf), part-of and regulates (including positive and negative) relationships. This is typically used as a query constraint and for faceting where the range is a biological process
    * range: [RelationshipType](RelationshipType.md)*
    * inherited from: [GoTermBioentityMixin](GoTermBioentityMixin.md)
 * [regulates closure label](regulates_closure_label.md)
    * Description: parent field for fields used for storing the label of the closure concept. See also: closure concept field
    * range: **string***
    * inherited from: [GoTermBioentityMixin](GoTermBioentityMixin.md)
 * [regulates, entity to entity](regulates_entity_to_entity.md) *subsets*: (translator_minimal)
    * Description: describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
    * range: [MolecularEntity](MolecularEntity.md)
    * inherited from: [MolecularEntity](MolecularEntity.md)
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
