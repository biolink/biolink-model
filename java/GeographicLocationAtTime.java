import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


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
        return new ToStringBuilder(this).append("timepoint", timepoint).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(timepoint).toHashCode();
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
        return new EqualsBuilder().append(timepoint, rhs.timepoint).isEquals();
    }

}
