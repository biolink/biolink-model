---
layout: default
---

## sequence variant modulates treatment association


An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.

URI: [http://bioentity.io/vocab/SequenceVariantModulatesTreatmentAssociation](http://bioentity.io/vocab/SequenceVariantModulatesTreatmentAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[sequence variant modulates treatment association|], [sequence variant modulates treatment association|]-association type >[ontology class|], [sequence variant modulates treatment association|]-subject >[sequence variant|has gene], [genomic entity|has biological sequence]^-[sequence variant|has gene], [sequence variant|has gene]-has gene >[gene|], [gene or gene product|]^-[gene|], [gene|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [sequence variant|has gene]-in taxon >[organism taxon|], [sequence variant modulates treatment association|]-relation >[relationship type|], [sequence variant modulates treatment association|]-object >[treatment|treats;has exposure parts], [environment|]^-[treatment|treats;has exposure parts], [treatment|treats;has exposure parts]-treats >[disease or phenotypic feature|in taxon], [biological entity|]^-[disease or phenotypic feature|in taxon], [disease or phenotypic feature|in taxon]-in taxon >[organism taxon|], [treatment|treats;has exposure parts]-has exposure parts >[drug exposure|], [environment|]^-[drug exposure|], [sequence variant modulates treatment association|]-qualifiers >[ontology class|], [sequence variant modulates treatment association|]-publications >[publication|], [information content entity|]^-[publication|], [sequence variant modulates treatment association|]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings


## Inheritance

 *  is_a: [association](Association.html)

## Children



## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _variant that modulates the treatment of some disease_
    * __range__: [sequence variant](SequenceVariant.html) [required]
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
    * _treatment whose efficacy is modulated by the subject variant_
    * __range__: [treatment](Treatment.html) [required]
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
