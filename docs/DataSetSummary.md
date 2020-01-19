---
parent: Mixins
title: biolink:DataSetSummary
grand_parent: Browse Biolink Model
---

# Type: DataSetSummary




URI: [biolink:DataSetSummary](https://w3id.org/biolink/vocab/DataSetSummary)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[DistributionLevel]<distribution(i)%200..1-%20\[DataSetSummary&#124;source_web_page:string%20%3F;title(i):string%20%3F;id(i):identifier_type;name(i):label_type;category(i):iri_type%20%2B],%20\[DataSet]<versionOf(i)%200..1-%20\[DataSetSummary],%20\[DataFile]<source%20data%20file(i)%200..1-%20\[DataSetSummary],%20\[DataSetVersion]^-\[DataSetSummary])

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
    * inherited from: [DataSetVersion](DataSetVersion.md)
 * [source data file](source_data_file.md)  <sub>OPT</sub>
    * range: [DataFile](DataFile.md)
    * inherited from: [DataSetVersion](DataSetVersion.md)
 * [versionOf](versionOf.md)  <sub>OPT</sub>
    * range: [DataSet](DataSet.md)
    * inherited from: [DataSetVersion](DataSetVersion.md)
 * [distribution](distribution.md)  <sub>OPT</sub>
    * range: [DistributionLevel](DistributionLevel.md)
    * inherited from: [DataSetVersion](DataSetVersion.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [IdentifierType](types/IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](types/IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [source web page](source_web_page.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
