import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * DiseaseToPhenotypicFeatureAssociation
 * <p>
 * An association between a disease and a phenotypic feature in which the phenotypic feature is associated with the disease in some way
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class DiseaseToPhenotypicFeatureAssociation {


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
        if ((other instanceof DiseaseToPhenotypicFeatureAssociation) == false) {
            return false;
        }
        DiseaseToPhenotypicFeatureAssociation rhs = ((DiseaseToPhenotypicFeatureAssociation) other);
        return new EqualsBuilder().isEquals();
    }

}
