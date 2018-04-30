---
layout: default
---

## variant to disease association


None

URI: [http://bioentity.io/vocab/VariantToDiseaseAssociation](http://bioentity.io/vocab/VariantToDiseaseAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[variant to disease association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;frequency qualifier;severity qualifier;onset qualifier], [variant to disease association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;frequency qualifier;severity qualifier;onset qualifier]-association type >[ontology class|], [variant to disease association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;frequency qualifier;severity qualifier;onset qualifier]-subject >[sequence variant|has gene], [genomic entity|has biological sequence]^-[sequence variant|has gene], [sequence variant|has gene]-has gene >[gene|], [gene or gene product|]^-[gene|], [gene|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [sequence variant|has gene]-in taxon >[organism taxon|], [variant to disease association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;frequency qualifier;severity qualifier;onset qualifier]-relation >[relationship type|], [variant to disease association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;frequency qualifier;severity qualifier;onset qualifier]-object >[disease|], [disease or phenotypic feature|in taxon]^-[disease|], [disease|]-in taxon >[organism taxon|], [variant to disease association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;frequency qualifier;severity qualifier;onset qualifier]-qualifiers >[ontology class|], [variant to disease association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;frequency qualifier;severity qualifier;onset qualifier]-publications >[publication|], [information content entity|]^-[publication|], [variant to disease association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;frequency qualifier;severity qualifier;onset qualifier]-provided by >[provider|], [administrative entity|]^-[provider|], [variant to disease association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;frequency qualifier;severity qualifier;onset qualifier]-frequency qualifier >[frequency value|], [attribute|]^-[frequency value|], [variant to disease association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;frequency qualifier;severity qualifier;onset qualifier]-severity qualifier >[severity value|], [attribute|]^-[severity value|], [variant to disease association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;name;category;frequency qualifier;severity qualifier;onset qualifier]-onset qualifier >[onset|], [attribute|]^-[onset|])
## Mappings


## Inheritance

 *  is_a: [association](Association.html)
 *  mixin: [variant to thing association](VariantToThingAssociation.html)
 *  mixin: [entity to disease association](EntityToDiseaseAssociation.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _a sequence variant in which the allele state is associated in some way with the disease state_
    * __range__: [sequence variant](SequenceVariant.html) [required]
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _E.g. is pathogenic for_
    * __range__: [relationship type](RelationshipType.html) [required]
    * subproperty_of: [GENO:0000790](http://purl.obolibrary.org/obo/GENO_0000790)
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _a disease that is associated with that variant_
    * __range__: [disease](Disease.html) [required]
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
    * __range__: identifier type [required]
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
