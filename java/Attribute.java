import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * Attribute
 * <p>
 * A property or characteristic of an entity. For example, an apple may have properties such as color, shape, age, crispiness. An environmental sample may have attributes such as depth, lat, long, material.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "category",
    "description",
    "full_name",
    "has_attribute_type",
    "has_qualitative_value",
    "has_quantitative_value",
    "id",
    "interacts_with",
    "iri",
    "name",
    "node_property",
    "related_to",
    "subclass_of",
    "synonym",
    "systematic_synonym"
})
public class Attribute {

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * (Required)
     * 
     */
    @JsonProperty("category")
    @JsonPropertyDescription("Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag")
    private List<String> category = new ArrayList<String>();
    /**
     * a human-readable description of a thing
     * 
     */
    @JsonProperty("description")
    @JsonPropertyDescription("a human-readable description of a thing")
    private String description;
    /**
     * a long-form human readable name for a thing
     * 
     */
    @JsonProperty("full_name")
    @JsonPropertyDescription("a long-form human readable name for a thing")
    private String fullName;
    /**
     * connects an attribute to a class that describes it
     * 
     */
    @JsonProperty("has_attribute_type")
    @JsonPropertyDescription("connects an attribute to a class that describes it")
    private String hasAttributeType;
    /**
     * connects an attribute to a value
     * 
     */
    @JsonProperty("has_qualitative_value")
    @JsonPropertyDescription("connects an attribute to a value")
    private String hasQualitativeValue;
    /**
     * connects an attribute to a value
     * 
     */
    @JsonProperty("has_quantitative_value")
    @JsonPropertyDescription("connects an attribute to a value")
    private List<String> hasQuantitativeValue = new ArrayList<String>();
    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * (Required)
     * 
     */
    @JsonProperty("id")
    @JsonPropertyDescription("A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI")
    private String id;
    /**
     * holds between any two entities that directly or indirectly interact with each other
     * 
     */
    @JsonProperty("interacts_with")
    @JsonPropertyDescription("holds between any two entities that directly or indirectly interact with each other")
    private List<String> interactsWith = new ArrayList<String>();
    /**
     * An IRI for the node. This is determined by the id using expansion rules.
     * 
     */
    @JsonProperty("iri")
    @JsonPropertyDescription("An IRI for the node. This is determined by the id using expansion rules.")
    private String iri;
    /**
     * A human-readable name for a thing
     * (Required)
     * 
     */
    @JsonProperty("name")
    @JsonPropertyDescription("A human-readable name for a thing")
    private String name;
    /**
     * A grouping for any property that holds between a node and a value
     * 
     */
    @JsonProperty("node_property")
    @JsonPropertyDescription("A grouping for any property that holds between a node and a value")
    private String nodeProperty;
    /**
     * A relationship that is asserted between two named things
     * 
     */
    @JsonProperty("related_to")
    @JsonPropertyDescription("A relationship that is asserted between two named things")
    private List<String> relatedTo = new ArrayList<String>();
    /**
     * holds between two classes where the domain class is a specialization of the range class
     * 
     */
    @JsonProperty("subclass_of")
    @JsonPropertyDescription("holds between two classes where the domain class is a specialization of the range class")
    private List<String> subclassOf = new ArrayList<String>();
    /**
     * Alternate human-readable names for a thing
     * 
     */
    @JsonProperty("synonym")
    @JsonPropertyDescription("Alternate human-readable names for a thing")
    private List<String> synonym = new ArrayList<String>();
    /**
     * more commonly used for gene symbols in yeast
     * 
     */
    @JsonProperty("systematic_synonym")
    @JsonPropertyDescription("more commonly used for gene symbols in yeast")
    private List<String> systematicSynonym = new ArrayList<String>();

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * (Required)
     * 
     */
    @JsonProperty("category")
    public List<String> getCategory() {
        return category;
    }

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * (Required)
     * 
     */
    @JsonProperty("category")
    public void setCategory(List<String> category) {
        this.category = category;
    }

    /**
     * a human-readable description of a thing
     * 
     */
    @JsonProperty("description")
    public String getDescription() {
        return description;
    }

    /**
     * a human-readable description of a thing
     * 
     */
    @JsonProperty("description")
    public void setDescription(String description) {
        this.description = description;
    }

    /**
     * a long-form human readable name for a thing
     * 
     */
    @JsonProperty("full_name")
    public String getFullName() {
        return fullName;
    }

    /**
     * a long-form human readable name for a thing
     * 
     */
    @JsonProperty("full_name")
    public void setFullName(String fullName) {
        this.fullName = fullName;
    }

    /**
     * connects an attribute to a class that describes it
     * 
     */
    @JsonProperty("has_attribute_type")
    public String getHasAttributeType() {
        return hasAttributeType;
    }

    /**
     * connects an attribute to a class that describes it
     * 
     */
    @JsonProperty("has_attribute_type")
    public void setHasAttributeType(String hasAttributeType) {
        this.hasAttributeType = hasAttributeType;
    }

    /**
     * connects an attribute to a value
     * 
     */
    @JsonProperty("has_qualitative_value")
    public String getHasQualitativeValue() {
        return hasQualitativeValue;
    }

