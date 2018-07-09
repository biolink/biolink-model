# Class: taxon closure mixin


An association that includes flattened inlined objects, such as subject_taxon_closure

URI: [http://bioentity.io/vocab/TaxonClosureMixin](http://bioentity.io/vocab/TaxonClosureMixin)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[TaxonClosureMixin|subject_taxon_closure_label:string%20*;object_taxon_closure_label:string%20*]-%20object%20taxon%20closure%20*>\[OntologyClass],%20\[TaxonClosureMixin]-%20object%20taxon%20%3F>\[OrganismTaxon],%20\[TaxonClosureMixin]-%20subject%20taxon%20closure%20*>\[OntologyClass],%20\[TaxonClosureMixin]-%20subject%20taxon%20%3F>\[OrganismTaxon],%20\[ExtensionsAndEvidenceAssociationMixin]uses%20-.->\[TaxonClosureMixin])
## Mappings

## Inheritance

## Children

 * [ExtensionsAndEvidenceAssociationMixin](ExtensionsAndEvidenceAssociationMixin.md) (mixin)  - An injected mixing that adds additional fields to association objects. This is a mixture of (a) closures for denormalization (b) evidence fields specific to the GO model.
## Used in

## Fields

 * _[object taxon](object_taxon.md)_
    * _the taxonomic class of the entity in the object slot_
    * range: [OrganismTaxon](OrganismTaxon.md)
    * __Local__
 * _[object taxon closure](object_taxon_closure.md)_
    * _The taxon class or ancestor class for the object_
    * range: [OntologyClass](OntologyClass.md)*
    * __Local__
 * _[object taxon closure label](object_taxon_closure_label.md)_
    * _The label for the taxon class or ancestor class for the object_
    * range: **string***
    * __Local__
 * _[object taxon label](object_taxon_label.md)_
    * range: label
    * __Local__
 * _[subject taxon](subject_taxon.md)_
    * _the taxonomic class of the entity in the object slot_
    * range: [OrganismTaxon](OrganismTaxon.md)
    * __Local__
 * _[subject taxon closure](subject_taxon_closure.md)_
    * _The taxon class or ancestor class for the subject_
    * range: [OntologyClass](OntologyClass.md)*
    * __Local__
 * _[subject taxon closure label](subject_taxon_closure_label.md)_
    * _The label for the taxon class or ancestor class for the subject_
    * range: **string***
    * __Local__
 * _[subject taxon label](subject_taxon_label.md)_
    * range: label
    * __Local__
