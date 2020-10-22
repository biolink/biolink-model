import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * GeneFamily
 * <p>
 * any grouping of multiple genes or gene products related by common descent
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class GeneFamily {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(GeneFamily.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof GeneFamily) == false) {
            return false;
        }
        GeneFamily rhs = ((GeneFamily) other);
        return true;
    }

}
