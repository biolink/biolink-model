import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * PropertyValuePair
 * <p>
 * null
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "filler",
    "relation"
})
public class PropertyValuePair {

    /**
     * The value in a property-value tuple
     * 
     */
    @JsonProperty("filler")
    @JsonPropertyDescription("The value in a property-value tuple")
    private String filler;
    /**
     * the relationship type by which a subject is connected to an object in an association
     * 
     */
    @JsonProperty("relation")
    @JsonPropertyDescription("the relationship type by which a subject is connected to an object in an association")
    private String relation;

    /**
     * The value in a property-value tuple
     * 
     */
    @JsonProperty("filler")
    public String getFiller() {
        return filler;
    }

    /**
     * The value in a property-value tuple
     * 
     */
    @JsonProperty("filler")
    public void setFiller(String filler) {
        this.filler = filler;
    }

    /**
     * the relationship type by which a subject is connected to an object in an association
     * 
     */
    @JsonProperty("relation")
    public String getRelation() {
        return relation;
    }

    /**
     * the relationship type by which a subject is connected to an object in an association
     * 
     */
    @JsonProperty("relation")
    public void setRelation(String relation) {
        this.relation = relation;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("filler", filler).append("relation", relation).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(filler).append(relation).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof PropertyValuePair) == false) {
            return false;
        }
        PropertyValuePair rhs = ((PropertyValuePair) other);
        return new EqualsBuilder().append(filler, rhs.filler).append(relation, rhs.relation).isEquals();
    }

}
