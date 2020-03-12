import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * ActivityAndBehavior
 * <p>
 * Activity or behavior of any independent integral living, organization or mechanical actor in the world
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class ActivityAndBehavior {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(ActivityAndBehavior.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof ActivityAndBehavior) == false) {
            return false;
        }
        ActivityAndBehavior rhs = ((ActivityAndBehavior) other);
        return true;
    }

}
