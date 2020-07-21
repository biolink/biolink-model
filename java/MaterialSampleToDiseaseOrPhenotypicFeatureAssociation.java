import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * MaterialSampleToDiseaseOrPhenotypicFeatureAssociation
 * <p>
 * An association between a material sample and a disease or phenotype
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class MaterialSampleToDiseaseOrPhenotypicFeatureAssociation {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(MaterialSampleToDiseaseOrPhenotypicFeatureAssociation.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof MaterialSampleToDiseaseOrPhenotypicFeatureAssociation) == false) {
            return false;
        }
        MaterialSampleToDiseaseOrPhenotypicFeatureAssociation rhs = ((MaterialSampleToDiseaseOrPhenotypicFeatureAssociation) other);
        return true;
    }

}
