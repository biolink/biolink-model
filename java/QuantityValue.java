import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * QuantityValue
 * <p>
 * A value of an attribute that is quantitative and measurable, expressed as a combination of a unit and a numeric value
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "has_numeric_value",
    "has_unit"
})
public class QuantityValue {

    /**
     * connects a quantity value to a number
     * 
     */
    @JsonProperty("has_numeric_value")
    @JsonPropertyDescription("connects a quantity value to a number")
    private String hasNumericValue;
    /**
     * connects a quantity value to a unit
     * 
     */
    @JsonProperty("has_unit")
    @JsonPropertyDescription("connects a quantity value to a unit")
    private String hasUnit;

    /**
     * connects a quantity value to a number
     * 
     */
    @JsonProperty("has_numeric_value")
    public String getHasNumericValue() {
        return hasNumericValue;
    }

    /**
     * connects a quantity value to a number
     * 
     */
    @JsonProperty("has_numeric_value")
    public void setHasNumericValue(String hasNumericValue) {
        this.hasNumericValue = hasNumericValue;
    }

    /**
     * connects a quantity value to a unit
     * 
     */
    @JsonProperty("has_unit")
    public String getHasUnit() {
        return hasUnit;
    }

    /**
     * connects a quantity value to a unit
     * 
     */
    @JsonProperty("has_unit")
    public void setHasUnit(String hasUnit) {
        this.hasUnit = hasUnit;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("hasNumericValue", hasNumericValue).append("hasUnit", hasUnit).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasUnit).append(hasNumericValue).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof QuantityValue) == false) {
            return false;
        }
        QuantityValue rhs = ((QuantityValue) other);
        return new EqualsBuilder().append(hasUnit, rhs.hasUnit).append(hasNumericValue, rhs.hasNumericValue).isEquals();
    }

}
