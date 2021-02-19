---
parent: Associations
title: biolink:FunctionalAssociation
grand_parent: Classes
layout: default
---

# Class: FunctionalAssociation


An association between a macromolecular machine mixin (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed.

URI: [biolink:FunctionalAssociation](https://w3id.org/biolink/vocab/FunctionalAssociation)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[OntologyClass],[MacromolecularMachineToMolecularActivityAssociation],[MacromolecularMachineToCellularComponentAssociation],[MacromolecularMachineToBiologicalProcessAssociation],[MacromolecularMachineMixin],[GeneToGoTermAssociation],[GeneOntologyClass],[GeneOntologyClass]%3Cobject%201..1-++[FunctionalAssociation%7Cpredicate(i):predicate_type;relation(i):uriorcurie;negated(i):boolean%20%3F;type(i):string%20%3F;category(i):category_type%20%2A;id(i):string;iri(i):iri_type%20%3F;name(i):label_type%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[MacromolecularMachineMixin]%3Csubject%201..1-++[FunctionalAssociation],[FunctionalAssociation]%5E-[MacromolecularMachineToMolecularActivityAssociation],[FunctionalAssociation]%5E-[MacromolecularMachineToCellularComponentAssociation],[FunctionalAssociation]%5E-[MacromolecularMachineToBiologicalProcessAssociation],[FunctionalAssociation]%5E-[GeneToGoTermAssociation],[Association]%5E-[FunctionalAssociation],[Attribute],[Association],[Agent])

---


## Parents

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence

## Children

 * [GeneToGoTermAssociation](GeneToGoTermAssociation.md)
 * [MacromolecularMachineToBiologicalProcessAssociation](MacromolecularMachineToBiologicalProcessAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it.
 * [MacromolecularMachineToCellularComponentAssociation](MacromolecularMachineToCellularComponentAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a cellular component (as represented in the GO cellular component branch), where the entity carries out its function in the cellular component.
 * [MacromolecularMachineToMolecularActivityAssociation](MacromolecularMachineToMolecularActivityAssociation.md) - A functional association between a macromolecular machine (gene, gene product or complex) and a molecular activity (as represented in the GO molecular function branch), where the entity carries out the activity, or contributes to its execution.

## Referenced by class


## Attributes


### Own

 * [functional association➞object](functional_association_object.md)  <sub>REQ</sub>
    * Description: class describing the activity, process or localization of the gene product
    * range: [GeneOntologyClass](GeneOntologyClass.md)
    * Example:    
    * Example:    
 * [functional association➞subject](functional_association_subject.md)  <sub>REQ</sub>
    * Description: gene, product or macromolecular complex mixin that has the function associated with the GO term
    * range: [MacromolecularMachineMixin](MacromolecularMachineMixin.md)
    * Example:    

### Inherited from association:

 * [subject](subject.md)  <sub>REQ</sub>
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [predicate](predicate.md)  <sub>REQ</sub>
    * Description: A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
    * range: [PredicateType](types/PredicateType.md)
 * [object](object.md)  <sub>REQ</sub>
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [NamedThing](NamedThing.md)
 * [relation](relation.md)  <sub>REQ</sub>
    * Description: The relation which describes an association between a subject and an object in a more granular manner. Usually this is a term from Relation Ontology, but it can be any edge CURIE.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [negated](negated.md)  <sub>OPT</sub>
    * Description: if set to true, then the association is negated i.e. is not true
    * range: [Boolean](types/Boolean.md)
 * [qualifiers](qualifiers.md)  <sub>0..*</sub>
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)
 * [publications](publications.md)  <sub>0..*</sub>
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)
 * [association➞type](association_type.md)  <sub>OPT</sub>
    * Description: rdf:type of biolink:Association should be fixed at rdf:Statement
    * range: [String](types/String.md)
 * [association➞category](association_category.md)  <sub>0..*</sub>
    * range: [CategoryType](types/CategoryType.md)

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

### Domain for slot:

 * [functional association➞object](functional_association_object.md)  <sub>REQ</sub>
    * Description: class describing the activity, process or localization of the gene product
    * range: [GeneOntologyClass](GeneOntologyClass.md)
    * Example:    
    * Example:    
 * [functional association➞subject](functional_association_subject.md)  <sub>REQ</sub>
    * Description: gene, product or macromolecular complex mixin that has the function associated with the GO term
    * range: [MacromolecularMachineMixin](MacromolecularMachineMixin.md)
    * Example:    
