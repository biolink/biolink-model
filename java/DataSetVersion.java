import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * DataSetVersion
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "distribution",
    "source_data_file",
    "title",
    "type",
    "versionOf"
})
public class DataSetVersion {

    @JsonProperty("distribution")
    private String distribution;
    @JsonProperty("source_data_file")
    private String sourceDataFile;
    @JsonProperty("title")
    private String title;
    @JsonProperty("type")
    private String type;
    @JsonProperty("versionOf")
    private String versionOf;

    @JsonProperty("distribution")
    public String getDistribution() {
        return distribution;
    }

    @JsonProperty("distribution")
    public void setDistribution(String distribution) {
        this.distribution = distribution;
    }

    @JsonProperty("source_data_file")
    public String getSourceDataFile() {
        return sourceDataFile;
    }

    @JsonProperty("source_data_file")
    public void setSourceDataFile(String sourceDataFile) {
        this.sourceDataFile = sourceDataFile;
    }

    @JsonProperty("title")
    public String getTitle() {
        return title;
    }

    @JsonProperty("title")
    public void setTitle(String title) {
        this.title = title;
    }

    @JsonProperty("type")
    public String getType() {
        return type;
    }

    @JsonProperty("type")
    public void setType(String type) {
        this.type = type;
    }

    @JsonProperty("versionOf")
    public String getVersionOf() {
        return versionOf;
    }

    @JsonProperty("versionOf")
    public void setVersionOf(String versionOf) {
        this.versionOf = versionOf;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("distribution", distribution).append("sourceDataFile", sourceDataFile).append("title", title).append("type", type).append("versionOf", versionOf).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(distribution).append(title).append(type).append(versionOf).append(sourceDataFile).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof DataSetVersion) == false) {
            return false;
        }
        DataSetVersion rhs = ((DataSetVersion) other);
        return new EqualsBuilder().append(distribution, rhs.distribution).append(title, rhs.title).append(type, rhs.type).append(versionOf, rhs.versionOf).append(sourceDataFile, rhs.sourceDataFile).isEquals();
    }

}
