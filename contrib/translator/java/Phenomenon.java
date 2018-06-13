import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * Phenomenon
 * <p>
 * a fact or situation that is observed to exist or happen, especially one whose cause or explanation is in question
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class Phenomenon {


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
        if ((other instanceof Phenomenon) == false) {
            return false;
        }
        Phenomenon rhs = ((Phenomenon) other);
        return new EqualsBuilder().isEquals();
    }

}
