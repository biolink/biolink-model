import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * DataSetSummary
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "source_web_page"
})
public class DataSetSummary {

    @JsonProperty("source_web_page")
    private String sourceWebPage;

    @JsonProperty("source_web_page")
    public String getSourceWebPage() {
        return sourceWebPage;
    }

    @JsonProperty("source_web_page")
    public void setSourceWebPage(String sourceWebPage) {
        this.sourceWebPage = sourceWebPage;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("sourceWebPage", sourceWebPage).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(sourceWebPage).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof DataSetSummary) == false) {
            return false;
        }
        DataSetSummary rhs = ((DataSetSummary) other);
        return new EqualsBuilder().append(sourceWebPage, rhs.sourceWebPage).isEquals();
    }

}
