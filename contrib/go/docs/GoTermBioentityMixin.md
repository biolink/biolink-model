# Class: go term bioentity mixin


mixes in GO properties to bio-entities

URI: [http://w3id.org/biolink/vocab/GoTermBioentityMixin](http://w3id.org/biolink/vocab/GoTermBioentityMixin)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GoTermBioentityMixin|isa_partof_closure_label:label_type%20*;regulates_closure_label:label_type%20*;full_name(i):label_type%20%3F;systematic_synonym(i):label_type%20%3F]-%20regulates%20closure%20*>\[RelationshipType],%20\[GoTermBioentityMixin]-%20isa%20partof%20closure%20*>\[OntologyClass],%20\[GoTermBioentityMixin]uses%20-.->\[HasGenomicName],%20\[MolecularEntity]uses%20-.->\[GoTermBioentityMixin])
## Mappings

## Inheritance

 *  mixin: [HasGenomicName](HasGenomicName.md) - mixing class for any entity that has a full name and a systematic synonym
## Children

 * [MolecularEntity](MolecularEntity.md) (mixin)  - A gene, gene product, small molecule or macromolecule (including protein complex)
## Used in

## Fields

 * [isa partof closure](isa_partof_closure.md)
    * Description: Ancestors (reflexive) of the object field following is_a (subClassOf) and part-of links. This is typically used as a query constraint and for faceting. The combination of is_a and part of is a common pattern, and can be used in gene expression queries (finding genes that are expressed in a structure, a subtype, or a part of that structure) or in GO queries (in any of the three branches of GO)
    * range: [OntologyClass](OntologyClass.md)*
    * __Local__
 * [isa partof closure label](isa_partof_closure_label.md)
    * Description: parent field for fields used for storing the label of the closure concept. See also: closure concept field
    * range: [LabelType](LabelType.md)*
    * __Local__
 * [regulates closure](regulates_closure.md)
    * Description: Ancestors (reflexive) of the object field following is_a (subClassOf), part-of and regulates (including positive and negative) relationships. This is typically used as a query constraint and for faceting where the range is a biological process
    * range: [RelationshipType](RelationshipType.md)*
    * __Local__
 * [regulates closure label](regulates_closure_label.md)
    * Description: parent field for fields used for storing the label of the closure concept. See also: closure concept field
    * range: [LabelType](LabelType.md)*
    * __Local__
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
