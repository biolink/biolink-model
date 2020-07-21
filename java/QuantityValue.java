import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(QuantityValue.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("hasNumericValue");
        sb.append('=');
        sb.append(((this.hasNumericValue == null)?"<null>":this.hasNumericValue));
        sb.append(',');
        sb.append("hasUnit");
        sb.append('=');
        sb.append(((this.hasUnit == null)?"<null>":this.hasUnit));
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
        result = ((result* 31)+((this.hasUnit == null)? 0 :this.hasUnit.hashCode()));
        result = ((result* 31)+((this.hasNumericValue == null)? 0 :this.hasNumericValue.hashCode()));
        return result;
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
        return (((this.hasUnit == rhs.hasUnit)||((this.hasUnit!= null)&&this.hasUnit.equals(rhs.hasUnit)))&&((this.hasNumericValue == rhs.hasNumericValue)||((this.hasNumericValue!= null)&&this.hasNumericValue.equals(rhs.hasNumericValue))));
    }

}
