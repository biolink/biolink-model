---
parent: Classes
title: biolink:NamedThing
grand_parent: Browse Biolink Model
---

# Type: NamedThing


a databased entity or concept/class

URI: [biolink:NamedThing](https://w3id.org/biolink/vocab/NamedThing)

WD:Q35120
{: .mapping-label }

UMLSSG:OBJC
{: .mapping-label }

UMLSSC:T071
{: .mapping-label }

UMLSST:enty
{: .mapping-label }

UMLSSC:T072
{: .mapping-label }

UMLSST:phob
{: .mapping-label }

UMLSSC:T073
{: .mapping-label }

UMLSST:mnob
{: .mapping-label }

UMLSSC:T168
{: .mapping-label }

UMLSST:food
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Attribute]-%20has%20qualitative%20value%200..1>\[NamedThing&#124;id:identifier_type;name:label_type;category:iri_type%20%2B],%20\[MaterialSampleDerivationAssociation]-%20object%201..1>\[NamedThing],%20\[Association]-%20object%201..1>\[NamedThing],%20\[Association]-%20subject%201..1>\[NamedThing],%20\[VariantToDiseaseAssociation]-%20object%201..1>\[NamedThing],%20\[VariantToDiseaseAssociation]-%20subject%201..1>\[NamedThing],%20\[NamedThing]^-\[PlanetaryEntity],%20\[NamedThing]^-\[PhysicalEntity],%20\[NamedThing]^-\[OntologyClass],%20\[NamedThing]^-\[Occurrent],%20\[NamedThing]^-\[MaterialSample],%20\[NamedThing]^-\[InformationContentEntity],%20\[NamedThing]^-\[Device],%20\[NamedThing]^-\[DataSet],%20\[NamedThing]^-\[DataFile],%20\[NamedThing]^-\[ClinicalEntity],%20\[NamedThing]^-\[BiologicalEntity],%20\[NamedThing]^-\[AdministrativeEntity])

---


## Children

 * [AdministrativeEntity](AdministrativeEntity.md)
 * [BiologicalEntity](BiologicalEntity.md)
 * [ClinicalEntity](ClinicalEntity.md) - Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
 * [DataFile](DataFile.md)
 * [DataSet](DataSet.md)
 * [Device](Device.md) - A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment
 * [InformationContentEntity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.
 * [MaterialSample](MaterialSample.md) - A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
 * [Occurrent](Occurrent.md) - A processual entity
 * [OntologyClass](OntologyClass.md) - a concept or class in an ontology, vocabulary or thesaurus
 * [PhysicalEntity](PhysicalEntity.md) - An entity that has physical properties such as mass, volume, or charge
 * [PlanetaryEntity](PlanetaryEntity.md) - Any entity or process that exists at the level of the whole planet

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[affects](affects.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[affects risk for](affects_risk_for.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[caused by](caused_by.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[causes](causes.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[coexists with](coexists_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[colocalizes with](colocalizes_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[contributes to](contributes_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[derives from](derives_from.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[derives into](derives_into.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[disrupts](disrupts.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[filler](filler.md)*  <sub>OPT</sub>  **[NamedThing](NamedThing.md)**
 *  **[Occurrent](Occurrent.md)** *[has input](has_input.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Occurrent](Occurrent.md)** *[has output](has_output.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[has part](has_part.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Occurrent](Occurrent.md)** *[has participant](has_participant.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Attribute](Attribute.md)** *[has qualitative value](has_qualitative_value.md)*  <sub>OPT</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[homologous to](homologous_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[interacts with](interacts_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[located in](located_in.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[location of](location_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[MaterialSampleDerivationAssociation](MaterialSampleDerivationAssociation.md)** *[material sample derivation association➞object](material_sample_derivation_association_object.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[model of](model_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[ModelToDiseaseMixin](ModelToDiseaseMixin.md)** *[model to disease mixin➞subject](model_to_disease_mixin_subject.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[negatively regulates](negatively_regulates.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Association](Association.md)** *[object](object.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[occurs in](occurs_in.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[orthologous to](orthologous_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[overlaps](overlaps.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[paralogous to](paralogous_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[part of](part_of.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[physically interacts with](physically_interacts_with.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[positively regulates](positively_regulates.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[predisposes](predisposes.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[prevents](prevents.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[produces](produces.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[regulates](regulates.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[related to](related_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[same as](same_as.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[Association](Association.md)** *[subject](subject.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[DiseaseOrPhenotypicFeature](DiseaseOrPhenotypicFeature.md)** *[treated by](treated_by.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**
 *  **[VariantToDiseaseAssociation](VariantToDiseaseAssociation.md)** *[variant to disease association➞object](variant_to_disease_association_object.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[VariantToDiseaseAssociation](VariantToDiseaseAssociation.md)** *[variant to disease association➞subject](variant_to_disease_association_subject.md)*  <sub>REQ</sub>  **[NamedThing](NamedThing.md)**
 *  **[NamedThing](NamedThing.md)** *[xenologous to](xenologous_to.md)*  <sub>0..*</sub>  **[NamedThing](NamedThing.md)**

## Attributes


### Own

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [actively involved in](actively_involved_in.md)  <sub>0..*</sub>
    * Description: holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
    * range: [Occurrent](Occurrent.md)
    * in subsets: (translator_minimal)
 * [affects](affects.md)  <sub>0..*</sub>
    * Description: describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [affects risk for](affects_risk_for.md)  <sub>0..*</sub>
    * Description: holds between two entities where exposure to one entity alters the chance of developing the other
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [aggregate statistic](aggregate_statistic.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [capable of](capable_of.md)  <sub>0..*</sub>
    * Description: holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.
    * range: [Occurrent](Occurrent.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal)
 * [caused by](caused_by.md)  <sub>0..*</sub>
    * Description: holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or  generation of the other
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [causes](causes.md)  <sub>0..*</sub>
    * Description: holds between two entities where the occurrence, existence, or activity of one causes the occurrence or  generation of the other
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [coexists with](coexists_with.md)  <sub>0..*</sub>
    * Description: holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [colocalizes with](colocalizes_with.md)  <sub>0..*</sub>
    * Description: holds between two entities that are observed to be located in the same place.
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [contributes to](contributes_to.md)  <sub>0..*</sub>
    * Description: holds between two entities where the occurrence, existence, or activity of one causes or contributes to the occurrence or generation of the other
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [creation date](creation_date.md)  <sub>OPT</sub>
    * Description: date on which thing was created. This can be applied to nodes or edges
    * range: [Date](types/Date.md)
 * [derives from](derives_from.md)  <sub>0..*</sub>
    * Description: holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal,samples)
 * [derives into](derives_into.md)  <sub>0..*</sub>
    * Description: holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (translator_minimal)
 * [disrupts](disrupts.md)  <sub>0..*</sub>
    * Description: describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [end interbase coordinate](end_interbase_coordinate.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [filler](filler.md)  <sub>OPT</sub>
    * Description: The value in a property-value tuple
    * range: [NamedThing](NamedThing.md)
 * [full name](full_name.md)  <sub>OPT</sub>
    * Description: a long-form human readable name for a thing
    * range: [LabelType](types/LabelType.md)
 * [genome build](genome_build.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [has biological sequence](has_biological_sequence.md)  <sub>OPT</sub>
    * Description: connects a genomic feature to its sequence
    * range: [BiologicalSequence](types/BiologicalSequence.md)
 * [has chemical formula](has_chemical_formula.md)  <sub>OPT</sub>
    * Description: description of chemical compound based on element symbols
    * range: [ChemicalFormulaValue](types/ChemicalFormulaValue.md)
 * [has count](has_count.md)  <sub>OPT</sub>
    * Description: number of things with a particular property
    * range: [Integer](types/Integer.md)
 * [has drug](has_drug.md)  <sub>OPT</sub>
    * Description: connects an entity to a single drug
    * range: [Drug](Drug.md)
 * [has gene](has_gene.md)  <sub>OPT</sub>
    * Description: connects an entity to a single gene
    * range: [Gene](Gene.md)
 * [has molecular consequence](has_molecular_consequence.md)  <sub>0..*</sub>
    * Description: connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583
    * range: [OntologyClass](OntologyClass.md)
 * [has part](has_part.md)  <sub>0..*</sub>
    * Description: holds between wholes and their parts (material entities or processes)
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [has percentage](has_percentage.md)  <sub>OPT</sub>
    * Description: equivalent to has quotient multiplied by 100
    * range: [Double](types/Double.md)
 * [has quotient](has_quotient.md)  <sub>OPT</sub>
    * range: [Double](types/Double.md)
 * [has total](has_total.md)  <sub>OPT</sub>
    * Description: total number of things in a particular reference set
    * range: [Integer](types/Integer.md)
 * [has zygosity](has_zygosity.md)  <sub>OPT</sub>
    * range: [Zygosity](Zygosity.md)
 * [homologous to](homologous_to.md)  <sub>0..*</sub>
    * Description: holds between two biological entities that have common evolutionary origin
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * in subsets: (translator_minimal)
 * [interacts with](interacts_with.md)  <sub>0..*</sub>
    * Description: holds between any two entities that directly or indirectly interact with each other
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [interbase coordinate](interbase_coordinate.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal)
 * [latitude](latitude.md)  <sub>OPT</sub>
    * Description: latitude
    * range: [Float](types/Float.md)
 * [located in](located_in.md)  <sub>0..*</sub>
    * Description: holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [location of](location_of.md)  <sub>0..*</sub>
    * Description: holds between material entity or site and a material entity that is located within it (but not considered a part of it)
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [longitude](longitude.md)  <sub>OPT</sub>
    * Description: longitude
    * range: [Float](types/Float.md)
 * [manifestation of](manifestation_of.md)  <sub>0..*</sub>
    * Description: used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome
    * range: [Disease](Disease.md)
    * in subsets: (translator_minimal)
 * [model of](model_of.md)  <sub>0..*</sub>
    * Description: holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [negatively regulates](negatively_regulates.md)  <sub>0..*</sub>
    * range: [NamedThing](NamedThing.md)
 * [node property](node_property.md)  <sub>OPT</sub>
    * Description: A grouping for any property that holds between a node and a value
    * range: [String](types/String.md)
 * [occurs in](occurs_in.md)  <sub>0..*</sub>
    * Description: holds between a process and a material entity or site within which the process occurs
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [orthologous to](orthologous_to.md)  <sub>0..*</sub>
    * Description: a homology relationship between entities (typically genes) that diverged after a speciation event.
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [overlaps](overlaps.md)  <sub>0..*</sub>
    * Description: holds between entties that overlap in their extents (materials or processes)
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [paralogous to](paralogous_to.md)  <sub>0..*</sub>
    * Description: a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [part of](part_of.md)  <sub>0..*</sub>
    * Description: holds between parts and wholes (material entities or processes)
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [participates in](participates_in.md)  <sub>0..*</sub>
    * Description: holds between a continuant and a process, where the continuant is somehow involved in the process
    * range: [Occurrent](Occurrent.md)
    * in subsets: (translator_minimal)
 * [phase](phase.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [physically interacts with](physically_interacts_with.md)  <sub>0..*</sub>
    * Description: holds between two entities that make physical contact as part of some interaction
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [positively regulates](positively_regulates.md)  <sub>0..*</sub>
    * range: [NamedThing](NamedThing.md)
 * [predisposes](predisposes.md)  <sub>0..*</sub>
    * Description: holds between two entities where exposure to one entity increases the chance of developing the other
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [prevents](prevents.md)  <sub>0..*</sub>
    * Description: holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical substance, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [produces](produces.md)  <sub>0..*</sub>
    * Description: holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [regulates](regulates.md)  <sub>0..*</sub>
    * range: [NamedThing](NamedThing.md)
 * [related to](related_to.md)  <sub>0..*</sub>
    * Description: A relationship that is asserted between two named things
    * range: [NamedThing](NamedThing.md)
 * [same as](same_as.md)  <sub>0..*</sub>
    * Description: holds between two entities that are considered equivalent to each other
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [start interbase coordinate](start_interbase_coordinate.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [synonym](synonym.md)  <sub>0..*</sub>
    * Description: Alternate human-readable names for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [systematic synonym](systematic_synonym.md)  <sub>0..*</sub>
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](types/LabelType.md)
 * [timepoint](timepoint.md)  <sub>OPT</sub>
    * Description: a point in time
    * range: [TimeType](types/TimeType.md)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [update date](update_date.md)  <sub>OPT</sub>
    * Description: date on which thing was updated. This can be applied to nodes or edges
    * range: [Date](types/Date.md)
 * [xenologous to](xenologous_to.md)  <sub>0..*</sub>
    * Description: a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
    * range: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | WD:Q35120 |
|  | | UMLSSG:OBJC |
|  | | UMLSSC:T071 |
|  | | UMLSST:enty |
|  | | UMLSSC:T072 |
|  | | UMLSST:phob |
|  | | UMLSSC:T073 |
|  | | UMLSST:mnob |
|  | | UMLSSC:T168 |
|  | | UMLSST:food |

