import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * BiologicalProcessOrActivity
 * <p>
 * Either an individual molecular activity, or a collection of causally connected molecular activities
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class BiologicalProcessOrActivity {


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
        if ((other instanceof BiologicalProcessOrActivity) == false) {
            return false;
        }
        BiologicalProcessOrActivity rhs = ((BiologicalProcessOrActivity) other);
        return new EqualsBuilder().isEquals();
    }

}
