---
parent: Mixins
title: biolink:DataSetSummary
grand_parent: Browse Biolink Model
layout: default
---

# Type: DataSetSummary




URI: [biolink:DataSetSummary](https://w3id.org/biolink/vocab/DataSetSummary)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DistributionLevel],[DataSetVersion],[DataSetVersion]%5E-[DataSetSummary|source_web_page:string%20%3F;title(i):string%20%3F;type(i):string%20%3F;id(i):string;name(i):label_type;category(i):category_type%20%2B],[DataSet],[DataFile])

---


## Parents

 *  is_a: [DataSetVersion](DataSetVersion.md)

## Referenced by class


## Attributes


### Own

 * [source web page](source_web_page.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from data set version:

 * [title](title.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [source data file](source_data_file.md)  <sub>OPT</sub>
    * range: [DataFile](DataFile.md)
 * [versionOf](versionOf.md)  <sub>OPT</sub>
    * range: [DataSet](DataSet.md)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [distribution](distribution.md)  <sub>OPT</sub>
    * range: [DistributionLevel](DistributionLevel.md)

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

 * [source web page](source_web_page.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
