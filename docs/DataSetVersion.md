---
parent: Entities
title: biolink:DataSetVersion
grand_parent: Classes
layout: default
---

# Class: DataSetVersion




URI: [biolink:DataSetVersion](https://w3id.org/biolink/vocab/DataSetVersion)

dctypes:Dataset
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DistributionLevel],[DistributionLevel]%3Cdistribution%200..1-%20[DataSetVersion%7Ctitle:string%20%3F;type:string%20%3F;id(i):string;name(i):label_type;category(i):category_type%20%2B],[DataSet]%3Cversion%20of%200..1-%20[DataSetVersion],[DataFile]%3Csource%20data%20file%200..1-%20[DataSetVersion],[DataSetVersion]%5E-[DistributionLevel],[DataSetVersion]%5E-[DataSetSummary],[DataSet]%5E-[DataSetVersion],[DataSetSummary],[DataSet],[DataFile])

---


## Parents

 *  is_a: [DataSet](DataSet.md)

## Children

 * [DataSetSummary](DataSetSummary.md)
 * [DistributionLevel](DistributionLevel.md)

## Referenced by class


## Attributes


### Own

 * [distribution](distribution.md)  <sub>OPT</sub>
    * range: [DistributionLevel](DistributionLevel.md)
 * [source data file](source_data_file.md)  <sub>OPT</sub>
    * range: [DataFile](DataFile.md)
 * [title](title.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [version of](version_of.md)  <sub>OPT</sub>
    * range: [DataSet](DataSet.md)

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
    * Description: Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class.
 * In a neo4j database this MAY correspond to the neo4j label tag.
 * In an RDF database it should be a biolink model class URI.
This field is multi-valued. It should include values for ancestors of the biolink class; for example, a protein such as Shh would have category values `bl:Protein`, `bl:GeneProduct`, `bl:MolecularEntity`, ...
In an RDF database, nodes will typically have an rdf:type triples. This can be to the most specific biolink class, or potentially to a class more specific than something in biolink. For example, a sequence feature `f` may have a rdf:type assertion to a SO class such as TF_binding_site, which is more specific than anything in biolink. Here we would have categories {bl:GenomicEntity, bl:MolecularEntity, bl:NamedThing}
    * range: [CategoryType](types/CategoryType.md)
    * in subsets: (translator_minimal)

### Domain for slot:

 * [distribution](distribution.md)  <sub>OPT</sub>
    * range: [DistributionLevel](DistributionLevel.md)
 * [source data file](source_data_file.md)  <sub>OPT</sub>
    * range: [DataFile](DataFile.md)
 * [title](title.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [version of](version_of.md)  <sub>OPT</sub>
    * range: [DataSet](DataSet.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | dctypes:Dataset |

