---
parent: Classes
title: biolink:SourceFile
grand_parent: Browse Biolink Model
layout: default
---

# Type: SourceFile




URI: [biolink:SourceFile](https://w3id.org/biolink/vocab/SourceFile)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DataFile]%5E-[SourceFile%7Csource_version:string%20%3F;retrievedOn:date%20%3F;id(i):string;name(i):label_type;category(i):category_type%20%2B],[DataFile])

---


## Parents

 *  is_a: [DataFile](DataFile.md)

## Referenced by class


## Attributes


### Own

 * [retrievedOn](retrievedOn.md)  <sub>OPT</sub>
    * range: [Date](types/Date.md)
 * [source version](source_version.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [retrievedOn](retrievedOn.md)  <sub>OPT</sub>
    * range: [Date](types/Date.md)
 * [source version](source_version.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
