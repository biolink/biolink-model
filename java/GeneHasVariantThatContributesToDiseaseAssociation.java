import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
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
        StringBuilder sb = new StringBuilder();
        sb.append(GeneHasVariantThatContributesToDiseaseAssociation.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("sequenceVariantQualifier");
        sb.append('=');
        sb.append(((this.sequenceVariantQualifier == null)?"<null>":this.sequenceVariantQualifier));
        sb.append(',');
        sb.append("subject");
        sb.append('=');
        sb.append(((this.subject == null)?"<null>":this.subject));
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
        result = ((result* 31)+((this.sequenceVariantQualifier == null)? 0 :this.sequenceVariantQualifier.hashCode()));
        result = ((result* 31)+((this.subject == null)? 0 :this.subject.hashCode()));
        return result;
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
        return (((this.sequenceVariantQualifier == rhs.sequenceVariantQualifier)||((this.sequenceVariantQualifier!= null)&&this.sequenceVariantQualifier.equals(rhs.sequenceVariantQualifier)))&&((this.subject == rhs.subject)||((this.subject!= null)&&this.subject.equals(rhs.subject))));
    }

}
