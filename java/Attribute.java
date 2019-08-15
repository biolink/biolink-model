import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * Attribute
 * <p>
 * A property or characteristic of an entity
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "category",
    "description",
    "full_name",
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
        return new ToStringBuilder(this).append("category", category).append("description", description).append("fullName", fullName).append("id", id).append("interactsWith", interactsWith).append("iri", iri).append("name", name).append("nodeProperty", nodeProperty).append("relatedTo", relatedTo).append("subclassOf", subclassOf).append("synonym", synonym).append("systematicSynonym", systematicSynonym).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(iri).append(nodeProperty).append(systematicSynonym).append(description).append(fullName).append(relatedTo).append(interactsWith).append(synonym).append(subclassOf).append(name).append(id).append(category).toHashCode();
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
        return new EqualsBuilder().append(iri, rhs.iri).append(nodeProperty, rhs.nodeProperty).append(systematicSynonym, rhs.systematicSynonym).append(description, rhs.description).append(fullName, rhs.fullName).append(relatedTo, rhs.relatedTo).append(interactsWith, rhs.interactsWith).append(synonym, rhs.synonym).append(subclassOf, rhs.subclassOf).append(name, rhs.name).append(id, rhs.id).append(category, rhs.category).isEquals();
    }

}
