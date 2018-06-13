import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * CausalActivityModel
 * <p>
 * A graph-based representation of how a collection of gene products operate together to achieve a biological objective. A GO-CAM model is a specialization of a named graph containing instances of GO molecular functions, entities, processes, cellular components etc, connected via causal relationships.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "title"
})
public class CausalActivityModel {

    /**
     * Narrative text describing the entity
     * 
     */
    @JsonProperty("title")
    @JsonPropertyDescription("Narrative text describing the entity")
    private String title;

    /**
     * Narrative text describing the entity
     * 
     */
    @JsonProperty("title")
    public String getTitle() {
        return title;
    }

    /**
     * Narrative text describing the entity
     * 
     */
    @JsonProperty("title")
    public void setTitle(String title) {
        this.title = title;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("title", title).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(title).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof CausalActivityModel) == false) {
            return false;
        }
        CausalActivityModel rhs = ((CausalActivityModel) other);
        return new EqualsBuilder().append(title, rhs.title).isEquals();
    }

}
