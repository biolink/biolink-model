import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(OntologyClass.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("subclassOf");
        sb.append('=');
        sb.append(((this.subclassOf == null)?"<null>":this.subclassOf));
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
        result = ((result* 31)+((this.subclassOf == null)? 0 :this.subclassOf.hashCode()));
        return result;
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
        return ((this.subclassOf == rhs.subclassOf)||((this.subclassOf!= null)&&this.subclassOf.equals(rhs.subclassOf)));
    }

}
