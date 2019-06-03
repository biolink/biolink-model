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
 * Occurrent
 * <p>
 * A processual entity
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "has_input",
    "has_participant",
    "negatively_regulates_process_to_process",
    "positively_regulates_process_to_process",
    "precedes",
    "regulates_process_to_process"
})
public class Occurrent {

    /**
     * holds between a process and a continuant, where the continuant is an input into the process
     * 
     */
    @JsonProperty("has_input")
    @JsonPropertyDescription("holds between a process and a continuant, where the continuant is an input into the process")
    private List<String> hasInput = new ArrayList<String>();
    /**
     * holds between a process and a continuant, where the continuant is somehow involved in the process
     * 
     */
    @JsonProperty("has_participant")
    @JsonPropertyDescription("holds between a process and a continuant, where the continuant is somehow involved in the process")
    private List<String> hasParticipant = new ArrayList<String>();
    @JsonProperty("negatively_regulates_process_to_process")
    private List<String> negativelyRegulatesProcessToProcess = new ArrayList<String>();
    @JsonProperty("positively_regulates_process_to_process")
    private List<String> positivelyRegulatesProcessToProcess = new ArrayList<String>();
    /**
     * holds between two processes, where one completes before the other begins
     * 
     */
    @JsonProperty("precedes")
    @JsonPropertyDescription("holds between two processes, where one completes before the other begins")
    private List<String> precedes = new ArrayList<String>();
    @JsonProperty("regulates_process_to_process")
    private List<String> regulatesProcessToProcess = new ArrayList<String>();

    /**
     * holds between a process and a continuant, where the continuant is an input into the process
     * 
     */
    @JsonProperty("has_input")
    public List<String> getHasInput() {
        return hasInput;
    }

    /**
     * holds between a process and a continuant, where the continuant is an input into the process
     * 
     */
    @JsonProperty("has_input")
    public void setHasInput(List<String> hasInput) {
        this.hasInput = hasInput;
    }

    /**
     * holds between a process and a continuant, where the continuant is somehow involved in the process
     * 
     */
    @JsonProperty("has_participant")
    public List<String> getHasParticipant() {
        return hasParticipant;
    }

    /**
     * holds between a process and a continuant, where the continuant is somehow involved in the process
     * 
     */
    @JsonProperty("has_participant")
    public void setHasParticipant(List<String> hasParticipant) {
        this.hasParticipant = hasParticipant;
    }

    @JsonProperty("negatively_regulates_process_to_process")
    public List<String> getNegativelyRegulatesProcessToProcess() {
        return negativelyRegulatesProcessToProcess;
    }

    @JsonProperty("negatively_regulates_process_to_process")
    public void setNegativelyRegulatesProcessToProcess(List<String> negativelyRegulatesProcessToProcess) {
        this.negativelyRegulatesProcessToProcess = negativelyRegulatesProcessToProcess;
    }

    @JsonProperty("positively_regulates_process_to_process")
    public List<String> getPositivelyRegulatesProcessToProcess() {
        return positivelyRegulatesProcessToProcess;
    }

    @JsonProperty("positively_regulates_process_to_process")
    public void setPositivelyRegulatesProcessToProcess(List<String> positivelyRegulatesProcessToProcess) {
        this.positivelyRegulatesProcessToProcess = positivelyRegulatesProcessToProcess;
    }

    /**
     * holds between two processes, where one completes before the other begins
     * 
     */
    @JsonProperty("precedes")
    public List<String> getPrecedes() {
        return precedes;
    }

    /**
     * holds between two processes, where one completes before the other begins
     * 
     */
    @JsonProperty("precedes")
    public void setPrecedes(List<String> precedes) {
        this.precedes = precedes;
    }

    @JsonProperty("regulates_process_to_process")
    public List<String> getRegulatesProcessToProcess() {
        return regulatesProcessToProcess;
    }

    @JsonProperty("regulates_process_to_process")
    public void setRegulatesProcessToProcess(List<String> regulatesProcessToProcess) {
        this.regulatesProcessToProcess = regulatesProcessToProcess;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("hasInput", hasInput).append("hasParticipant", hasParticipant).append("negativelyRegulatesProcessToProcess", negativelyRegulatesProcessToProcess).append("positivelyRegulatesProcessToProcess", positivelyRegulatesProcessToProcess).append("precedes", precedes).append("regulatesProcessToProcess", regulatesProcessToProcess).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(precedes).append(positivelyRegulatesProcessToProcess).append(regulatesProcessToProcess).append(negativelyRegulatesProcessToProcess).append(hasInput).append(hasParticipant).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof Occurrent) == false) {
            return false;
        }
        Occurrent rhs = ((Occurrent) other);
        return new EqualsBuilder().append(precedes, rhs.precedes).append(positivelyRegulatesProcessToProcess, rhs.positivelyRegulatesProcessToProcess).append(regulatesProcessToProcess, rhs.regulatesProcessToProcess).append(negativelyRegulatesProcessToProcess, rhs.negativelyRegulatesProcessToProcess).append(hasInput, rhs.hasInput).append(hasParticipant, rhs.hasParticipant).isEquals();
    }

}
