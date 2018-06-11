# Class: functional association


An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed

URI: [http://bioentity.io/vocab/FunctionalAssociation](http://bioentity.io/vocab/FunctionalAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[FunctionalAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[FunctionalAssociation]-%20publications(i)%20*>\[Publication],%20\[FunctionalAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[FunctionalAssociation]-%20relation(i)>\[RelationshipType],%20\[FunctionalAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[FunctionalAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[FunctionalAssociation]-%20object>\[GeneOntologyClass],%20\[FunctionalAssociation]-%20subject>\[MacromolecularMachine],%20\[FunctionalAssociation]^-\[MacromolecularMachineToMolecularActivityAssociation],%20\[FunctionalAssociation]^-\[MacromolecularMachineToCellularComponentAssociation],%20\[FunctionalAssociation]^-\[MacromolecularMachineToBiologicalProcessAssociation],%20\[FunctionalAssociation]^-\[GeneToGoTermAssociation],%20\[Association]^-\[FunctionalAssociation])
## Mappings

## Inheritance

 *  is_a: association
## Children

 * gene to go term association
 * macromolecular machine to biological process association
 * macromolecular machine to cellular component association
 * macromolecular machine to molecular activity association
## Used in

## Fields

 * _functional association object_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: gene ontology class [required]
    * Example: [GO:0016301](http://purl.obolibrary.org/obo/GO_0016301) kinase activity
    * Example: [GO:0045211](http://purl.obolibrary.org/obo/GO_0045211) postsynaptic membrane
    * __Local__
 * _functional association subject_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: macromolecular machine [required]
    * Example: [ZFIN:ZDB-GENE-050417-357](http://purl.obolibrary.org/obo/ZFIN_ZDB-GENE-050417-357) twist1b
    * __Local__
 * _association slot_
    * _any slot that relates an association to another entity_
    * range: **string**
    * inherited from: association
 * _association type_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: ontology class
    * inherited from: association
 * _category_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: label type
    * inherited from: named thing
 * _description_
    * _a human-readable description of a thing_
    * range: narrative text
    * inherited from: named thing
 * _full name_
    * _a long-form human readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _id_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: identifier type
    * inherited from: named thing
 * _iri_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: iri type
    * inherited from: named thing
 * _name_
    * _A human-readable name for a thing_
    * range: label type
    * inherited from: named thing
 * _negated_
    * _if set to true, then the association is negated i.e. is not true_
    * range: **boolean**
    * inherited from: association
 * _node property_
    * _A grouping for any property that holds between a node and a value_
    * range: **string**
    * inherited from: named thing
 * _provided by_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: provider
    * inherited from: association
 * _publications_
    * _connects an association to publications supporting the association_
    * range: publication*
    * inherited from: association
 * _qualifiers_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: ontology class*
    * inherited from: association
 * _related to_
    * _A grouping for any relationship type that holds between any two things_
    * range: named thing
    * inherited from: named thing
 * _relation_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: relationship type [required]
    * inherited from: association
 * _systematic synonym_
    * _more commonly used for gene symbols in yeast_
    * range: label type
    * inherited from: named thing
