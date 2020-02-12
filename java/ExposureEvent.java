import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * ExposureEvent
 * <p>
 * A feature of the environment of an organism that influences one or more phenotypic features of that organism, potentially mediated by genes
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "has_receptor",
    "has_route",
    "has_stressor"
})
public class ExposureEvent {

    /**
     * the organism or organism part being exposed
     * 
     */
    @JsonProperty("has_receptor")
    @JsonPropertyDescription("the organism or organism part being exposed")
    private String hasReceptor;
    /**
     * the process that results in the stressor coming into direct contact with the receptor
     * 
     */
    @JsonProperty("has_route")
    @JsonPropertyDescription("the process that results in the stressor coming into direct contact with the receptor")
    private String hasRoute;
    /**
     * the process or entity that the receptor is being exposed to
     * 
     */
    @JsonProperty("has_stressor")
    @JsonPropertyDescription("the process or entity that the receptor is being exposed to")
    private String hasStressor;

    /**
     * the organism or organism part being exposed
     * 
     */
    @JsonProperty("has_receptor")
    public String getHasReceptor() {
        return hasReceptor;
    }

    /**
     * the organism or organism part being exposed
     * 
     */
    @JsonProperty("has_receptor")
    public void setHasReceptor(String hasReceptor) {
        this.hasReceptor = hasReceptor;
    }

    /**
     * the process that results in the stressor coming into direct contact with the receptor
     * 
     */
    @JsonProperty("has_route")
    public String getHasRoute() {
        return hasRoute;
    }

    /**
     * the process that results in the stressor coming into direct contact with the receptor
     * 
     */
    @JsonProperty("has_route")
    public void setHasRoute(String hasRoute) {
        this.hasRoute = hasRoute;
    }

    /**
     * the process or entity that the receptor is being exposed to
     * 
     */
    @JsonProperty("has_stressor")
    public String getHasStressor() {
        return hasStressor;
    }

    /**
     * the process or entity that the receptor is being exposed to
     * 
     */
    @JsonProperty("has_stressor")
    public void setHasStressor(String hasStressor) {
        this.hasStressor = hasStressor;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("hasReceptor", hasReceptor).append("hasRoute", hasRoute).append("hasStressor", hasStressor).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasRoute).append(hasReceptor).append(hasStressor).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof ExposureEvent) == false) {
            return false;
        }
        ExposureEvent rhs = ((ExposureEvent) other);
        return new EqualsBuilder().append(hasRoute, rhs.hasRoute).append(hasReceptor, rhs.hasReceptor).append(hasStressor, rhs.hasStressor).isEquals();
    }

}
