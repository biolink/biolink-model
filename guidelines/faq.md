## FAQ

Address commonly asked questions.

### How do I type nodes in a graph with concepts that are not in the Biolink Model?

- `rdfs:subClassOf` or `rdf:type` edges in addition to `biolink:category`

### How do I type edges in a graph with concepts that are not in the Biolink Model?

- `rdf:type`

### How do I add properties that are not in the Biolink Model

- each node and/or edge can have properties that are outside of Biolink Model
- For a more structure it is recommended to use `biolink:Attribute` and `biolink:has_attribute`

### What is the serialized form of Biolink Model?

```
KGX TSV
```

```
KGX JSON
```

```
KGX NT
```

### What is the difference between predicate, relation, association_type?

predicate - `rdf:predicate`
relation - `association slot`
association_type - `rdf:type`

### 