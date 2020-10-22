import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * DiseaseOrPhenotypicFeatureAssociationToLocationAssociation
 * <p>
 * An association between either a disease or a phenotypic feature and an anatomical entity, where the disease/feature manifests in that site.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "object"
})
public class DiseaseOrPhenotypicFeatureAssociationToLocationAssociation {

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    private String object;

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    public void setObject(String object) {
        this.object = object;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(DiseaseOrPhenotypicFeatureAssociationToLocationAssociation.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("object");
        sb.append('=');
        sb.append(((this.object == null)?"<null>":this.object));
        sb.append(',');
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
        result = ((result* 31)+((this.object == null)? 0 :this.object.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof DiseaseOrPhenotypicFeatureAssociationToLocationAssociation) == false) {
            return false;
        }
        DiseaseOrPhenotypicFeatureAssociationToLocationAssociation rhs = ((DiseaseOrPhenotypicFeatureAssociationToLocationAssociation) other);
        return ((this.object == rhs.object)||((this.object!= null)&&this.object.equals(rhs.object)));
    }

}
