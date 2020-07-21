import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * GeneProduct
 * <p>
 * The functional molecular product of a single gene. Gene products are either proteins or functional RNA molecules
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class GeneProduct {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(GeneProduct.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof GeneProduct) == false) {
            return false;
        }
        GeneProduct rhs = ((GeneProduct) other);
        return true;
    }

}
