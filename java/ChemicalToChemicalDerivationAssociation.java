import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * ChemicalToChemicalDerivationAssociation
 * <p>
 * A causal relationship between two chemical entities, where the subject represents the upstream entity and the object represents the downstream. For any such association there is an implicit reaction:
 *   IF
 *   R has-input C1 AND
 *   R has-output C2 AND
 *   R enabled-by P AND
 *   R type Reaction
 *   THEN
 *   C1 derives-into C2 <<change is catalyzed by P>>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "change_is_catalyzed_by",
    "object",
    "relation",
    "subject"
})
public class ChemicalToChemicalDerivationAssociation {

    @JsonProperty("change_is_catalyzed_by")
    private List<String> changeIsCatalyzedBy = new ArrayList<String>();
    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    private String object;
    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("relation")
    private String relation;
    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    private String subject;

    @JsonProperty("change_is_catalyzed_by")
    public List<String> getChangeIsCatalyzedBy() {
        return changeIsCatalyzedBy;
    }

    @JsonProperty("change_is_catalyzed_by")
    public void setChangeIsCatalyzedBy(List<String> changeIsCatalyzedBy) {
        this.changeIsCatalyzedBy = changeIsCatalyzedBy;
    }

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
        return new ToStringBuilder(this).append("changeIsCatalyzedBy", changeIsCatalyzedBy).append("object", object).append("relation", relation).append("subject", subject).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(subject).append(changeIsCatalyzedBy).append(object).append(relation).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof ChemicalToChemicalDerivationAssociation) == false) {
            return false;
        }
        ChemicalToChemicalDerivationAssociation rhs = ((ChemicalToChemicalDerivationAssociation) other);
        return new EqualsBuilder().append(subject, rhs.subject).append(changeIsCatalyzedBy, rhs.changeIsCatalyzedBy).append(object, rhs.object).append(relation, rhs.relation).isEquals();
    }

}
