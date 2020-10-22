import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(MaterialSample.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("hasAttribute");
        sb.append('=');
        sb.append(((this.hasAttribute == null)?"<null>":this.hasAttribute));
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
        result = ((result* 31)+((this.hasAttribute == null)? 0 :this.hasAttribute.hashCode()));
        return result;
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
        return ((this.hasAttribute == rhs.hasAttribute)||((this.hasAttribute!= null)&&this.hasAttribute.equals(rhs.hasAttribute)));
    }

}
