import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * Treatment
 * <p>
 * A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "has_part",
    "treats"
})
public class Treatment {

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("has_part")
    private List<String> hasPart = new ArrayList<String>();
    /**
     * holds between a therapeutic procedure or chemical substance and a disease or phenotypic feature that it is used to treat
     * (Required)
     * 
     */
    @JsonProperty("treats")
    @JsonPropertyDescription("holds between a therapeutic procedure or chemical substance and a disease or phenotypic feature that it is used to treat")
    private List<String> treats = new ArrayList<String>();

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("has_part")
    public List<String> getHasPart() {
        return hasPart;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("has_part")
    public void setHasPart(List<String> hasPart) {
        this.hasPart = hasPart;
    }

    /**
     * holds between a therapeutic procedure or chemical substance and a disease or phenotypic feature that it is used to treat
     * (Required)
     * 
     */
    @JsonProperty("treats")
    public List<String> getTreats() {
        return treats;
    }

    /**
     * holds between a therapeutic procedure or chemical substance and a disease or phenotypic feature that it is used to treat
     * (Required)
     * 
     */
    @JsonProperty("treats")
    public void setTreats(List<String> treats) {
        this.treats = treats;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(Treatment.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("hasPart");
        sb.append('=');
        sb.append(((this.hasPart == null)?"<null>":this.hasPart));
        sb.append(',');
        sb.append("treats");
        sb.append('=');
        sb.append(((this.treats == null)?"<null>":this.treats));
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
        result = ((result* 31)+((this.hasPart == null)? 0 :this.hasPart.hashCode()));
        result = ((result* 31)+((this.treats == null)? 0 :this.treats.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof Treatment) == false) {
            return false;
        }
        Treatment rhs = ((Treatment) other);
        return (((this.hasPart == rhs.hasPart)||((this.hasPart!= null)&&this.hasPart.equals(rhs.hasPart)))&&((this.treats == rhs.treats)||((this.treats!= null)&&this.treats.equals(rhs.treats))));
    }

}
