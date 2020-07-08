import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(MolecularActivity.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("enabledBy");
        sb.append('=');
        sb.append(((this.enabledBy == null)?"<null>":this.enabledBy));
        sb.append(',');
        sb.append("hasInput");
        sb.append('=');
        sb.append(((this.hasInput == null)?"<null>":this.hasInput));
        sb.append(',');
        sb.append("hasOutput");
        sb.append('=');
        sb.append(((this.hasOutput == null)?"<null>":this.hasOutput));
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
        result = ((result* 31)+((this.enabledBy == null)? 0 :this.enabledBy.hashCode()));
        result = ((result* 31)+((this.hasOutput == null)? 0 :this.hasOutput.hashCode()));
        result = ((result* 31)+((this.hasInput == null)? 0 :this.hasInput.hashCode()));
        return result;
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
        return ((((this.enabledBy == rhs.enabledBy)||((this.enabledBy!= null)&&this.enabledBy.equals(rhs.enabledBy)))&&((this.hasOutput == rhs.hasOutput)||((this.hasOutput!= null)&&this.hasOutput.equals(rhs.hasOutput))))&&((this.hasInput == rhs.hasInput)||((this.hasInput!= null)&&this.hasInput.equals(rhs.hasInput))));
    }

}
