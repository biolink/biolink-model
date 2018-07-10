# Class: gene




URI: [http://bioentity.io/vocab/Gene](http://bioentity.io/vocab/Gene)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Gene|id(i):identifier_type%20%3F;category(i):label_type%20%3F;uri(i):uri%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F;has_biological_sequence(i):biological_sequence%20%3F;name(i):symbol_type%20%3F]-%20expressed%20in(i)%20%3F>\[AnatomicalEntity],%20\[Gene]-%20in%20cell%20population%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[Gene]-%20in%20complex%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[Gene]-%20in%20pathway%20with(i)%20%3F>\[GeneOrGeneProduct],%20\[Gene]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[Gene]-%20regulates,%20entity%20to%20entity(i)%20%3F>\[MolecularEntity],%20\[Gene]-%20molecularly%20interacts%20with(i)%20%3F>\[MolecularEntity],%20\[Gene]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[Gene]-%20related%20to(i)%20%3F>\[NamedThing],%20\[Gene]-%20gene%20associated%20with%20condition%20%3F>\[DiseaseOrPhenotypicFeature],%20\[Gene]-%20has%20gene%20product%20%3F>\[GeneProduct],%20\[Gene]-%20genetically%20interacts%20with%20%3F>\[Gene],%20\[GeneToGeneProductRelationship]-%20subject(i)>\[Gene],%20\[Gene]-%20genetically%20interacts%20with%20%3F>\[Gene],%20\[GenotypeToGeneAssociation]-%20object(i)>\[Gene],%20\[SequenceVariant]-%20has%20gene(i)%20%3F>\[Gene],%20\[SequenceVariant]-%20has%20gene(i)%20*>\[Gene],%20\[TranscriptToGeneRelationship]-%20object(i)>\[Gene],%20\[GeneOrGeneProduct]^-\[Gene])
## Mappings

 * [SO:0000704](http://purl.obolibrary.org/obo/SO_0000704)
 * [SIO:010035](http://semanticscience.org/resource/SIO_010035)
 * [WD:Q7187](http://purl.obolibrary.org/obo/WD_Q7187)
 * [UMLSSG:GENE](http://purl.obolibrary.org/obo/UMLSSG_GENE)
## Inheritance

 *  is_a: [GeneOrGeneProduct](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
## Children

## Used in

 *  class: **[GeneToGeneProductRelationship](GeneToGeneProductRelationship.md)** *[gene to gene product relationship.subject](gene_to_gene_product_relationship_subject.md)* **[Gene](Gene.md)**
 *  class: **[Gene](Gene.md)** *[genetically interacts with](genetically_interacts_with.md)* **[Gene](Gene.md)**
 *  class: **[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)** *[genotype to gene association.object](genotype_to_gene_association_object.md)* **[Gene](Gene.md)**
 *  class: **[SequenceVariant](SequenceVariant.md)** *[has gene](has_gene.md)* **[Gene](Gene.md)**
 *  class: **[SequenceVariant](SequenceVariant.md)** *[sequence variant.has gene](sequence_variant_has_gene.md)* **[Gene](Gene.md)**
 *  class: **[TranscriptToGeneRelationship](TranscriptToGeneRelationship.md)** *[transcript to gene relationship.object](transcript_to_gene_relationship_object.md)* **[Gene](Gene.md)**
## Fields

 * [gene associated with condition](gene_associated_with_condition.md) *subsets*: (translator_minimal)
    * Description: holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
    * range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
    * __Local__
 * [genetically interacts with](genetically_interacts_with.md) *subsets*: (translator_minimal)
    * Description: holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
    * range: [Gene](Gene.md)
    * __Local__
 * [has gene product](has_gene_product.md) *subsets*: (translator_minimal)
    * Description: holds between a gene and a transcribed and/or translated product generated from it
    * range: [GeneProduct](GeneProduct.md)
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
 * [expressed in](expressed_in.md) *subsets*: (translator_minimal)
    * Description: holds between a gene or gene product and an anatomical entity in which it is expressed
    * range: [AnatomicalEntity](AnatomicalEntity.md)
    * inherited from: [GeneOrGeneProduct](GeneOrGeneProduct.md)
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
 * [in cell population with](in_cell_population_with.md) *subsets*: (translator_minimal)
    * Description: holds between two genes or gene products that are expressed in the same cell type or population 
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * inherited from: [GeneOrGeneProduct](GeneOrGeneProduct.md)
 * [in complex with](in_complex_with.md) *subsets*: (translator_minimal)
    * Description: holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * inherited from: [GeneOrGeneProduct](GeneOrGeneProduct.md)
 * [in pathway with](in_pathway_with.md) *subsets*: (translator_minimal)
    * Description: holds between two genes or gene products that are part of in the same biological pathway
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * inherited from: [GeneOrGeneProduct](GeneOrGeneProduct.md)
 * [in taxon](in_taxon.md) *subsets*: (translator_minimal)
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
 * [iri](iri.md) *subsets*: (translator_minimal)
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
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
 * [uri](uri.md)
    * Description: URI expansion of CURIE
    * range: [uri](uri.md)
    * inherited from: [NamedThing](NamedThing.md)
