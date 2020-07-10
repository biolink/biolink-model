import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * GenotypicSex
 * <p>
 * An attribute corresponding to the genotypic sex of the individual, based upon genotypic composition of sex chromosomes.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class GenotypicSex {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(GenotypicSex.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof GenotypicSex) == false) {
            return false;
        }
        GenotypicSex rhs = ((GenotypicSex) other);
        return true;
    }

}
