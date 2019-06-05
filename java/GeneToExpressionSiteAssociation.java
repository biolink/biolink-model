import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * GeneToExpressionSiteAssociation
 * <p>
 * An association between a gene and an expression site, possibly qualified by stage/timing info.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "object",
    "quantifier_qualifier",
    "relation",
    "stage_qualifier",
    "subject"
})
public class GeneToExpressionSiteAssociation {

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    private String object;
    @JsonProperty("quantifier_qualifier")
    private String quantifierQualifier;
    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("relation")
    private String relation;
    @JsonProperty("stage_qualifier")
    private String stageQualifier;
    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    private String subject;

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    public void setObject(String object) {
        this.object = object;
    }

    @JsonProperty("quantifier_qualifier")
    public String getQuantifierQualifier() {
        return quantifierQualifier;
    }

    @JsonProperty("quantifier_qualifier")
    public void setQuantifierQualifier(String quantifierQualifier) {
        this.quantifierQualifier = quantifierQualifier;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("relation")
    public String getRelation() {
        return relation;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("relation")
    public void setRelation(String relation) {
        this.relation = relation;
    }

    @JsonProperty("stage_qualifier")
    public String getStageQualifier() {
        return stageQualifier;
    }

    @JsonProperty("stage_qualifier")
    public void setStageQualifier(String stageQualifier) {
        this.stageQualifier = stageQualifier;
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
        return new ToStringBuilder(this).append("object", object).append("quantifierQualifier", quantifierQualifier).append("relation", relation).append("stageQualifier", stageQualifier).append("subject", subject).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(stageQualifier).append(quantifierQualifier).append(subject).append(object).append(relation).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof GeneToExpressionSiteAssociation) == false) {
            return false;
        }
        GeneToExpressionSiteAssociation rhs = ((GeneToExpressionSiteAssociation) other);
        return new EqualsBuilder().append(stageQualifier, rhs.stageQualifier).append(quantifierQualifier, rhs.quantifierQualifier).append(subject, rhs.subject).append(object, rhs.object).append(relation, rhs.relation).isEquals();
    }

}
