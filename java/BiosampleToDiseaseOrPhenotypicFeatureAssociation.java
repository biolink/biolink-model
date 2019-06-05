import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * BiosampleToDiseaseOrPhenotypicFeatureAssociation
 * <p>
 * An association between a biosample and a disease or phenotype
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class BiosampleToDiseaseOrPhenotypicFeatureAssociation {


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
        if ((other instanceof BiosampleToDiseaseOrPhenotypicFeatureAssociation) == false) {
            return false;
        }
        BiosampleToDiseaseOrPhenotypicFeatureAssociation rhs = ((BiosampleToDiseaseOrPhenotypicFeatureAssociation) other);
        return new EqualsBuilder().isEquals();
    }

}
