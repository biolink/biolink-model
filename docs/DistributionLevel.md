
# Class: distribution level




URI: [biolink:DistributionLevel](https://w3id.org/biolink/vocab/DistributionLevel)

![img](images/DistributionLevel.png)

## Parents

 *  is_a: [DataSetVersion](DataSetVersion.md)

## Referenced by class

 *  **[DataSetVersion](DataSetVersion.md)** *[distribution](distribution.md)*  <sub>OPT</sub>  **[DistributionLevel](DistributionLevel.md)**

## Attributes


### Own

 * [downloadURL](downloadURL.md)  <sub>OPT</sub>
    * range: [String](String.md)

### Inherited from data set version:

 * [title](title.md)  <sub>OPT</sub>
    * range: [String](String.md)
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
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [name](name.md)  <sub>REQ</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](LabelType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)
 * [category](category.md)  <sub>1..*</sub>
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
    * range: [IriType](IriType.md)
    * inherited from: [NamedThing](NamedThing.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [downloadURL](downloadURL.md)  <sub>OPT</sub>
    * range: [String](String.md)
