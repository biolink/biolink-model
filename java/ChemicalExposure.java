import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * ChemicalExposure
 * <p>
 * A chemical exposure is an intake of a particular chemical substance
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class ChemicalExposure {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(ChemicalExposure.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof ChemicalExposure) == false) {
            return false;
        }
        ChemicalExposure rhs = ((ChemicalExposure) other);
        return true;
    }

}
