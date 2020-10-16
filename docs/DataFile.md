---
parent: Entities
title: biolink:DataFile
grand_parent: Classes
layout: default
---

# Class: DataFile




URI: [biolink:DataFile](https://w3id.org/biolink/vocab/DataFile)

EFO:0004095
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[SourceFile],[NamedThing],[DataSetVersion],[DataSetVersion]-%20source%20data%20file%200..1%3E[DataFile%7Cid(i):string;name(i):label_type;category(i):category_type%20%2B],[DataFile]%5E-[SourceFile],[NamedThing]%5E-[DataFile])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [SourceFile](SourceFile.md)

## Referenced by class

 *  **[DataSetVersion](DataSetVersion.md)** *[source data file](source_data_file.md)*  <sub>OPT</sub>  **[DataFile](DataFile.md)**

## Attributes


### Inherited from gene product:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)

### Inherited from named thing:

 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | EFO:0004095 |

