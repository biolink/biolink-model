---
layout: default
---

## association


A typed association between two entities, supported by evidence

URI: [http://bioentity.io/vocab/Association](http://bioentity.io/vocab/Association)
## Mappings

 * [OBAN:association](http://purl.obolibrary.org/obo/OBAN_association)
 * [rdf:Statement](http://purl.obolibrary.org/obo/rdf_Statement)
 * [owl:Axiom](http://purl.obolibrary.org/obo/owl_Axiom)

## Inheritance

 *  is_a: [information content entity](InformationContentEntity.html)

## Children

 *  child: [genotype to genotype part association](GenotypeToGenotypePartAssociation.html)
 *  child: [genotype to gene association](GenotypeToGeneAssociation.html)
 *  child: [genotype to variant association](GenotypeToVariantAssociation.html)
 *  child: [gene to gene association](GeneToGeneAssociation.html)
 *  child: [molecular interaction](MolecularInteraction.html)
 *  child: [chemical to thing association](ChemicalToThingAssociation.html)
 *  child: [case to thing association](CaseToThingAssociation.html)
 *  child: [chemical to gene association](ChemicalToGeneAssociation.html)
 *  child: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.html)
 *  child: [chemical to pathway association](ChemicalToPathwayAssociation.html)
 *  child: [chemical to gene association](ChemicalToGeneAssociation.html)
 *  child: [biosample to thing association](BiosampleToThingAssociation.html)
 *  child: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.html)
 *  child: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.html)
 *  child: [entity to disease association](EntityToDiseaseAssociation.html)
 *  child: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.html)
 *  child: [disease to thing association](DiseaseToThingAssociation.html)
 *  child: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.html)
 *  child: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.html)
 *  child: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.html)
 *  child: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.html)
 *  child: [gene to thing association](GeneToThingAssociation.html)
 *  child: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.html)
 *  child: [gene to disease association](GeneToDiseaseAssociation.html)
 *  child: [genotype to thing association](GenotypeToThingAssociation.html)
 *  child: [gene to expression site association](GeneToExpressionSiteAssociation.html)
 *  child: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.html)
 *  child: [gene to go term association](GeneToGoTermAssociation.html)
 *  child: [genomic sequence localization](GenomicSequenceLocalization.html)
 *  child: [sequence feature relationship](SequenceFeatureRelationship.html)
 *  child: [sequence feature to sequence relationship](SequenceFeatureToSequenceRelationship.html)
 *  child: [gene regulatory relationship](GeneRegulatoryRelationship.html)
 *  child: [molecular activity to gene product association](MolecularActivityToGeneProductAssociation.html)
 *  child: [molecular activity to location association](MolecularActivityToLocationAssociation.html)
 *  child: [molecular activity to biological process association](MolecularActivityToBiologicalProcessAssociation.html)
 *  child: [molecular activity to downstream molecular activity association](MolecularActivityToDownstreamMolecularActivityAssociation.html)
 *  child: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.html)

## Used in

 *  class: [association result set](AssociationResultSet.html) references: [association](Association.html)

## Fields

 * [association type](association_type.html)
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * __range__: [ontology class](OntologyClass.html)
    * __Local__
 * [subject](subject.html)
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: None [required]
    * __Local__
 * [negated](negated.html)
    * _if set to true, then the association is negated i.e. is not true_
    * __range__: boolean
    * __Local__
 * [relation](relation.html)
    * _the relationship type by which a subject is connected to an object in an association_
    * __range__: [relationship type](RelationshipType.html) [required]
    * __Local__
 * [object](object.html)
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * __range__: None [required]
    * __Local__
 * [qualifiers](qualifiers.html)
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * __range__: [ontology class](OntologyClass.html)*
    * __Local__
 * [publications](publications.html)
    * _connects an association to publications supporting the association_
    * __range__: [publication](Publication.html)*
    * __Local__
 * [provided by](provided_by.html)
    * _connects an association to the agent (person, organization or group) that provided it_
    * __range__: [provider](Provider.html)
    * __Local__
 * [id](id.html)
    * __range__: identifier type [required]
    * inherited from: [named thing](NamedThing.html)
 * [label](label.html)
    * _A human-readable name for a thing_
    * __range__: label type
    * inherited from: [named thing](NamedThing.html)
