import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * PairwiseGeneToGeneInteraction
 * <p>
 * An interaction between two genes or two gene products. May be physical (e.g. protein binding) or genetic (between genes). May be symmetric (e.g. protein interaction) or directed (e.g. phosphorylation)
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "relation"
})
public class PairwiseGeneToGeneInteraction {

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("relation")
    private String relation;

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("relation")
    public String getRelation() {
        return relation;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("relation")
    public void setRelation(String relation) {
        this.relation = relation;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(PairwiseGeneToGeneInteraction.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("relation");
        sb.append('=');
        sb.append(((this.relation == null)?"<null>":this.relation));
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
        result = ((result* 31)+((this.relation == null)? 0 :this.relation.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof PairwiseGeneToGeneInteraction) == false) {
            return false;
        }
        PairwiseGeneToGeneInteraction rhs = ((PairwiseGeneToGeneInteraction) other);
        return ((this.relation == rhs.relation)||((this.relation!= null)&&this.relation.equals(rhs.relation)));
    }

}
