import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(ExposureEvent.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("hasReceptor");
        sb.append('=');
        sb.append(((this.hasReceptor == null)?"<null>":this.hasReceptor));
        sb.append(',');
        sb.append("hasRoute");
        sb.append('=');
        sb.append(((this.hasRoute == null)?"<null>":this.hasRoute));
        sb.append(',');
        sb.append("hasStressor");
        sb.append('=');
        sb.append(((this.hasStressor == null)?"<null>":this.hasStressor));
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
        result = ((result* 31)+((this.hasRoute == null)? 0 :this.hasRoute.hashCode()));
        result = ((result* 31)+((this.hasReceptor == null)? 0 :this.hasReceptor.hashCode()));
        result = ((result* 31)+((this.hasStressor == null)? 0 :this.hasStressor.hashCode()));
        return result;
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
        return ((((this.hasRoute == rhs.hasRoute)||((this.hasRoute!= null)&&this.hasRoute.equals(rhs.hasRoute)))&&((this.hasReceptor == rhs.hasReceptor)||((this.hasReceptor!= null)&&this.hasReceptor.equals(rhs.hasReceptor))))&&((this.hasStressor == rhs.hasStressor)||((this.hasStressor!= null)&&this.hasStressor.equals(rhs.hasStressor))));
    }

}
