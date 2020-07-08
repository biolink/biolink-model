import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * PhysicalEntity
 * <p>
 * An entity that has physical properties such as mass, volume, or charge
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class PhysicalEntity {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(PhysicalEntity.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof PhysicalEntity) == false) {
            return false;
        }
        PhysicalEntity rhs = ((PhysicalEntity) other);
        return true;
    }

}
