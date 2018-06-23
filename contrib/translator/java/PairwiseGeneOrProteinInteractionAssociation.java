import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * PairwiseGeneOrProteinInteractionAssociation
 * <p>
 * An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "relation"
})
public class PairwiseGeneOrProteinInteractionAssociation {

    /**
     * interaction relationship type
     * 
     */
    @JsonProperty("relation")
    @JsonPropertyDescription("interaction relationship type")
    private String relation;

    /**
     * interaction relationship type
     * 
     */
    @JsonProperty("relation")
    public String getRelation() {
        return relation;
    }

    /**
     * interaction relationship type
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
        if ((other instanceof PairwiseGeneOrProteinInteractionAssociation) == false) {
            return false;
        }
        PairwiseGeneOrProteinInteractionAssociation rhs = ((PairwiseGeneOrProteinInteractionAssociation) other);
        return new EqualsBuilder().append(relation, rhs.relation).isEquals();
    }

}
