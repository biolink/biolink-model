---
layout: default
---

## association result set


None

URI: [http://bioentity.io/vocab/AssociationResultSet](http://bioentity.io/vocab/AssociationResultSet)


![img](http://yuml.me/diagram/nofunky/class/[information content entity]^-[association result set], [association result set]-associations >[association], [information content entity]^-[association], [association]-association type >[ontology class], [association]-relation >[relationship type], [association]-qualifiers >[ontology class], [association]-publications >[publication], [information content entity]^-[publication], [association]-provided by >[provider], [administrative entity]^-[provider])
## Mappings


## Inheritance

 *  is_a: [information content entity](InformationContentEntity.html)

## Children



## Fields

 * [associations](associations.html)
    * __range__: [association](Association.html)*
    * __Local__
 * [id](id.html)
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
