---
title: "Working with the Biolink Model"
parent: "Biolink Model Guidelines"
layout: default
nav_order: 4
---

# Working with Biolink Model

The [model](understanding-the-model.md) and how to [curate the model](curating-the-model.md) has been addressed in other sections. But how to make use of the Biolink Model in practical terms?
How to use the classes and slots defined in the model for representing nodes and edges in a graph?

We can consider a small example and see how it can be represented using the Biolink Model.

Example:
```
protein1 protein2
9606.ENSP00000000233 9606.ENSP00000272298
9606.ENSP00000000233 9606.ENSP00000253401
9606.ENSP00000000233 9606.ENSP00000401445
```

The above lines are from [STRING DB](https://string-db.org/).

The information can be represented using Biolink Model as follows:
- use Biolink entity class `protein` for protein entities
- use Biolink entity class `gene` for gene entities
- use Biolink predicate slot `interacts with` as the relationship or predicate for representing an edge between interacting partners
- use Biolink association class `gene to gene association` to type the edge

One modeling consideration we are going to make here is that we will be projecting the interaction between proteins to interaction between genes.


## Annotating nodes

Each individual protein and gene can be treated as nodes in a graph.

Each protein node has `protein` as its category.

Each gene node has `gene` as its category.

As per the model, protein nodes should have identifiers from `UniProtKB` and gene nodes should have identifiers `NCBIGene`. 



One can further type the protein and gene entities using the Biolink slot `type` (which corresponds to `rdf:type`).

In [KGX serialization format](https://github.com/biolink/kgx/blob/master/data-preparation.md) the nodes can be represented as follows:
```tsv
id	name	category	provided_by	xref	type	in_taxon
UniProtKB:P84085	ARF5	biolink:Protein	STRING	ENSEMBL:ENSP00000000233		NCBITaxon:9606
UniProtKB:P0DP24	CALM2	biolink:Protein	STRING	ENSEMBL:ENSP00000272298		NCBITaxon:9606
UniProtKB:O43307	ARHGEF9	biolink:Protein	STRING	ENSEMBL:ENSP00000253401		NCBITaxon:9606
UniProtKB:O75460	ERN1	biolink:Protein	STRING	ENSEMBL:ENSP00000401445		NCBITaxon:9606
NCBIGene:381	ARF5	biolink:Gene	STRING	ENSEMBL:ENSG00000004059	SO:0001217	NCBITaxon:9606
NCBIGene:805	CALM2	biolink:Gene	STRING	ENSEMBL:ENSG00000143933	SO:0001217	NCBITaxon:9606
NCBIGene:23229	ARHGEF9	biolink:Gene	STRING	ENSEMBL:ENSG00000131089	SO:0001217	NCBITaxon:9606
NCBIGene:2081	ERN1	biolink:Gene	STRING	ENSEMBL:ENSG00000178607	SO:0001217	NCBITaxon:9606
```

> **Note:** While the entity classes are defined as `gene` and `protein` in the model, when using them the reference to the class should always be in their CURIE form which includes the `biolink` prefix.


### Node semantics

There are three ways of attaching semantics to a node:
- using Biolink slot `category`
  - the value of the `category` must be from the [`named thing` hierarchy](https://biolink.github.io/biolink-model/docs/NamedThing)
- using Biolink slot `type`
  - can have a value from any external ontology, controlled vocabulary, thesauri, or taxonomy
- using Biolink predicate slot `subclass_of` (or `rdfs:subClassOf`)
  - can have a value from any external ontology, controlled vocabulary, thesauri, or taxonomy


## Annotating edges

Each individual interaction between genes can be treated as an edge with,
- `interacts with` as its `predicate`
- `gene to gene association` as its `category`

And we have additional edges that go from gene to protein to signify that a gene encodes for a protein via the Biolink 
predicate slot `has gene product`.

In [KGX serialization format](https://github.com/biolink/kgx/blob/master/data-preparation.md) the edges can be represented as follows:
```tsv
id  subject predicate   object    provided_by category
985eb9e6-e0bf-4cef-be0a-3d8ea12d228b	NCBIGene:381	biolink:interacts_with	NCBIGene:805	STRING	biolink:GeneToGeneAssociation
5550b653-69ff-48cc-a1ef-638ecdc50ea3	NCBIGene:381	biolink:interacts_with	NCBIGene:23229	STRING	biolink:GeneToGeneAssociation
8bff8da0-6da2-4154-b507-a8e9f75c55f8	NCBIGene:381	biolink:interacts_with	NCBIGene:2081	STRING	biolink:GeneToGeneAssociation
36e2edf0-d490-4417-9407-7070f4320083	NCBIGene:381	biolink:has_gene_product	UniProtKB:P84085	STRING	
0dd21d53-4985-467c-8e6d-0a79c0410016	NCBIGene:805	biolink:has_gene_product	UniProtKB:P0DP24	STRING	
fe5f9383-c5f6-4eba-9dc4-185e6d331459	NCBIGene:23229	biolink:has_gene_product	UniProtKB:O43307	STRING	
8c60c2b2-ff6c-45d5-a18f-e927ab1dec35	NCBIGene:2081	biolink:has_gene_product	UniProtKB:O75460	STRING	
```

> **Note:** While association class is defined as `gene to gene association` and predicate slots are defined 
as `interacts with` and `has gene product` in the model, when using them the reference to the class should always 
be in their CURIE form which includes the `biolink` prefix.


### Edge semantics

There are 3 ways of attaching the semantics to an edge:
- using the Biolink association slot `predicate`
  - must have a value from the [`related to` hierarchy](https://biolink.github.io/biolink-model/docs/related_to)
- using the Biolink slot `category`
  - must have a value from the [`association` hierarchy](https://biolink.github.io/biolink-model/docs/Association)
- using Biolink slot `type`
  - can have a value from any external ontology, controlled vocabulary, thesauri, or taxonomy


## Biolink Model representation in Neo4j

The model itself is very close to labelled property graphs.

The previous example can be easily converted to a Neo4j compatible TSV using [KGX](https://github.com/biolink/kgx).

`nodes.tsv`:

```tsv
id:ID	name	category:LABEL	xref	provided_by:string[]	in_taxon	type
UniProtKB:P84085	ARF5	biolink:Protein	ENSEMBL:ENSP00000000233	STRING	NCBITaxon:9606	
UniProtKB:P0DP24	CALM2	biolink:Protein	ENSEMBL:ENSP00000272298	STRING	NCBITaxon:9606	
UniProtKB:O43307	ARHGEF9	biolink:Protein	ENSEMBL:ENSP00000253401	STRING	NCBITaxon:9606	
UniProtKB:O75460	ERN1	biolink:Protein	ENSEMBL:ENSP00000401445	STRING	NCBITaxon:9606	
NCBIGene:381	ARF5	biolink:Gene	ENSEMBL:ENSG00000004059	STRING	NCBITaxon:9606	SO:0001217
NCBIGene:805	CALM2	biolink:Gene	ENSEMBL:ENSG00000143933	STRING	NCBITaxon:9606	SO:0001217
NCBIGene:23229	ARHGEF9	biolink:Gene	ENSEMBL:ENSG00000131089	STRING	NCBITaxon:9606	SO:0001217
NCBIGene:2081	ERN1	biolink:Gene	ENSEMBL:ENSG00000178607	STRING	NCBITaxon:9606	SO:0001217
```


`edges.tsv`:
```tsv
id	subject:START_ID	predicate:TYPE	object:END_ID	provided_by:string[]	category:string[]
985eb9e6-e0bf-4cef-be0a-3d8ea12d228b	NCBIGene:381	biolink:interacts_with	NCBIGene:805	STRING	biolink:GeneToGeneAssociation
5550b653-69ff-48cc-a1ef-638ecdc50ea3	NCBIGene:381	biolink:interacts_with	NCBIGene:23229	STRING	biolink:GeneToGeneAssociation
8bff8da0-6da2-4154-b507-a8e9f75c55f8	NCBIGene:381	biolink:interacts_with	NCBIGene:2081	STRING	biolink:GeneToGeneAssociation
36e2edf0-d490-4417-9407-7070f4320083	NCBIGene:381	biolink:has_gene_product	UniProtKB:P84085	STRING	
0dd21d53-4985-467c-8e6d-0a79c0410016	NCBIGene:805	biolink:has_gene_product	UniProtKB:P0DP24	STRING	
fe5f9383-c5f6-4eba-9dc4-185e6d331459	NCBIGene:23229	biolink:has_gene_product	UniProtKB:O43307	STRING	
8c60c2b2-ff6c-45d5-a18f-e927ab1dec35	NCBIGene:2081	biolink:has_gene_product	UniProtKB:O75460	STRING	
```


## Biolink Model representation in RDF

Since RDF graphs do not allow for properties on edges, the most practical alternative is to use reification where an 
edge is transformed into a node of type `biolink:Association` (or its descendants) and any edge properties then becomes
properties of this reified node.

Using reification, the previous example can be easily converted to RDF using [KGX](https://github.com/biolink/kgx),


```turtle
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix biolink: <https://w3id.org/biolink/vocab/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

<http://identifiers.org/uniprot/P84085>
  rdfs:label "ARF5"^^xsd:string ;
  biolink:category biolink:Protein ;
  biolink:provided_by "STRING" ;
  biolink:xref <http://identifiers.org/ensembl/ENSP00000000233> ;
  biolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> .

<http://identifiers.org/uniprot/P0DP24>
  rdfs:label "CALM2"^^xsd:string ;
  biolink:category biolink:Protein ;
  biolink:provided_by "STRING" ;
  biolink:xref <http://identifiers.org/ensembl/ENSP00000272298> ;
  biolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> .

<http://identifiers.org/uniprot/O43307>
  rdfs:label "ARHGEF9"^^xsd:string ;
  biolink:category biolink:Protein ;
  biolink:provided_by "STRING" ;
  biolink:xref <http://identifiers.org/ensembl/ENSP00000253401> ;
  biolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> .

<http://identifiers.org/uniprot/O75460>
  rdfs:label "ERN1"^^xsd:string ;
  biolink:category biolink:Protein ;
  biolink:provided_by "STRING" ;
  biolink:xref <http://identifiers.org/ensembl/ENSP00000401445> ;
  biolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> .

<http://www.ncbi.nlm.nih.gov/gene/381>
  rdfs:label "ARF5"^^xsd:string ;
  biolink:category biolink:Gene ;
  biolink:provided_by "STRING" ;
  biolink:xref <http://identifiers.org/ensembl/ENSG00000004059> ;
  a <http://purl.obolibrary.org/obo/SO_0001217> ;
  biolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> ;
  biolink:has_gene_product <http://identifiers.org/uniprot/P84085> .

<http://www.ncbi.nlm.nih.gov/gene/805>
  rdfs:label "CALM2"^^xsd:string ;
  biolink:category biolink:Gene ;
  biolink:provided_by "STRING" ;
  biolink:xref <http://identifiers.org/ensembl/ENSG00000143933> ;
  a <http://purl.obolibrary.org/obo/SO_0001217> ;
  biolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> ;
  biolink:has_gene_product <http://identifiers.org/uniprot/P0DP24> .

<http://www.ncbi.nlm.nih.gov/gene/23229>
  rdfs:label "ARHGEF9"^^xsd:string ;
  biolink:category biolink:Gene ;
  biolink:provided_by "STRING" ;
  biolink:xref <http://identifiers.org/ensembl/ENSG00000131089> ;
  a <http://purl.obolibrary.org/obo/SO_0001217> ;
  biolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> ;
  biolink:has_gene_product <http://identifiers.org/uniprot/O43307> .

<http://www.ncbi.nlm.nih.gov/gene/2081>
  rdfs:label "ERN1"^^xsd:string ;
  biolink:category biolink:Gene ;
  biolink:provided_by "STRING" ;
  biolink:xref <http://identifiers.org/ensembl/ENSG00000178607> ;
  a <http://purl.obolibrary.org/obo/SO_0001217> ;
  biolink:in_taxon <http://purl.obolibrary.org/obo/NCBITaxon_9606> ;
  biolink:has_gene_product <http://identifiers.org/uniprot/O75460> .

<https://www.example.org/UNKNOWN/985eb9e6-e0bf-4cef-be0a-3d8ea12d228b>
  rdf:subject <http://www.ncbi.nlm.nih.gov/gene/381> ;
  rdf:predicate biolink:interacts_with ;
  rdf:object <http://www.ncbi.nlm.nih.gov/gene/805> ;
  biolink:provided_by "STRING" ;
  biolink:category biolink:GeneToGeneAssociation .

<https://www.example.org/UNKNOWN/5550b653-69ff-48cc-a1ef-638ecdc50ea3>
  rdf:subject <http://www.ncbi.nlm.nih.gov/gene/381> ;
  rdf:predicate biolink:interacts_with ;
  rdf:object <http://www.ncbi.nlm.nih.gov/gene/23229> ;
  biolink:provided_by "STRING" ;
  biolink:category biolink:GeneToGeneAssociation .

<https://www.example.org/UNKNOWN/8bff8da0-6da2-4154-b507-a8e9f75c55f8>
  rdf:subject <http://www.ncbi.nlm.nih.gov/gene/381> ;
  rdf:predicate biolink:interacts_with ;
  rdf:object <http://www.ncbi.nlm.nih.gov/gene/2081> ;
  biolink:provided_by "STRING" ;
  biolink:category biolink:GeneToGeneAssociation .
```

