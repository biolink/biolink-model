# Class: variant to population association


An association between a variant and a population, where the variant has particular frequency in the population

URI: [http://w3id.org/biolink/vocab/VariantToPopulationAssociation](http://w3id.org/biolink/vocab/VariantToPopulationAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[VariantToPopulationAssociation|has_quotient:double%20%3F;has_count:integer%20%3F;has_total:integer%20%3F;subject_taxon_closure_label(i):label_type%20*;object_taxon_closure_label(i):label_type%20*;has_evidence(i):evidence_instance%20%3F;id(i):identifier_type%20%3F;relation(i):iri_type;negated(i):boolean%20%3F;association_slot(i):string%20%3F;has_percentage(i):double%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[VariantToPopulationAssociation]-%20publications(i)%20*>\[Publication],%20\[VariantToPopulationAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[VariantToPopulationAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[VariantToPopulationAssociation]-%20has%20evidence%20type(i)%20%3F>\[EvidenceType],%20\[VariantToPopulationAssociation]-%20object%20extensions(i)%20*>\[PropertyValuePair],%20\[VariantToPopulationAssociation]-%20object%20taxon%20closure(i)%20*>\[OntologyClass],%20\[VariantToPopulationAssociation]-%20object%20taxon(i)%20%3F>\[OrganismTaxon],%20\[VariantToPopulationAssociation]-%20subject%20taxon%20closure(i)%20*>\[OntologyClass],%20\[VariantToPopulationAssociation]-%20subject%20taxon(i)%20%3F>\[OrganismTaxon],%20\[VariantToPopulationAssociation]-%20object>\[PopulationOfIndividualOrganisms],%20\[VariantToPopulationAssociation]-%20subject>\[SequenceVariant],%20\[VariantToPopulationAssociation]uses%20-.->\[VariantToThingAssociation],%20\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQuantifier],%20\[VariantToPopulationAssociation]uses%20-.->\[FrequencyQualifier],%20\[Association]^-\[VariantToPopulationAssociation])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
 *  mixin: [VariantToThingAssociation](VariantToThingAssociation.md)
 *  mixin: [FrequencyQuantifier](FrequencyQuantifier.md)
 *  mixin: [FrequencyQualifier](FrequencyQualifier.md) - Qualifier for freqency type associations
## Children

## Used in

## Fields

 * [variant to population association.has count](variant_to_population_association_has_count.md)
    * Description: number in object population that carry a particular allele, aka allele count
    * range: **integer**
    * __Local__
 * [variant to population association.has quotient](variant_to_population_association_has_quotient.md)
    * Description: frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency
    * range: **double**
    * __Local__
 * [variant to population association.has total](variant_to_population_association_has_total.md)
    * Description: number all populations that carry a particular allele, aka allele number
    * range: **integer**
    * __Local__
 * [variant to population association.object](variant_to_population_association_object.md)
    * Description: the population that is observed to have the frequency
    * range: [PopulationOfIndividualOrganisms](PopulationOfIndividualOrganisms.md) [required]
    * __Local__
 * [variant to population association.subject](variant_to_population_association_subject.md)
    * Description: an allele that has a certain frequency in a given population
    * range: [SequenceVariant](SequenceVariant.md) [required]
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
 * [has evidence](has_evidence.md)
    * Description: connects an association to an instance of supporting evidence
    * range: [EvidenceInstance](EvidenceInstance.md)
    * inherited from: [ExtensionsAndEvidenceAssociationMixin](ExtensionsAndEvidenceAssociationMixin.md)
 * [has evidence type](has_evidence_type.md)
    * Description: connects an association to the class of evidence used
    * range: [EvidenceType](EvidenceType.md)
    * inherited from: [ExtensionsAndEvidenceAssociationMixin](ExtensionsAndEvidenceAssociationMixin.md)
 * [has percentage](has_percentage.md)
    * Description: equivalent to has quotient multiplied by 100
    * range: **double**
    * inherited from: [FrequencyQuantifier](FrequencyQuantifier.md)
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * inherited from: [Association](Association.md)
 * [object extensions](object_extensions.md)
    * Description: Additional relationships that are true of the object in the context of the association. For example, if the object is an anatomical term in an expression association, the object extensions may include part-of links
    * range: [PropertyValuePair](PropertyValuePair.md)*
    * inherited from: [ExtensionsAndEvidenceAssociationMixin](ExtensionsAndEvidenceAssociationMixin.md)
 * [object taxon](object_taxon.md)
    * Description: the taxonomic class of the entity in the object slot
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [object taxon closure](object_taxon_closure.md)
    * Description: The taxon class or ancestor class for the object
    * range: [OntologyClass](OntologyClass.md)*
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [object taxon closure label](object_taxon_closure_label.md)
    * Description: The label for the taxon class or ancestor class for the object
    * range: [LabelType](LabelType.md)*
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [object taxon label](object_taxon_label.md)
    * range: label
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
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
 * [subject taxon](subject_taxon.md)
    * Description: the taxonomic class of the entity in the object slot
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [subject taxon closure](subject_taxon_closure.md)
    * Description: The taxon class or ancestor class for the subject
    * range: [OntologyClass](OntologyClass.md)*
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [subject taxon closure label](subject_taxon_closure_label.md)
    * Description: The label for the taxon class or ancestor class for the subject
    * range: [LabelType](LabelType.md)*
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
 * [subject taxon label](subject_taxon_label.md)
    * range: label
    * inherited from: [TaxonClosureMixin](TaxonClosureMixin.md)
