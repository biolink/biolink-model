---
parent: Entities
title: biolink:DistributionLevel
grand_parent: Classes
layout: default
---

# Class: DistributionLevel




URI: [biolink:DistributionLevel](https://w3id.org/biolink/vocab/DistributionLevel)

dcat:Distribution
{: .mapping-label }


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[DataSetVersion]-%20distribution%200..1%3E[DistributionLevel%7Cdownload_url:string%20%3F;title(i):string%20%3F;type(i):string%20%3F;id(i):string;name(i):label_type;category(i):category_type%20%2B],[DataSetVersion]%5E-[DistributionLevel],[DataSetVersion],[DataSet],[DataFile])

---


## Parents

 *  is_a: [DataSetVersion](DataSetVersion.md)

## Referenced by class

 *  **[DataSetVersion](DataSetVersion.md)** *[distribution](distribution.md)*  <sub>OPT</sub>  **[DistributionLevel](DistributionLevel.md)**

## Attributes


### Own

 * [download url](download_url.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from data set version:

 * [title](title.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [source data file](source_data_file.md)  <sub>OPT</sub>
    * range: [DataFile](DataFile.md)
 * [version of](version_of.md)  <sub>OPT</sub>
    * range: [DataSet](DataSet.md)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [distribution](distribution.md)  <sub>OPT</sub>
    * range: [DistributionLevel](DistributionLevel.md)

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

 * [download url](download_url.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | dcat:Distribution |

