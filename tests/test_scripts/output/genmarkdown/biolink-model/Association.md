# Class: association


A typed association between two entities, supported by evidence

URI: [http://bioentity.io/vocab/Association](http://bioentity.io/vocab/Association)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[InformationContentEntity]^-\[Association|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;subject:string;negated:boolean%20%3F;object:string;association_slot:string%20%3F],%20\[Association]^-\[AnatomicalEntityToAnatomicalEntityAssociation],%20\[Association]^-\[BiosampleToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[BiosampleToThingAssociation],%20\[Association]^-\[CaseToPhenotypicFeatureAssociation],%20\[Association]^-\[CaseToThingAssociation],%20\[Association]^-\[CellLineToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[CellLineToThingAssociation],%20\[Association]^-\[ChemicalToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[ChemicalToGeneAssociation],%20\[Association]^-\[ChemicalToPathwayAssociation],%20\[Association]^-\[ChemicalToThingAssociation],%20\[Association]^-\[DiseaseOrPhenotypicFeatureAssociationToThingAssociation],%20\[Association]^-\[DiseaseToPhenotypicFeatureAssociation],%20\[Association]^-\[DiseaseToThingAssociation],%20\[Association]^-\[EntityToPhenotypicFeatureAssociation],%20\[Association]^-\[EnvironmentToPhenotypicFeatureAssociation],%20\[Association]^-\[FunctionalAssociation],%20\[Association]^-\[GeneRegulatoryRelationship],%20\[Association]^-\[GeneToDiseaseAssociation],%20\[Association]^-\[GeneToExpressionSiteAssociation],%20\[Association]^-\[GeneToGeneAssociation],%20\[Association]^-\[GeneToPhenotypicFeatureAssociation],%20\[Association]^-\[GeneToThingAssociation],%20\[Association]^-\[GenomicSequenceLocalization],%20\[Association]^-\[GenotypeToGeneAssociation],%20\[Association]^-\[GenotypeToGenotypePartAssociation],%20\[Association]^-\[GenotypeToPhenotypicFeatureAssociation],%20\[Association]^-\[GenotypeToThingAssociation],%20\[Association]^-\[GenotypeToVariantAssociation],%20\[Association]^-\[MolecularInteraction],%20\[Association]^-\[PopulationToPopulationAssociation],%20\[Association]^-\[SequenceFeatureRelationship],%20\[Association]^-\[SequenceVariantModulatesTreatmentAssociation],%20\[Association]^-\[ThingToDiseaseOrPhenotypicFeatureAssociation],%20\[Association]^-\[VariantToDiseaseAssociation],%20\[Association]^-\[VariantToPhenotypicFeatureAssociation],%20\[Association]^-\[VariantToPopulationAssociation],%20\[Association]^-\[VariantToThingAssociation],%20\[Association]-%20related%20to(i)%20%3F>\[NamedThing],%20\[Association]-%20association%20type%20%3F>\[OntologyClass],%20\[Association]-%20relation>\[RelationshipType],%20\[Association]-%20qualifiers%20*>\[OntologyClass],%20\[Association]-%20publications%20*>\[Publication],%20\[Association]-%20provided%20by%20%3F>\[Provider])
## Mappings

 * [OBAN:association](http://purl.obolibrary.org/obo/OBAN_association)
 * [rdf:Statement](http://purl.obolibrary.org/obo/rdf_Statement)
 * [owl:Axiom](http://purl.obolibrary.org/obo/owl_Axiom)
## Inheritance

 *  is_a: [information content entity](InformationContentEntity.md) - a piece of information that typically describes some piece of biology or is used as support.
## Children

 *  child: [anatomical entity to anatomical entity association](AnatomicalEntityToAnatomicalEntityAssociation.md)
 *  child: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md) - An association between a biosample and a disease or phenotype
 *  child: [biosample to thing association](BiosampleToThingAssociation.md) - An association between a biosample and something
 *  child: [case to phenotypic feature association](CaseToPhenotypicFeatureAssociation.md) - An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
 *  child: [case to thing association](CaseToThingAssociation.md) - An abstract association for use where the case is the subject
 *  child: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype
 *  child: [cell line to thing association](CellLineToThingAssociation.md) - An relationship between a cell line and another entity
 *  child: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
 *  child: [chemical to gene association](ChemicalToGeneAssociation.md) - An interaction between a chemical entity and a gene or gene product
 *  child: [chemical to pathway association](ChemicalToPathwayAssociation.md) - An interaction between a chemical entity and a biological process or pathway
 *  child: [chemical to thing association](ChemicalToThingAssociation.md) - An interaction between a chemical entity and another entity
 *  child: [disease or phenotypic feature association to thing association](DiseaseOrPhenotypicFeatureAssociationToThingAssociation.md)
 *  child: [disease to phenotypic feature association](DiseaseToPhenotypicFeatureAssociation.md) - An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
 *  child: [disease to thing association](DiseaseToThingAssociation.md)
 *  child: [entity to phenotypic feature association](EntityToPhenotypicFeatureAssociation.md)
 *  child: [environment to phenotypic feature association](EnvironmentToPhenotypicFeatureAssociation.md) - Any association between an environment and a phenotypic feature, where being in the environment influences the phenotype
 *  child: [functional association](FunctionalAssociation.md) - An association between a macromolecular machine (gene, gene product or complex of gene products) and either a molecular activity, a biological process or a cellular location in which a function is executed
 *  child: [gene regulatory relationship](GeneRegulatoryRelationship.md) - A regulatory relationship between two genes
 *  child: [gene to disease association](GeneToDiseaseAssociation.md)
 *  child: [gene to expression site association](GeneToExpressionSiteAssociation.md) - An association between a gene and an expression site, possibly qualified by stage/timing info.
 *  child: [gene to gene association](GeneToGeneAssociation.md) - abstract parent class for different kinds of gene-gene or gene product to gene product relationships. Includes homology and interaction.
 *  child: [gene to phenotypic feature association](GeneToPhenotypicFeatureAssociation.md)
 *  child: [gene to thing association](GeneToThingAssociation.md)
 *  child: [genomic sequence localization](GenomicSequenceLocalization.md) - A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
 *  child: [genotype to gene association](GenotypeToGeneAssociation.md) - Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
 *  child: [genotype to genotype part association](GenotypeToGenotypePartAssociation.md) - Any association between one genotype and a genotypic entity that is a sub-component of it
 *  child: [genotype to phenotypic feature association](GenotypeToPhenotypicFeatureAssociation.md) - Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
 *  child: [genotype to thing association](GenotypeToThingAssociation.md)
 *  child: [genotype to variant association](GenotypeToVariantAssociation.md) - Any association between a genotype and a sequence variant.
 *  child: [molecular interaction](MolecularInteraction.md) - An interaction at the molecular level between two physical entities
 *  child: [population to population association](PopulationToPopulationAssociation.md) - An association between a two populations
 *  child: [sequence feature relationship](SequenceFeatureRelationship.md) - For example, a particular exon is part of a particular transcript or gene
 *  child: [sequence variant modulates treatment association](SequenceVariantModulatesTreatmentAssociation.md) - An association between a sequence variant and a treatment or health intervention. The treatment object itself encompasses both the disease and the drug used.
 *  child: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md)
 *  child: [variant to disease association](VariantToDiseaseAssociation.md)
 *  child: [variant to phenotypic feature association](VariantToPhenotypicFeatureAssociation.md)
 *  child: [variant to population association](VariantToPopulationAssociation.md) - An association between a variant and a population, where the variant has particular frequency in the population
 *  child: [variant to thing association](VariantToThingAssociation.md)
## Used in

## Fields

 * _[association slot](association_slot.md)_
    * _any slot that relates an association to another entity_
    * range: string
    * __Local__
 * _[association type](association_type.md)_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: [ontology class](OntologyClass.md)
    * __Local__
 * _[negated](negated.md)_
    * _if set to true, then the association is negated i.e. is not true_
    * range: boolean
    * __Local__
 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: string [required]
    * __Local__
 * _[provided by](provided_by.md)_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: [provider](Provider.md)
    * __Local__
 * _[publications](publications.md)_
    * _connects an association to publications supporting the association_
    * range: [publication](Publication.md)*
    * __Local__
 * _[qualifiers](qualifiers.md)_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: [ontology class](OntologyClass.md)*
    * __Local__
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * __Local__
 * _[subject](subject.md)_
    * _connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: string [required]
    * __Local__
 * _[category](category.md) *subsets*: (translator_minimal)_
    * _Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[description](description.md) *subsets*: (translator_minimal)_
    * _a human-readable description of a thing_
    * range: [narrative text](NarrativeText.md)
    * inherited from: [named thing](NamedThing.md)
 * _[full name](full_name.md)_
    * _a long-form human readable name for a thing_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[id](id.md) *subsets*: (translator_minimal)_
    * _A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI_
    * range: [identifier type](IdentifierType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[iri](iri.md) *subsets*: (translator_minimal)_
    * _An IRI for the node. This is determined by the id using expansion rules._
    * range: [iri type](IriType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[name](name.md) *subsets*: (translator_minimal)_
    * _A human-readable name for a thing_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
 * _[node property](node_property.md)_
    * _A grouping for any property that holds between a node and a value_
    * range: string
    * inherited from: [named thing](NamedThing.md)
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[systematic synonym](systematic_synonym.md)_
    * _more commonly used for gene symbols in yeast_
    * range: [label type](LabelType.md)
    * inherited from: [named thing](NamedThing.md)
