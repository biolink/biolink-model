---
parent: Entities
title: biolink:AnatomicalEntity
grand_parent: Classes
layout: default
---

# Class: AnatomicalEntity


A subcellular location, cell type or gross anatomical part

URI: [biolink:AnatomicalEntity](https://w3id.org/biolink/vocab/AnatomicalEntity)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PhysicalEssence],[PathologicalAnatomicalStructure],[OrganismalEntity],[OrganismTaxon],[GrossAnatomicalStructure],[GeneToExpressionSiteAssociation],[GeneOrGeneProduct],[GeneAffectsChemicalAssociation],[DiseaseOrPhenotypicFeatureToLocationAssociation],[ChemicalGeneInteractionAssociation],[ChemicalAffectsGeneAssociation],[CellularComponent],[Cell],[Attribute],[Association],[AnatomicalEntityToAnatomicalEntityPartOfAssociation],[AnatomicalEntityToAnatomicalEntityOntogenicAssociation],[AnatomicalEntityToAnatomicalEntityAssociation],[AnatomicalEntityToAnatomicalEntityAssociation]-%20object%201..1%3E[AnatomicalEntity%7Cin_taxon_label(i):label_type%20%3F;provided_by(i):string%20%2A;xref(i):uriorcurie%20%2A;full_name(i):label_type%20%3F;synonym(i):label_type%20%2A;category(i):category_type%20%2B;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%2A;name(i):label_type%20%3F;description(i):narrative_text%20%3F;deprecated(i):boolean%20%3F],[AnatomicalEntityToAnatomicalEntityAssociation]-%20subject%201..1%3E[AnatomicalEntity],[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20object%201..1%3E[AnatomicalEntity],[AnatomicalEntityToAnatomicalEntityOntogenicAssociation]-%20subject%201..1%3E[AnatomicalEntity],[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20object%201..1%3E[AnatomicalEntity],[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20subject%201..1%3E[AnatomicalEntity],[ChemicalAffectsGeneAssociation]-%20anatomical%20context%20qualifier%200..1%3E[AnatomicalEntity],[ChemicalAffectsGeneAssociation]-%20object%20context%20qualifier%200..1%3E[AnatomicalEntity],[ChemicalAffectsGeneAssociation]-%20subject%20context%20qualifier%200..1%3E[AnatomicalEntity],[ChemicalGeneInteractionAssociation]-%20anatomical%20context%20qualifier%200..1%3E[AnatomicalEntity],[ChemicalGeneInteractionAssociation]-%20object%20context%20qualifier%200..1%3E[AnatomicalEntity],[ChemicalGeneInteractionAssociation]-%20subject%20context%20qualifier%200..1%3E[AnatomicalEntity],[DiseaseOrPhenotypicFeatureToLocationAssociation]-%20object%201..1%3E[AnatomicalEntity],[GeneExpressionMixin]-%20expression%20site%200..1%3E[AnatomicalEntity],[GeneAffectsChemicalAssociation]-%20anatomical%20context%20qualifier%200..1%3E[AnatomicalEntity],[GeneAffectsChemicalAssociation]-%20object%20context%20qualifier%200..1%3E[AnatomicalEntity],[GeneAffectsChemicalAssociation]-%20subject%20context%20qualifier%200..1%3E[AnatomicalEntity],[GeneToExpressionSiteAssociation]-%20object%201..1%3E[AnatomicalEntity],[AnatomicalEntity]uses%20-.-%3E[PhysicalEssence],[AnatomicalEntity]%5E-[PathologicalAnatomicalStructure],[AnatomicalEntity]%5E-[GrossAnatomicalStructure],[AnatomicalEntity]%5E-[CellularComponent],[AnatomicalEntity]%5E-[Cell],[OrganismalEntity]%5E-[AnatomicalEntity],[GeneExpressionMixin])

---


## Identifier prefixes

 * UBERON
 * GO
 * CL
 * UMLS
 * MESH
 * NCIT
 * EMAPA
 * ZFA
 * FBbt
 * WBbt

## Parents

 *  is_a: [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding chemical entities

## Uses Mixins

 *  mixin: [PhysicalEssence](PhysicalEssence.md) - Semantic mixin concept.  Pertains to entities that have physical properties such as mass, volume, or charge.

## Children

 * [Cell](Cell.md)
 * [CellularComponent](CellularComponent.md) - A location in or around a cell
 * [GrossAnatomicalStructure](GrossAnatomicalStructure.md)
 * [PathologicalAnatomicalStructure](PathologicalAnatomicalStructure.md) - An anatomical structure with the potential of have an abnormal or deleterious effect at the subcellular, cellular, multicellular, or organismal level.

## Referenced by class

 *  **[AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityOntogenicAssociation](AnatomicalEntityToAnatomicalEntityOntogenicAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[AnatomicalEntityToAnatomicalEntityPartOfAssociation](AnatomicalEntityToAnatomicalEntityPartOfAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md)** *[anatomical context qualifier](anatomical_context_qualifier.md)*  <sub>0..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md)** *[object context qualifier](object_context_qualifier.md)*  <sub>0..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[ChemicalAffectsGeneAssociation](ChemicalAffectsGeneAssociation.md)** *[subject context qualifier](subject_context_qualifier.md)*  <sub>0..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md)** *[anatomical context qualifier](anatomical_context_qualifier.md)*  <sub>0..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md)** *[object context qualifier](object_context_qualifier.md)*  <sub>0..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[ChemicalGeneInteractionAssociation](ChemicalGeneInteractionAssociation.md)** *[subject context qualifier](subject_context_qualifier.md)*  <sub>0..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[DiseaseOrPhenotypicFeatureToLocationAssociation](DiseaseOrPhenotypicFeatureToLocationAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[GeneOrGeneProduct](GeneOrGeneProduct.md)** *[expressed in](expressed_in.md)*  <sub>0..\*</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[Association](Association.md)** *[expression site](expression_site.md)*  <sub>0..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md)** *[anatomical context qualifier](anatomical_context_qualifier.md)*  <sub>0..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md)** *[object context qualifier](object_context_qualifier.md)*  <sub>0..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[GeneAffectsChemicalAssociation](GeneAffectsChemicalAssociation.md)** *[subject context qualifier](subject_context_qualifier.md)*  <sub>0..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**
 *  **[GeneToExpressionSiteAssociation](GeneToExpressionSiteAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[AnatomicalEntity](AnatomicalEntity.md)**

## Attributes


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

### Inherited from organismal entity:

 * [has attribute](has_attribute.md)  <sub>0..\*</sub>
     * Description: connects any entity to an attribute
     * Range: [Attribute](Attribute.md)
     * in subsets: (samples)

### Inherited from thing with taxon:

 * [in taxon](in_taxon.md)  <sub>0..\*</sub>
     * Description: connects an entity to its taxonomic classification. Only certain kinds of entities can be taxonomically classified; see 'thing with taxon'
     * Range: [OrganismTaxon](OrganismTaxon.md)
     * in subsets: (translator_minimal)
 * [in taxon label](in_taxon_label.md)  <sub>0..1</sub>
     * Description: The human readable scientific name for the taxon of the entity.
     * Range: [LabelType](types/LabelType.md)
     * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | model_organism_database |
| **Exact Mappings:** | | UBERON:0001062 |
|  | | WIKIDATA:Q4936952 |
|  | | UMLSSG:ANAT |
|  | | STY:T017 |
|  | | FMA:62955 |
|  | | CARO:0000000 |
|  | | SIO:001262 |
|  | | STY:T029 |
|  | | STY:T030 |
| **Narrow Mappings:** | | ZFA:0100000 |
|  | | FBbt:10000000 |
|  | | EMAPA:0 |
|  | | MA:0000001 |
|  | | XAO:0000000 |
|  | | WBbt:0000100 |
|  | | NCIT:C12219 |
|  | | GO:0110165 |
|  | | STY:T031 |
| **Related Mappings:** | | SNOMEDCT:123037004 |

