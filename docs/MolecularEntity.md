---
parent: Entities
title: biolink:MolecularEntity
grand_parent: Classes
layout: default
---

# Class: MolecularEntity


A molecular entity is a chemical entity composed of individual or covalently bonded atoms.

URI: [biolink:MolecularEntity](https://w3id.org/biolink/vocab/MolecularEntity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SmallMolecule],[ReactionToParticipantAssociation],[Polypeptide],[PairwiseMolecularInteraction],[NucleicAcidEntity],[NamedThing],[MolecularActivity]-%20has%20input%200..%2A%3E[MolecularEntity%7Cis_metabolite:boolean%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[MolecularActivity]-%20has%20output%200..%2A%3E[MolecularEntity],[PairwiseMolecularInteraction]-%20object%201..1%3E[MolecularEntity],[PairwiseMolecularInteraction]-%20subject%201..1%3E[MolecularEntity],[ReactionToParticipantAssociation]-%20subject%201..1%3E[MolecularEntity],[MolecularEntity]%5E-[SmallMolecule],[MolecularEntity]%5E-[Polypeptide],[MolecularEntity]%5E-[NucleicAcidEntity],[ChemicalEntity]%5E-[MolecularEntity],[MolecularActivity],[Drug],[ChemicalEntity],[Attribute],[Agent])

---


## Parents

 *  is_a: [ChemicalEntity](ChemicalEntity.md) - A chemical entity is a physical entity that pertains to chemistry or biochemistry.

## Children

 * [NucleicAcidEntity](NucleicAcidEntity.md) - A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included, even if they do not represent a physical molecule.
 * [Polypeptide](Polypeptide.md) - A polypeptide is a molecular entity characterized by availability in protein databases of amino-acid-based sequence representations of its precise primary structure; for convenience of representation, partial sequences of various kinds are included, even if they do not represent a physical molecule.
 * [SmallMolecule](SmallMolecule.md) - A small molecule entity is a molecular entity characterized by availability in small-molecule databases of SMILES, InChI, IUPAC, or other unambiguous representation of its precise chemical structure; for convenience of representation, any valid chemical representation is included, even if it is not strictly molecular (e.g., sodium ion).

## Referenced by class

 *  **[MolecularEntity](MolecularEntity.md)** *[decreases molecular interaction](decreases_molecular_interaction.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[Drug](Drug.md)** *[has active ingredient](has_active_ingredient.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[NamedThing](NamedThing.md)** *[has constituent](has_constituent.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[Drug](Drug.md)** *[has excipient](has_excipient.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[has metabolite](has_metabolite.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[increases molecular interaction](increases_molecular_interaction.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[is metabolite of](is_metabolite_of.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[molecular activity➞has input](molecular_activity_has_input.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[molecular activity➞has output](molecular_activity_has_output.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[molecular interaction decreased by](molecular_interaction_decreased_by.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[molecular interaction increased by](molecular_interaction_increased_by.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[molecularly interacts with](molecularly_interacts_with.md)*  <sub>0..*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[PairwiseMolecularInteraction](PairwiseMolecularInteraction.md)** *[pairwise molecular interaction➞object](pairwise_molecular_interaction_object.md)*  <sub>REQ</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[PairwiseMolecularInteraction](PairwiseMolecularInteraction.md)** *[pairwise molecular interaction➞subject](pairwise_molecular_interaction_subject.md)*  <sub>REQ</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[ReactionToParticipantAssociation](ReactionToParticipantAssociation.md)** *[reaction to participant association➞subject](reaction_to_participant_association_subject.md)*  <sub>REQ</sub>  **[MolecularEntity](MolecularEntity.md)**

## Attributes


### Own

 * [is metabolite](is_metabolite.md)  <sub>OPT</sub>
     * Description: indicates whether a molecular entity is a metabolite
     * range: [Boolean](types/Boolean.md)

### Inherited from entity:

 * [id](id.md)  <sub>REQ</sub>
     * Description: A unique identifier for an entity. Must be either a CURIE shorthand for a URI or a complete URI
     * range: [String](types/String.md)
     * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
     * Description: An IRI for an entity. This is determined by the id using expansion rules.
     * range: [IriType](types/IriType.md)
     * in subsets: (translator_minimal,samples)
 * [category](category.md)  <sub>0..*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)
 * [type](type.md)  <sub>OPT</sub>
     * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
     * Description: a human-readable description of an entity
     * range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [source](source.md)  <sub>OPT</sub>
     * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
     * range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..*</sub>
     * Description: connects an association to the agent (person, organization or group) that provided it
     * range: [Agent](Agent.md)
 * [has attribute](has_attribute.md)  <sub>0..*</sub>
     * Description: connects any entity to an attribute
     * range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from macromolecular machine mixin:

 * [macromolecular machine mixin➞name](macromolecular_machine_mixin_name.md)  <sub>OPT</sub>
     * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * range: [SymbolType](types/SymbolType.md)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
     * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [is metabolite](is_metabolite.md)  <sub>OPT</sub>
     * Description: indicates whether a molecular entity is a metabolite
     * range: [Boolean](types/Boolean.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | translator_minimal |
| **Narrow Mappings:** | | UMLSSC:T088 |
|  | | UMLSSC:T085 |
|  | | UMLSSG:T127 |

