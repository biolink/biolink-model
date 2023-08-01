---
parent: Entities
title: biolink:DiseaseOrPhenotypicFeature
grand_parent: Classes
layout: default
---

# Class: DiseaseOrPhenotypicFeature


Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.  Please see definitions of phenotypic feature and disease in this model for their independent descriptions.  This class is helpful to enforce domains and ranges   that may involve either a disease or a phenotypic feature.

URI: [biolink:DiseaseOrPhenotypicFeature](https://w3id.org/biolink/vocab/DiseaseOrPhenotypicFeature)


---

![img](https://yuml.me/diagram/nofunky;dir:TB/class/[PhenotypicFeature],[OrganismTaxon],[NamedThing],[GeneticInheritance],[GeneToDiseaseOrPhenotypicFeatureAssociation],[Gene],[EntityToDiseaseOrPhenotypicFeatureAssociationMixin],[Drug],[DiseaseOrPhenotypicFeatureToEntityAssociationMixin],[CellLineToDiseaseOrPhenotypicFeatureAssociation]-%20subject%201..1%3E[DiseaseOrPhenotypicFeature%7Cin_taxon_label(i):label_type%20%3F;provided_by(i):string%20%2A;xref(i):uriorcurie%20%2A;full_name(i):label_type%20%3F;synonym(i):label_type%20%2A;category(i):category_type%20%2B;id(i):string;iri(i):iri_type%20%3F;type(i):string%20%2A;name(i):label_type%20%3F;description(i):narrative_text%20%3F],[ChemicalToDiseaseOrPhenotypicFeatureAssociation]-%20object%201..1%3E[DiseaseOrPhenotypicFeature],[DiseaseOrPhenotypicFeatureToEntityAssociationMixin]-%20subject%201..1%3E[DiseaseOrPhenotypicFeature],[EntityToDiseaseOrPhenotypicFeatureAssociationMixin]-%20object%201..1%3E[DiseaseOrPhenotypicFeature],[GeneToDiseaseOrPhenotypicFeatureAssociation]-%20object%201..1%3E[DiseaseOrPhenotypicFeature],[GeneExpressionMixin]-%20phenotypic%20state%200..1%3E[DiseaseOrPhenotypicFeature],[DiseaseOrPhenotypicFeature]%5E-[PhenotypicFeature],[DiseaseOrPhenotypicFeature]%5E-[Disease],[BiologicalEntity]%5E-[DiseaseOrPhenotypicFeature],[GeneExpressionMixin],[Disease],[DiagnosticAid],[ChemicalToDiseaseOrPhenotypicFeatureAssociation],[ChemicalOrDrugOrTreatment],[ChemicalEntityOrGeneOrGeneProduct],[CellLineToDiseaseOrPhenotypicFeatureAssociation],[BiologicalEntity],[Attribute],[Association])

---


## Parents

 *  is_a: [BiologicalEntity](BiologicalEntity.md)

## Children

 * [Disease](Disease.md) - A disorder of structure or function, especially one that produces specific  signs, phenotypes or symptoms or that affects a specific location and is not simply a  direct result of physical injury.  A disposition to undergo pathological processes that exists in an  organism because of one or more disorders in that organism.
 * [PhenotypicFeature](PhenotypicFeature.md) - A combination of entity and quality that makes up a phenotyping statement. An observable characteristic of an  individual resulting from the interaction of its genotype with its molecular and physical environment.

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[ameliorates](ameliorates.md)*  <sub>0..\*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[NamedThing](NamedThing.md)** *[animal model available from](animal_model_available_from.md)*  <sub>0..\*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[ChemicalEntityOrGeneOrGeneProduct](ChemicalEntityOrGeneOrGeneProduct.md)** *[biomarker for](biomarker_for.md)*  <sub>0..\*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[CellLineToDiseaseOrPhenotypicFeatureAssociation](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[Gene](Gene.md)** *[condition associated with gene](condition_associated_with_gene.md)*  <sub>0..\*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[Drug](Drug.md)** *[contraindicated for](contraindicated_for.md)*  <sub>0..\*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[DiagnosticAid](DiagnosticAid.md)** *[diagnoses](diagnoses.md)*  <sub>0..\*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[DiseaseOrPhenotypicFeatureToEntityAssociationMixin](DiseaseOrPhenotypicFeatureToEntityAssociationMixin.md)** *[subject](subject.md)*  <sub>1..1</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[EntityToDiseaseOrPhenotypicFeatureAssociationMixin](EntityToDiseaseOrPhenotypicFeatureAssociationMixin.md)** *[object](object.md)*  <sub>1..1</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[BiologicalEntity](BiologicalEntity.md)** *[exacerbates](exacerbates.md)*  <sub>0..\*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[GeneToDiseaseOrPhenotypicFeatureAssociation](GeneToDiseaseOrPhenotypicFeatureAssociation.md)** *[object](object.md)*  <sub>1..1</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md)** *[has adverse event](has_adverse_event.md)*  <sub>0..\*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md)** *[has side effect](has_side_effect.md)*  <sub>0..\*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[GeneticInheritance](GeneticInheritance.md)** *[mode of inheritance of](mode_of_inheritance_of.md)*  <sub>0..\*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[Association](Association.md)** *[phenotypic state](phenotypic_state.md)*  <sub>0..1</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**
 *  **[ChemicalOrDrugOrTreatment](ChemicalOrDrugOrTreatment.md)** *[treats](treats.md)*  <sub>0..\*</sub>  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)**

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
| **Aliases:** | | phenome |
| **Narrow Mappings:** | | STY:T033 |

