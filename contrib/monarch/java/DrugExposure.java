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
 * DrugExposure
 * <p>
 * A drug exposure is an intake of a particular chemical substance
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "drug",
    "id",
    "label"
})
public class DrugExposure {

    @JsonProperty("drug")
    private List<String> drug = new ArrayList<String>();
    @JsonProperty("id")
    private String id;
    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    @JsonPropertyDescription("A human-readable name for a thing")
    private String label;

    @JsonProperty("drug")
    public List<String> getDrug() {
        return drug;
    }

    @JsonProperty("drug")
    public void setDrug(List<String> drug) {
        this.drug = drug;
    }

    @JsonProperty("id")
    public String getId() {
        return id;
    }

    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    public String getLabel() {
        return label;
    }

    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    public void setLabel(String label) {
        this.label = label;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("drug", drug).append("id", id).append("label", label).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(id).append(label).append(drug).toHashCode();
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
        return new EqualsBuilder().append(id, rhs.id).append(label, rhs.label).append(drug, rhs.drug).isEquals();
    }

}
