# Class: chemical substance


May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part

URI: [http://bioentity.io/vocab/ChemicalSubstance](http://bioentity.io/vocab/ChemicalSubstance)

![img](images/ChemicalSubstance.png)
## Mappings

 * [SIO:010004](http://semanticscience.org/resource/SIO_010004)
 * [UMLSSG:CHEM](http://purl.obolibrary.org/obo/UMLSSG_CHEM)
 * [WD:Q79529](http://purl.obolibrary.org/obo/WD_Q79529)
 * [CHEBI:24431](http://purl.obolibrary.org/obo/CHEBI_24431)
## Inheritance

 *  is_a: [molecular entity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)
## Children

 *  child: [metabolite](Metabolite.md) - Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
 *  child: [drug](Drug.md) - A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
## Used in

 *  class: [chemical substance](ChemicalSubstance.md) references: [metabolite](Metabolite.md)
 *  class: [chemical substance](ChemicalSubstance.md) references: [drug](Drug.md)
## Fields

 * _[related to](related_to.md)_
    * _A grouping for any relationship type that holds between any two things_
    * range: [named thing](NamedThing.md)
    * inherited from: [named thing](NamedThing.md)
 * _[molecularly interacts with](molecularly_interacts_with.md) *subsets: translator_minimal*_
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[regulates, entity to entity](regulates_entity_to_entity.md) *subsets: translator_minimal*_
    * range: [molecular entity](MolecularEntity.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[biomarker for](biomarker_for.md) *subsets: translator_minimal*_
    * _holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature._
    * range: [disease or phenotypic feature](DiseaseOrPhenotypicFeature.md)
    * inherited from: [molecular entity](MolecularEntity.md)
 * _[in taxon](in_taxon.md) *subsets: translator_minimal*_
    * _connects a thing to a class representing a taxon_
    * range: [organism taxon](OrganismTaxon.md)
    * inherited from: [thing with taxon](ThingWithTaxon.md)
