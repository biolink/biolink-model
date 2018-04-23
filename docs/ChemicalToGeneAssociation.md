---
layout: default
---

## chemical to gene association


An interaction between a chemical entity and a gene or gene product

URI: [http://bioentity.io/vocab/ChemicalToGeneAssociation](http://bioentity.io/vocab/ChemicalToGeneAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[chemical to gene association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label], [chemical to gene association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label]-association type >[ontology class|], [chemical to gene association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label]-subject >[chemical substance|], [molecular entity|in taxon]^-[chemical substance|], [chemical substance|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [chemical to gene association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label]-relation >[relationship type|], [chemical to gene association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label]-object >[gene or gene product|], [genomic entity|has biological sequence]^-[gene or gene product|], [gene or gene product|]-in taxon >[organism taxon|], [chemical to gene association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label]-qualifiers >[ontology class|], [chemical to gene association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label]-publications >[publication|], [information content entity|]^-[publication|], [chemical to gene association|association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label]-provided by >[provider|], [administrative entity|]^-[provider|])
## Mappings

 * [SIO:001257](http://semanticscience.org/resource/SIO_001257)

## Inheritance

 *  is_a: [association](Association.html)
 *  mixin: [chemical to thing association](ChemicalToThingAssociation.html)

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
    * _the gene or gene product that is affected by the chemical_
    * __range__: [gene or gene product](GeneOrGeneProduct.html) [required]
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
