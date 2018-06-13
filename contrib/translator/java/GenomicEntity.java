import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * GenomicEntity
 * <p>
 * an entity that can either be directly located on a genome (gene, transcript, exon, regulatory region) or is encoded in a genome (protein)
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "has_biological_sequence"
})
public class GenomicEntity {

    /**
     * connects a genomic feature to its sequence
     * 
     */
    @JsonProperty("has_biological_sequence")
    @JsonPropertyDescription("connects a genomic feature to its sequence")
    private String hasBiologicalSequence;

    /**
     * connects a genomic feature to its sequence
     * 
     */
    @JsonProperty("has_biological_sequence")
    public String getHasBiologicalSequence() {
        return hasBiologicalSequence;
    }

    /**
     * connects a genomic feature to its sequence
     * 
     */
    @JsonProperty("has_biological_sequence")
    public void setHasBiologicalSequence(String hasBiologicalSequence) {
        this.hasBiologicalSequence = hasBiologicalSequence;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("hasBiologicalSequence", hasBiologicalSequence).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasBiologicalSequence).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof GenomicEntity) == false) {
            return false;
        }
        GenomicEntity rhs = ((GenomicEntity) other);
        return new EqualsBuilder().append(hasBiologicalSequence, rhs.hasBiologicalSequence).isEquals();
    }

}
