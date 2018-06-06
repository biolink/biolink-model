# Class: chemical substance


May be a chemical entity or a formulation with a chemical entity as active ingredient, or a complex material with multiple chemical entities as part

URI: [http://bioentity.io/vocab/ChemicalSubstance](http://bioentity.io/vocab/ChemicalSubstance)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[MolecularEntity]^-\[ChemicalSubstance|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):label_type%20%3F;node_property(i):string%20%3F;iri(i):iri_type%20%3F;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F],%20\[ChemicalSubstance]^-\[Drug],%20\[ChemicalSubstance]^-\[Metabolite],%20\[ChemicalSubstance]-%20related%20to(i)%20%3F>\[NamedThing],%20\[ChemicalSubstance]-%20molecularly%20interacts%20with(i)%20%3F>\[MolecularEntity],%20\[ChemicalSubstance]-%20regulates,%20entity%20to%20entity(i)%20%3F>\[MolecularEntity],%20\[ChemicalSubstance]-%20biomarker%20for(i)%20%3F>\[DiseaseOrPhenotypicFeature],%20\[ChemicalSubstance]-%20in%20taxon(i)%20%3F>\[OrganismTaxon])
## Mappings

 * [SIO:010004](http://semanticscience.org/resource/SIO_010004)
 * [UMLSSG:CHEM](http://purl.obolibrary.org/obo/UMLSSG_CHEM)
 * [WD:Q79529](http://purl.obolibrary.org/obo/WD_Q79529)
 * [CHEBI:24431](http://purl.obolibrary.org/obo/CHEBI_24431)
## Inheritance

 *  is_a: [molecular entity](MolecularEntity.md) - A gene, gene product, small molecule or macromolecule (including protein complex)
## Children

 *  child: [drug](Drug.md) - A substance intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease
 *  child: [metabolite](Metabolite.md) - Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
## Used in

 *  class: [chemical substance](ChemicalSubstance.md) references: [drug](Drug.md)
 *  class: [chemical substance](ChemicalSubstance.md) references: [metabolite](Metabolite.md)
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
