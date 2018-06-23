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
    "has_quotient",
    "has_total",
    "object",
    "subject"
})
public class VariantToPopulationAssociation {

    /**
     * number in object population that carry a particular allele, aka allele count
     * 
     */
    @JsonProperty("has_count")
    @JsonPropertyDescription("number in object population that carry a particular allele, aka allele count")
    private String hasCount;
    /**
     * frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency
     * 
     */
    @JsonProperty("has_quotient")
    @JsonPropertyDescription("frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency")
    private String hasQuotient;
    /**
     * number all populations that carry a particular allele, aka allele number
     * 
     */
    @JsonProperty("has_total")
    @JsonPropertyDescription("number all populations that carry a particular allele, aka allele number")
    private String hasTotal;
    /**
     * the population that is observed to have the frequency
     * 
     */
    @JsonProperty("object")
    @JsonPropertyDescription("the population that is observed to have the frequency")
    private String object;
    /**
     * an allele that has a certain frequency in a given population
     * 
     */
    @JsonProperty("subject")
    @JsonPropertyDescription("an allele that has a certain frequency in a given population")
    private String subject;

    /**
     * number in object population that carry a particular allele, aka allele count
     * 
     */
    @JsonProperty("has_count")
    public String getHasCount() {
        return hasCount;
    }

    /**
     * number in object population that carry a particular allele, aka allele count
     * 
     */
    @JsonProperty("has_count")
    public void setHasCount(String hasCount) {
        this.hasCount = hasCount;
    }

    /**
     * frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency
     * 
     */
    @JsonProperty("has_quotient")
    public String getHasQuotient() {
        return hasQuotient;
    }

    /**
     * frequency of allele in population, expressed as a number with allele divided by number in reference population, aka allele frequency
     * 
     */
    @JsonProperty("has_quotient")
    public void setHasQuotient(String hasQuotient) {
        this.hasQuotient = hasQuotient;
    }

    /**
     * number all populations that carry a particular allele, aka allele number
     * 
     */
    @JsonProperty("has_total")
    public String getHasTotal() {
        return hasTotal;
    }

    /**
     * number all populations that carry a particular allele, aka allele number
     * 
     */
    @JsonProperty("has_total")
    public void setHasTotal(String hasTotal) {
        this.hasTotal = hasTotal;
    }

    /**
     * the population that is observed to have the frequency
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * the population that is observed to have the frequency
     * 
     */
    @JsonProperty("object")
    public void setObject(String object) {
        this.object = object;
    }

    /**
     * an allele that has a certain frequency in a given population
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * an allele that has a certain frequency in a given population
     * 
     */
    @JsonProperty("subject")
    public void setSubject(String subject) {
        this.subject = subject;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("hasCount", hasCount).append("hasQuotient", hasQuotient).append("hasTotal", hasTotal).append("object", object).append("subject", subject).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasCount).append(hasQuotient).append(hasTotal).append(subject).append(object).toHashCode();
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
        return new EqualsBuilder().append(hasCount, rhs.hasCount).append(hasQuotient, rhs.hasQuotient).append(hasTotal, rhs.hasTotal).append(subject, rhs.subject).append(object, rhs.object).isEquals();
    }

}
