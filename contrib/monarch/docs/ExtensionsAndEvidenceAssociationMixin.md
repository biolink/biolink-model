---
layout: default
---

## extensions and evidence association mixin


An injected mixing that adds additional fields to association objects. This is a mixture of (a) closures for denormalization (b) evidence fields specific to the monarch model.

URI: [http://bioentity.io/vocab/ExtensionsAndEvidenceAssociationMixin](http://bioentity.io/vocab/ExtensionsAndEvidenceAssociationMixin)
## Mappings


## Inheritance

 *  mixin: [taxon closure mixin](TaxonClosureMixin.html)

## Children

 *  mixin: [association](Association.html)

## Used in

 *  class: [association result set](AssociationResultSet.html) references: [association](Association.html)
 *  class: [association result set](AssociationResultSet.html) references: [association](Association.html)

## Fields

 * [subject extensions](subject_extensions.html)
    * _Additional relationships that are true of the subject in the context of the association. For example, if the subject is a gene product in a functional association, the subject extensions may represent  an isoform or a specific post-translational state_
    * __range__: [property value pair](PropertyValuePair.html)*
    * __Local__
 * [object extensions](object_extensions.html)
    * _Additional relationships that are true of the object in the context of the association. For example, if the object is an anatomical term in an expression association, the object extensions may include part-of links_
    * __range__: [property value pair](PropertyValuePair.html)*
    * __Local__
 * [has evidence graph](has_evidence_graph.html)
    * _connects an association to a graph object including a path from subject to object_
    * __range__: evidence graph
    * __Local__
 * [has evidence type](has_evidence_type.html)
    * _connects an association to the class of evidence used_
    * __range__: [evidence type](EvidenceType.html)
    * __Local__
 * [has evidence](has_evidence.html)
    * _connects an association to an instance of supporting evidence_
    * __range__: evidence instance
    * __Local__
 * [subject taxon](subject_taxon.html)
    * _the taxonomic class of the entity in the object slot_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [taxon closure mixin](TaxonClosureMixin.html)
 * [subject taxon label](subject_taxon_label.html)
    * __range__: label
    * inherited from: [taxon closure mixin](TaxonClosureMixin.html)
 * [subject taxon closure](subject_taxon_closure.html)
    * _The taxon class or ancestor class for the subject_
    * __range__: [ontology class](OntologyClass.html)*
    * inherited from: [taxon closure mixin](TaxonClosureMixin.html)
 * [subject taxon closure label](subject_taxon_closure_label.html)
    * _The label for the taxon class or ancestor class for the subject_
    * __range__: label type*
    * inherited from: [taxon closure mixin](TaxonClosureMixin.html)
 * [object taxon](object_taxon.html)
    * _the taxonomic class of the entity in the object slot_
    * __range__: [organism taxon](OrganismTaxon.html)
    * inherited from: [taxon closure mixin](TaxonClosureMixin.html)
 * [object taxon label](object_taxon_label.html)
    * __range__: label
    * inherited from: [taxon closure mixin](TaxonClosureMixin.html)
 * [object taxon closure](object_taxon_closure.html)
    * _The taxon class or ancestor class for the object_
    * __range__: [ontology class](OntologyClass.html)*
    * inherited from: [taxon closure mixin](TaxonClosureMixin.html)
 * [object taxon closure label](object_taxon_closure_label.html)
    * _The label for the taxon class or ancestor class for the object_
    * __range__: label type*
    * inherited from: [taxon closure mixin](TaxonClosureMixin.html)
