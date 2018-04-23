---
layout: default
---

## association result set


None

URI: [http://bioentity.io/vocab/AssociationResultSet](http://bioentity.io/vocab/AssociationResultSet)


![img](http://yuml.me/diagram/nofunky/class/[information content entity|]^-[association result set|associations], [association result set|associations]-associations >[association|association type;subject;negated;relation;object;qualifiers;publications;provided by], [information content entity|]^-[association|association type;subject;negated;relation;object;qualifiers;publications;provided by], [association|association type;subject;negated;relation;object;qualifiers;publications;provided by]-association type >[ontology class|], [association|association type;subject;negated;relation;object;qualifiers;publications;provided by]-relation >[relationship type|], [association|association type;subject;negated;relation;object;qualifiers;publications;provided by]-qualifiers >[ontology class|], [association|association type;subject;negated;relation;object;qualifiers;publications;provided by]-publications >[publication|], [information content entity|]^-[publication|], [association|association type;subject;negated;relation;object;qualifiers;publications;provided by]-provided by >[provider|], [administrative entity|]^-[provider|])
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
