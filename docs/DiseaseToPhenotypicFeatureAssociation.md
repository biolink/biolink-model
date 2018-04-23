---
layout: default
---

## disease to phenotypic feature association


An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way

URI: [http://bioentity.io/vocab/DiseaseToPhenotypicFeatureAssociation](http://bioentity.io/vocab/DiseaseToPhenotypicFeatureAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[disease to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category], [disease to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-association type >[ontology class|], [disease to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-subject >[disease|], [disease or phenotypic feature|in taxon]^-[disease|], [disease|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [disease to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-relation >[relationship type|], [disease to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-object >[phenotypic feature|], [disease or phenotypic feature|in taxon]^-[phenotypic feature|], [phenotypic feature|]-in taxon >[organism taxon|], [disease to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-qualifiers >[ontology class|], [disease to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-publications >[publication|], [information content entity|]^-[publication|], [disease to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-provided by >[provider|], [administrative entity|]^-[provider|], [disease to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-frequency qualifier >[frequency value|], [attribute|]^-[frequency value|], [disease to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-severity qualifier >[severity value|], [attribute|]^-[severity value|], [disease to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-onset qualifier >[onset|], [attribute|]^-[onset|], [disease to phenotypic feature association|frequency qualifier;severity qualifier;onset qualifier;sex qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-sex qualifier >[biological sex|], [attribute|]^-[biological sex|])
## Mappings


## Inheritance

 *  is_a: [association](Association.html)
 *  mixin: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html)
 *  mixin: [disease to thing association](DiseaseToThingAssociation.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: [disease](Disease.html) [required]
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
 * [frequency qualifier](frequency_qualifier.html)
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * __range__: [frequency value](FrequencyValue.html)
    * inherited from: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html)
 * [severity qualifier](severity_qualifier.html)
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * __range__: [severity value](SeverityValue.html)
    * inherited from: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html)
 * [onset qualifier](onset_qualifier.html)
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * __range__: [onset](Onset.html)
    * inherited from: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html)
 * [sex qualifier](sex_qualifier.html)
    * _a qualifier used in a phenotypic association to state whether the association is specific to a particular sex._
    * __range__: [biological sex](BiologicalSex.html)
    * inherited from: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html)
