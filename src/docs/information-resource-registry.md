---
title: "Modifying or Adding to the Information Resource (infores) Registry"
parent: "Biolink Model Guidelines"
layout: default
nav_order: 10
---

## What is Source Retrieval Provenance?
'Source retrieval provenance' describes the set of Information Resources through which the knowledge expressed in an 
Edge was passed, through various retrieval and/or transform operations, on its way to its current serialized form. 
For example, the provenance of a Gene-Chemical Edge in a message sent to a Translator ARA (e.g. ARAGORN) might be 
traced through the Translator KP that provided it (e.g. MolePro), one or more intermediate aggregator resources 
(e.g. ChEMBL), and back to the resource that originally created/curated it (e.g. ClinicalTrials.org).

ARAGORN  -- retrieved_from -->   MolePro  -- retrieved_from -->  ChEMBL  -- retrieved_from -->  ClinicalTrials.gov

To be clear, source retrieval provenance concerns the mechanical retrieval and transformation of data between web 
accessible information systems. It does not trace the source of knowledge back to specific publications or data sets. 
And it is not concerned with the reasoning, inference or analysis activities that generate knowledge in the first place.

### Biolink Edge Properties for Source Retrieval Provenance
We define the following hierarchy of edge properties in Biolink for capturing Information Resources through which 
knowledge expressed in a given edge was retrieved on its way to its presently serialized form (e.g. a TRAPI message 
sent to an ARA). Full definitions and metadata for each can be found in the Biolink Model.
 
* **biolink:knowledge_source**: 
  * An Information Resource from which the knowledge expressed in an Association was retrieved, 
  directly or indirectly
* **biolink:primary_knowledge_source**: 
  * The most upstream source of the knowledge expressed in an Association that a 
  knowledge provider can identify. 
* **biolink:aggregator_knowledge_source**:  
  * An intermediate aggregator resource from which knowledge expressed in an 
  Association was retrieved downstream of the original source, on its path to its current serialized form.  
* **`biolink:supporting_data_source`**: 
  * An Information Resource from which data was retrieved and subsequently used as
  evidence to generate the knowledge expressed in an Association (e.g. through computation on, reasoning or inference 
  over the retrieved data).


### Standard Identifiers for Information Resources
We also define a standard ‘InfoRes identifier’ for each Information Resource that provides data to Translator KPs and 
ARAs, as well as for Translator KPs and ARAs themselves.The CURIE form of these identifiers will be used to populate 
the ‘value’ field of Attributes describing retrieval provenance information. 
InfoRes identifiers are created as computable IRIs in the w3id namespace, to facilitate formal representation of 
Information Resource instances as nodes in a knowledge graph. The namespace for these IRIs is  https://w3id.org/infores,
and the prefix for CURIE-based representations is infores. The identifier component of the IRI is a short form human 
readable name or abbreviation.  

The following are examples of InfoRes IRI identifiers and their CURIE forms:

* External Resource IRI: https://w3id.org/infores/dgidb
  * External Resource CURIE: infores:dgidb
* Translator Resource IRI: https://w3id.org/infores/molepro
  * Translator Resource CURIE: infores:molepro

Initially, InfoRes identifiers are being created for version-agnostic parent resources only (e.g. an IRI for DGIdb, but
not separate IRIs for DGIdb v4.2.0, or DGIdb v3.0.0). Future work may create version-specific identifiers, and/or 
provide a way to capture version information in a separate field/attribute. 

#### Implementation Guidance and Constraints: 
We have created a InfoRes Catalog here, to store these identifiers along with metadata about the Information Resource 
they specify. Data creators should consult the ‘id’ column of the InfoRes Catalog to find CURIEs for specific 
Information Resources. Use these CURIEs to populate the ‘value’ field in an Attribute object that uses one of the 
source retrieval provenance edge properties described above as its key. 
   
#### Adding a new Information Resource entry: 
If there is no record in the catalog for a given resource, users should make a pull request that adds a row for the 
missing resource directly to the google sheet. Minimally, add the ‘name’ and ‘url’ for the resource (if one exists). 
You may also suggest an infores CURIE in the ‘id’ column, and populate any of the other metadata columns as desired 
(see Appendices 1 and 2 for more guidance)  Tag an SRI curator (@sierra-moxon or @mbrush) as a reviewer, who 
will review and finalize the request. 

#### Editing metadata for an existing entry: 
KP / ARA representatives can create a pull request to add or edit the metadata provided for an existing resource in 
much the same manner as adding a new resource.  Tag an SRI curator (@sierra-moxon or @mbrush) as a reviewer, who will 
review and finalize the request.

