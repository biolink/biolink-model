import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * ConfidenceLevel
 * <p>
 * Level of confidence in a statement
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class ConfidenceLevel {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(ConfidenceLevel.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof ConfidenceLevel) == false) {
            return false;
        }
        ConfidenceLevel rhs = ((ConfidenceLevel) other);
        return true;
    }

}
