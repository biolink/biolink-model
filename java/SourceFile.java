import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


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
        return new ToStringBuilder(this).append("retrievedOn", retrievedOn).append("sourceVersion", sourceVersion).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(retrievedOn).append(sourceVersion).toHashCode();
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
        return new EqualsBuilder().append(retrievedOn, rhs.retrievedOn).append(sourceVersion, rhs.sourceVersion).isEquals();
    }

}
