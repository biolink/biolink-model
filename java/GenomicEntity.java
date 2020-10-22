import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(GenomicEntity.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("hasBiologicalSequence");
        sb.append('=');
        sb.append(((this.hasBiologicalSequence == null)?"<null>":this.hasBiologicalSequence));
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
        result = ((result* 31)+((this.hasBiologicalSequence == null)? 0 :this.hasBiologicalSequence.hashCode()));
        return result;
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
        return ((this.hasBiologicalSequence == rhs.hasBiologicalSequence)||((this.hasBiologicalSequence!= null)&&this.hasBiologicalSequence.equals(rhs.hasBiologicalSequence)));
    }

}
