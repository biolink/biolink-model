# Class: knowledge graph


A collection of knowledge elements definitions

URI: [http://w3id.org/biolink/vocab/KnowledgeGraph](http://w3id.org/biolink/vocab/KnowledgeGraph)

![img](images/KnowledgeGraph.png)
## Mappings

## Inheritance

## Children

## Used in

## Fields

 * [default_curi_maps](default_curi_maps.md)
    * Description: List of prefixcommon biocontexts to be fetched to resolve id_prefixes and inline prefix variables
    * range: **string***
    * __Local__
 * [default_prefix](default_prefix.md)
    * Description: default and base prefix -- used for ':' identifiers, @base and @vocab
    * range: **string**
    * __Local__
 * [entities](entities.md)
    * Description: the collection of nodes (vertices) that represent entities or concepts
    * range: [NamedThing](NamedThing.md)*
    * __Local__
 * [generation_date](generation_date.md)
    * Description: date that the knowledge graph was loaded/generated.  Supplied by the loader
    * range: **date**
    * __Local__
 * [knowledge graph.id](kg_id.md)
    * Description: a globally unique identifier for a knowledge graph
    * range: **string**
    * __Local__
 * [kg_source](kg_source.md)
    * Description: name, uri or description of the source of the knowledge source.  Supplied by the loader
    * range: **string**
    * __Local__
 * [kg_source_version](kg_source_version.md)
    * Description: version identifier of the knowledge graph.  Supplied by the loader
    * range: **integer**
    * __Local__
 * [kg_version](kg_version.md)
    * Description: Version of the biolink model used to load the schema. Supplied by the loader
    * range: **string**
    * __Local__
 * [prefixes](prefixes.md)
    * Description: Additional prefixes to be added to the context beyond those fetched from prefixcommons in id_prefixes
    * range: [Prefix](Prefix.md)*
    * __Local__
 * [relationship types](relationship_types.md)
    * Description: -> the collection of edges that represent relationship types in the knowledge graph
    * range: [Association](Association.md)*
    * __Local__
