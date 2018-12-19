# Class: variant to thing association




URI: [http://w3id.org/biolink/vocab/VariantToThingAssociation](http://w3id.org/biolink/vocab/VariantToThingAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[VariantToThingAssociation|id(i):identifier_type%20%3F;relation(i):iri_type;object(i):iri_type;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[VariantToThingAssociation]-%20publications(i)%20*>\[Publication],%20\[VariantToThingAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[VariantToThingAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[VariantToThingAssociation]-%20subject>\[SequenceVariant],%20\[VariantToPopulationAssociation]uses%20-.->\[VariantToThingAssociation],%20\[VariantToPhenotypicFeatureAssociation]uses%20-.->\[VariantToThingAssociation],%20\[VariantToDiseaseAssociation]uses%20-.->\[VariantToThingAssociation],%20\[Association]^-\[VariantToThingAssociation])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

 * [VariantToDiseaseAssociation](VariantToDiseaseAssociation.md) (mixin) 
 * [VariantToPhenotypicFeatureAssociation](VariantToPhenotypicFeatureAssociation.md) (mixin) 
 * [VariantToPopulationAssociation](VariantToPopulationAssociation.md) (mixin)  - An association between a variant and a population, where the variant has particular frequency in the population
## Used in

## Fields

 * [variant to thing association.subject](variant_to_thing_association_subject.md)
    * Description: a sequence variant in which the allele state is associated with some other entity
    * range: [SequenceVariant](SequenceVariant.md) [required]
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
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * inherited from: [Association](Association.md)
 * [object](object.md)
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [IriType](IriType.md) [required]
    * inherited from: [Association](Association.md)
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
    * range: [IriType](IriType.md) [required]
    * inherited from: [Association](Association.md)
