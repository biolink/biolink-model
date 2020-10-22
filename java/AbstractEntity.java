import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * AbstractEntity
 * <p>
 * Any thing that is not a process or a physical mass-bearing entity
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class AbstractEntity {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(AbstractEntity.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof AbstractEntity) == false) {
            return false;
        }
        AbstractEntity rhs = ((AbstractEntity) other);
        return true;
    }

}
