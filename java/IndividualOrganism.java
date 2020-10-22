import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * IndividualOrganism
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "in_taxon"
})
public class IndividualOrganism {

    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    @JsonPropertyDescription("connects a thing to a class representing a taxon")
    private List<String> inTaxon = new ArrayList<String>();

    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    public List<String> getInTaxon() {
        return inTaxon;
    }

    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    public void setInTaxon(List<String> inTaxon) {
        this.inTaxon = inTaxon;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(IndividualOrganism.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("inTaxon");
        sb.append('=');
        sb.append(((this.inTaxon == null)?"<null>":this.inTaxon));
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
        result = ((result* 31)+((this.inTaxon == null)? 0 :this.inTaxon.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof IndividualOrganism) == false) {
            return false;
        }
        IndividualOrganism rhs = ((IndividualOrganism) other);
        return ((this.inTaxon == rhs.inTaxon)||((this.inTaxon!= null)&&this.inTaxon.equals(rhs.inTaxon)));
    }

}
