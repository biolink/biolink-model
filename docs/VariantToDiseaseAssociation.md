---
layout: default
---

## variant to disease association


None

URI: [http://bioentity.io/vocab/VariantToDiseaseAssociation](http://bioentity.io/vocab/VariantToDiseaseAssociation)


![img](http://yuml.me/diagram/nofunky/class/[association]^-[variant to disease association], [variant to disease association]-association type >[ontology class], [variant to disease association]-subject >[sequence variant], [genomic entity]^-[sequence variant], [sequence variant]-has gene >[gene], [gene or gene product]^-[gene], [gene]-in taxon >[organism taxon], [ontology class]^-[organism taxon], [sequence variant]-in taxon >[organism taxon], [variant to disease association]-relation >[relationship type], [variant to disease association]-object >[disease], [disease or phenotypic feature]^-[disease], [disease]-in taxon >[organism taxon], [variant to disease association]-qualifiers >[ontology class], [variant to disease association]-publications >[publication], [information content entity]^-[publication], [variant to disease association]-provided by >[provider], [administrative entity]^-[provider], [variant to disease association]-frequency qualifier >[frequency value], [attribute]^-[frequency value], [variant to disease association]-severity qualifier >[severity value], [attribute]^-[severity value], [variant to disease association]-onset qualifier >[onset], [attribute]^-[onset])
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
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
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
