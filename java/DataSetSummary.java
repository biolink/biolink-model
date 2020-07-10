import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(DataSetSummary.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("sourceWebPage");
        sb.append('=');
        sb.append(((this.sourceWebPage == null)?"<null>":this.sourceWebPage));
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
        result = ((result* 31)+((this.sourceWebPage == null)? 0 :this.sourceWebPage.hashCode()));
        return result;
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
        return ((this.sourceWebPage == rhs.sourceWebPage)||((this.sourceWebPage!= null)&&this.sourceWebPage.equals(rhs.sourceWebPage)));
    }

}
