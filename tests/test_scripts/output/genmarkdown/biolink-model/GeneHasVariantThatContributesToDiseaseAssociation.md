# Class: gene has variant that contributes to disease association




URI: [http://w3id.org/biolink/vocab/GeneHasVariantThatContributesToDiseaseAssociation](http://w3id.org/biolink/vocab/GeneHasVariantThatContributesToDiseaseAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneHasVariantThatContributesToDiseaseAssociation|id(i):identifier_type%20%3F;relation(i):iri_type;object(i):iri_type;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20onset%20qualifier(i)%20%3F>\[Onset],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20severity%20qualifier(i)%20%3F>\[SeverityValue],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20publications(i)%20*>\[Publication],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20subject>\[GeneOrGeneProduct],%20\[GeneHasVariantThatContributesToDiseaseAssociation]-%20sequence%20variant%20qualifier%20%3F>\[SequenceVariant],%20\[GeneToDiseaseAssociation]^-\[GeneHasVariantThatContributesToDiseaseAssociation])
## Mappings

## Inheritance

 *  is_a: [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md)
## Children

## Used in

## Fields

 * [gene has variant that contributes to disease association.subject](gene_has_variant_that_contributes_to_disease_association_subject.md)
    * Description: A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md) [required]
    * __Local__
 * [sequence variant qualifier](sequence_variant_qualifier.md)
    * Description: a qualifier used in an association where the variant
    * range: [SequenceVariant](SequenceVariant.md)
    * __Local__
 * [association slot](association_slot.md)
    * Description: any slot that relates an association to another entity
    * range: **string**
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [association.id](association_id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [Association](Association.md)
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * inherited from: [Association](Association.md)
 * [object](object.md)
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: [IriType](IriType.md) [required]
    * inherited from: [Association](Association.md)
 * [onset qualifier](onset_qualifier.md)
    * Description: a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
    * range: [Onset](Onset.md)
    * inherited from: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md)
 * [provided by](provided_by.md)
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)*
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)*
    * inherited from: [Association](Association.md)
 * [relation](relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [IriType](IriType.md) [required]
    * inherited from: [Association](Association.md)
 * [severity qualifier](severity_qualifier.md)
    * Description: a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
    * range: [SeverityValue](SeverityValue.md)
    * inherited from: [EntityToFeatureOrDiseaseQualifiers](EntityToFeatureOrDiseaseQualifiers.md)
