import java.util.ArrayList;
import java.util.List;
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
    "enabled_by",
    "has_input",
    "has_output"
})
public class MolecularActivity {

    @JsonProperty("enabled_by")
    private List<String> enabledBy = new ArrayList<String>();
    @JsonProperty("has_input")
    private List<String> hasInput = new ArrayList<String>();
    @JsonProperty("has_output")
    private List<String> hasOutput = new ArrayList<String>();

    @JsonProperty("enabled_by")
    public List<String> getEnabledBy() {
        return enabledBy;
    }

    @JsonProperty("enabled_by")
    public void setEnabledBy(List<String> enabledBy) {
        this.enabledBy = enabledBy;
    }

    @JsonProperty("has_input")
    public List<String> getHasInput() {
        return hasInput;
    }

    @JsonProperty("has_input")
    public void setHasInput(List<String> hasInput) {
        this.hasInput = hasInput;
    }

    @JsonProperty("has_output")
    public List<String> getHasOutput() {
        return hasOutput;
    }

    @JsonProperty("has_output")
    public void setHasOutput(List<String> hasOutput) {
        this.hasOutput = hasOutput;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("enabledBy", enabledBy).append("hasInput", hasInput).append("hasOutput", hasOutput).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(enabledBy).append(hasOutput).append(hasInput).toHashCode();
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
        return new EqualsBuilder().append(enabledBy, rhs.enabledBy).append(hasOutput, rhs.hasOutput).append(hasInput, rhs.hasInput).isEquals();
    }

}
