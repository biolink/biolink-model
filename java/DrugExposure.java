import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * DrugExposure
 * <p>
 * A drug exposure is an intake of a particular chemical substance
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "has_drug"
})
public class DrugExposure {

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("has_drug")
    private List<String> hasDrug = new ArrayList<String>();

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("has_drug")
    public List<String> getHasDrug() {
        return hasDrug;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("has_drug")
    public void setHasDrug(List<String> hasDrug) {
        this.hasDrug = hasDrug;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(DrugExposure.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("hasDrug");
        sb.append('=');
        sb.append(((this.hasDrug == null)?"<null>":this.hasDrug));
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
        result = ((result* 31)+((this.hasDrug == null)? 0 :this.hasDrug.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof DrugExposure) == false) {
            return false;
        }
        DrugExposure rhs = ((DrugExposure) other);
        return ((this.hasDrug == rhs.hasDrug)||((this.hasDrug!= null)&&this.hasDrug.equals(rhs.hasDrug)));
    }

}
