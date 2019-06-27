
# Class: genotype


An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background

URI: [biolink:Genotype](https://w3id.org/biolink/vocab/Genotype)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[OrganismTaxon]<in%20taxon(i)%200..*-%20\[Genotype|has_biological_sequence(i):biological_sequence%20%3F;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[Zygosity]<has%20zygosity%200..1-%20\[Genotype],%20\[GenotypeToGeneAssociation]-%20subject%201..1>\[Genotype],%20\[GenotypeToGenotypePartAssociation]-%20object%201..1>\[Genotype],%20\[GenotypeToGenotypePartAssociation]-%20subject%201..1>\[Genotype],%20\[GenotypeToPhenotypicFeatureAssociation]-%20subject%201..1>\[Genotype],%20\[GenotypeToThingAssociation]-%20subject%201..1>\[Genotype],%20\[GenotypeToVariantAssociation]-%20subject%201..1>\[Genotype],%20\[GenomicEntity]^-\[Genotype])

## Parents

 *  is_a: [GenomicEntity](GenomicEntity.md) - an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)

## Referenced by class

 *  **[GenotypeToGeneAssociation](GenotypeToGeneAssociation.md)** *[subject](genotype_to_gene_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md)** *[object](genotype_to_genotype_part_association_object.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToGenotypePartAssociation](GenotypeToGenotypePartAssociation.md)** *[subject](genotype_to_genotype_part_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToPhenotypicFeatureAssociation](GenotypeToPhenotypicFeatureAssociation.md)** *[subject](genotype_to_phenotypic_feature_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToThingAssociation](GenotypeToThingAssociation.md)** *[subject](genotype_to_thing_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**
 *  **[GenotypeToVariantAssociation](GenotypeToVariantAssociation.md)** *[subject](genotype_to_variant_association_subject.md)*  <sub>REQ</sub>  **[Genotype](Genotype.md)**

## Attributes


### Own

 * [has zygosity](has_zygosity.md)  <sub>OPT</sub>
    * range: [Zygosity](Zygosity.md)

### Inherited from genomic entity:

 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](BiologicalSequence.md)
    * inherited from: [GenomicEntity](GenomicEntity.md)

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

 * [has zygosity](has_zygosity.md)  <sub>OPT</sub>
    * range: [Zygosity](Zygosity.md)
