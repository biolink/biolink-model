---
parent: Associations
title: biolink:GenomicSequenceLocalization
grand_parent: Classes
layout: default
---

# Class: GenomicSequenceLocalization


A relationship between a sequence feature and a nucleic acid entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig.

URI: [biolink:GenomicSequenceLocalization](https://w3id.org/biolink/vocab/GenomicSequenceLocalization)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SequenceAssociation],[Publication],[OntologyClass],[NucleicAcidEntity],[NucleicAcidEntity]%3Cobject%201..1-%20[GenomicSequenceLocalization%7Cstart_interbase_coordinate:integer%20%3F;end_interbase_coordinate:integer%20%3F;genome_build:strand_enum%20%3F;strand:strand_enum%20%3F;phase:phase_enum%20%3F;predicate:predicate_type;relation(i):uriorcurie;negated(i):boolean%20%3F;type(i):string%20%3F;category(i):category_type%20%2A;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[NucleicAcidEntity]%3Csubject%201..1-%20[GenomicSequenceLocalization],[SequenceAssociation]%5E-[GenomicSequenceLocalization],[Attribute],[Agent])

---


## Parents

 *  is_a: [SequenceAssociation](SequenceAssociation.md) - An association between a sequence feature and a nucleic acid entity it is localized to.

## Referenced by class


## Attributes


### Own

 * [end interbase coordinate](end_interbase_coordinate.md)  <sub>OPT</sub>
     * Description: The position at which the subject nucleic acid entity ends on the chromosome or other entity to which it is located on.
     * Range: [Integer](types/Integer.md)
 * [genome build](genome_build.md)  <sub>OPT</sub>
     * Description: The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens.
     * Range: [strand_enum](strand_enum.md)
 * [genomic sequence localization➞object](genomic_sequence_localization_object.md)  <sub>REQ</sub>
     * Range: [NucleicAcidEntity](NucleicAcidEntity.md)
 * [genomic sequence localization➞predicate](genomic_sequence_localization_predicate.md)  <sub>REQ</sub>
     * Range: [PredicateType](types/PredicateType.md)
 * [genomic sequence localization➞subject](genomic_sequence_localization_subject.md)  <sub>REQ</sub>
     * Range: [NucleicAcidEntity](NucleicAcidEntity.md)
 * [start interbase coordinate](start_interbase_coordinate.md)  <sub>OPT</sub>
     * Description: The position at which the subject nucleic acid entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 0).
     * Range: [Integer](types/Integer.md)
 * [strand](strand.md)  <sub>OPT</sub>
     * Description: The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand).
     * Range: [strand_enum](strand_enum.md)

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
     * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
     * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * Range: [PredicateType](types/PredicateType.md)
 * [object](object.md)  <sub>REQ</sub>
     * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * Range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>REQ</sub>
     * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
     * Range: [Uriorcurie](types/Uriorcurie.md)
 * [negated](negated.md)  <sub>OPT</sub>
     * Description: if set to true, then the association is negated i.e. is not true
     * Range: [Boolean](types/Boolean.md)
 * [qualifiers](qualifiers.md)  <sub>0..\*</sub>
     * Description: connects an association to qualifiers that modify or qualify the meaning of that association
     * Range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..\*</sub>
     * Description: connects an association to publications supporting the association
     * Range: [Publication](Publication.md)
 * [association➞type](association_type.md)  <sub>OPT</sub>
     * Description: rdf:type of biolink:Association should be fixed at rdf:Statement
     * Range: [String](types/String.md)
 * [association➞category](association_category.md)  <sub>0..\*</sub>
     * Range: [CategoryType](types/CategoryType.md)

### Inherited from entity:

 * [id](id.md)  <sub>REQ</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * Range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
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
 * [type](type.md)  <sub>OPT</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [source](source.md)  <sub>OPT</sub>
     * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: connects an association to the agent (person, organization or group) that provided it
     * Range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from macromolecular machine mixin:

 * [macromolecular machine mixin➞name](macromolecular_machine_mixin_name.md)  <sub>OPT</sub>
     * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * Range: [SymbolType](types/SymbolType.md)

### Domain for slot:

 * [end interbase coordinate](end_interbase_coordinate.md)  <sub>OPT</sub>
     * Description: The position at which the subject nucleic acid entity ends on the chromosome or other entity to which it is located on.
     * Range: [Integer](types/Integer.md)
 * [genome build](genome_build.md)  <sub>OPT</sub>
     * Description: The version of the genome on which a feature is located. For example, GRCh38 for Homo sapiens.
     * Range: [strand_enum](strand_enum.md)
 * [genomic sequence localization➞object](genomic_sequence_localization_object.md)  <sub>REQ</sub>
     * Range: [NucleicAcidEntity](NucleicAcidEntity.md)
 * [genomic sequence localization➞predicate](genomic_sequence_localization_predicate.md)  <sub>REQ</sub>
     * Range: [PredicateType](types/PredicateType.md)
 * [genomic sequence localization➞subject](genomic_sequence_localization_subject.md)  <sub>REQ</sub>
     * Range: [NucleicAcidEntity](NucleicAcidEntity.md)
 * [start interbase coordinate](start_interbase_coordinate.md)  <sub>OPT</sub>
     * Description: The position at which the subject nucleic acid entity starts on the chromosome or other entity to which it is located on. (ie: the start of the sequence being referenced is 0).
     * Range: [Integer](types/Integer.md)
 * [strand](strand.md)  <sub>OPT</sub>
     * Description: The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand).
     * Range: [strand_enum](strand_enum.md)
