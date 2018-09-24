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
    "drug"
})
public class DrugExposure {

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("drug")
    private List<String> drug = new ArrayList<String>();

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("drug")
    public List<String> getDrug() {
        return drug;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("drug")
    public void setDrug(List<String> drug) {
        this.drug = drug;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("drug", drug).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(drug).toHashCode();
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
        return new EqualsBuilder().append(drug, rhs.drug).isEquals();
    }

}
