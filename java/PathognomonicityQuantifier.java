import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * PathognomonicityQuantifier
 * <p>
 * A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class PathognomonicityQuantifier {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(PathognomonicityQuantifier.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof PathognomonicityQuantifier) == false) {
            return false;
        }
        PathognomonicityQuantifier rhs = ((PathognomonicityQuantifier) other);
        return true;
    }

}
