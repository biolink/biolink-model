---
layout: default
---

## gene to disease association


None

URI: [http://bioentity.io/vocab/GeneToDiseaseAssociation](http://bioentity.io/vocab/GeneToDiseaseAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[gene to disease association|frequency qualifier;severity qualifier;onset qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category], [gene to disease association|frequency qualifier;severity qualifier;onset qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-association type >[ontology class|], [gene to disease association|frequency qualifier;severity qualifier;onset qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-subject >[gene or gene product|], [genomic entity|has biological sequence]^-[gene or gene product|], [gene or gene product|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [gene to disease association|frequency qualifier;severity qualifier;onset qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-relation >[relationship type|], [gene to disease association|frequency qualifier;severity qualifier;onset qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-object >[disease|], [disease or phenotypic feature|in taxon]^-[disease|], [disease|]-in taxon >[organism taxon|], [gene to disease association|frequency qualifier;severity qualifier;onset qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-qualifiers >[ontology class|], [gene to disease association|frequency qualifier;severity qualifier;onset qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-publications >[publication|], [information content entity|]^-[publication|], [gene to disease association|frequency qualifier;severity qualifier;onset qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-provided by >[provider|], [administrative entity|]^-[provider|], [gene to disease association|frequency qualifier;severity qualifier;onset qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-frequency qualifier >[frequency value|], [attribute|]^-[frequency value|], [gene to disease association|frequency qualifier;severity qualifier;onset qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-severity qualifier >[severity value|], [attribute|]^-[severity value|], [gene to disease association|frequency qualifier;severity qualifier;onset qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category]-onset qualifier >[onset|], [attribute|]^-[onset|])
## Mappings

 * [SIO:000983](http://semanticscience.org/resource/SIO_000983)

## Inheritance

 *  is_a: [association](Association.html)
 *  mixin: [entity to disease association](EntityToDiseaseAssociation.html)
 *  mixin: [gene to thing association](GeneToThingAssociation.html)

## Children

 *  child: [gene as a model of disease association](GeneAsAModelOfDiseaseAssociation.html)
 *  child: [gene has variant that contributes to disease association](GeneHasVariantThatContributesToDiseaseAssociation.html)


## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _gene in which variation is correlated with the disease - may be protective or causative or associative, or as a model_
    * __range__: [gene or gene product](GeneOrGeneProduct.html) [required]
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
    * _disease_
    * __range__: [disease](Disease.html) [required]
    * Example: [MONDO:0020066](http://purl.obolibrary.org/obo/MONDO_0020066) Ehlers-Danlos syndrome
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
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * __range__: identifier type
    * inherited from: [named thing](NamedThing.html)
 * [name](name.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [category](category.html)
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
 * [frequency qualifier](frequency_qualifier.html)
    * _a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject_
    * __range__: [frequency value](FrequencyValue.html)
    * inherited from: [entity to disease association](EntityToDiseaseAssociation.html)
 * [severity qualifier](severity_qualifier.html)
    * _a qualifier used in a phenotypic association to state how severe the phenotype is in the subject_
    * __range__: [severity value](SeverityValue.html)
    * inherited from: [entity to disease association](EntityToDiseaseAssociation.html)
 * [onset qualifier](onset_qualifier.html)
    * _a qualifier used in a phenotypic association to state when the phenotype appears is in the subject_
    * __range__: [onset](Onset.html)
    * inherited from: [entity to disease association](EntityToDiseaseAssociation.html)
