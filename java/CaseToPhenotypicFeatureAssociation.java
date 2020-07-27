import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(CaseToPhenotypicFeatureAssociation.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof CaseToPhenotypicFeatureAssociation) == false) {
            return false;
        }
        CaseToPhenotypicFeatureAssociation rhs = ((CaseToPhenotypicFeatureAssociation) other);
        return true;
    }

}
