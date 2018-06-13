import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * Exon
 * <p>
 * A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class Exon {


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
        if ((other instanceof Exon) == false) {
            return false;
        }
        Exon rhs = ((Exon) other);
        return new EqualsBuilder().isEquals();
    }

}
