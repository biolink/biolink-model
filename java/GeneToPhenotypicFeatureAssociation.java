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
    "frequency_qualifier",
    "onset_qualifier",
    "severity_qualifier",
    "sex_qualifier",
    "subject"
})
public class GeneToPhenotypicFeatureAssociation {

    /**
     * a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
     * 
     */
    @JsonProperty("frequency_qualifier")
    @JsonPropertyDescription("a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject")
    private String frequencyQualifier;
    /**
     * a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
     * 
     */
    @JsonProperty("onset_qualifier")
    @JsonPropertyDescription("a qualifier used in a phenotypic association to state when the phenotype appears is in the subject")
    private String onsetQualifier;
    /**
     * a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
     * 
     */
    @JsonProperty("severity_qualifier")
    @JsonPropertyDescription("a qualifier used in a phenotypic association to state how severe the phenotype is in the subject")
    private String severityQualifier;
    /**
     * a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
     * 
     */
    @JsonProperty("sex_qualifier")
    @JsonPropertyDescription("a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.")
    private String sexQualifier;
    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    private String subject;

    /**
     * a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
     * 
     */
    @JsonProperty("frequency_qualifier")
    public String getFrequencyQualifier() {
        return frequencyQualifier;
    }

    /**
     * a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
     * 
     */
    @JsonProperty("frequency_qualifier")
    public void setFrequencyQualifier(String frequencyQualifier) {
        this.frequencyQualifier = frequencyQualifier;
    }

    /**
     * a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
     * 
     */
    @JsonProperty("onset_qualifier")
    public String getOnsetQualifier() {
        return onsetQualifier;
    }

    /**
     * a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
     * 
     */
    @JsonProperty("onset_qualifier")
    public void setOnsetQualifier(String onsetQualifier) {
        this.onsetQualifier = onsetQualifier;
    }

    /**
     * a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
     * 
     */
    @JsonProperty("severity_qualifier")
    public String getSeverityQualifier() {
        return severityQualifier;
    }

    /**
     * a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
     * 
     */
    @JsonProperty("severity_qualifier")
    public void setSeverityQualifier(String severityQualifier) {
        this.severityQualifier = severityQualifier;
    }

    /**
     * a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
     * 
     */
    @JsonProperty("sex_qualifier")
    public String getSexQualifier() {
        return sexQualifier;
    }

    /**
     * a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
     * 
     */
    @JsonProperty("sex_qualifier")
    public void setSexQualifier(String sexQualifier) {
        this.sexQualifier = sexQualifier;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    public void setSubject(String subject) {
        this.subject = subject;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("frequencyQualifier", frequencyQualifier).append("onsetQualifier", onsetQualifier).append("severityQualifier", severityQualifier).append("sexQualifier", sexQualifier).append("subject", subject).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(frequencyQualifier).append(sexQualifier).append(onsetQualifier).append(severityQualifier).append(subject).toHashCode();
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
        return new EqualsBuilder().append(frequencyQualifier, rhs.frequencyQualifier).append(sexQualifier, rhs.sexQualifier).append(onsetQualifier, rhs.onsetQualifier).append(severityQualifier, rhs.severityQualifier).append(subject, rhs.subject).isEquals();
    }

}
