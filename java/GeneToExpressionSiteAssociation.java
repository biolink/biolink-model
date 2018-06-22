import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
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
     * location in which the gene is expressed
     * 
     */
    @JsonProperty("object")
    @JsonPropertyDescription("location in which the gene is expressed")
    private String object;
    /**
     * can be used to indicate magnitude, or also ranking
     * 
     */
    @JsonProperty("quantifier_qualifier")
    @JsonPropertyDescription("can be used to indicate magnitude, or also ranking")
    private String quantifierQualifier;
    /**
     * expression relationship
     * 
     */
    @JsonProperty("relation")
    @JsonPropertyDescription("expression relationship")
    private String relation;
    /**
     * stage at which the gene is expressed in the site
     * 
     */
    @JsonProperty("stage_qualifier")
    @JsonPropertyDescription("stage at which the gene is expressed in the site")
    private String stageQualifier;
    /**
     * gene in which variation is correlated with the phenotypic feature
     * 
     */
    @JsonProperty("subject")
    @JsonPropertyDescription("gene in which variation is correlated with the phenotypic feature")
    private String subject;

    /**
     * location in which the gene is expressed
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * location in which the gene is expressed
     * 
     */
    @JsonProperty("object")
    public void setObject(String object) {
        this.object = object;
    }

    /**
     * can be used to indicate magnitude, or also ranking
     * 
     */
    @JsonProperty("quantifier_qualifier")
    public String getQuantifierQualifier() {
        return quantifierQualifier;
    }

    /**
     * can be used to indicate magnitude, or also ranking
     * 
     */
    @JsonProperty("quantifier_qualifier")
    public void setQuantifierQualifier(String quantifierQualifier) {
        this.quantifierQualifier = quantifierQualifier;
    }

    /**
     * expression relationship
     * 
     */
    @JsonProperty("relation")
    public String getRelation() {
        return relation;
    }

    /**
     * expression relationship
     * 
     */
    @JsonProperty("relation")
    public void setRelation(String relation) {
        this.relation = relation;
    }

    /**
     * stage at which the gene is expressed in the site
     * 
     */
    @JsonProperty("stage_qualifier")
    public String getStageQualifier() {
        return stageQualifier;
    }

    /**
     * stage at which the gene is expressed in the site
     * 
     */
    @JsonProperty("stage_qualifier")
    public void setStageQualifier(String stageQualifier) {
        this.stageQualifier = stageQualifier;
    }

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
