---
parent: Entities
title: biolink:Transcript
grand_parent: Classes
layout: default
---

# Class: Transcript


An RNA synthesized on a DNA or RNA template by an RNA polymerase.

URI: [biolink:Transcript](https://w3id.org/biolink/vocab/Transcript)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[TranscriptToGeneRelationship],[ExonToTranscriptRelationship]-%20object%201..1%3E[Transcript%7Chas_biological_sequence(i):biological_sequence%20%3F;is_metabolite(i):boolean%20%3F;available_from(i):drug_availability_enum%20%2A;max_tolerated_dose(i):string%20%3F;is_toxic(i):boolean%20%3F;provided_by(i):string%20%2A;xref(i):uriorcurie%20%2A;category(i):category_type%20%2B;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):string%20%3F],[TranscriptToGeneRelationship]-%20subject%201..1%3E[Transcript],[Transcript]%5E-[RNAProduct],[NucleicAcidEntity]%5E-[Transcript],[Protein],[OrganismTaxon],[NucleicAcidEntity],[Gene],[ExonToTranscriptRelationship],[ChemicalRole],[ChemicalEntityOrGeneOrGeneProduct],[ChemicalEntity],[Attribute],[RNAProduct])

---


## Identifier prefixes

 * ENSEMBL
 * FB

## Parents

 *  is_a: [NucleicAcidEntity](NucleicAcidEntity.md) - A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included.

## Children

 * [RNAProduct](RNAProduct.md)

## Referenced by class

 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[affects splicing of](affects_splicing_of.md)*  <sub>0..\*</sub>  **[Transcript](Transcript.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[decreases splicing of](decreases_splicing_of.md)*  <sub>0..\*</sub>  **[Transcript](Transcript.md)**
 *  **[ExonToTranscriptRelationship](ExonToTranscriptRelationship.md)** *[object](object.md)*  <sub>1..1</sub>  **[Transcript](Transcript.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[increases splicing of](increases_splicing_of.md)*  <sub>0..\*</sub>  **[Transcript](Transcript.md)**
 *  **[Gene](Gene.md)** *[transcribed to](transcribed_to.md)*  <sub>0..\*</sub>  **[Transcript](Transcript.md)**
 *  **[TranscriptToGeneRelationship](TranscriptToGeneRelationship.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[Transcript](Transcript.md)**
 *  **[Protein](Protein.md)** *[translation of](translation_of.md)*  <sub>0..\*</sub>  **[Transcript](Transcript.md)**

## Attributes


### Inherited from chemical entity:

 * [trade name](trade_name.md)  <sub>0..1</sub>
     * Range: [ChemicalEntity](ChemicalEntity.md)
 * [available from](available_from.md)  <sub>0..\*</sub>
     * Range: [drug_availability_enum](drug_availability_enum.md)
 * [max tolerated dose](max_tolerated_dose.md)  <sub>0..1</sub>
     * Description: The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.
     * Range: [String](types/String.md)
 * [is toxic](is_toxic.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [has chemical role](has_chemical_role.md)  <sub>0..\*</sub>
     * Description: A role is particular behaviour which a material entity may exhibit.
     * Range: [ChemicalRole](ChemicalRole.md)

### Inherited from entity:

 * [id](id.md)  <sub>1..1</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>0..1</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * Range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)
 * [type](type.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [source](source.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from gene product mixin:

 * [xref](xref.md)  <sub>0..\*</sub>
     * Description: Alternate CURIEs for a thing
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (translator_minimal)

### Inherited from genomic entity:

 * [has biological sequence](has_biological_sequence.md)  <sub>0..1</sub>
     * Description: connects a genomic feature to its sequence
     * Range: [BiologicalSequence](types/BiologicalSequence.md)

### Inherited from macromolecular machine mixin:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)

### Inherited from molecular entity:

 * [is metabolite](is_metabolite.md)  <sub>0..1</sub>
     * Description: indicates whether a molecular entity is a metabolite
     * Range: [Boolean](types/Boolean.md)

### Inherited from named thing:

 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     * Range: [String](types/String.md)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..\*</sub>
     * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * Range: [OrganismTaxon](OrganismTaxon.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | SO:0000673 |
|  | | SIO:010450 |
|  | | WIKIDATA:Q7243183 |
|  | | dcid:RNATranscript |

