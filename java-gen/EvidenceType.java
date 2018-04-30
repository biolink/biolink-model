import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * EvidenceType
 * <p>
 * Class of evidence that supports an association
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "category",
    "id",
    "name"
})
public class EvidenceType {

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * 
     */
    @JsonProperty("category")
    @JsonPropertyDescription("Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag")
    private String category;
    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * 
     */
    @JsonProperty("id")
    @JsonPropertyDescription("A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI")
    private String id;
    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("name")
    @JsonPropertyDescription("A human-readable name for a thing")
    private String name;

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * 
     */
    @JsonProperty("category")
    public String getCategory() {
        return category;
    }

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * 
     */
    @JsonProperty("category")
    public void setCategory(String category) {
        this.category = category;
    }

    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * 
     */
    @JsonProperty("id")
    public String getId() {
        return id;
    }

    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * 
     */
    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("name")
    public String getName() {
        return name;
    }

    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("name")
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("category", category).append("id", id).append("name", name).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(name).append(id).append(category).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof EvidenceType) == false) {
            return false;
        }
        EvidenceType rhs = ((EvidenceType) other);
        return new EqualsBuilder().append(name, rhs.name).append(id, rhs.id).append(category, rhs.category).isEquals();
    }

}
