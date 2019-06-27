import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * OntologyClass
 * <p>
 * a concept or class in an ontology, vocabulary or thesaurus
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "subclass_of"
})
public class OntologyClass {

    /**
     * holds between two classes where the domain class is a specialization of the range class
     * 
     */
    @JsonProperty("subclass_of")
    @JsonPropertyDescription("holds between two classes where the domain class is a specialization of the range class")
    private List<String> subclassOf = new ArrayList<String>();

    /**
     * holds between two classes where the domain class is a specialization of the range class
     * 
     */
    @JsonProperty("subclass_of")
    public List<String> getSubclassOf() {
        return subclassOf;
    }

    /**
     * holds between two classes where the domain class is a specialization of the range class
     * 
     */
    @JsonProperty("subclass_of")
    public void setSubclassOf(List<String> subclassOf) {
        this.subclassOf = subclassOf;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("subclassOf", subclassOf).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(subclassOf).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof OntologyClass) == false) {
            return false;
        }
        OntologyClass rhs = ((OntologyClass) other);
        return new EqualsBuilder().append(subclassOf, rhs.subclassOf).isEquals();
    }

}
