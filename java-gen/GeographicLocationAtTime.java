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
    "id",
    "label",
    "latitude",
    "longitude",
    "timepoint"
})
public class GeographicLocationAtTime {

    @JsonProperty("id")
    private String id;
    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    @JsonPropertyDescription("A human-readable name for a thing")
    private String label;
    /**
     * latitude
     * 
     */
    @JsonProperty("latitude")
    @JsonPropertyDescription("latitude")
    private String latitude;
    /**
     * longitude
     * 
     */
    @JsonProperty("longitude")
    @JsonPropertyDescription("longitude")
    private String longitude;
    /**
     * a point in time
     * 
     */
    @JsonProperty("timepoint")
    @JsonPropertyDescription("a point in time")
    private String timepoint;

    @JsonProperty("id")
    public String getId() {
        return id;
    }

    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    public String getLabel() {
        return label;
    }

    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    public void setLabel(String label) {
        this.label = label;
    }

    /**
     * latitude
     * 
     */
    @JsonProperty("latitude")
    public String getLatitude() {
        return latitude;
    }

    /**
     * latitude
     * 
     */
    @JsonProperty("latitude")
    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }

    /**
     * longitude
     * 
     */
    @JsonProperty("longitude")
    public String getLongitude() {
        return longitude;
    }

    /**
     * longitude
     * 
     */
    @JsonProperty("longitude")
    public void setLongitude(String longitude) {
        this.longitude = longitude;
    }

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
        return new ToStringBuilder(this).append("id", id).append("label", label).append("latitude", latitude).append("longitude", longitude).append("timepoint", timepoint).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(id).append(label).append(latitude).append(longitude).append(timepoint).toHashCode();
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
        return new EqualsBuilder().append(id, rhs.id).append(label, rhs.label).append(latitude, rhs.latitude).append(longitude, rhs.longitude).append(timepoint, rhs.timepoint).isEquals();
    }

}
