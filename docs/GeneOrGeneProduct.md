
# Type: gene or gene product


a union of genes or gene products. Frequently an identifier for one will be used as proxy for another

URI: [biolink:GeneOrGeneProduct](https://w3id.org/biolink/vocab/GeneOrGeneProduct)


![img](images/GeneOrGeneProduct.svg)

## Parents

 *  is_a: [MacromolecularMachine](MacromolecularMachine.md) - A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.

## Children

 * [Gene](Gene.md)
 * [GeneProduct](GeneProduct.md) - The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules

## Referenced by class

 *  **[ChemicalToGeneAssociation](ChemicalToGeneAssociation.md)** *[chemical to gene association➞object](chemical_to_gene_association_object.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[AnatomicalEntity](AnatomicalEntity.md)** *[expresses](expresses.md)*  <sub>0..*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneAsAModelOfDiseaseAssociation](GeneAsAModelOfDiseaseAssociation.md)** *[gene as a model of disease association➞subject](gene_as_a_model_of_disease_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneHasVariantThatContributesToDiseaseAssociation](GeneHasVariantThatContributesToDiseaseAssociation.md)** *[gene has variant that contributes to disease association➞subject](gene_has_variant_that_contributes_to_disease_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneRegulatoryRelationship](GeneRegulatoryRelationship.md)** *[gene regulatory relationship➞object](gene_regulatory_relationship_object.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneRegulatoryRelationship](GeneRegulatoryRelationship.md)** *[gene regulatory relationship➞subject](gene_regulatory_relationship_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)** *[gene to disease association➞subject](gene_to_disease_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[gene to expression site association➞subject](gene_to_expression_site_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToGeneAssociation](GeneToGeneAssociation.md)** *[gene to gene association➞object](gene_to_gene_association_object.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToGeneAssociation](GeneToGeneAssociation.md)** *[gene to gene association➞subject](gene_to_gene_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md)** *[gene to phenotypic feature association➞subject](gene_to_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneToThingAssociation](GeneToThingAssociation.md)** *[gene to thing association➞subject](gene_to_thing_association_subject.md)*  <sub>REQ</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[in cell population with](in_cell_population_with.md)*  <sub>0..*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[in complex with](in_complex_with.md)*  <sub>0..*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[in pathway with](in_pathway_with.md)*  <sub>0..*</sub>  **[GeneOrGeneProduct](GeneOrGeneProduct.md)**

## Attributes


### Inherited from macromolecular machine:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)
 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [macromolecular machine➞name](macromolecular_machine_name.md)  <sub>REQ</sub>
    * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
    * range: [SymbolType](types/SymbolType.md)
