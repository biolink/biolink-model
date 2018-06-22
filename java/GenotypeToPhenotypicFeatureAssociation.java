import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * GenotypeToPhenotypicFeatureAssociation
 * <p>
 * Any association between one genotype and a phenotypic feature, where having the genotype confers the phenotype, either in isolation or through environment
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "relation",
    "subject"
})
public class GenotypeToPhenotypicFeatureAssociation {

    /**
     * the relationship type by which a subject is connected to an object in an association
     * 
     */
    @JsonProperty("relation")
    @JsonPropertyDescription("the relationship type by which a subject is connected to an object in an association")
    private String relation;
    /**
     * genotype that is associated with the phenotypic feature
     * 
     */
    @JsonProperty("subject")
    @JsonPropertyDescription("genotype that is associated with the phenotypic feature")
    private String subject;

    /**
     * the relationship type by which a subject is connected to an object in an association
     * 
     */
    @JsonProperty("relation")
    public String getRelation() {
        return relation;
    }

    /**
     * the relationship type by which a subject is connected to an object in an association
     * 
     */
    @JsonProperty("relation")
    public void setRelation(String relation) {
        this.relation = relation;
    }

    /**
     * genotype that is associated with the phenotypic feature
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * genotype that is associated with the phenotypic feature
     * 
     */
    @JsonProperty("subject")
    public void setSubject(String subject) {
        this.subject = subject;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("relation", relation).append("subject", subject).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(subject).append(relation).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof GenotypeToPhenotypicFeatureAssociation) == false) {
            return false;
        }
        GenotypeToPhenotypicFeatureAssociation rhs = ((GenotypeToPhenotypicFeatureAssociation) other);
        return new EqualsBuilder().append(subject, rhs.subject).append(relation, rhs.relation).isEquals();
    }

}
