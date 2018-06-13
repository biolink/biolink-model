import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
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
    "has_exposure_parts",
    "treats"
})
public class Treatment {

    @JsonProperty("has_exposure_parts")
    private List<String> hasExposureParts = new ArrayList<String>();
    @JsonProperty("treats")
    private String treats;

    @JsonProperty("has_exposure_parts")
    public List<String> getHasExposureParts() {
        return hasExposureParts;
    }

    @JsonProperty("has_exposure_parts")
    public void setHasExposureParts(List<String> hasExposureParts) {
        this.hasExposureParts = hasExposureParts;
    }

    @JsonProperty("treats")
    public String getTreats() {
        return treats;
    }

    @JsonProperty("treats")
    public void setTreats(String treats) {
        this.treats = treats;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("hasExposureParts", hasExposureParts).append("treats", treats).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasExposureParts).append(treats).toHashCode();
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
        return new EqualsBuilder().append(hasExposureParts, rhs.hasExposureParts).append(treats, rhs.treats).isEquals();
    }

}