### The Information Resource Registry (infores) data model
An information resource is defined as a web-accessible resource that provides data. An InformationResource 
(designated by its identifier in curie form, e.g. 'infores:monarchintiative') is a Biolink Model class that provides 
a standard way to identify and describe information resources. The InformationResource class details can be found here:
[information-resource.yaml](information-resource.yaml) and contains the following properties:

- **id**: the identifier of the information resource (e.g. 'infores:monarchintiative')
- **name**: the name of the information resource (e.g. 'Monarch Initiative')
- **description**: a description of the information resource (e.g. 'Monarch is a platform for biomedical data discovery 
and integration')
- **url**: the url of the information resource (e.g. 'https://monarchinitiative.org/')
- **status**: the status of the information resource (e.g. 'released', 'deprecated', etc.  Please see the enumeration 
listed in the model yaml for more information)


### Modifying an existing Information Resource entry in the registry:
Making changes to the registry MUST be done via pull requests to the biolink-model github repository.  Any of the 
fields in an Information Resource entry can be modified, but the id field MUST not be changed.  If the id field is
changed, it MUST be treated as a new entry and the old entry MUST be deprecated. 

### Adding a new Information Resource entry to the registry: 
Adding a new entry to the registry is as easy as adding a stanza to the information-resource.yaml file in the biolink-model
repository and submitting the change via pull request in the repository.  Alternatively, making a ticket for a new
resource in the biolink-model GitHub repository will also work.  

#### Minting new Information Resource identifiers:

- Each smartAPI-registered Translator API gets its own InfoRes, as will each upstream source from which it aggregates knowledge.
  - Each upstream source from which a Translator API retrieves data computed on to generate knowledge will also get its own InfoRes.
- Create an InfoRes IRI for each registered Biothings-generated API, that includes a 'biothings-' prefix in the identifier component. 
If the resource whose content was wrapped in a Biothigns API is a pre-existing resource with established use and identity, an 
InfoRes is created for it as well.
- Identifiers should be short, readable, strings deliminated with a dash ('-').  These identifiers will be used 
in user-facing applications and should be as readable as possible.
- In general, the 'status' field of an Information Resource stanza should be one of two values: 'released' or 'deprecated'.

The following is an example of a new entry in the
information-resource.yaml file:
```
- id: infores:my-new-resource
  name: My New Resource
  description: This is a new resource
  url: https://my-new-resource.org/
  status: released
```

### Removing an infores stanza from the registry:
In an effort to maintain the integrity of the applications that use the Information Resource Registry identifiers downstream, 
we will not be removing entries from the registry.  But, if an information resource is no longer available, we will
mark it as deprecated in the registry and downstream applications (like the Biolink Model Toolkit) will no longer
serve deprecated Information Resources from their methods.  


### Appendix 1: InfoRes Catalog Metadata Dictionary

At present, a minimal set of metadata is being collected in the InfoRes Registry using the following Biolink node 
properties, which will be expanded in future iterations.

name:  a fully informative name for the resource (we recommend a name that is as informative and unambiguous as 
possible - spelling out all acronyms that are not common knowledge, and including the name of the owning organization 
when the name alone may be ambiguous).

id: the CURIE form of the InfoRes identifier, wherein a short form name of the resources serves as a human readable 
identifier component (e.g. ‘infores:dgidb’)

* **synonym**:
  * other names for the resource (will facilitate search/discovery)
* **url**: 
  * a url describing the resource - preferably its primary home page for the resource (if one exists)
* **description**: 
  * a free text description of the resource

#### Appendix 2: Rules for Minting InfoRes Names and Identifiers
A short form human understandable name or abbreviation is used as the identifier component of an InfoRes IRI, 
and should follow these conventions:

* Use lowercase characters only.
* Keep as short as possible while remaining understandable and unambiguous. 
* Acronyms are good where they are well-established and used in practice in our domain (e.g. infores:omim, not infores:online-mendelian-inheritance-in-man). Otherwise, spell out the name to the extent needed to be understood by the user (e.g. infores:drug-repurposing-hub, not infores:drh).  
* Where it makes sense to do so, adopt the base url of the resources home web address, or its registered prefix in an authority like identifiers.org.
* Use a hyphen (-) to separate words where needed (e.g. infores:drug-repurposing-hub), unless the words are not separated in common practice or the website url (e.g. we use infores:monarchinitiative, not infores:monarch-initiative, because their website is https://monarchinitiative.org/).
* All other non-alphanumeric characters are not allowed as delimiters.
* If we begin creating version-specific identifiers, a dot (.) will be reserved as a separator between the base resource name and its version. And versions will be specified using either dot-separated numerals (e.g. '1.1.2'), or release dates in ISO8601 format (e.g. '2021-04-18').


#### Appendix 3: Conventions for Crafting Identifiers for Translator Registry Resources
Translator applies many services that wrap or annotate existing resources in APIs to serve content that is better 
aligned with Translator standards. This practice can lead to confusion around what represents a separate Information 
Resource, and how resources may be related to each other. Below we describe conventions we apply for InfoRes creation 
for different scenarios / use cases we encounter in the registry.
 
Aggregator Scenario: KPs/ARAs that aggregate content from one or more existing resource and transform the semantics 
and or structure of the data to be better aligned with Translator standards

Resource Examples:
Molecular Data Provider, Biolink, ROBOKOP, SRI Reference KG, RTX KG2  (these aggregate content from multiple sources into a single KG / API)
Automat APIs (stands up a separate API per source - each of which gets its own InfoRes)

##### InfoRes Convention: Each smartAPI-registered Translator API gets its own InfoRes, as will each upstream source from 
which it aggregates knowledge.

Knowledge Generator Use Case: KPs/ARAs that retrieve data from existing sources and curate or analyze the data to generate new knowledge
Resource Examples: Multiomics Wellness, Drug Response, and Clinical Risk KPs,  ICEES KP, COHD KP, 
Connections Hypothesis KP, Text Mining KP (here the 'data' is publication text from which associations are curated)

##### InfoRes Convention:  Each smart-API registered Translator API gets its own InfoRes, as will each upstream source from 
which it retrieves data computed on to generate knowledge

SmartAPI Annotation Use Case: KPs/ARAs (just Service Provider) that annotate an existing/external API in the smartAPI 
registry, imposing Biolink semantics onto the data it serves (without actually standing up a new API or transforming 
the data itself).

Examples: LitVar API, ChEMBL API, EBI Proteins API, QuickGO API, OpenTargets API, RGD API, and others that Service 
Provider registers in the smartAPI Registry so BTE can consume/integrate/navigate their data (and subsequently 
transform to TRAPI compliant form)

##### InfoRes Convention: Create an InfoRes only for the external resource, (as smartAPI annotation/registration itself 
doesn’t create a new API resource for each of these sources)
 
BioThings API-ification Use Case:  KPs / ARAs (just Service Provider) that apply the Biothings toolkit to stand up a 
novel API serving data from an existing resource (and often aligning data with Translator standards in the process). 
The Biothings-wrapped resources may be external knowledge bases (e.g. DISEASES) or internal Translator KPs (e.g. BigGim). 

Examples:
External resources such as DGIdb, DISEASES, EBIgene2phenotype, Gene Ontology Biological Process API, Human Phenotype 
Ontology, SEMMED Anatomy API.

Internal Translator KPs such as BigGim1, Multiomics Drug Response API, Text Mining Provider APIs

##### InfoRes Convention: Create an InfoRes IRI for each registered Biothings-generated API 

This includes a 'biothings-' prefix in the identifier component. If the resource whose content was wrapped in a 
Biothigns API is a pre-existing resource with established use and identity, an InfoRes is created for it as well. 

Note that this is closely related to Automat KPs described in the Aggregator Use Case - but here the Biothings pipeline 
and tools are used to facilitate API generation, and the resulting APIs often do not achieve full TRAPI compliance as 
they do with Automat. But their semantic annotation in the smartAPI registry allows BTE to use them as if they were,
and generate TRAPI-compliant data from them. Ultimately, we treat these resources the same as we do Automat resources 
(creating separate InfoRes identifiers for the Translator API-ification of the source and the source itself).

At present we don’t create a separate InfoRes when the wrapped resource is a Translator KP (e.g. BigGIM, Multiomics 
Drug Response API) -  but we can do this if desired, and may need to if these resources eventually stand up their 
own separate APIs. 

An example highlighting the difference between the SmartAPI Annotation and BioThings API-ification use cases can be 
found in comparing how we treat two registry entries for Service Provider supported EBI services:

In the case of the EBI Proteins API, Service Provider merely creates a smartAPI registry entry where it annotates 
various endpoints of the external EBI API to enable overlay of Biolink semantics onto the data they return. Here, 
a single InfoRes is created for the external EBI API (infores:ebi-proteins), as Service Provider doesn't actually 
create a novel API resource.

In the case of the EBIgene2phenotype API, Service Provider creates a new Biothings API that transforms and serves 
EBI data from a new resource, that is also registered in smartAPI. Here, separate InfoRes identifiers are created 
for this new Biothings API (infores:biothings-ebi-gene2phenotype), and for the external 
EBI API (infores:ebi-gene2phenotype)
 