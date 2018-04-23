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
    "category",
    "id",
    "label",
    "latitude",
    "longitude",
    "timepoint"
})
public class GeographicLocationAtTime {

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class
     * 
     */
    @JsonProperty("category")
    @JsonPropertyDescription("Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class")
    private String category;
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

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class
     * 
     */
    @JsonProperty("category")
    public String getCategory() {
        return category;
    }

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class
     * 
     */
    @JsonProperty("category")
    public void setCategory(String category) {
        this.category = category;
    }

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
        return new ToStringBuilder(this).append("category", category).append("id", id).append("label", label).append("latitude", latitude).append("longitude", longitude).append("timepoint", timepoint).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(latitude).append(id).append(label).append(category).append(longitude).append(timepoint).toHashCode();
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
        return new EqualsBuilder().append(latitude, rhs.latitude).append(id, rhs.id).append(label, rhs.label).append(category, rhs.category).append(longitude, rhs.longitude).append(timepoint, rhs.timepoint).isEquals();
    }

}
