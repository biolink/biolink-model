import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * ProteinIsoform
 * <p>
 * Represents a protein that is a specific isoform of the canonical or reference protein. See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4114032/
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class ProteinIsoform {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(ProteinIsoform.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof ProteinIsoform) == false) {
            return false;
        }
        ProteinIsoform rhs = ((ProteinIsoform) other);
        return true;
    }

}
