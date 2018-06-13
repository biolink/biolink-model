import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


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
        return new ToStringBuilder(this).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().toHashCode();
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
        return new EqualsBuilder().isEquals();
    }

}
