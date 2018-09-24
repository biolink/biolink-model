import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * GeneToGeneHomologyAssociation
 * <p>
 * A homology association between two genes. May be orthology (in which case the species of subject and object should differ) or paralogy (in which case the species may be the same)
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "relation"
})
public class GeneToGeneHomologyAssociation {

    /**
     * homology relationship type
     * (Required)
     * 
     */
    @JsonProperty("relation")
    @JsonPropertyDescription("homology relationship type")
    private String relation;

    /**
     * homology relationship type
     * (Required)
     * 
     */
    @JsonProperty("relation")
    public String getRelation() {
        return relation;
    }

    /**
     * homology relationship type
     * (Required)
     * 
     */
    @JsonProperty("relation")
    public void setRelation(String relation) {
        this.relation = relation;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("relation", relation).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(relation).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof GeneToGeneHomologyAssociation) == false) {
            return false;
        }
        GeneToGeneHomologyAssociation rhs = ((GeneToGeneHomologyAssociation) other);
        return new EqualsBuilder().append(relation, rhs.relation).isEquals();
    }

}
