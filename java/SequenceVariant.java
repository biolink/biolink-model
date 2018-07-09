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
 * SequenceVariant
 * <p>
 * An allele that varies in its sequence from what is considered the reference allele at that locus.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "has_biological_sequence",
    "has_gene",
    "id"
})
public class SequenceVariant {

    /**
     * The state of the sequence w.r.t a reference sequence
     * 
     */
    @JsonProperty("has_biological_sequence")
    @JsonPropertyDescription("The state of the sequence w.r.t a reference sequence")
    private String hasBiologicalSequence;
    /**
     * Each allele can be associated with any number of genes
     * 
     */
    @JsonProperty("has_gene")
    @JsonPropertyDescription("Each allele can be associated with any number of genes")
    private List<String> hasGene = new ArrayList<String>();
    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * 
     */
    @JsonProperty("id")
    @JsonPropertyDescription("A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI")
    private String id;

    /**
     * The state of the sequence w.r.t a reference sequence
     * 
     */
    @JsonProperty("has_biological_sequence")
    public String getHasBiologicalSequence() {
        return hasBiologicalSequence;
    }

    /**
     * The state of the sequence w.r.t a reference sequence
     * 
     */
    @JsonProperty("has_biological_sequence")
    public void setHasBiologicalSequence(String hasBiologicalSequence) {
        this.hasBiologicalSequence = hasBiologicalSequence;
    }

    /**
     * Each allele can be associated with any number of genes
     * 
     */
    @JsonProperty("has_gene")
    public List<String> getHasGene() {
        return hasGene;
    }

    /**
     * Each allele can be associated with any number of genes
     * 
     */
    @JsonProperty("has_gene")
    public void setHasGene(List<String> hasGene) {
        this.hasGene = hasGene;
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

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("hasBiologicalSequence", hasBiologicalSequence).append("hasGene", hasGene).append("id", id).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasBiologicalSequence).append(hasGene).append(id).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof SequenceVariant) == false) {
            return false;
        }
        SequenceVariant rhs = ((SequenceVariant) other);
        return new EqualsBuilder().append(hasBiologicalSequence, rhs.hasBiologicalSequence).append(hasGene, rhs.hasGene).append(id, rhs.id).isEquals();
    }

}
