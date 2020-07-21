import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * Phenomenon
 * <p>
 * a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class Phenomenon {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(Phenomenon.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof Phenomenon) == false) {
            return false;
        }
        Phenomenon rhs = ((Phenomenon) other);
        return true;
    }

}
