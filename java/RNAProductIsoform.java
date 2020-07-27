import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * RNAProductIsoform
 * <p>
 * Represents a protein that is a specific isoform of the canonical or reference RNA
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class RNAProductIsoform {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(RNAProductIsoform.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof RNAProductIsoform) == false) {
            return false;
        }
        RNAProductIsoform rhs = ((RNAProductIsoform) other);
        return true;
    }

}
