---
parent: Class Mixins
title: biolink:ThingWithTaxon
grand_parent: Classes
layout: default
---

# Class: ThingWithTaxon


A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes

URI: [biolink:ThingWithTaxon](https://w3id.org/biolink/vocab/ThingWithTaxon)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OrganismTaxon]%3Cin%20taxon%200..%2A-%20[ThingWithTaxon],[NucleicAcidEntity]uses%20-.-%3E[ThingWithTaxon],[GenomicBackgroundExposure]uses%20-.-%3E[ThingWithTaxon],[DiseaseOrPhenotypicFeature]uses%20-.-%3E[ThingWithTaxon],[BiologicalEntity]uses%20-.-%3E[ThingWithTaxon],[OrganismTaxon],[NucleicAcidEntity],[GenomicBackgroundExposure],[DiseaseOrPhenotypicFeature],[BiologicalEntity])

---


## Mixin for

 * [BiologicalEntity](BiologicalEntity.md) (mixin) 
 * [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) (mixin)  - Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate. distinct, others such as MESH conflate.  Please see definitions of phenotypic feature and disease in this model for their independent descriptions.  This class is helpful to enforce domains and ranges   that may involve either a disease or a phenotypic feature.
 * [GenomicBackgroundExposure](GenomicBackgroundExposure.md) (mixin)  - A genomic background exposure is where an individual's specific genomic background of genes, sequence variants or other pre-existing genomic conditions constitute a kind of 'exposure' to the organism, leading to or influencing an outcome.
 * [NucleicAcidEntity](NucleicAcidEntity.md) (mixin)  - A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included.

## Referenced by class

 *  **[OrganismTaxon](OrganismTaxon.md)** *[taxon of](taxon_of.md)*  <sub>0..\*</sub>  **[ThingWithTaxon](ThingWithTaxon.md)**

## Attributes


### Own

 * [in taxon](in_taxon.md)  <sub>0..\*</sub>
     * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * Range: [OrganismTaxon](OrganismTaxon.md)
     * in subsets: (translator_minimal)

### Domain for slot:

 * [in taxon](in_taxon.md)  <sub>0..\*</sub>
     * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * Range: [OrganismTaxon](OrganismTaxon.md)
     * in subsets: (translator_minimal)