    /**
     * connects an attribute to a value
     * 
     */
    @JsonProperty("has_qualitative_value")
    public void setHasQualitativeValue(String hasQualitativeValue) {
        this.hasQualitativeValue = hasQualitativeValue;
    }

    /**
     * connects an attribute to a value
     * 
     */
    @JsonProperty("has_quantitative_value")
    public List<String> getHasQuantitativeValue() {
        return hasQuantitativeValue;
    }

    /**
     * connects an attribute to a value
     * 
     */
    @JsonProperty("has_quantitative_value")
    public void setHasQuantitativeValue(List<String> hasQuantitativeValue) {
        this.hasQuantitativeValue = hasQuantitativeValue;
    }

    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * (Required)
     * 
     */
    @JsonProperty("id")
    public String getId() {
        return id;
    }

    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * (Required)
     * 
     */
    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    /**
     * holds between any two entities that directly or indirectly interact with each other
     * 
     */
    @JsonProperty("interacts_with")
    public List<String> getInteractsWith() {
        return interactsWith;
    }

    /**
     * holds between any two entities that directly or indirectly interact with each other
     * 
     */
    @JsonProperty("interacts_with")
    public void setInteractsWith(List<String> interactsWith) {
        this.interactsWith = interactsWith;
    }

    /**
     * An IRI for the node. This is determined by the id using expansion rules.
     * 
     */
    @JsonProperty("iri")
    public String getIri() {
        return iri;
    }

    /**
     * An IRI for the node. This is determined by the id using expansion rules.
     * 
     */
    @JsonProperty("iri")
    public void setIri(String iri) {
        this.iri = iri;
    }

    /**
     * A human-readable name for a thing
     * (Required)
     * 
     */
    @JsonProperty("name")
    public String getName() {
        return name;
    }

    /**
     * A human-readable name for a thing
     * (Required)
     * 
     */
    @JsonProperty("name")
    public void setName(String name) {
        this.name = name;
    }

    /**
     * A grouping for any property that holds between a node and a value
     * 
     */
    @JsonProperty("node_property")
    public String getNodeProperty() {
        return nodeProperty;
    }

    /**
     * A grouping for any property that holds between a node and a value
     * 
     */
    @JsonProperty("node_property")
    public void setNodeProperty(String nodeProperty) {
        this.nodeProperty = nodeProperty;
    }

    /**
     * A relationship that is asserted between two named things
     * 
     */
    @JsonProperty("related_to")
    public List<String> getRelatedTo() {
        return relatedTo;
    }

    /**
     * A relationship that is asserted between two named things
     * 
     */
    @JsonProperty("related_to")
    public void setRelatedTo(List<String> relatedTo) {
        this.relatedTo = relatedTo;
    }

    /**
     * holds between two classes where the domain class is a specialization of the range class
     * 
     */
    @JsonProperty("subclass_of")
    public List<String> getSubclassOf() {
        return subclassOf;
    }

    /**
     * holds between two classes where the domain class is a specialization of the range class
     * 
     */
    @JsonProperty("subclass_of")
    public void setSubclassOf(List<String> subclassOf) {
        this.subclassOf = subclassOf;
    }

    /**
     * Alternate human-readable names for a thing
     * 
     */
    @JsonProperty("synonym")
    public List<String> getSynonym() {
        return synonym;
    }

    /**
     * Alternate human-readable names for a thing
     * 
     */
    @JsonProperty("synonym")
    public void setSynonym(List<String> synonym) {
        this.synonym = synonym;
    }

    /**
     * more commonly used for gene symbols in yeast
     * 
     */
    @JsonProperty("systematic_synonym")
    public List<String> getSystematicSynonym() {
        return systematicSynonym;
    }

