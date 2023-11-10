
# Slot: object


connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.

URI: [biolink:gene_to_disease_or_phenotypic_feature_association_object](https://w3id.org/biolink/vocab/gene_to_disease_or_phenotypic_feature_association_object)


## Domain and Range

[GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md) &#8594;  <sub>1..1</sub> [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)

## Parents

 *  is_a: [object](object.md)

## Children

 *  [gene to disease association➞object](gene_to_disease_association_object.md)
 *  [gene to phenotypic feature association➞object](gene_to_phenotypic_feature_association_object.md)

## Used by

 * [GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Local names:** | | descriptor (ga4gh) |
|  | | node with incoming relationship (neo4j) |
| **Mappings:** | | rdf:object |
| **Exact Mappings:** | | owl:annotatedTarget |
|  | | OBAN:association_has_object |

