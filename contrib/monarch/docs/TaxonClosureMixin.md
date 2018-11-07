# Class: taxon closure mixin


An association that includes flattened inlined objects, such as subject_taxon_closure

URI: [http://w3id.org/biolink/vocab/TaxonClosureMixin](http://w3id.org/biolink/vocab/TaxonClosureMixin)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[TaxonClosureMixin|subject_taxon_closure_label:label_type%20*;object_taxon_closure_label:label_type%20*]-%20object%20taxon%20closure%20*>\[OntologyClass],%20\[TaxonClosureMixin]-%20object%20taxon%20%3F>\[OrganismTaxon],%20\[TaxonClosureMixin]-%20subject%20taxon%20closure%20*>\[OntologyClass],%20\[TaxonClosureMixin]-%20subject%20taxon%20%3F>\[OrganismTaxon],%20\[ExtensionsAndEvidenceAssociationMixin]uses%20-.->\[TaxonClosureMixin])
## Mappings

## Inheritance

## Children

 * [ExtensionsAndEvidenceAssociationMixin](ExtensionsAndEvidenceAssociationMixin.md) (mixin)  - An injected mixing that adds additional fields to association objects. This is a mixture of (a) closures for denormalization (b) evidence fields specific to the monarch model.
## Used in

## Fields

 * [object taxon](object_taxon.md)
    * Description: the taxonomic class of the entity in the object slot
    * range: [OrganismTaxon](OrganismTaxon.md)
    * __Local__
 * [object taxon closure](object_taxon_closure.md)
    * Description: The taxon class or ancestor class for the object
    * range: [OntologyClass](OntologyClass.md)*
    * __Local__
 * [object taxon closure label](object_taxon_closure_label.md)
    * Description: The label for the taxon class or ancestor class for the object
    * range: [LabelType](LabelType.md)*
    * __Local__
 * [object taxon label](object_taxon_label.md)
    * range: label
    * __Local__
 * [subject taxon](subject_taxon.md)
    * Description: the taxonomic class of the entity in the object slot
    * range: [OrganismTaxon](OrganismTaxon.md)
    * __Local__
 * [subject taxon closure](subject_taxon_closure.md)
    * Description: The taxon class or ancestor class for the subject
    * range: [OntologyClass](OntologyClass.md)*
    * __Local__
 * [subject taxon closure label](subject_taxon_closure_label.md)
    * Description: The label for the taxon class or ancestor class for the subject
    * range: [LabelType](LabelType.md)*
    * __Local__
 * [subject taxon label](subject_taxon_label.md)
    * range: label
    * __Local__
