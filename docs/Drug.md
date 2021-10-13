---
parent: Entities
title: biolink:Drug
grand_parent: Classes
layout: default
---

# Class: Drug


A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease

URI: [biolink:Drug](https://w3id.org/biolink/vocab/Drug)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClass],[NamedThing],[MolecularMixture],[MolecularEntity],[DrugToEntityAssociationMixin],[DrugToEntityAssociationMixin]-%20subject%201..1%3E[Drug%7Chighest_FDA_approval_status(i):string%20%3F;available_from(i):drug_availability_enum%20%2A;max_tolerated_dose(i):string%20%3F;is_toxic(i):boolean%20%3F;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Treatment]-%20has%20drug%200..%2A%3E[Drug],[Drug]uses%20-.-%3E[ChemicalOrDrugOrTreatment],[Drug]uses%20-.-%3E[OntologyClass],[MolecularMixture]%5E-[Drug],[Treatment],[DiseaseOrPhenotypicFeature],[ChemicalOrDrugOrTreatment],[ChemicalMixture],[ChemicalEntity],[Attribute],[Agent])

---


## Identifier prefixes

 * RXCUI
 * NDC
 * PHARMGKB.DRUG
 * DRUGBANK
 * DrugCentral
 * KEGG.DRUG
 * KEGG.DGROUP
 * SIDER.DRUG

## Parents

 *  is_a: [MolecularMixture](MolecularMixture.md) - A molecular mixture is a chemical mixture composed of two or more molecular entities with known concentration and stoichiometry.

## Uses Mixins

 *  mixin: [ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md)
 *  mixin: [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus. Note that nodes in a biolink compatible KG can be considered both instances of biolink classes, and OWL classes in their own right. In general you should not need to use this class directly. Instead, use the appropriate biolink class. For example, for the GO concept of endocytosis (GO:0006897), use bl:BiologicalProcess as the type.

## Referenced by class

 *  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)** *[adverse event caused by](adverse_event_caused_by.md)*  <sub>0..\*</sub>  **[Drug](Drug.md)**
 *  **[DrugToEntityAssociationMixin](DrugToEntityAssociationMixin.md)** *[drug to entity association mixin➞subject](drug_to_entity_association_mixin_subject.md)*  <sub>1..1</sub>  **[Drug](Drug.md)**
 *  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)** *[has contraindication](has_contraindication.md)*  <sub>0..\*</sub>  **[Drug](Drug.md)**
 *  **[NamedThing](NamedThing.md)** *[has drug](has_drug.md)*  <sub>0..\*</sub>  **[Drug](Drug.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[is active ingredient of](is_active_ingredient_of.md)*  <sub>0..\*</sub>  **[Drug](Drug.md)**
 *  **[MolecularEntity](MolecularEntity.md)** *[is excipient of](is_excipient_of.md)*  <sub>0..\*</sub>  **[Drug](Drug.md)**

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

### Inherited from chemical mixture:

 * [is supplement](is_supplement.md)  <sub>0..1</sub>
     * Range: [ChemicalMixture](ChemicalMixture.md)
 * [highest FDA approval status](highest_FDA_approval_status.md)  <sub>0..1</sub>
     * Description: Should be the highest level of FDA approval this chemical entity or device has, regardless of which disease, condition or phenotype it is currently being reviewed to treat.  For specific levels of FDA approval for a specific condition, disease, phenotype, etc., see the association slot, 'FDA approval status.'
     * Range: [String](types/String.md)

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

 * [macromolecular machine mixin➞name](macromolecular_machine_mixin_name.md)  <sub>0..1</sub>
     * Description: genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * Range: [SymbolType](types/SymbolType.md)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..\*</sub>
     * Range: [NamedThing](NamedThing.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | The CHEBI ID represents a role rather than a substance |
| **Exact Mappings:** | | WIKIDATA:Q12140 |
|  | | CHEBI:23888 |
|  | | STY:T200 |
| **Narrow Mappings:** | | STY:T195 |
| **Broad Mappings:** | | STY:T121 |
