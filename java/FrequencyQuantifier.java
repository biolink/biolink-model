import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(FrequencyQuantifier.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("hasCount");
        sb.append('=');
        sb.append(((this.hasCount == null)?"<null>":this.hasCount));
        sb.append(',');
        sb.append("hasPercentage");
        sb.append('=');
        sb.append(((this.hasPercentage == null)?"<null>":this.hasPercentage));
        sb.append(',');
        sb.append("hasQuotient");
        sb.append('=');
        sb.append(((this.hasQuotient == null)?"<null>":this.hasQuotient));
        sb.append(',');
        sb.append("hasTotal");
        sb.append('=');
        sb.append(((this.hasTotal == null)?"<null>":this.hasTotal));
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
        result = ((result* 31)+((this.hasPercentage == null)? 0 :this.hasPercentage.hashCode()));
        result = ((result* 31)+((this.hasCount == null)? 0 :this.hasCount.hashCode()));
        result = ((result* 31)+((this.hasQuotient == null)? 0 :this.hasQuotient.hashCode()));
        result = ((result* 31)+((this.hasTotal == null)? 0 :this.hasTotal.hashCode()));
        return result;
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
        return (((((this.hasPercentage == rhs.hasPercentage)||((this.hasPercentage!= null)&&this.hasPercentage.equals(rhs.hasPercentage)))&&((this.hasCount == rhs.hasCount)||((this.hasCount!= null)&&this.hasCount.equals(rhs.hasCount))))&&((this.hasQuotient == rhs.hasQuotient)||((this.hasQuotient!= null)&&this.hasQuotient.equals(rhs.hasQuotient))))&&((this.hasTotal == rhs.hasTotal)||((this.hasTotal!= null)&&this.hasTotal.equals(rhs.hasTotal))));
    }

}