    /**
     * more commonly used for gene symbols in yeast
     * 
     */
    @JsonProperty("systematic_synonym")
    public void setSystematicSynonym(List<String> systematicSynonym) {
        this.systematicSynonym = systematicSynonym;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(Attribute.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("category");
        sb.append('=');
        sb.append(((this.category == null)?"<null>":this.category));
        sb.append(',');
        sb.append("description");
        sb.append('=');
        sb.append(((this.description == null)?"<null>":this.description));
        sb.append(',');
        sb.append("fullName");
        sb.append('=');
        sb.append(((this.fullName == null)?"<null>":this.fullName));
        sb.append(',');
        sb.append("hasAttributeType");
        sb.append('=');
        sb.append(((this.hasAttributeType == null)?"<null>":this.hasAttributeType));
        sb.append(',');
        sb.append("hasQualitativeValue");
        sb.append('=');
        sb.append(((this.hasQualitativeValue == null)?"<null>":this.hasQualitativeValue));
        sb.append(',');
        sb.append("hasQuantitativeValue");
        sb.append('=');
        sb.append(((this.hasQuantitativeValue == null)?"<null>":this.hasQuantitativeValue));
        sb.append(',');
        sb.append("id");
        sb.append('=');
        sb.append(((this.id == null)?"<null>":this.id));
        sb.append(',');
        sb.append("interactsWith");
        sb.append('=');
        sb.append(((this.interactsWith == null)?"<null>":this.interactsWith));
        sb.append(',');
        sb.append("iri");
        sb.append('=');
        sb.append(((this.iri == null)?"<null>":this.iri));
        sb.append(',');
        sb.append("name");
        sb.append('=');
        sb.append(((this.name == null)?"<null>":this.name));
        sb.append(',');
        sb.append("nodeProperty");
        sb.append('=');
        sb.append(((this.nodeProperty == null)?"<null>":this.nodeProperty));
        sb.append(',');
        sb.append("relatedTo");
        sb.append('=');
        sb.append(((this.relatedTo == null)?"<null>":this.relatedTo));
        sb.append(',');
        sb.append("subclassOf");
        sb.append('=');
        sb.append(((this.subclassOf == null)?"<null>":this.subclassOf));
        sb.append(',');
        sb.append("synonym");
        sb.append('=');
        sb.append(((this.synonym == null)?"<null>":this.synonym));
        sb.append(',');
        sb.append("systematicSynonym");
        sb.append('=');
        sb.append(((this.systematicSynonym == null)?"<null>":this.systematicSynonym));
        sb.append(',');
        if (sb.charAt((sb.length()- 1)) == ',') {
            sb.setCharAt((sb.length()- 1), ']');
        } else {
            sb.append(']');
        }
        return sb.toString();
    }

    @Override
    public int hashCode() {
        int result = 1;
        result = ((result* 31)+((this.hasQuantitativeValue == null)? 0 :this.hasQuantitativeValue.hashCode()));
        result = ((result* 31)+((this.iri == null)? 0 :this.iri.hashCode()));
        result = ((result* 31)+((this.nodeProperty == null)? 0 :this.nodeProperty.hashCode()));
        result = ((result* 31)+((this.systematicSynonym == null)? 0 :this.systematicSynonym.hashCode()));
        result = ((result* 31)+((this.description == null)? 0 :this.description.hashCode()));
        result = ((result* 31)+((this.fullName == null)? 0 :this.fullName.hashCode()));
        result = ((result* 31)+((this.relatedTo == null)? 0 :this.relatedTo.hashCode()));
        result = ((result* 31)+((this.interactsWith == null)? 0 :this.interactsWith.hashCode()));
        result = ((result* 31)+((this.synonym == null)? 0 :this.synonym.hashCode()));
        result = ((result* 31)+((this.subclassOf == null)? 0 :this.subclassOf.hashCode()));
        result = ((result* 31)+((this.name == null)? 0 :this.name.hashCode()));
        result = ((result* 31)+((this.hasAttributeType == null)? 0 :this.hasAttributeType.hashCode()));
        result = ((result* 31)+((this.id == null)? 0 :this.id.hashCode()));
        result = ((result* 31)+((this.category == null)? 0 :this.category.hashCode()));
        result = ((result* 31)+((this.hasQualitativeValue == null)? 0 :this.hasQualitativeValue.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof Attribute) == false) {
            return false;
        }
        Attribute rhs = ((Attribute) other);
        return ((((((((((((((((this.hasQuantitativeValue == rhs.hasQuantitativeValue)||((this.hasQuantitativeValue!= null)&&this.hasQuantitativeValue.equals(rhs.hasQuantitativeValue)))&&((this.iri == rhs.iri)||((this.iri!= null)&&this.iri.equals(rhs.iri))))&&((this.nodeProperty == rhs.nodeProperty)||((this.nodeProperty!= null)&&this.nodeProperty.equals(rhs.nodeProperty))))&&((this.systematicSynonym == rhs.systematicSynonym)||((this.systematicSynonym!= null)&&this.systematicSynonym.equals(rhs.systematicSynonym))))&&((this.description == rhs.description)||((this.description!= null)&&this.description.equals(rhs.description))))&&((this.fullName == rhs.fullName)||((this.fullName!= null)&&this.fullName.equals(rhs.fullName))))&&((this.relatedTo == rhs.relatedTo)||((this.relatedTo!= null)&&this.relatedTo.equals(rhs.relatedTo))))&&((this.interactsWith == rhs.interactsWith)||((this.interactsWith!= null)&&this.interactsWith.equals(rhs.interactsWith))))&&((this.synonym == rhs.synonym)||((this.synonym!= null)&&this.synonym.equals(rhs.synonym))))&&((this.subclassOf == rhs.subclassOf)||((this.subclassOf!= null)&&this.subclassOf.equals(rhs.subclassOf))))&&((this.name == rhs.name)||((this.name!= null)&&this.name.equals(rhs.name))))&&((this.hasAttributeType == rhs.hasAttributeType)||((this.hasAttributeType!= null)&&this.hasAttributeType.equals(rhs.hasAttributeType))))&&((this.id == rhs.id)||((this.id!= null)&&this.id.equals(rhs.id))))&&((this.category == rhs.category)||((this.category!= null)&&this.category.equals(rhs.category))))&&((this.hasQualitativeValue == rhs.hasQualitativeValue)||((this.hasQualitativeValue!= null)&&this.hasQualitativeValue.equals(rhs.hasQualitativeValue))));
    }

}
