import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


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
        return new ToStringBuilder(this).append("hasDrug", hasDrug).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasDrug).toHashCode();
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
        return new EqualsBuilder().append(hasDrug, rhs.hasDrug).isEquals();
    }

}
