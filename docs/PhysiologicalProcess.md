# Class: physiological process




URI: [http://w3id.org/biolink/vocab/PhysiologicalProcess](http://w3id.org/biolink/vocab/PhysiologicalProcess)

![img](images/PhysiologicalProcess.png)
## Mappings

 * [UMLSSG:PHYS](http://purl.obolibrary.org/obo/UMLSSG_PHYS)
 * [UMLSSC:T032](http://purl.obolibrary.org/obo/UMLSSC_T032)
 * [UMLSST:orga](http://purl.obolibrary.org/obo/UMLSST_orga)
 * [UMLSSC:T039](http://purl.obolibrary.org/obo/UMLSSC_T039)
 * [UMLSST:phsf](http://purl.obolibrary.org/obo/UMLSST_phsf)
 * [UMLSSC:T040](http://purl.obolibrary.org/obo/UMLSSC_T040)
 * [UMLSST:orgf](http://purl.obolibrary.org/obo/UMLSST_orgf)
 * [UMLSSC:T041](http://purl.obolibrary.org/obo/UMLSSC_T041)
 * [UMLSST:menp](http://purl.obolibrary.org/obo/UMLSST_menp)
 * [UMLSSC:T042](http://purl.obolibrary.org/obo/UMLSSC_T042)
 * [UMLSST:ortf](http://purl.obolibrary.org/obo/UMLSST_ortf)
 * [UMLSSC:T043](http://purl.obolibrary.org/obo/UMLSSC_T043)
 * [UMLSST:celf](http://purl.obolibrary.org/obo/UMLSST_celf)
 * [UMLSSC:T045](http://purl.obolibrary.org/obo/UMLSSC_T045)
 * [UMLSST:genf](http://purl.obolibrary.org/obo/UMLSST_genf)
 * [UMLSSC:T201](http://purl.obolibrary.org/obo/UMLSSC_T201)
 * [UMLSST:clna](http://purl.obolibrary.org/obo/UMLSST_clna)
## Inheritance

 *  is_a: [BiologicalProcess](BiologicalProcess.md) - One or more causally connected executions of molecular functions
## Children

## Fields

 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [has input](has_input.md) *subsets*: (translator_minimal)
    * Description: holds between a process and a continuant, where the continuant is an input into the process
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Occurrent](Occurrent.md)
 * [has participant](has_participant.md) *subsets*: (translator_minimal)
    * Description: holds between a process and a continuant, where the continuant is somehow involved in the process 
    * range: [NamedThing](NamedThing.md)
    * inherited from: [Occurrent](Occurrent.md)
 * [has phenotype](has_phenotype.md) *subsets*: (translator_minimal)
    * Description: holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). 
    * range: [Phenotype](Phenotype.md)
    * inherited from: [BiologicalEntity](BiologicalEntity.md)
 * [id](id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [iri](iri.md) *subsets*: (translator_minimal)
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [name](name.md) *subsets*: (translator_minimal)
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [node property](node_property.md)
    * Description: A grouping for any property that holds between a node and a value
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * [precedes](precedes.md) *subsets*: (translator_minimal)
    * Description: holds between two processes, where one completes before the other begins
    * range: [Occurrent](Occurrent.md)
    * inherited from: [Occurrent](Occurrent.md)
 * [regulates, process to process](regulates_process_to_process.md) *subsets*: (translator_minimal)
    * Description: describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
    * range: [Occurrent](Occurrent.md)
    * inherited from: [Occurrent](Occurrent.md)
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [synonym](synonym.md) *subsets*: (translator_minimal)
    * Description: Alternate human-readable names for a thing
    * range: [LabelType](LabelType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
