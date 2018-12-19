# Class: gene to thing association




URI: [http://w3id.org/biolink/vocab/GeneToThingAssociation](http://w3id.org/biolink/vocab/GeneToThingAssociation)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[GeneToThingAssociation|id(i):identifier_type%20%3F;object(i):string;negated(i):boolean%20%3F;association_slot(i):string%20%3F]-%20provided%20by(i)%20%3F>\[Provider],%20\[GeneToThingAssociation]-%20publications(i)%20*>\[Publication],%20\[GeneToThingAssociation]-%20qualifiers(i)%20*>\[OntologyClass],%20\[GeneToThingAssociation]-%20association%20type(i)%20%3F>\[OntologyClass],%20\[GeneToThingAssociation]-%20relation(i)>\[RelationshipType],%20\[GeneToThingAssociation]-%20subject>\[GeneOrGeneProduct],%20\[GeneToPhenotypicFeatureAssociation]uses%20-.->\[GeneToThingAssociation],%20\[GeneToDiseaseAssociation]uses%20-.->\[GeneToThingAssociation],%20\[Association]^-\[GeneToThingAssociation])
## Mappings

## Inheritance

 *  is_a: [Association](Association.md) - A typed association between two entities, supported by evidence
## Children

 * [GeneToDiseaseAssociation](GeneToDiseaseAssociation.md) (mixin) 
 * [GeneToPhenotypicFeatureAssociation](GeneToPhenotypicFeatureAssociation.md) (mixin) 
## Used in

## Fields

 * [gene to thing association.subject](gene_to_thing_association_subject.md)
    * Description: gene that is the subject of the association
    * range: [GeneOrGeneProduct](GeneOrGeneProduct.md) [required]
    * __Local__
 * [association slot](association_slot.md)
    * Description: any slot that relates an association to another entity
    * range: **string**
    * inherited from: [Association](Association.md)
 * [association type](association_type.md)
    * Description: connects an association to the type of association (e.g. gene to phenotype)
    * range: [OntologyClass](OntologyClass.md)
    * inherited from: [Association](Association.md)
 * [association.id](association_id.md) *subsets*: (translator_minimal)
    * Description: A unique identifier for an association
    * range: [IdentifierType](IdentifierType.md)
    * inherited from: [Association](Association.md)
 * [negated](negated.md)
    * Description: if set to true, then the association is negated i.e. is not true
    * range: **boolean**
    * inherited from: [Association](Association.md)
 * [object](object.md)
    * Description: connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
    * range: **string** [required]
    * inherited from: [Association](Association.md)
 * [provided by](provided_by.md)
    * Description: connects an association to the agent (person, organization or group) that provided it
    * range: [Provider](Provider.md)
    * inherited from: [Association](Association.md)
 * [publications](publications.md)
    * Description: connects an association to publications supporting the association
    * range: [Publication](Publication.md)*
    * inherited from: [Association](Association.md)
 * [qualifiers](qualifiers.md)
    * Description: connects an association to qualifiers that modify or qualify the meaning of that association
    * range: [OntologyClass](OntologyClass.md)*
    * inherited from: [Association](Association.md)
 * [relation](relation.md)
    * Description: the relationship type by which a subject is connected to an object in an association
    * range: [RelationshipType](RelationshipType.md) [required]
    * inherited from: [Association](Association.md)
