
# Slot: upstream resource ids


An upstream InformationResource from which the resource being described directly retrieved a record of the knowledge expressed in the Edge, or data used to generate this knowledge. This is an array because there are cases where a merged Edge holds knowledge that was retrieved from multiple sources. e.g. an Edge provided by the ARAGORN ARA can expressing knowledge it retrieved from both the automat-mychem-info and molepro KPs, which both provided it with records of this single fact.

URI: [biolink:upstream_resource_ids](https://w3id.org/biolink/vocab/upstream_resource_ids)


## Domain and Range

[RetrievalSource](RetrievalSource.md) &#8594;  <sub>0..1</sub> [Uriorcurie](types/Uriorcurie.md)

## Parents

 *  is_a: [node property](node_property.md)

## Children

 *  [retrieval source➞upstream resource ids](retrieval_source_upstream_resource_ids.md)

## Used by

