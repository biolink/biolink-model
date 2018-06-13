import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * MolecularActivity
 * <p>
 * An execution of a molecular function carried out by a gene product or macromolecular complex.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "enabled_by"
})
public class MolecularActivity {

    @JsonProperty("enabled_by")
    private String enabledBy;

    @JsonProperty("enabled_by")
    public String getEnabledBy() {
        return enabledBy;
    }

    @JsonProperty("enabled_by")
    public void setEnabledBy(String enabledBy) {
        this.enabledBy = enabledBy;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("enabledBy", enabledBy).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(enabledBy).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof MolecularActivity) == false) {
            return false;
        }
        MolecularActivity rhs = ((MolecularActivity) other);
        return new EqualsBuilder().append(enabledBy, rhs.enabledBy).isEquals();
    }

}
