---
layout: default
---

## chemical to disease or phenotypic feature association


An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype

URI: [http://bioentity.io/vocab/ChemicalToDiseaseOrPhenotypicFeatureAssociation](http://bioentity.io/vocab/ChemicalToDiseaseOrPhenotypicFeatureAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[chemical to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category], [chemical to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-association type >[ontology class|], [chemical to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-subject >[chemical substance|], [molecular entity|in taxon]^-[chemical substance|], [chemical substance|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [chemical to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-relation >[relationship type|], [chemical to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-object >[disease or phenotypic feature|in taxon], [biological entity|]^-[disease or phenotypic feature|in taxon], [disease or phenotypic feature|in taxon]-in taxon >[organism taxon|], [chemical to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-qualifiers >[ontology class|], [chemical to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-publications >[publication|], [information content entity|]^-[publication|], [chemical to disease or phenotypic feature association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label;category]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings

 * [SIO:000993](http://semanticscience.org/resource/SIO_000993)

## Inheritance

 *  is_a: [association](Association.html)
 *  mixin: [chemical to thing association](ChemicalToThingAssociation.html)
 *  mixin: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _the chemical substance or entity that is an interactor_
    * __range__: [chemical substance](ChemicalSubstance.html) [required]
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
    * _the disease or phenotype that is affected by the chemical_
    * __range__: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.html) [required]
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
