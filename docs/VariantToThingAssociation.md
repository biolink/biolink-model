# Class: variant to thing association




URI: [http://bioentity.io/vocab/VariantToThingAssociation](http://bioentity.io/vocab/VariantToThingAssociation)

![img](images/VariantToThingAssociation.png)
## Mappings

## Inheritance

 *  is_a: [association](Association.md) - A typed association between two entities, supported by evidence
## Children

 *  mixin: [variant to disease association](VariantToDiseaseAssociation.md)
 *  mixin: [variant to population association](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population
 *  mixin: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
## Used in

 *  class: [variant to thing association](VariantToThingAssociation.md) references: [variant to disease association](VariantToDiseaseAssociation.md)
 *  class: [variant to thing association](VariantToThingAssociation.md) references: [variant to population association](VariantToPopulationAssociation.md)
 *  class: [variant to thing association](VariantToThingAssociation.md) references: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
## Fields

 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [sequence variant](SequenceVariant.md) [required]
    * Example: [ClinVar:38077](http://purl.obolibrary.org/obo/ClinVar_38077) ClinVar representation of NM_000059.3(BRCA2):c.7007G>A (p.Arg2336His)
    * Example: [ClinGen:CA024716](http://purl.obolibrary.org/obo/ClinGen_CA024716) chr13:g.32921033G>C (hg19) in ClinGen
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[association type](association_type.md)_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: [ontology class](OntologyClass.md)
    * inherited from: None
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * inherited from: None
 * _[qualifiers](qualifiers.md)_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: [ontology class](OntologyClass.md)*
    * inherited from: None
 * _[publications](publications.md)_
    * _connects an association to publications supporting the association_
    * range: [publication](Publication.md)*
    * inherited from: None
 * _[provided by](provided_by.md)_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: [provider](Provider.md)
    * inherited from: None
