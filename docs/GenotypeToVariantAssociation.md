---
layout: default
---

## genotype to variant association


Any association between a genotype and a sequence variant.

URI: [http://bioentity.io/vocab/GenotypeToVariantAssociation](http://bioentity.io/vocab/GenotypeToVariantAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association|association type;subject;negated;relation;object;qualifiers;publications;provided by]^-[genotype to variant association|], [genotype to variant association|]-association type >[ontology class|], [genotype to variant association|]-subject >[genotype|has zygosity], [genomic entity|has biological sequence]^-[genotype|has zygosity], [genotype|has zygosity]-has zygosity >[zygosity|], [attribute|]^-[zygosity|], [genotype|has zygosity]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [genotype to variant association|]-relation >[relationship type|], [genotype to variant association|]-object >[sequence variant|has gene], [genomic entity|has biological sequence]^-[sequence variant|has gene], [sequence variant|has gene]-has gene >[gene|], [gene or gene product|]^-[gene|], [gene|]-in taxon >[organism taxon|], [sequence variant|has gene]-in taxon >[organism taxon|], [genotype to variant association|]-qualifiers >[ontology class|], [genotype to variant association|]-publications >[publication|], [information content entity|]^-[publication|], [genotype to variant association|]-provided by >[provider|], [administrative entity|]^-[provider|])
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
    * _parent genotype_
    * __range__: [genotype](Genotype.html) [required]
    * inherited from: [association](Association.html)
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: xsd:boolean
    * inherited from: [association](Association.html)
 * [relation](relation.html)
    * _the relationship type used to connect genotype to gene_
    * __range__: [relationship type](RelationshipType.html) [required]
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _gene implicated in genotype_
    * __range__: [sequence variant](SequenceVariant.html) [required]
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
