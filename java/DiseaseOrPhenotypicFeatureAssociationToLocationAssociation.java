import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


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
        return new ToStringBuilder(this).append("object", object).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(object).toHashCode();
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
        return new EqualsBuilder().append(object, rhs.object).isEquals();
    }

}
