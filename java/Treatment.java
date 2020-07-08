import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


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
        return new ToStringBuilder(this).append("hasPart", hasPart).append("treats", treats).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasPart).append(treats).toHashCode();
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
        return new EqualsBuilder().append(hasPart, rhs.hasPart).append(treats, rhs.treats).isEquals();
    }

}
