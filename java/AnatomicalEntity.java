import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * AnatomicalEntity
 * <p>
 * A subcellular location, cell type or gross anatomical part
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "expresses"
})
public class AnatomicalEntity {

    /**
     * holds between an anatomical entity and gene or gene product that is expressed there
     * 
     */
    @JsonProperty("expresses")
    @JsonPropertyDescription("holds between an anatomical entity and gene or gene product that is expressed there")
    private String expresses;

    /**
     * holds between an anatomical entity and gene or gene product that is expressed there
     * 
     */
    @JsonProperty("expresses")
    public String getExpresses() {
        return expresses;
    }

    /**
     * holds between an anatomical entity and gene or gene product that is expressed there
     * 
     */
    @JsonProperty("expresses")
    public void setExpresses(String expresses) {
        this.expresses = expresses;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("expresses", expresses).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(expresses).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof AnatomicalEntity) == false) {
            return false;
        }
        AnatomicalEntity rhs = ((AnatomicalEntity) other);
        return new EqualsBuilder().append(expresses, rhs.expresses).isEquals();
    }

}
