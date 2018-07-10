# Class: extensions and evidence association mixin


An injected mixing that adds additional fields to association objects. This is a mixture of (a) closures for denormalization (b) evidence fields specific to the GO model.

URI: [http://bioentity.io/vocab/ExtensionsAndEvidenceAssociationMixin](http://bioentity.io/vocab/ExtensionsAndEvidenceAssociationMixin)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ExtensionsAndEvidenceAssociationMixin|has_evidence:evidence_instance%20%3F;subject:string;subject_taxon_closure_label(i):string%20*;object_taxon_closure_label(i):string%20*]-%20object%20taxon%20closure(i)%20*>\[OntologyClass],%20\[ExtensionsAndEvidenceAssociationMixin]-%20object%20taxon(i)%20%3F>\[OrganismTaxon],%20\[ExtensionsAndEvidenceAssociationMixin]-%20subject%20taxon%20closure(i)%20*>\[OntologyClass],%20\[ExtensionsAndEvidenceAssociationMixin]-%20subject%20taxon(i)%20%3F>\[OrganismTaxon],%20\[ExtensionsAndEvidenceAssociationMixin]-%20has%20evidence%20type%20%3F>\[EvidenceType],%20\[ExtensionsAndEvidenceAssociationMixin]-%20object%20extensions%20*>\[PropertyValuePair],%20\[ExtensionsAndEvidenceAssociationMixin]uses%20-.->\[TaxonClosureMixin],%20\[Association]uses%20-.->\[ExtensionsAndEvidenceAssociationMixin])
## Mappings

## Inheritance

 *  mixin: [TaxonClosureMixin](TaxonClosureMixin.md) - An association that includes flattened inlined objects, such as subject_taxon_closure
## Children

 * [Association](Association.md) (mixin)  - A typed association between two entities, supported by evidence
## Used in

## Fields

 * [extensions and evidence association mixin.subject](extensions_and_evidence_association_mixin_subject.md)
    * Description: connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: **string** [required]
    * __Local__
 * [has evidence](has_evidence.md)
    * Description: connects an association to an instance of supporting evidence
    * range: [EvidenceInstance](EvidenceInstance.md)
    * __Local__
 * [has evidence type](has_evidence_type.md)
    * Description: connects an association to the class of evidence used
    * range: [EvidenceType](EvidenceType.md)
    * __Local__
 * [object extensions](object_extensions.md)
    * Description: Additional relationships that are true of the object in the context of the association. For example, if the object is an anatomical term in an expression association, the object extensions may include part-of links
    * range: [PropertyValuePair](PropertyValuePair.md)*
    * __Local__
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
    * range: **string***
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [object taxon label](object_taxon_label.md)
    * range: label
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
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
    * range: **string***
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [subject taxon label](subject_taxon_label.md)
    * range: label
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
