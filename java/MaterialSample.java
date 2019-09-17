import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * MaterialSample
 * <p>
 * A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use. [SIO]
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "has_attribute"
})
public class MaterialSample {

    /**
     * connects any named thing to an attribute
     * 
     */
    @JsonProperty("has_attribute")
    @JsonPropertyDescription("connects any named thing to an attribute")
    private List<String> hasAttribute = new ArrayList<String>();

    /**
     * connects any named thing to an attribute
     * 
     */
    @JsonProperty("has_attribute")
    public List<String> getHasAttribute() {
        return hasAttribute;
    }

    /**
     * connects any named thing to an attribute
     * 
     */
    @JsonProperty("has_attribute")
    public void setHasAttribute(List<String> hasAttribute) {
        this.hasAttribute = hasAttribute;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("hasAttribute", hasAttribute).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasAttribute).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof MaterialSample) == false) {
            return false;
        }
        MaterialSample rhs = ((MaterialSample) other);
        return new EqualsBuilder().append(hasAttribute, rhs.hasAttribute).isEquals();
    }

}
