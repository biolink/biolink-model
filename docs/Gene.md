
# Class: gene




URI: [biolink:Gene](https://w3id.org/biolink/vocab/Gene)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[Gene|name(i):symbol_type;has_biological_sequence(i):biological_sequence%20%3F;id(i):identifier_type;category(i):iri_type%20%2B],%20\[GeneToGeneProductRelationship]-%20subject%201..1>\[Gene],%20\[GenotypeToGeneAssociation]-%20object%201..1>\[Gene],%20\[SequenceVariant]-%20has%20gene%200..*>\[Gene],%20\[TranscriptToGeneRelationship]-%20object%201..1>\[Gene],%20\[GeneOrGeneProduct]^-\[Gene])

## Parents

 *  is_a: [GeneOrGeneProduct](GeneOrGeneProduct.md) - a union of genes or gene products. Frequently an identifier for one will be used as proxy for another

## Referenced by class

 *  **[GeneToGeneProductRelationship](GeneToGeneProductRelationship.md)** *[subject](gene_to_gene_product_relationship_subject.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**
 *  **[Gene](Gene.md)** *[genetically interacts with](genetically_interacts_with.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)** *[object](genotype_to_gene_association_object.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[has gene](has_gene.md)*  <sub>OPT</sub>  **[Gene](Gene.md)**
 *  **[SequenceVariant](SequenceVariant.md)** *[has gene](sequence_variant_has_gene.md)*  <sub>0..*</sub>  **[Gene](Gene.md)**
 *  **[TranscriptToGeneRelationship](TranscriptToGeneRelationship.md)** *[object](transcript_to_gene_relationship_object.md)*  <sub>REQ</sub>  **[Gene](Gene.md)**

## Attributes


### Inherited from genomic entity:

 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](BiologicalSequence.md)
    * inherited from: [GenomicEntity](GenomicEntity.md)

### Inherited from macromolecular machine:

 * [name](macromolecular_machine_name.md)  <sub>REQ</sub>
    * range: [SymbolType](SymbolType.md)
    * inherited from: [MacromolecularMachine](MacromolecularMachine.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..*</sub>
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [gene associated with condition](gene_associated_with_condition.md)  <sub>0..*</sub>
    * Description: holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
    * range: [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)
    * in subsets: (translator_minimal)
 * [genetically interacts with](genetically_interacts_with.md)  <sub>0..*</sub>
    * Description: holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
    * range: [Gene](Gene.md)
    * in subsets: (translator_minimal)
 * [has gene product](has_gene_product.md)  <sub>0..*</sub>
    * Description: holds between a gene and a transcribed and/or translated product generated from it
    * range: [GeneProduct](GeneProduct.md)
    * in subsets: (translator_minimal)
