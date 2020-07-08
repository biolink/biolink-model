import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * Metabolite
 * <p>
 * Any intermediate or product resulting from metabolism. Includes primary and secondary metabolites.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class Metabolite {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(Metabolite.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof Metabolite) == false) {
            return false;
        }
        Metabolite rhs = ((Metabolite) other);
        return true;
    }

}
