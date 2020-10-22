import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * VariantToPopulationAssociation
 * <p>
 * An association between a variant and a population, where the variant has particular frequency in the population
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "has_count",
    "has_percentage",
    "has_quotient",
    "has_total",
    "object",
    "subject"
})
public class VariantToPopulationAssociation {

    @JsonProperty("has_count")
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
    @JsonProperty("has_total")
    private String hasTotal;
    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    private String object;
    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    private String subject;

    @JsonProperty("has_count")
    public String getHasCount() {
        return hasCount;
    }

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

    @JsonProperty("has_total")
    public String getHasTotal() {
        return hasTotal;
    }

    @JsonProperty("has_total")
    public void setHasTotal(String hasTotal) {
        this.hasTotal = hasTotal;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    public void setObject(String object) {
        this.object = object;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    public void setSubject(String subject) {
        this.subject = subject;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(VariantToPopulationAssociation.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        sb.append("object");
        sb.append('=');
        sb.append(((this.object == null)?"<null>":this.object));
        sb.append(',');
        sb.append("subject");
        sb.append('=');
        sb.append(((this.subject == null)?"<null>":this.subject));
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
        result = ((result* 31)+((this.hasQuotient == null)? 0 :this.hasQuotient.hashCode()));
        result = ((result* 31)+((this.subject == null)? 0 :this.subject.hashCode()));
        result = ((result* 31)+((this.hasCount == null)? 0 :this.hasCount.hashCode()));
        result = ((result* 31)+((this.hasTotal == null)? 0 :this.hasTotal.hashCode()));
        result = ((result* 31)+((this.object == null)? 0 :this.object.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof VariantToPopulationAssociation) == false) {
            return false;
        }
        VariantToPopulationAssociation rhs = ((VariantToPopulationAssociation) other);
        return (((((((this.hasPercentage == rhs.hasPercentage)||((this.hasPercentage!= null)&&this.hasPercentage.equals(rhs.hasPercentage)))&&((this.hasQuotient == rhs.hasQuotient)||((this.hasQuotient!= null)&&this.hasQuotient.equals(rhs.hasQuotient))))&&((this.subject == rhs.subject)||((this.subject!= null)&&this.subject.equals(rhs.subject))))&&((this.hasCount == rhs.hasCount)||((this.hasCount!= null)&&this.hasCount.equals(rhs.hasCount))))&&((this.hasTotal == rhs.hasTotal)||((this.hasTotal!= null)&&this.hasTotal.equals(rhs.hasTotal))))&&((this.object == rhs.object)||((this.object!= null)&&this.object.equals(rhs.object))));
    }

}
