import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * GeneToPhenotypicFeatureAssociation
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "subject"
})
public class GeneToPhenotypicFeatureAssociation {

    /**
     * gene in which variation is correlated with the phenotypic feature
     * 
     */
    @JsonProperty("subject")
    @JsonPropertyDescription("gene in which variation is correlated with the phenotypic feature")
    private String subject;

    /**
     * gene in which variation is correlated with the phenotypic feature
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * gene in which variation is correlated with the phenotypic feature
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
        if ((other instanceof GeneToPhenotypicFeatureAssociation) == false) {
            return false;
        }
        GeneToPhenotypicFeatureAssociation rhs = ((GeneToPhenotypicFeatureAssociation) other);
        return new EqualsBuilder().append(subject, rhs.subject).isEquals();
    }

}
