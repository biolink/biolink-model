import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * ClinicalEntity
 * <p>
 * Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "id",
    "label"
})
public class ClinicalEntity {

    @JsonProperty("id")
    private String id;
    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    @JsonPropertyDescription("A human-readable name for a thing")
    private String label;

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
        return new ToStringBuilder(this).append("id", id).append("label", label).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(id).append(label).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof ClinicalEntity) == false) {
            return false;
        }
        ClinicalEntity rhs = ((ClinicalEntity) other);
        return new EqualsBuilder().append(id, rhs.id).append(label, rhs.label).isEquals();
    }

}
