import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * DistributionLevel
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "downloadURL"
})
public class DistributionLevel {

    @JsonProperty("downloadURL")
    private String downloadURL;

    @JsonProperty("downloadURL")
    public String getDownloadURL() {
        return downloadURL;
    }

    @JsonProperty("downloadURL")
    public void setDownloadURL(String downloadURL) {
        this.downloadURL = downloadURL;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("downloadURL", downloadURL).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(downloadURL).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof DistributionLevel) == false) {
            return false;
        }
        DistributionLevel rhs = ((DistributionLevel) other);
        return new EqualsBuilder().append(downloadURL, rhs.downloadURL).isEquals();
    }

}
