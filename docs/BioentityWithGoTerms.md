---
layout: default
---

## bioentity with go terms


this serves as exemplar for the time being, corresponding to the bioentity document type in amigo, which has a single entry per bioentity, with associated GO information

URI: [http://bioentity.io/vocab/BioentityWithGoTerms](http://bioentity.io/vocab/BioentityWithGoTerms)
## Mappings


## Inheritance

 *  is_a: [molecular entity](MolecularEntity.html)
 *  mixin: [has genomic name](HasGenomicName.html)

## Children



## Fields

 * [isa partof closure](isa_partof_closure.html)
    * _Ancestors (reflexive) of the object field following is_a (subClassOf) and part-of links. This is typically used as a query constraint and for faceting. The combination of is_a and part of is a common pattern, and can be used in gene expression queries (finding genes that are expressed in a structure, a subtype, or a part of that structure) or in GO queries (in any of the three branches of GO)_
    * __range__: [ontology class](OntologyClass.html)*
    * __Local__
 * [regulates closure](regulates_closure.html)
    * _Ancestors (reflexive) of the object field following is_a (subClassOf), part-of and regulates (including positive and negative) relationships. This is typically used as a query constraint and for faceting where the range is a biological process_
    * __range__: [relationship type](RelationshipType.html)*
    * __Local__
 * [id](id.html)
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [in taxon](in_taxon.html)
    * _connects a thing to a class representing a taxon_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [thing with taxon](ThingWithTaxon.html)
 * [full name](full_name.html)
    * _a long-form human readable name for a thing_
    * __range__: label type
    * inherited from: [has genomic name](HasGenomicName.html)
 * [systematic synonym](systematic_synonym.html)
    * _more commonly used for gene symbols in yeast_
    * __range__: label type
    * inherited from: [has genomic name](HasGenomicName.html)
