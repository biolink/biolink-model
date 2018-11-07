# Class: molecular event




URI: [http://w3id.org/biolink/vocab/MolecularEvent](http://w3id.org/biolink/vocab/MolecularEvent)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[MolecularEvent|upstream_causal_relationship:string%20%3F;downstream_causal_relationship:string%20%3F]-%20occurs%20in%20%3F>\[NamedThing],%20\[MolecularEvent]-%20part%20of%20%3F>\[NamedThing],%20\[MolecularEvent]-%20enabled%20by%20%3F>\[GeneOrGeneProduct])
## Mappings

## Inheritance

## Children

## Used in

## Fields

 * [downstream causal relationship](downstream_causal_relationship.md)
    * range: **string**
    * __Local__
 * [enabled by](enabled_by.md)
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md)
    * __Local__
 * [occurs in](occurs_in.md) *subsets*: (translator_minimal)
    * Description: holds between a process and a material entity or site within which the process occurs
    * range: [NamedThing](NamedThing.md)
    * __Local__
 * [part of](part_of.md) *subsets*: (translator_minimal)
    * Description: holds between parts and wholes (material entities or processes)
    * range: [NamedThing](NamedThing.md)
    * __Local__
 * [upstream causal relationship](upstream_causal_relationship.md)
    * range: **string**
    * __Local__
