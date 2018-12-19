# Class: gene to gene homology association


A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)

URI: [http://w3id.org/biolink/vocab/GeneToGeneHomologyAssociation](http://w3id.org/biolink/vocab/GeneToGeneHomologyAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneToGeneHomologyAssociation|relation:iri_type;subject_taxon_closure_label(i):label_type%20*;object_taxon_closure_label(i):label_type%20*;has_evidence(i):evidence_instance%20%3F;id(i):identifier_type%20%3F;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20object(i)>\[GeneOrGeneProduct],%20\[GeneToGeneHomologyAssociation]-%20subject(i)>\[GeneOrGeneProduct],%20\[GeneToGeneHomologyAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[GeneToGeneHomologyAssociation]-%20publications(i)%20*>\[Publication],%20\[GeneToGeneHomologyAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GeneToGeneHomologyAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GeneToGeneHomologyAssociation]-%20has%20evidence%20type(i)%20%3F>\[EvidenceType],%20\[GeneToGeneHomologyAssociation]-%20object%20extensions(i)%20*>\[PropertyValuePair],%20\[GeneToGeneHomologyAssociation]-%20object%20taxon%20closure(i)%20*>\[OntologyClass],%20\[GeneToGeneHomologyAssociation]-%20object%20taxon(i)%20%3F>\[OrganismTaxon],%20\[GeneToGeneHomologyAssociation]-%20subject%20taxon%20closure(i)%20*>\[OntologyClass],%20\[GeneToGeneHomologyAssociation]-%20subject%20taxon(i)%20%3F>\[OrganismTaxon],%20\[GeneToGeneAssociation]^-\[GeneToGeneHomologyAssociation])
## Mappings

## Inheritance

 *  is_a: [GeneToGeneAssociation](GeneToGeneAssociation.md) - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
## Children

## Used in

## Fields

 * [gene to gene homology association.relation](gene_to_gene_homology_association_relation.md)
    * Description: homology relationship type
    * range: [IriType](IriType.md) [required]
    * edge label: [homologous to](homologous_to.md) *subsets*: (translator_minimal)
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
 * [gene to gene association.object](gene_to_gene_association_object.md)
    * Description: the object gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as proxy for the gene or vice versa
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md) [required]
    * inherited from: [GeneToGeneAssociation](GeneToGeneAssociation.md)
 * [gene to gene association.subject](gene_to_gene_association_subject.md)
    * Description: the subject gene in the association. If the relation is symmetric, subject vs object is arbitrary. We allow a gene product to stand as proxy for the gene or vice versa
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md) [required]
    * inherited from: [GeneToGeneAssociation](GeneToGeneAssociation.md)
 * [has evidence](has_evidence.md)
    * Description: connects an association to an instance of supporting evidence
    * range: [EvidenceInstance](EvidenceInstance.md)
    * inherited from: [ExtensionsAndEvidenceAssociationMixin](ExtensionsAndEvidenceAssociationMixin.md)
 * [has evidence type](has_evidence_type.md)
    * Description: connects an association to the class of evidence used
    * range: [EvidenceType](EvidenceType.md)
    * inherited from: [ExtensionsAndEvidenceAssociationMixin](ExtensionsAndEvidenceAssociationMixin.md)
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
