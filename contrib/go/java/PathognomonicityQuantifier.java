import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * PathognomonicityQuantifier
 * <p>
 * A relationship quantifier between a variant or symptom and a disease, which is high when the presence of the feature implies the existence of the disease
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class PathognomonicityQuantifier {


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
        if ((other instanceof PathognomonicityQuantifier) == false) {
            return false;
        }
        PathognomonicityQuantifier rhs = ((PathognomonicityQuantifier) other);
        return new EqualsBuilder().isEquals();
    }

}
