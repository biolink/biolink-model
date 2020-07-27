import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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

    @JsonProperty("has_biological_sequence")
    private String hasBiologicalSequence;
    @JsonProperty("has_gene")
    private List<String> hasGene = new ArrayList<String>();
    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("id")
    private String id;

    @JsonProperty("has_biological_sequence")
    public String getHasBiologicalSequence() {
        return hasBiologicalSequence;
    }

    @JsonProperty("has_biological_sequence")
    public void setHasBiologicalSequence(String hasBiologicalSequence) {
        this.hasBiologicalSequence = hasBiologicalSequence;
    }

    @JsonProperty("has_gene")
    public List<String> getHasGene() {
        return hasGene;
    }

    @JsonProperty("has_gene")
    public void setHasGene(List<String> hasGene) {
        this.hasGene = hasGene;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("id")
    public String getId() {
        return id;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(SequenceVariant.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("hasBiologicalSequence");
        sb.append('=');
        sb.append(((this.hasBiologicalSequence == null)?"<null>":this.hasBiologicalSequence));
        sb.append(',');
        sb.append("hasGene");
        sb.append('=');
        sb.append(((this.hasGene == null)?"<null>":this.hasGene));
        sb.append(',');
        sb.append("id");
        sb.append('=');
        sb.append(((this.id == null)?"<null>":this.id));
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
        result = ((result* 31)+((this.hasGene == null)? 0 :this.hasGene.hashCode()));
        result = ((result* 31)+((this.id == null)? 0 :this.id.hashCode()));
        return result;
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
        return ((((this.hasBiologicalSequence == rhs.hasBiologicalSequence)||((this.hasBiologicalSequence!= null)&&this.hasBiologicalSequence.equals(rhs.hasBiologicalSequence)))&&((this.hasGene == rhs.hasGene)||((this.hasGene!= null)&&this.hasGene.equals(rhs.hasGene))))&&((this.id == rhs.id)||((this.id!= null)&&this.id.equals(rhs.id))));
    }

}
