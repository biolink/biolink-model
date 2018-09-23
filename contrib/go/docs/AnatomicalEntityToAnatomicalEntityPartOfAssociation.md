# Class: anatomical entity to anatomical entity part of association


A relationship between two anatomical entities where the relationship is mereological, i.e the two entities are related by parthood. This includes relationships between cellular components and cells, between cells and tissues, tissues and whole organisms

URI: [http://bioentity.io/vocab/AnatomicalEntityToAnatomicalEntityPartOfAssociation](http://bioentity.io/vocab/AnatomicalEntityToAnatomicalEntityPartOfAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[AnatomicalEntityToAnatomicalEntityPartOfAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20*;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;title(i):label_type%20%3F;subject_taxon_closure_label(i):label_type%20*;object_taxon_closure_label(i):label_type%20*;has_evidence(i):evidence_instance%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20publications(i)%20*>\[Publication],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20has%20evidence%20type(i)%20%3F>\[EvidenceType],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20object%20extensions(i)%20*>\[PropertyValuePair],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20object%20taxon%20closure(i)%20*>\[OntologyClass],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20object%20taxon(i)%20%3F>\[OrganismTaxon],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20subject%20taxon%20closure(i)%20*>\[OntologyClass],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20subject%20taxon(i)%20%3F>\[OrganismTaxon],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20relation>\[RelationshipType],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20object>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityPartOfAssociation]-%20subject>\[AnatomicalEntity],%20\[AnatomicalEntityToAnatomicalEntityAssociation]^-\[AnatomicalEntityToAnatomicalEntityPartOfAssociation])
## Mappings

## Inheritance

 *  is_a: [AnatomicalEntityToAnatomicalEntityAssociation](AnatomicalEntityToAnatomicalEntityAssociation.md)
## Children

## Used in

## Fields

 * [anatomical entity to anatomical entity part of association.object](anatomical_entity_to_anatomical_entity_part_of_association_object.md)
    * Description: the whole
    * range: [AnatomicalEntity](AnatomicalEntity.md) [required]
    * __Local__
 * [anatomical entity to anatomical entity part of association.relation](anatomical_entity_to_anatomical_entity_part_of_association_relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [RelationshipType](RelationshipType.md) [required]
    * edge label: [part of](part_of.md) *subsets*: (translator_minimal)
    * __Local__
 * [anatomical entity to anatomical entity part of association.subject](anatomical_entity_to_anatomical_entity_part_of_association_subject.md)
    * Description: the part
    * range: [AnatomicalEntity](AnatomicalEntity.md) [required]
    * __Local__
 * [association slot](association_slot.md)
    * Description: any slot that relates an association to another entity
    * range: **string**
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [LabelType](LabelType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [has evidence](has_evidence.md)
    * Description: connects an association to an instance of supporting evidence
    * range: [EvidenceInstance](EvidenceInstance.md)
    * inherited from: [ExtensionsAndEvidenceAssociationMixin](ExtensionsAndEvidenceAssociationMixin.md)
 * [has evidence type](has_evidence_type.md)
    * Description: connects an association to the class of evidence used
    * range: [EvidenceType](EvidenceType.md)
    * inherited from: [ExtensionsAndEvidenceAssociationMixin](ExtensionsAndEvidenceAssociationMixin.md)
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
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * inherited from: [Association](Association.md)
 * [node property](node_property.md)
    * Description: A grouping for any property that holds between a node and a value
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * [object extensions](object_extensions.md)
    * Description: Additional relationships that are true of the object in the context of the association. For example, if the object is an anatomical term in an expression association, the object extensions may include part-of links
    * range: [PropertyValuePair](PropertyValuePair.md)*
    * inherited from: [ExtensionsAndEvidenceAssociationMixin](ExtensionsAndEvidenceAssociationMixin.md)
 * [object taxon](object_taxon.md)
    * Description: the taxonomic class of the entity in the object slot
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [object taxon closure](object_taxon_closure.md)
    * Description: The taxon class or ancestor class for the object
    * range: [OntologyClass](OntologyClass.md)*
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [object taxon closure label](object_taxon_closure_label.md)
    * Description: The label for the taxon class or ancestor class for the object
    * range: [LabelType](LabelType.md)*
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [object taxon label](object_taxon_label.md)
    * range: label
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [provided by](provided_by.md)
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)*
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)*
    * inherited from: [Association](Association.md)
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [subject taxon](subject_taxon.md)
    * Description: the taxonomic class of the entity in the object slot
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [subject taxon closure](subject_taxon_closure.md)
    * Description: The taxon class or ancestor class for the subject
    * range: [OntologyClass](OntologyClass.md)*
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [subject taxon closure label](subject_taxon_closure_label.md)
    * Description: The label for the taxon class or ancestor class for the subject
    * range: [LabelType](LabelType.md)*
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [subject taxon label](subject_taxon_label.md)
    * range: label
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [title](title.md)
    * Description: Narrative text describing the entity
    * range: [LabelType](LabelType.md)
    * inherited from: [InformationContentEntity](InformationContentEntity.md)
