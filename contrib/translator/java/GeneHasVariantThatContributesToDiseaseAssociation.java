import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * GeneHasVariantThatContributesToDiseaseAssociation
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "sequence_variant_qualifier",
    "subject"
})
public class GeneHasVariantThatContributesToDiseaseAssociation {

    /**
     * a qualifier used in an association where the variant
     * 
     */
    @JsonProperty("sequence_variant_qualifier")
    @JsonPropertyDescription("a qualifier used in an association where the variant")
    private String sequenceVariantQualifier;
    /**
     * A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.
     * (Required)
     * 
     */
    @JsonProperty("subject")
    @JsonPropertyDescription("A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.")
    private String subject;

    /**
     * a qualifier used in an association where the variant
     * 
     */
    @JsonProperty("sequence_variant_qualifier")
    public String getSequenceVariantQualifier() {
        return sequenceVariantQualifier;
    }

    /**
     * a qualifier used in an association where the variant
     * 
     */
    @JsonProperty("sequence_variant_qualifier")
    public void setSequenceVariantQualifier(String sequenceVariantQualifier) {
        this.sequenceVariantQualifier = sequenceVariantQualifier;
    }

    /**
     * A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.
     * (Required)
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * A gene that has a role in modeling the disease. This may be a model organism ortholog of a known disease gene, or it may be a gene whose mutants recapitulate core features of the disease.
     * (Required)
     * 
     */
    @JsonProperty("subject")
    public void setSubject(String subject) {
        this.subject = subject;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("sequenceVariantQualifier", sequenceVariantQualifier).append("subject", subject).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(sequenceVariantQualifier).append(subject).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof GeneHasVariantThatContributesToDiseaseAssociation) == false) {
            return false;
        }
        GeneHasVariantThatContributesToDiseaseAssociation rhs = ((GeneHasVariantThatContributesToDiseaseAssociation) other);
        return new EqualsBuilder().append(sequenceVariantQualifier, rhs.sequenceVariantQualifier).append(subject, rhs.subject).isEquals();
    }

}
