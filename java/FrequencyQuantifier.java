import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * FrequencyQuantifier
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "has_count",
    "has_percentage",
    "has_quotient",
    "has_total"
})
public class FrequencyQuantifier {

    /**
     * number of things with a particular property
     * 
     */
    @JsonProperty("has_count")
    @JsonPropertyDescription("number of things with a particular property")
    private String hasCount;
    /**
     * equivalent to has quotient multiplied by 100
     * 
     */
    @JsonProperty("has_percentage")
    @JsonPropertyDescription("equivalent to has quotient multiplied by 100")
    private String hasPercentage;
    @JsonProperty("has_quotient")
    private String hasQuotient;
    /**
     * total number of things in a particular reference set
     * 
     */
    @JsonProperty("has_total")
    @JsonPropertyDescription("total number of things in a particular reference set")
    private String hasTotal;

    /**
     * number of things with a particular property
     * 
     */
    @JsonProperty("has_count")
    public String getHasCount() {
        return hasCount;
    }

    /**
     * number of things with a particular property
     * 
     */
    @JsonProperty("has_count")
    public void setHasCount(String hasCount) {
        this.hasCount = hasCount;
    }

    /**
     * equivalent to has quotient multiplied by 100
     * 
     */
    @JsonProperty("has_percentage")
    public String getHasPercentage() {
        return hasPercentage;
    }

    /**
     * equivalent to has quotient multiplied by 100
     * 
     */
    @JsonProperty("has_percentage")
    public void setHasPercentage(String hasPercentage) {
        this.hasPercentage = hasPercentage;
    }

    @JsonProperty("has_quotient")
    public String getHasQuotient() {
        return hasQuotient;
    }

    @JsonProperty("has_quotient")
    public void setHasQuotient(String hasQuotient) {
        this.hasQuotient = hasQuotient;
    }

    /**
     * total number of things in a particular reference set
     * 
     */
    @JsonProperty("has_total")
    public String getHasTotal() {
        return hasTotal;
    }

    /**
     * total number of things in a particular reference set
     * 
     */
    @JsonProperty("has_total")
    public void setHasTotal(String hasTotal) {
        this.hasTotal = hasTotal;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("hasCount", hasCount).append("hasPercentage", hasPercentage).append("hasQuotient", hasQuotient).append("hasTotal", hasTotal).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasPercentage).append(hasCount).append(hasQuotient).append(hasTotal).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof FrequencyQuantifier) == false) {
            return false;
        }
        FrequencyQuantifier rhs = ((FrequencyQuantifier) other);
        return new EqualsBuilder().append(hasPercentage, rhs.hasPercentage).append(hasCount, rhs.hasCount).append(hasQuotient, rhs.hasQuotient).append(hasTotal, rhs.hasTotal).isEquals();
    }

}
