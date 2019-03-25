# Class: individual organism




URI: [http://w3id.org/biolink/vocab/IndividualOrganism](http://w3id.org/biolink/vocab/IndividualOrganism)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[IndividualOrganism|id(i):identifier_type%20%3F;name(i):label_type%20%3F;category(i):iri_type%20*;node_property(i):string%20%3F;iri(i):iri_type%20%3F;synonym(i):label_type%20*;full_name(i):label_type%20%3F;description(i):narrative_text%20%3F;systematic_synonym(i):label_type%20%3F;has_phenotype(i):phenotype%20%3F]-%20related%20to(i)%20%3F>\[NamedThing],%20\[IndividualOrganism]-%20in%20taxon(i)%20%3F>\[OrganismTaxon],%20\[IndividualOrganism]uses%20-.->\[ThingWithTaxon],%20\[IndividualOrganism]^-\[Case],%20\[OrganismalEntity]^-\[IndividualOrganism])
## Mappings

 * [SIO:010000](http://semanticscience.org/resource/SIO_010000)
 * [WD:Q795052](http://purl.obolibrary.org/obo/WD_Q795052)
 * [UMLSSG:LIVB](http://purl.obolibrary.org/obo/UMLSSG_LIVB)
 * [UMLSSC:T001](http://purl.obolibrary.org/obo/UMLSSC_T001)
 * [UMLSST:orgm](http://purl.obolibrary.org/obo/UMLSST_orgm)
 * [UMLSSC:T002](http://purl.obolibrary.org/obo/UMLSSC_T002)
 * [UMLSST:plnt](http://purl.obolibrary.org/obo/UMLSST_plnt)
 * [UMLSSC:T004](http://purl.obolibrary.org/obo/UMLSSC_T004)
 * [UMLSST:fngs](http://purl.obolibrary.org/obo/UMLSST_fngs)
 * [UMLSSC:T005](http://purl.obolibrary.org/obo/UMLSSC_T005)
 * [UMLSST:virs](http://purl.obolibrary.org/obo/UMLSST_virs)
 * [UMLSSC:T007](http://purl.obolibrary.org/obo/UMLSSC_T007)
 * [UMLSST:bact](http://purl.obolibrary.org/obo/UMLSST_bact)
 * [UMLSSC:T008](http://purl.obolibrary.org/obo/UMLSSC_T008)
 * [UMLSST:anim](http://purl.obolibrary.org/obo/UMLSST_anim)
 * [UMLSSC:T010](http://purl.obolibrary.org/obo/UMLSSC_T010)
 * [UMLSST:vtbt](http://purl.obolibrary.org/obo/UMLSST_vtbt)
 * [UMLSSC:T011](http://purl.obolibrary.org/obo/UMLSSC_T011)
 * [UMLSST:amph](http://purl.obolibrary.org/obo/UMLSST_amph)
 * [UMLSSC:T012](http://purl.obolibrary.org/obo/UMLSSC_T012)
 * [UMLSST:bird](http://purl.obolibrary.org/obo/UMLSST_bird)
 * [UMLSSC:T013](http://purl.obolibrary.org/obo/UMLSSC_T013)
 * [UMLSST:fish](http://purl.obolibrary.org/obo/UMLSST_fish)
 * [UMLSSC:T014](http://purl.obolibrary.org/obo/UMLSSC_T014)
 * [UMLSST:rept](http://purl.obolibrary.org/obo/UMLSST_rept)
 * [UMLSSC:T015](http://purl.obolibrary.org/obo/UMLSSC_T015)
 * [UMLSST:mamm](http://purl.obolibrary.org/obo/UMLSST_mamm)
 * [UMLSSC:T016](http://purl.obolibrary.org/obo/UMLSSC_T016)
 * [UMLSST:humn](http://purl.obolibrary.org/obo/UMLSST_humn)
 * [UMLSSC:T096](http://purl.obolibrary.org/obo/UMLSSC_T096)
 * [UMLSST:grup](http://purl.obolibrary.org/obo/UMLSST_grup)
 * [UMLSSC:T097](http://purl.obolibrary.org/obo/UMLSSC_T097)
 * [UMLSST:prog](http://purl.obolibrary.org/obo/UMLSST_prog)
 * [UMLSSC:T099](http://purl.obolibrary.org/obo/UMLSSC_T099)
 * [UMLSST:famg](http://purl.obolibrary.org/obo/UMLSST_famg)
 * [UMLSSC:T100](http://purl.obolibrary.org/obo/UMLSSC_T100)
 * [UMLSST:aggp](http://purl.obolibrary.org/obo/UMLSST_aggp)
 * [UMLSSC:T101](http://purl.obolibrary.org/obo/UMLSSC_T101)
 * [UMLSST:podg](http://purl.obolibrary.org/obo/UMLSST_podg)
 * [UMLSSC:T194](http://purl.obolibrary.org/obo/UMLSSC_T194)
 * [UMLSST:arch](http://purl.obolibrary.org/obo/UMLSST_arch)
 * [UMLSSC:T204](http://purl.obolibrary.org/obo/UMLSSC_T204)
 * [UMLSST:euka](http://purl.obolibrary.org/obo/UMLSST_euka)
 * [NCBITaxon:1](http://purl.obolibrary.org/obo/NCBITaxon_1)
## Inheritance

 *  is_a: [OrganismalEntity](OrganismalEntity.md) - A named entity that is either a part of an organism, a whole organism, population or clade of organisms, excluding molecular entities
 *  mixin: [ThingWithTaxon](ThingWithTaxon.md) - A mixin that can be used on any entity with a taxon
## Children

 * [Case](Case.md) - An individual organism that has a patient role in some clinical context.
## Used in

## Fields

 * [category](category.md) *subsets*: (translator_minimal)
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md) *subsets*: (translator_minimal)
    * Description: a human-readable description of a thing
    * range: [NarrativeText](NarrativeText.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [full name](full_name.md)
    * Description: a long-form human readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [has phenotype](has_phenotype.md) *subsets*: (translator_minimal)
    * Description: holds between a biological entity and a phenotype, where a phenotype is construed broadly as any kind of quality of an organism part, a collection of these qualities, or a change in quality or qualities (e.g. abnormally increased temperature). 
    * range: [Phenotype](Phenotype.md)
    * inherited from: [BiologicalEntity](BiologicalEntity.md)
 * [id](id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [in taxon](in_taxon.md) *subsets*: (translator_minimal)
    * Description: connects a thing to a class representing a taxon
    * range: [OrganismTaxon](OrganismTaxon.md)
    * inherited from: [ThingWithTaxon](ThingWithTaxon.md)
 * [iri](iri.md) *subsets*: (translator_minimal)
    * Description: An IRI for the node. This is determined by the id using expansion rules.
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [name](name.md) *subsets*: (translator_minimal)
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [node property](node_property.md)
    * Description: A grouping for any property that holds between a node and a value
    * range: **string**
    * inherited from: [NamedThing](NamedThing.md)
 * [related to](related_to.md)
    * Description: A grouping for any relationship type that holds between any two things
    * range: [NamedThing](NamedThing.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [synonym](synonym.md) *subsets*: (translator_minimal)
    * Description: Alternate human-readable names for a thing
    * range: [LabelType](LabelType.md)*
    * inherited from: [NamedThing](NamedThing.md)
 * [systematic synonym](systematic_synonym.md)
    * Description: more commonly used for gene symbols in yeast
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
