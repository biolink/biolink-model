---
parent: Entities
title: biolink:Agent
grand_parent: Classes
layout: default
---

# Class: Agent


person, group, organization or project that provides a piece of information (i.e. a knowledge association)

URI: [biolink:Agent](https://w3id.org/biolink/vocab/Agent)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Publication],[NamedThing],[InformationContentEntity],[ContributorAssociation],[Attribute],[Association],[ContributorAssociation]-%20object%201..1%3E[Agent%7Caffiliation:uriorcurie%20%2A;address:string%20%3F;id:string;name:label_type%20%3F;iri(i):iri_type%20%3F;type(i):string%20%3F;description(i):narrative_text%20%3F;source(i):label_type%20%3F],[Entity]-%20provided%20by%200..%2A%3E[Agent],[AdministrativeEntity]%5E-[Agent],[Entity],[AdministrativeEntity])

---


## Identifier prefixes

 * isbn
 * ORCID
 * ScopusID
 * ResearchID
 * GSID
 * isni

## Parents

 *  is_a: [AdministrativeEntity](AdministrativeEntity.md)

## Referenced by class

 *  **[Publication](Publication.md)** *[author](author.md)*  <sub>0..*</sub>  **[Agent](Agent.md)**
 *  **[InformationContentEntity](InformationContentEntity.md)** *[contributor](contributor.md)*  <sub>0..*</sub>  **[Agent](Agent.md)**
 *  **[ContributorAssociation](ContributorAssociation.md)** *[contributor association➞object](contributor_association_object.md)*  <sub>REQ</sub>  **[Agent](Agent.md)**
 *  **[Publication](Publication.md)** *[editor](editor.md)*  <sub>0..*</sub>  **[Agent](Agent.md)**
 *  **[Association](Association.md)** *[provided by](provided_by.md)*  <sub>0..*</sub>  **[Agent](Agent.md)**
 *  **[InformationContentEntity](InformationContentEntity.md)** *[provider](provider.md)*  <sub>0..*</sub>  **[Agent](Agent.md)**
 *  **[Publication](Publication.md)** *[publisher](publisher.md)*  <sub>0..*</sub>  **[Agent](Agent.md)**

## Attributes


### Own

 * [address](address.md)  <sub>OPT</sub>
    * Description: the particulars of the place where someone or an organization is situated.  For now, this slot is a simple text "blob" containing all relevant details of the given location for fitness of purpose. For the moment, this "address" can include other contact details such as email and phone number(?).
    * range: [String](types/String.md)
 * [affiliation](affiliation.md)  <sub>0..*</sub>
    * Description: a professional relationship between one provider (often a person) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [agent➞id](agent_id.md)  <sub>REQ</sub>
    * Description: Different classes of agents have distinct preferred identifiers. For publishers, use the ISBN publisher code. See https://grp.isbn-international.org/ for publisher code lookups. For editors, authors and  individual providers, use the individual's ORCID if available; Otherwise, a ScopusID, ResearchID or Google Scholar ID ('GSID') may be used if the author ORCID is unknown. Institutional agents could be identified by an International Standard Name Identifier ('ISNI') code.
    * range: [String](types/String.md)
 * [agent➞name](agent_name.md)  <sub>OPT</sub>
    * Description: it is recommended that an author's 'name' property be formatted as "surname, firstname initial."
    * range: [LabelType](types/LabelType.md)

### Inherited from entity:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a resource. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * in subsets: (translator_minimal)
 * [iri](iri.md)  <sub>OPT</sub>
    * Description: An IRI for an entity. This is determined by the id using expansion rules.
    * range: [IriType](types/IriType.md)
    * in subsets: (translator_minimal,samples)
 * [type](type.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human-readable name for a thing
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal,samples)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [NarrativeText](types/NarrativeText.md)
    * in subsets: (translator_minimal)
 * [source](source.md)  <sub>OPT</sub>
    * Description: a lightweight analog to the association class 'has provider' slot, which is the string name, or the authoritative (i.e. database) namespace, designating the origin of the entity to which the slot belongs.
    * range: [LabelType](types/LabelType.md)
    * in subsets: (translator_minimal)
 * [provided by](provided_by.md)  <sub>0..*</sub>
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Agent](Agent.md)

### Inherited from material sample:

 * [has attribute](has_attribute.md)  <sub>0..*</sub>
    * Description: connects any named thing to an attribute
    * range: [Attribute](Attribute.md)
    * in subsets: (samples)

### Inherited from named thing:

 * [named thing➞category](named_thing_category.md)  <sub>1..*</sub>
    * range: [NamedThing](NamedThing.md)

### Domain for slot:

 * [affiliation](affiliation.md)  <sub>0..*</sub>
    * Description: a professional relationship between one provider (often a person) within another provider (often an organization). Target provider identity should be specified by a CURIE. Providers may have multiple affiliations.
    * range: [Uriorcurie](types/Uriorcurie.md)
 * [agent➞id](agent_id.md)  <sub>REQ</sub>
    * Description: Different classes of agents have distinct preferred identifiers. For publishers, use the ISBN publisher code. See https://grp.isbn-international.org/ for publisher code lookups. For editors, authors and  individual providers, use the individual's ORCID if available; Otherwise, a ScopusID, ResearchID or Google Scholar ID ('GSID') may be used if the author ORCID is unknown. Institutional agents could be identified by an International Standard Name Identifier ('ISNI') code.
    * range: [String](types/String.md)
 * [agent➞name](agent_name.md)  <sub>OPT</sub>
    * Description: it is recommended that an author's 'name' property be formatted as "surname, firstname initial."
    * range: [LabelType](types/LabelType.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | group |
| **Exact Mappings:** | | prov:Agent |
|  | | dcterms:Agent |
| **Narrow Mappings:** | | UMLSSG:ORGA |
|  | | UMLSSC:T092 |
|  | | UMLSST:orgt |
|  | | UMLSSC:T093 |
|  | | UMLSST:hcro |
|  | | UMLSSC:T094 |
|  | | UMLSST:pros |
|  | | UMLSSC:T095 |
|  | | UMLSST:shro |
|  | | UMLSSC:T096 |
|  | | UMLSST:grup |
|  | | UMLSSC:T097 |
|  | | UMLSST:prog |

