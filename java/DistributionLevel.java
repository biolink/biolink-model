import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(DistributionLevel.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("downloadURL");
        sb.append('=');
        sb.append(((this.downloadURL == null)?"<null>":this.downloadURL));
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
        result = ((result* 31)+((this.downloadURL == null)? 0 :this.downloadURL.hashCode()));
        return result;
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
        return ((this.downloadURL == rhs.downloadURL)||((this.downloadURL!= null)&&this.downloadURL.equals(rhs.downloadURL)));
    }

}
