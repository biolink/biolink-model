---
title: "Modifying or Adding to the Information Resource (infores) Registry"
parent: "Biolink Model Guidelines"
layout: default
nav_order: 10
---

### The Information Resource Registry (infores) data model
An information resource is defined as a web-accessible resource that provides data. An InformationResource 
(designated by its identifier in curie form, e.g. 'infores:monarchintiative') is a Biolink Model class that provides 
a standard way to identify and describe information resources. The InformationResource class details can be found here:
[information-resource.yaml](../../information-resource.yaml) and contains the following properties:
- **id**: the identifier of the information resource (e.g. 'infores:monarch-intiative')
- **name**: the name of the information resource (e.g. 'Monarch Initiative')
- **description**: a description of the information resource (e.g. 'Monarch is a platform for biomedical data discovery and integration')
- **url**: the url of the information resource (e.g. 'https://monarchinitiative.org/')
- **status**: the status of the information resource (e.g. 'released', 'deprecated', etc.  Please see the enumeration listed 
in the model yaml for more information)


### Modifying an existing Information Resource entry in the registry:
Making changes to the registry MUST be done via pull requests to the biolink-model github repository.  Any of the 
fields in an Information Resource entry can be modified, but the id field MUST not be changed.  If the id field is
changed, it MUST be treated as a new entry and the old entry MUST be deprecated. 

### Adding a new Information Resource entry to the registry: 
Adding a new entry to the registry is as easy as adding a stanza to the information-resource.yaml file in the biolink-model
repository and submitting the change via pull request in the repository.  Alternatively, making a ticket for a new
resource in the biolink-model github repository will also work.  

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
