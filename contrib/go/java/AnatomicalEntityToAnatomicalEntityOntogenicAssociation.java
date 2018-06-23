import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * AnatomicalEntityToAnatomicalEntityOntogenicAssociation
 * <p>
 * A relationship between two anatomical entities where the relationship is ontogenic, i.e the two entities are related by development. A number of different relationship types can be used to specify the precise nature of the relationship
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "object",
    "relation",
    "subject"
})
public class AnatomicalEntityToAnatomicalEntityOntogenicAssociation {

    /**
     * the structure at an earlier time
     * 
     */
    @JsonProperty("object")
    @JsonPropertyDescription("the structure at an earlier time")
    private String object;
    /**
     * the relationship type by which a subject is connected to an object in an association
     * 
     */
    @JsonProperty("relation")
    @JsonPropertyDescription("the relationship type by which a subject is connected to an object in an association")
    private String relation;
    /**
     * the structure at a later time
     * 
     */
    @JsonProperty("subject")
    @JsonPropertyDescription("the structure at a later time")
    private String subject;

    /**
     * the structure at an earlier time
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * the structure at an earlier time
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
     * the structure at a later time
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * the structure at a later time
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
        if ((other instanceof AnatomicalEntityToAnatomicalEntityOntogenicAssociation) == false) {
            return false;
        }
        AnatomicalEntityToAnatomicalEntityOntogenicAssociation rhs = ((AnatomicalEntityToAnatomicalEntityOntogenicAssociation) other);
        return new EqualsBuilder().append(subject, rhs.subject).append(object, rhs.object).append(relation, rhs.relation).isEquals();
    }

}
