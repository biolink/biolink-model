import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * GeneOntologyClass
 * <p>
 * an ontology class that describes a functional aspect of a gene, gene prodoct or complex
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class GeneOntologyClass {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(GeneOntologyClass.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof GeneOntologyClass) == false) {
            return false;
        }
        GeneOntologyClass rhs = ((GeneOntologyClass) other);
        return true;
    }

}
