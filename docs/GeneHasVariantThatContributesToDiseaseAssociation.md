---
layout: default
---

## gene has variant that contributes to disease association


None

URI: [http://bioentity.io/vocab/GeneHasVariantThatContributesToDiseaseAssociation](http://bioentity.io/vocab/GeneHasVariantThatContributesToDiseaseAssociation)


![img](http://yuml.me/diagram/nofunky/class/[gene to disease association|frequency qualifier;severity qualifier;onset qualifier;association type;subject;negated;relation;object;qualifiers;publications;provided by;id;label]^-[gene has variant that contributes to disease association|sequence variant qualifier], [gene has variant that contributes to disease association|sequence variant qualifier]-sequence variant qualifier >[sequence variant|has gene], [genomic entity|has biological sequence]^-[sequence variant|has gene], [sequence variant|has gene]-has gene >[gene|], [gene or gene product|]^-[gene|], [gene|]-in taxon >[organism taxon|], [ontology class|]^-[organism taxon|], [sequence variant|has gene]-in taxon >[organism taxon|], [gene has variant that contributes to disease association|sequence variant qualifier]-association type >[ontology class|], [gene has variant that contributes to disease association|sequence variant qualifier]-subject >[gene or gene product|], [genomic entity|has biological sequence]^-[gene or gene product|], [gene or gene product|]-in taxon >[organism taxon|], [gene has variant that contributes to disease association|sequence variant qualifier]-relation >[relationship type|], [gene has variant that contributes to disease association|sequence variant qualifier]-object >[disease|], [disease or phenotypic feature|in taxon]^-[disease|], [disease|]-in taxon >[organism taxon|], [gene has variant that contributes to disease association|sequence variant qualifier]-qualifiers >[ontology class|], [gene has variant that contributes to disease association|sequence variant qualifier]-publications >[publication|], [information content entity|]^-[publication|], [gene has variant that contributes to disease association|sequence variant qualifier]-provided by >[provider|], [administrative entity|]^-[provider|], [gene has variant that contributes to disease association|sequence variant qualifier]-frequency qualifier >[frequency value|], [attribute|]^-[frequency value|], [gene has variant that contributes to disease association|sequence variant qualifier]-severity qualifier >[severity value|], [attribute|]^-[severity value|], [gene has variant that contributes to disease association|sequence variant qualifier]-onset qualifier >[onset|], [attribute|]^-[onset|])
## Mappings


## Inheritance

 *  is_a: [gene to disease association](GeneToDiseaseAssociation.html)

## Children



## Fields

 * [sequence variant qualifier](sequence_variant_qualifier.html)
    * _a qualifier used in an association where the variant_
    * __range__: [sequence variant](SequenceVariant.html)
    * __Local__
 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * inherited from: [association](Association.html)
 * [subject](subject.html)
    * _A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease._
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
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
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
    * __range__: identifier type
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
