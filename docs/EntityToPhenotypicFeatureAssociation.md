---
layout: default
---

## entity to phenotypic feature association


None

URI: [http://bioentity.io/vocab/EntityToPhenotypicFeatureAssociation](http://bioentity.io/vocab/EntityToPhenotypicFeatureAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[entity to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier], [entity to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier]-frequency qualifier >[frequency value|], [attribute|]^-[frequency value|], [entity to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier]-severity qualifier >[severity value|], [attribute|]^-[severity value|], [entity to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier]-onset qualifier >[onset|], [attribute|]^-[onset|], [entity to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier]-sex qualifier >[biological sex|], [attribute|]^-[biological sex|], [entity to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier]-association type >[ontology class|], [entity to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier]-relation >[relationship type|], [entity to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier]-object >[phenotypic feature|], [disease or phenotypic feature|in taxon]^-[phenotypic feature|], [phenotypic feature|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [entity to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier]-qualifiers >[ontology class|], [entity to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier]-publications >[publication|], [information content entity|]^-[publication|], [entity to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings


## Inheritance

 *  is_a: [association](Association.html)

## Children

 *  mixin: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.html)
 *  mixin: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.html)
 *  mixin: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.html)
 *  mixin: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html)
 *  mixin: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.html)
 *  mixin: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.html)


## Fields

 * [frequency qualifier](frequency_qualifier.html)
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * __range__: [frequency value](FrequencyValue.html)
    * __Local__
 * [severity qualifier](severity_qualifier.html)
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * __range__: [severity value](SeverityValue.html)
    * __Local__
 * [onset qualifier](onset_qualifier.html)
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * __range__: [onset](Onset.html)
    * __Local__
 * [sex qualifier](sex_qualifier.html)
    * _a qualifier used in a phenotypic association to state whether the association is specific to a particular sex._
    * __range__: [biological sex](BiologicalSex.html)
    * __Local__
 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: None [required]
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _the relationship type by which a subject is connected to an object in an association_
    * __range__: [relationship type](RelationshipType.html) [required]
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _phenotypic class_
    * __range__: [phenotypic feature](PhenotypicFeature.html) [required]
    * Example: [HP:0002487](http://purl.obolibrary.org/obo/HP_0002487) Hyperkinesis
    * Example: [WBPhenotype:0000180](http://purl.obolibrary.org/obo/WBPhenotype_0000180) axon morphology variant
    * Example: [MP:0001569](http://purl.obolibrary.org/obo/MP_0001569) abnormal circulating bilirubin level
    * inherited from: [association](Association.html)
 * [qualifiers](qualifiers.html)
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * __range__: [ontology class](OntologyClass.html)*
    * inherited from: [association](Association.html)
 * [publications](publications.html)
    * _connects an association to publications supporting the association_
    * __range__: [publication](Publication.html)*
    * inherited from: [association](Association.html)
 * [provided by](provided_by.html)
    * _connects an association to the agent (person, organization or group) that provided it_
    * __range__: [provider](Provider.html)
    * inherited from: [association](Association.html)
 * [id](id.html)
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
