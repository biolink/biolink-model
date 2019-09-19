import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * CaseToPhenotypicFeatureAssociation
 * <p>
 * An association between a case (e.g. individual patient) and a phenotypic feature in which the individual has or has had the phenotype
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class CaseToPhenotypicFeatureAssociation {


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
        if ((other instanceof CaseToPhenotypicFeatureAssociation) == false) {
            return false;
        }
        CaseToPhenotypicFeatureAssociation rhs = ((CaseToPhenotypicFeatureAssociation) other);
        return new EqualsBuilder().isEquals();
    }

}
