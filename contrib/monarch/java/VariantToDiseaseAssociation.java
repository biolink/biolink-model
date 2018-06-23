import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * VariantToDiseaseAssociation
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "object",
    "relation",
    "subject"
})
public class VariantToDiseaseAssociation {

    /**
     * a disease that is associated with that variant
     * 
     */
    @JsonProperty("object")
    @JsonPropertyDescription("a disease that is associated with that variant")
    private String object;
    /**
     * E.g. is pathogenic for
     * 
     */
    @JsonProperty("relation")
    @JsonPropertyDescription("E.g. is pathogenic for")
    private String relation;
    /**
     * a sequence variant in which the allele state is associated in some way with the disease state
     * 
     */
    @JsonProperty("subject")
    @JsonPropertyDescription("a sequence variant in which the allele state is associated in some way with the disease state")
    private String subject;

    /**
     * a disease that is associated with that variant
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * a disease that is associated with that variant
     * 
     */
    @JsonProperty("object")
    public void setObject(String object) {
        this.object = object;
    }

    /**
     * E.g. is pathogenic for
     * 
     */
    @JsonProperty("relation")
    public String getRelation() {
        return relation;
    }

    /**
     * E.g. is pathogenic for
     * 
     */
    @JsonProperty("relation")
    public void setRelation(String relation) {
        this.relation = relation;
    }

    /**
     * a sequence variant in which the allele state is associated in some way with the disease state
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * a sequence variant in which the allele state is associated in some way with the disease state
     * 
     */
    @JsonProperty("subject")
    public void setSubject(String subject) {
        this.subject = subject;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("object", object).append("relation", relation).append("subject", subject).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(subject).append(object).append(relation).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof VariantToDiseaseAssociation) == false) {
            return false;
        }
        VariantToDiseaseAssociation rhs = ((VariantToDiseaseAssociation) other);
        return new EqualsBuilder().append(subject, rhs.subject).append(object, rhs.object).append(relation, rhs.relation).isEquals();
    }

}
