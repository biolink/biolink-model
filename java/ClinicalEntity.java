import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * ClinicalEntity
 * <p>
 * Any entity or process that exists in the clinical domain and outside the biological realm. Diseases are placed under biological entities
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class ClinicalEntity {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(ClinicalEntity.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof ClinicalEntity) == false) {
            return false;
        }
        ClinicalEntity rhs = ((ClinicalEntity) other);
        return true;
    }

}
