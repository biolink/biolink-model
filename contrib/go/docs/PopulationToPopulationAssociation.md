# Class: population to population association


An association between a two populations

URI: [http://w3id.org/biolink/vocab/PopulationToPopulationAssociation](http://w3id.org/biolink/vocab/PopulationToPopulationAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[PopulationToPopulationAssociation|relation:iri_type;subject_taxon_closure_label(i):label_type%20*;object_taxon_closure_label(i):label_type%20*;has_evidence(i):evidence_instance%20%3F;id(i):identifier_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[PopulationToPopulationAssociation]-%20publications(i)%20*>\[Publication],%20\[PopulationToPopulationAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[PopulationToPopulationAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[PopulationToPopulationAssociation]-%20has%20evidence%20type(i)%20%3F>\[EvidenceType],%20\[PopulationToPopulationAssociation]-%20object%20extensions(i)%20*>\[PropertyValuePair],%20\[PopulationToPopulationAssociation]-%20object%20taxon%20closure(i)%20*>\[OntologyClass],%20\[PopulationToPopulationAssociation]-%20object%20taxon(i)%20%3F>\[OrganismTaxon],%20\[PopulationToPopulationAssociation]-%20subject%20taxon%20closure(i)%20*>\[OntologyClass],%20\[PopulationToPopulationAssociation]-%20subject%20taxon(i)%20%3F>\[OrganismTaxon],%20\[PopulationToPopulationAssociation]-%20object>\[PopulationOfIndividualOrganisms],%20\[PopulationToPopulationAssociation]-%20subject>\[PopulationOfIndividualOrganisms],%20\[Association]^-\[PopulationToPopulationAssociation])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

## Used in

## Fields

 * [population to population association.object](population_to_population_association_object.md)
    * Description: the population that form the object of the association
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) [required]
    * __Local__
 * [population to population association.relation](population_to_population_association_relation.md)
    * Description: A relationship type that holds between the subject and object populations. Standard mereological relations can be used. E.g. subject part-of object, subject overlaps object. Derivation relationships can also be used
    * range: [IriType](IriType.md) [required]
    * __Local__
 * [population to population association.subject](population_to_population_association_subject.md)
    * Description: the population that form the subject of the association
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) [required]
    * __Local__
 * [association slot](association_slot.md)
    * Description: any slot that relates an association to another entity
    * range: **string**
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [association.id](association_id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [Association](Association.md)
 * [has evidence](has_evidence.md)
    * Description: connects an association to an instance of supporting evidence
    * range: [EvidenceInstance](EvidenceInstance.md)
    * inherited from: [ExtensionsAndEvidenceAssociationMixin](ExtensionsAndEvidenceAssociationMixin.md)
 * [has evidence type](has_evidence_type.md)
    * Description: connects an association to the class of evidence used
    * range: [EvidenceType](EvidenceType.md)
    * inherited from: [ExtensionsAndEvidenceAssociationMixin](ExtensionsAndEvidenceAssociationMixin.md)
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * inherited from: [Association](Association.md)
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
