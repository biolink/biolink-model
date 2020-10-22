import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * GeographicLocationAtTime
 * <p>
 * a location that can be described in lat/long coordinates, for a particular time
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "timepoint"
})
public class GeographicLocationAtTime {

    /**
     * a point in time
     * 
     */
    @JsonProperty("timepoint")
    @JsonPropertyDescription("a point in time")
    private String timepoint;

    /**
     * a point in time
     * 
     */
    @JsonProperty("timepoint")
    public String getTimepoint() {
        return timepoint;
    }

    /**
     * a point in time
     * 
     */
    @JsonProperty("timepoint")
    public void setTimepoint(String timepoint) {
        this.timepoint = timepoint;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(GeographicLocationAtTime.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("timepoint");
        sb.append('=');
        sb.append(((this.timepoint == null)?"<null>":this.timepoint));
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
        result = ((result* 31)+((this.timepoint == null)? 0 :this.timepoint.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof GeographicLocationAtTime) == false) {
            return false;
        }
        GeographicLocationAtTime rhs = ((GeographicLocationAtTime) other);
        return ((this.timepoint == rhs.timepoint)||((this.timepoint!= null)&&this.timepoint.equals(rhs.timepoint)));
    }

}
