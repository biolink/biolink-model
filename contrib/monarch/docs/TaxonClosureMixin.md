---
layout: default
---

## taxon closure mixin


An association that includes flattened inlined objects, such as subject_taxon_closure

URI: [http://bioentity.io/vocab/TaxonClosureMixin](http://bioentity.io/vocab/TaxonClosureMixin)
## Mappings


## Inheritance


## Children

 *  mixin: [extensions and evidence association mixin](ExtensionsAndEvidenceAssociationMixin.html)

## Used in

 *  class: [association result set](AssociationResultSet.html) references: [association](Association.html)
 *  class: [association result set](AssociationResultSet.html) references: [association](Association.html)

## Fields

 * [subject taxon](subject_taxon.html)
    * _the taxonomic class of the entity in the object slot_
    * __range__: [organism taxon](OrganismTaxon.html)
    * __Local__
 * [subject taxon label](subject_taxon_label.html)
    * __range__: label
    * __Local__
 * [subject taxon closure](subject_taxon_closure.html)
    * _The taxon class or ancestor class for the subject_
    * __range__: [ontology class](OntologyClass.html)*
    * __Local__
 * [subject taxon closure label](subject_taxon_closure_label.html)
    * _The label for the taxon class or ancestor class for the subject_
    * __range__: label*
    * __Local__
 * [object taxon](object_taxon.html)
    * _the taxonomic class of the entity in the object slot_
    * __range__: [organism taxon](OrganismTaxon.html)
    * __Local__
 * [object taxon label](object_taxon_label.html)
    * __range__: label
    * __Local__
 * [object taxon closure](object_taxon_closure.html)
    * _The taxon class or ancestor class for the object_
    * __range__: [ontology class](OntologyClass.html)*
    * __Local__
 * [object taxon closure label](object_taxon_closure_label.html)
    * _The label for the taxon class or ancestor class for the object_
    * __range__: [ontology class](OntologyClass.html)*
    * __Local__
