---
layout: default
---

## genotype to genotype part association


Any association between one genotype and a genotypic entity that is a sub-component of it

URI: [http://bioentity.io/vocab/GenotypeToGenotypePartAssociation](http://bioentity.io/vocab/GenotypeToGenotypePartAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association]^-[genotype to genotype part association], [genotype to genotype part association]-association type >[ontology class], [genotype to genotype part association]-subject >[genotype], [genomic entity]^-[genotype], [genotype]-has zygosity >[zygosity], [attribute]^-[zygosity], [genotype]-in taxon >[organism taxon], [ontology class]^-[organism taxon], [genotype to genotype part association]-relation >[relationship type], [genotype to genotype part association]-object >[genotype], [genotype to genotype part association]-qualifiers >[ontology class], [genotype to genotype part association]-publications >[publication], [information content entity]^-[publication], [genotype to genotype part association]-provided by >[provider], [administrative entity]^-[provider])
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
    * _the relationship type by which a subject is connected to an object in an association_
    * __range__: [relationship type](RelationshipType.html) [required]
    * subproperty_of: [GENO:0000382](http://purl.obolibrary.org/obo/GENO_0000382)
    * inherited from: [association](Association.html)
 * [object](object.html)
    * _child genotype_
    * __range__: [genotype](Genotype.html) [required]
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
