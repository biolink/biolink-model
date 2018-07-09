import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * GeneToDiseaseAssociation
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "subject"
})
public class GeneToDiseaseAssociation {

    /**
     * gene in which variation is correlated with the disease - may be protective or causative or associative, or as a model
     * 
     */
    @JsonProperty("subject")
    @JsonPropertyDescription("gene in which variation is correlated with the disease - may be protective or causative or associative, or as a model")
    private String subject;

    /**
     * gene in which variation is correlated with the disease - may be protective or causative or associative, or as a model
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * gene in which variation is correlated with the disease - may be protective or causative or associative, or as a model
     * 
     */
    @JsonProperty("subject")
    public void setSubject(String subject) {
        this.subject = subject;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("subject", subject).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(subject).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof GeneToDiseaseAssociation) == false) {
            return false;
        }
        GeneToDiseaseAssociation rhs = ((GeneToDiseaseAssociation) other);
        return new EqualsBuilder().append(subject, rhs.subject).isEquals();
    }

}
