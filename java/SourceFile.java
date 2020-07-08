import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * SourceFile
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "retrievedOn",
    "source_version"
})
public class SourceFile {

    @JsonProperty("retrievedOn")
    private String retrievedOn;
    @JsonProperty("source_version")
    private String sourceVersion;

    @JsonProperty("retrievedOn")
    public String getRetrievedOn() {
        return retrievedOn;
    }

    @JsonProperty("retrievedOn")
    public void setRetrievedOn(String retrievedOn) {
        this.retrievedOn = retrievedOn;
    }

    @JsonProperty("source_version")
    public String getSourceVersion() {
        return sourceVersion;
    }

    @JsonProperty("source_version")
    public void setSourceVersion(String sourceVersion) {
        this.sourceVersion = sourceVersion;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(SourceFile.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("retrievedOn");
        sb.append('=');
        sb.append(((this.retrievedOn == null)?"<null>":this.retrievedOn));
        sb.append(',');
        sb.append("sourceVersion");
        sb.append('=');
        sb.append(((this.sourceVersion == null)?"<null>":this.sourceVersion));
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
        result = ((result* 31)+((this.retrievedOn == null)? 0 :this.retrievedOn.hashCode()));
        result = ((result* 31)+((this.sourceVersion == null)? 0 :this.sourceVersion.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof SourceFile) == false) {
            return false;
        }
        SourceFile rhs = ((SourceFile) other);
        return (((this.retrievedOn == rhs.retrievedOn)||((this.retrievedOn!= null)&&this.retrievedOn.equals(rhs.retrievedOn)))&&((this.sourceVersion == rhs.sourceVersion)||((this.sourceVersion!= null)&&this.sourceVersion.equals(rhs.sourceVersion))));
    }

}
