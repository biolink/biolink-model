# Class: ThingWithTaxon
_A mixin that can be used on any entity that can be taxonomically classified. This includes individual organisms; genes, their products and other molecular entities; body parts; biological processes_




* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [biolink:ThingWithTaxon](https://w3id.org/biolink/vocab/ThingWithTaxon)




## Inheritance

* **ThingWithTaxon**
    * [GenomicEntity](GenomicEntity.md)




## Slots

| Name | Range | Cardinality | Description  | Info |
| ---  | --- | --- | --- | --- |
| [in_taxon](in_taxon.md) | [OrganismTaxon](OrganismTaxon.md) | 0..* | connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'  | . |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [StudyPopulation](StudyPopulation.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [ThingWithTaxon](ThingWithTaxon.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [GenomicEntity](GenomicEntity.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [NucleicAcidEntity](NucleicAcidEntity.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [LifeStage](LifeStage.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [IndividualOrganism](IndividualOrganism.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [Disease](Disease.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [PhenotypicFeature](PhenotypicFeature.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [BehavioralFeature](BehavioralFeature.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [AnatomicalEntity](AnatomicalEntity.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [CellularComponent](CellularComponent.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [Cell](Cell.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [GrossAnatomicalStructure](GrossAnatomicalStructure.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [Gene](Gene.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [Genome](Genome.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [Exon](Exon.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [Transcript](Transcript.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [CodingSequence](CodingSequence.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [Polypeptide](Polypeptide.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [Protein](Protein.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [ProteinIsoform](ProteinIsoform.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [RNAProduct](RNAProduct.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [RNAProductIsoform](RNAProductIsoform.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [NoncodingRNAProduct](NoncodingRNAProduct.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [MicroRNA](MicroRNA.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [SiRNA](SiRNA.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [Genotype](Genotype.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [Haplotype](Haplotype.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [SequenceVariant](SequenceVariant.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [Snv](Snv.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [ReagentTargetedGene](ReagentTargetedGene.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [ClinicalFinding](ClinicalFinding.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [Case](Case.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [Cohort](Cohort.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [GenomicBackgroundExposure](GenomicBackgroundExposure.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |
| [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) | [in_taxon](in_taxon.md) | domain | thing with taxon |



## Identifier and Mapping Information









## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: thing with taxon
description: A mixin that can be used on any entity that can be taxonomically classified.
  This includes individual organisms; genes, their products and other molecular entities;
  body parts; biological processes
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
slots:
- in taxon

```
</details>

### Induced

<details>
```yaml
name: thing with taxon
description: A mixin that can be used on any entity that can be taxonomically classified.
  This includes individual organisms; genes, their products and other molecular entities;
  body parts; biological processes
from_schema: https://w3id.org/biolink/biolink-model
mixin: true
attributes:
  in taxon:
    name: in taxon
    aliases:
    - instance of
    - is organism source of gene product
    - organism has gene
    - gene found in organism
    - ' gene product has organism source'
    exact_mappings:
    - RO:0002162
    - WIKIDATA_PROPERTY:P703
    narrow_mappings:
    - RO:0002160
    annotations:
      biolink:canonical_predicate:
        tag: biolink:canonical_predicate
        value: 'True'
    description: connects an entity to its taxonomic classification. Only certain
      kinds of entities can be taxonomically classified; see 'thing with taxon'
    in_subset:
    - translator_minimal
    from_schema: https://w3id.org/biolink/biolink-model
    is_a: related to at instance level
    domain: thing with taxon
    multivalued: true
    inherited: true
    alias: in_taxon
    owner: thing with taxon
    range: organism taxon

```
</details>