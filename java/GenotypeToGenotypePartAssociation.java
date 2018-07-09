import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * GenotypeToGenotypePartAssociation
 * <p>
 * Any association between one genotype and a genotypic entity that is a sub-component of it
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "object",
    "relation",
    "subject"
})
public class GenotypeToGenotypePartAssociation {

    /**
     * child genotype
     * 
     */
    @JsonProperty("object")
    @JsonPropertyDescription("child genotype")
    private String object;
    /**
     * the relationship type by which a subject is connected to an object in an association
     * 
     */
    @JsonProperty("relation")
    @JsonPropertyDescription("the relationship type by which a subject is connected to an object in an association")
    private String relation;
    /**
     * parent genotype
     * 
     */
    @JsonProperty("subject")
    @JsonPropertyDescription("parent genotype")
    private String subject;

    /**
     * child genotype
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * child genotype
     * 
     */
    @JsonProperty("object")
    public void setObject(String object) {
        this.object = object;
    }

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
     * parent genotype
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * parent genotype
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
        if ((other instanceof GenotypeToGenotypePartAssociation) == false) {
            return false;
        }
        GenotypeToGenotypePartAssociation rhs = ((GenotypeToGenotypePartAssociation) other);
        return new EqualsBuilder().append(subject, rhs.subject).append(object, rhs.object).append(relation, rhs.relation).isEquals();
    }

}
