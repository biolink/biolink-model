# Biolink ShEx models
## Description
This directory carries the Shape Expressions (ShEx) definitions for the biolink metamodel and model. The models are
published in three formats:
* *.shex -- [ShEx Compact Syntax](http://shex.io/shex-semantics/#shexc) (ShExC) 
* *.json -- [ShEx JSON-LD syntax](http://shex.io/shex-semantics/#shexj) (ShExJ) 
* *.ttl  -- ShEx RDF interpretation of ShExJ expressed in [RDF turtle](https://www.w3.org/TR/turtle/)

There are also two variants of each publication
* biolink-model.*/meta.* -- definition of the model using [RDF Collections](https://www.w3.org/TR/rdf-schema/#ch_collectionvocab). 
This definition will work with any ShEx processor, but can be quite slow, as the collections are recursively defined
error detection requires evaluating collection permutations in some ShEx processors
* biolink-modelnc.*/meta.* -- definition of the model using the [list flattening](https://github.com/hsolbrig/CFGraph)
approach, a non-standard ShEx extension only available in [PyShEx](https://github.com/hsolbrig/PyShEx) at the moment.

## Use
### Command line

### 