# Class: chemical to thing association


An interaction between a chemical entity and another entity

URI: [http://w3id.org/biolink/vocab/ChemicalToThingAssociation](http://w3id.org/biolink/vocab/ChemicalToThingAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ChemicalToThingAssociation|subject_taxon_closure_label(i):label_type%20*;object_taxon_closure_label(i):label_type%20*;has_evidence(i):evidence_instance%20%3F;id(i):identifier_type%20%3F;object(i):string;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[ChemicalToThingAssociation]-%20publications(i)%20*>\[Publication],%20\[ChemicalToThingAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[ChemicalToThingAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[ChemicalToThingAssociation]-%20relation(i)>\[RelationshipType],%20\[ChemicalToThingAssociation]-%20has%20evidence%20type(i)%20%3F>\[EvidenceType],%20\[ChemicalToThingAssociation]-%20object%20extensions(i)%20*>\[PropertyValuePair],%20\[ChemicalToThingAssociation]-%20object%20taxon%20closure(i)%20*>\[OntologyClass],%20\[ChemicalToThingAssociation]-%20object%20taxon(i)%20%3F>\[OrganismTaxon],%20\[ChemicalToThingAssociation]-%20subject%20taxon%20closure(i)%20*>\[OntologyClass],%20\[ChemicalToThingAssociation]-%20subject%20taxon(i)%20%3F>\[OrganismTaxon],%20\[ChemicalToThingAssociation]-%20subject>\[ChemicalSubstance],%20\[ChemicalToPathwayAssociation]uses%20-.->\[ChemicalToThingAssociation],%20\[ChemicalToGeneAssociation]uses%20-.->\[ChemicalToThingAssociation],%20\[ChemicalToDiseaseOrPhenotypicFeatureAssociation]uses%20-.->\[ChemicalToThingAssociation],%20\[Association]^-\[ChemicalToThingAssociation])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

 * [ChemicalToDiseaseOrPhenotypicFeatureAssociation](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) (mixin)  - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
 * [ChemicalToGeneAssociation](ChemicalToGeneAssociation.md) (mixin)  - An interaction between a chemical entity and a gene or gene product
 * [ChemicalToPathwayAssociation](ChemicalToPathwayAssociation.md) (mixin)  - An interaction between a chemical entity and a biological process or pathway
## Used in

## Fields

 * [chemical to thing association.subject](chemical_to_thing_association_subject.md)
    * Description: the chemical substance or entity that is an interactor
    * range: [ChemicalSubstance](ChemicalSubstance.md) [required]
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
 * [object](object.md)
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: **string** [required]
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
 * [relation](relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [RelationshipType](RelationshipType.md) [required]
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
