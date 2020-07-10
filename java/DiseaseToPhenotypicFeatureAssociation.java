import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(DiseaseToPhenotypicFeatureAssociation.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof DiseaseToPhenotypicFeatureAssociation) == false) {
            return false;
        }
        DiseaseToPhenotypicFeatureAssociation rhs = ((DiseaseToPhenotypicFeatureAssociation) other);
        return true;
    }

}
