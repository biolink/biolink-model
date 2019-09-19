import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


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
        return new ToStringBuilder(this).append("hasCount", hasCount).append("hasPercentage", hasPercentage).append("hasQuotient", hasQuotient).append("hasTotal", hasTotal).append("object", object).append("subject", subject).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasPercentage).append(hasQuotient).append(subject).append(hasCount).append(hasTotal).append(object).toHashCode();
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
        return new EqualsBuilder().append(hasPercentage, rhs.hasPercentage).append(hasQuotient, rhs.hasQuotient).append(subject, rhs.subject).append(hasCount, rhs.hasCount).append(hasTotal, rhs.hasTotal).append(object, rhs.object).isEquals();
    }

}
