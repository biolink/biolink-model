import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * Publication
 * <p>
 * Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "id",
    "label"
})
public class Publication {

    @JsonProperty("id")
    private String id;
    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    @JsonPropertyDescription("A human-readable name for a thing")
    private String label;

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

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("id", id).append("label", label).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(id).append(label).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof Publication) == false) {
            return false;
        }
        Publication rhs = ((Publication) other);
        return new EqualsBuilder().append(id, rhs.id).append(label, rhs.label).isEquals();
    }

}
