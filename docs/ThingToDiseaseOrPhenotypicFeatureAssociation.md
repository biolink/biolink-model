# Class: thing to disease or phenotypic feature association




URI: [http://bioentity.io/vocab/ThingToDiseaseOrPhenotypicFeatureAssociation](http://bioentity.io/vocab/ThingToDiseaseOrPhenotypicFeatureAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Association]^-\[ThingToDiseaseOrPhenotypicFeatureAssociation|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;subject(i):string;negated(i):boolean%20%3F;association_slot(i):string%20%3F],%20\[ThingToDiseaseOrPhenotypicFeatureAssociation]-%20related%20to(i)%20%3F>\[NamedThing],%20\[ThingToDiseaseOrPhenotypicFeatureAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[ThingToDiseaseOrPhenotypicFeatureAssociation]-%20relation(i)>\[RelationshipType],%20\[ThingToDiseaseOrPhenotypicFeatureAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[ThingToDiseaseOrPhenotypicFeatureAssociation]-%20publications(i)%20*>\[Publication],%20\[ThingToDiseaseOrPhenotypicFeatureAssociation]-%20provided%20by(i)%20%3F>\[Provider],%20\[ThingToDiseaseOrPhenotypicFeatureAssociation]-%20object>\[DiseaseOrPhenotypicFeature])
## Mappings

## Inheritance

 *  is_a: [association](Association.md) - A typed association between two entities, supported by evidence
## Children

 *  mixin: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.md) - An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype
 *  mixin: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md) - An interaction between a chemical entity and a phenotype or disease, where the presence of the chemical gives rise to or exacerbates the phenotype
 *  mixin: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md) - An association between a biosample and a disease or phenotype
## Used in

 *  class: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md) references: [cell line to disease or phenotypic feature association](CellLineToDiseaseOrPhenotypicFeatureAssociation.md)
 *  class: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md) references: [chemical to disease or phenotypic feature association](ChemicalToDiseaseOrPhenotypicFeatureAssociation.md)
 *  class: [thing to disease or phenotypic feature association](ThingToDiseaseOrPhenotypicFeatureAssociation.md) references: [biosample to disease or phenotypic feature association](BiosampleToDiseaseOrPhenotypicFeatureAssociation.md)
## Fields

 * _[object](object.md)_
    * _connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object._
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md) [required]
    * Example: [MONDO:0017314](http://purl.obolibrary.org/obo/MONDO_0017314) Ehlers-Danlos syndrome, vascular type
    * Example: [MP:0013229](http://purl.obolibrary.org/obo/MP_0013229) abnormal brain ventricle size
    * __Local__
 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[association type](association_type.md)_
    * _connects an association to the type of association (e.g. gene to phenotype)_
    * range: [ontology class](OntologyClass.md)
    * inherited from: None
 * _[relation](relation.md)_
    * _the relationship type by which a subject is connected to an object in an association_
    * range: [relationship type](RelationshipType.md) [required]
    * inherited from: None
 * _[qualifiers](qualifiers.md)_
    * _connects an association to qualifiers that modify or qualify the meaning of that association_
    * range: [ontology class](OntologyClass.md)*
    * inherited from: None
 * _[publications](publications.md)_
    * _connects an association to publications supporting the association_
    * range: [publication](Publication.md)*
    * inherited from: None
 * _[provided by](provided_by.md)_
    * _connects an association to the agent (person, organization or group) that provided it_
    * range: [provider](Provider.md)
    * inherited from: None
