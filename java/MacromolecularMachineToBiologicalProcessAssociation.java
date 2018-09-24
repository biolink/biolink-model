import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * MacromolecularMachineToBiologicalProcessAssociation
 * <p>
 * A functional association between a macromolecular machine (gene, gene product or complex) and a biological process or pathway (as represented in the GO biological process branch), where the entity carries out some part of the process, regulates it, or acts upstream of it
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "object"
})
public class MacromolecularMachineToBiologicalProcessAssociation {

    /**
     * class describing the activity, process or localization of the gene product
     * (Required)
     * 
     */
    @JsonProperty("object")
    @JsonPropertyDescription("class describing the activity, process or localization of the gene product")
    private String object;

    /**
     * class describing the activity, process or localization of the gene product
     * (Required)
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * class describing the activity, process or localization of the gene product
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
        if ((other instanceof MacromolecularMachineToBiologicalProcessAssociation) == false) {
            return false;
        }
        MacromolecularMachineToBiologicalProcessAssociation rhs = ((MacromolecularMachineToBiologicalProcessAssociation) other);
        return new EqualsBuilder().append(object, rhs.object).isEquals();
    }

}
