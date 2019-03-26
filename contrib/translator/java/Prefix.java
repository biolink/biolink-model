import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * Prefix
 * <p>
 * Prefix URI map
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "local_name",
    "prefix_uri"
})
public class Prefix {

    /**
     * the nsname (sans ':' for a given prefix)
     * 
     */
    @JsonProperty("local_name")
    @JsonPropertyDescription("the nsname (sans ':' for a given prefix)")
    private String localName;
    /**
     * A URI associated with a given prefix
     * 
     */
    @JsonProperty("prefix_uri")
    @JsonPropertyDescription("A URI associated with a given prefix")
    private String prefixUri;

    /**
     * the nsname (sans ':' for a given prefix)
     * 
     */
    @JsonProperty("local_name")
    public String getLocalName() {
        return localName;
    }

    /**
     * the nsname (sans ':' for a given prefix)
     * 
     */
    @JsonProperty("local_name")
    public void setLocalName(String localName) {
        this.localName = localName;
    }

    /**
     * A URI associated with a given prefix
     * 
     */
    @JsonProperty("prefix_uri")
    public String getPrefixUri() {
        return prefixUri;
    }

    /**
     * A URI associated with a given prefix
     * 
     */
    @JsonProperty("prefix_uri")
    public void setPrefixUri(String prefixUri) {
        this.prefixUri = prefixUri;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("localName", localName).append("prefixUri", prefixUri).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(localName).append(prefixUri).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof Prefix) == false) {
            return false;
        }
        Prefix rhs = ((Prefix) other);
        return new EqualsBuilder().append(localName, rhs.localName).append(prefixUri, rhs.prefixUri).isEquals();
    }

}
