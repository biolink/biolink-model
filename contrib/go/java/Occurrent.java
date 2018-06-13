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
    private String hasInput;
    /**
     * holds between a process and a continuant, where the continuant is somehow involved in the process 
     * 
     */
    @JsonProperty("has_participant")
    @JsonPropertyDescription("holds between a process and a continuant, where the continuant is somehow involved in the process ")
    private String hasParticipant;
    /**
     * holds between two processes, where one completes before the other begins
     * 
     */
    @JsonProperty("precedes")
    @JsonPropertyDescription("holds between two processes, where one completes before the other begins")
    private String precedes;
    /**
     * describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
     * 
     */
    @JsonProperty("regulates_process_to_process")
    @JsonPropertyDescription("describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.")
    private String regulatesProcessToProcess;

    /**
     * holds between a process and a continuant, where the continuant is an input into the process
     * 
     */
    @JsonProperty("has_input")
    public String getHasInput() {
        return hasInput;
    }

    /**
     * holds between a process and a continuant, where the continuant is an input into the process
     * 
     */
    @JsonProperty("has_input")
    public void setHasInput(String hasInput) {
        this.hasInput = hasInput;
    }

    /**
     * holds between a process and a continuant, where the continuant is somehow involved in the process 
     * 
     */
    @JsonProperty("has_participant")
    public String getHasParticipant() {
        return hasParticipant;
    }

    /**
     * holds between a process and a continuant, where the continuant is somehow involved in the process 
     * 
     */
    @JsonProperty("has_participant")
    public void setHasParticipant(String hasParticipant) {
        this.hasParticipant = hasParticipant;
    }

    /**
     * holds between two processes, where one completes before the other begins
     * 
     */
    @JsonProperty("precedes")
    public String getPrecedes() {
        return precedes;
    }

    /**
     * holds between two processes, where one completes before the other begins
     * 
     */
    @JsonProperty("precedes")
    public void setPrecedes(String precedes) {
        this.precedes = precedes;
    }

    /**
     * describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
     * 
     */
    @JsonProperty("regulates_process_to_process")
    public String getRegulatesProcessToProcess() {
        return regulatesProcessToProcess;
    }

    /**
     * describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
     * 
     */
    @JsonProperty("regulates_process_to_process")
    public void setRegulatesProcessToProcess(String regulatesProcessToProcess) {
        this.regulatesProcessToProcess = regulatesProcessToProcess;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("hasInput", hasInput).append("hasParticipant", hasParticipant).append("precedes", precedes).append("regulatesProcessToProcess", regulatesProcessToProcess).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(precedes).append(regulatesProcessToProcess).append(hasInput).append(hasParticipant).toHashCode();
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
        return new EqualsBuilder().append(precedes, rhs.precedes).append(regulatesProcessToProcess, rhs.regulatesProcessToProcess).append(hasInput, rhs.hasInput).append(hasParticipant, rhs.hasParticipant).isEquals();
    }

}
