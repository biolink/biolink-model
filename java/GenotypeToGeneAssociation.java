import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * GenotypeToGeneAssociation
 * <p>
 * Any association between a genotype and a gene. The genotype have have multiple variants in that gene or a single one. There is no assumption of cardinality
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "object",
    "relation",
    "subject"
})
public class GenotypeToGeneAssociation {

    /**
     * gene implicated in genotype
     * (Required)
     * 
     */
    @JsonProperty("object")
    @JsonPropertyDescription("gene implicated in genotype")
    private String object;
    /**
     * the relationship type used to connect genotype to gene
     * (Required)
     * 
     */
    @JsonProperty("relation")
    @JsonPropertyDescription("the relationship type used to connect genotype to gene")
    private String relation;
    /**
     * parent genotype
     * (Required)
     * 
     */
    @JsonProperty("subject")
    @JsonPropertyDescription("parent genotype")
    private String subject;

    /**
     * gene implicated in genotype
     * (Required)
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * gene implicated in genotype
     * (Required)
     * 
     */
    @JsonProperty("object")
    public void setObject(String object) {
        this.object = object;
    }

    /**
     * the relationship type used to connect genotype to gene
     * (Required)
     * 
     */
    @JsonProperty("relation")
    public String getRelation() {
        return relation;
    }

    /**
     * the relationship type used to connect genotype to gene
     * (Required)
     * 
     */
    @JsonProperty("relation")
    public void setRelation(String relation) {
        this.relation = relation;
    }

    /**
     * parent genotype
     * (Required)
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * parent genotype
     * (Required)
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
        if ((other instanceof GenotypeToGeneAssociation) == false) {
            return false;
        }
        GenotypeToGeneAssociation rhs = ((GenotypeToGeneAssociation) other);
        return new EqualsBuilder().append(subject, rhs.subject).append(object, rhs.object).append(relation, rhs.relation).isEquals();
    }

}
