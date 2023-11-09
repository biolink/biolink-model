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

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[SmallMolecule],[ReactionToParticipantAssociation],[PairwiseMolecularInteraction],[NucleicAcidEntity],[NamedThing],[MolecularActivity]-%20has%20input%200..%2A%3E[MolecularEntity%7Cis_metabolite:boolean%20%3F;available_from(i):DrugAvailabilityEnum%20%2A;max_tolerated_dose(i):string%20%3F;is_toxic(i):boolean%20%3F;provided_by(i):string%20%2A;xref(i):uriorcurie%20%2A;full_name(i):label_type%20%3F;synonym(i):label_type%20%2A;category(i):category_type%20%2B;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%2A;name(i):label_type%20%3F;description(i):narrative_text%20%3F;deprecated(i):boolean%20%3F],[MolecularActivity]-%20has%20output%200..%2A%3E[MolecularEntity],[PairwiseMolecularInteraction]-%20object%201..1%3E[MolecularEntity],[PairwiseMolecularInteraction]-%20subject%201..1%3E[MolecularEntity],[ReactionToParticipantAssociation]-%20subject%201..1%3E[MolecularEntity],[MolecularEntity]%5E-[SmallMolecule],[MolecularEntity]%5E-[NucleicAcidEntity],[ChemicalEntity]%5E-[MolecularEntity],[MolecularActivity],[Drug],[ChemicalRole],[ChemicalEntity],[Attribute])

---


## Identifier prefixes

 * PUBCHEM.COMPOUND
 * CHEMBL.COMPOUND
 * UNII
 * CHEBI
 * DRUGBANK
 * MESH
 * CAS
 * DrugCentral
 * GTOPDB
 * HMDB
 * KEGG.COMPOUND
 * ChemBank
 * PUBCHEM.SUBSTANCE
 * SIDER.DRUG
 * INCHI
 * INCHIKEY
 * KEGG.GLYCAN
 * KEGG.DRUG
 * KEGG.ENVIRON
 * KEGG
 * UMLS

## Parents

 *  is_a: [ChemicalEntity](ChemicalEntity.md) - A chemical entity is a physical entity that pertains to chemistry or biochemistry.

## Children

 * [NucleicAcidEntity](NucleicAcidEntity.md) - A nucleic acid entity is a molecular entity characterized by availability in gene databases of nucleotide-based sequence representations of its precise sequence; for convenience of representation, partial sequences of various kinds are included.
 * [SmallMolecule](SmallMolecule.md) - A small molecule entity is a molecular entity characterized by availability in small-molecule databases of SMILES, InChI, IUPAC, or other unambiguous representation of its precise chemical structure; for convenience of representation, any valid chemical representation is included, even if it is not strictly molecular (e.g., sodium ion).

## Referenced by class

 *  **[Drug](Drug.md)** *[has active ingredient](has_active_ingredient.md)*  <sub>0..\*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[NamedThing](NamedThing.md)** *[has constituent](has_constituent.md)*  <sub>0..\*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[Drug](Drug.md)** *[has excipient](has_excipient.md)*  <sub>0..\*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[has metabolite](has_metabolite.md)*  <sub>0..\*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[is metabolite of](is_metabolite_of.md)*  <sub>0..\*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[has input](has_input.md)*  <sub>0..\*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[MolecularActivity](MolecularActivity.md)** *[has output](has_output.md)*  <sub>0..\*</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[PairwiseMolecularInteraction](PairwiseMolecularInteraction.md)** *[object](object.md)*  <sub>1..1</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[PairwiseMolecularInteraction](PairwiseMolecularInteraction.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[MolecularEntity](MolecularEntity.md)**
 *  **[ReactionToParticipantAssociation](ReactionToParticipantAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[MolecularEntity](MolecularEntity.md)**

## Attributes


### Own

 * [is metabolite](is_metabolite.md)  <sub>0..1</sub>
     * Description: indicates whether a molecular entity is a metabolite
     * Range: [Boolean](types/Boolean.md)

### Inherited from chemical entity:

 * [trade name](trade_name.md)  <sub>0..1</sub>
     * Range: [ChemicalEntity](ChemicalEntity.md)
 * [available from](available_from.md)  <sub>0..\*</sub>
     * Range: [DrugAvailabilityEnum](DrugAvailabilityEnum.md)
 * [max tolerated dose](max_tolerated_dose.md)  <sub>0..1</sub>
     * Description: The highest dose of a drug or treatment that does not cause unacceptable side effects. The maximum tolerated dose is determined in clinical trials by testing increasing doses on different groups of people until the highest dose with acceptable side effects is found. Also called MTD.
     * Range: [String](types/String.md)
 * [is toxic](is_toxic.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)
 * [has chemical role](has_chemical_role.md)  <sub>0..\*</sub>
     * Description: A role is particular behaviour which a chemical entity may exhibit.
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
 * [type](type.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Description: a human-readable description of an entity
     * Range: [NarrativeText](types/NarrativeText.md)
     * in subsets: (translator_minimal)
 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)
 * [deprecated](deprecated.md)  <sub>0..1</sub>
     * Description: A boolean flag indicating that an entity is no longer considered current or valid.
     * Range: [Boolean](types/Boolean.md)

### Inherited from gene product mixin:

 * [synonym](synonym.md)  <sub>0..\*</sub>
     * Description: Alternate human-readable names for a thing
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)
 * [xref](xref.md)  <sub>0..\*</sub>
     * Description: A database cross reference or alternative identifier for a NamedThing or edge between two  NamedThings.  This property should point to a database record or webpage that supports the existence of the edge, or  gives more detail about the edge. This property can be used on a node or edge to provide multiple URIs or CURIE cross references.
     * Range: [Uriorcurie](types/Uriorcurie.md)
     * in subsets: (translator_minimal)

### Inherited from macromolecular machine mixin:

 * [name](name.md)  <sub>0..1</sub>
     * Description: A human-readable name for an attribute or entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal,samples)

### Inherited from named thing:

 * [provided by](provided_by.md)  <sub>0..\*</sub>
     * Description: The value in this node property represents the knowledge provider that created or assembled the node and all of its attributes.  Used internally to represent how a particular node made its way into a knowledge provider or graph.
     * Range: [String](types/String.md)
 * [full name](full_name.md)  <sub>0..1</sub>
     * Description: a long-form human readable name for a thing
     * Range: [LabelType](types/LabelType.md)
 * [category](category.md)  <sub>0..\*</sub>
     * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `biolink:Protein`, `biolink:GeneProduct`, `biolink:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {biolink:GenomicEntity, biolink:MolecularEntity, biolink:NamedThing}
     * Range: [CategoryType](types/CategoryType.md)
     * in subsets: (translator_minimal)

### Domain for slot:

 * [is metabolite](is_metabolite.md)  <sub>0..1</sub>
     * Description: indicates whether a molecular entity is a metabolite
     * Range: [Boolean](types/Boolean.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | translator_minimal |
| **Narrow Mappings:** | | STY:T088 |
|  | | STY:T085 |
|  | | CHEBI:23367 |
|  | | bioschemas:MolecularEntity |

