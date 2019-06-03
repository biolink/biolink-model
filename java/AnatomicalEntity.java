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
 * AnatomicalEntity
 * <p>
 * A subcellular location, cell type or gross anatomical part
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "expresses",
    "in_taxon"
})
public class AnatomicalEntity {

    /**
     * holds between an anatomical entity and gene or gene product that is expressed there
     * 
     */
    @JsonProperty("expresses")
    @JsonPropertyDescription("holds between an anatomical entity and gene or gene product that is expressed there")
    private List<String> expresses = new ArrayList<String>();
    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    @JsonPropertyDescription("connects a thing to a class representing a taxon")
    private List<String> inTaxon = new ArrayList<String>();

    /**
     * holds between an anatomical entity and gene or gene product that is expressed there
     * 
     */
    @JsonProperty("expresses")
    public List<String> getExpresses() {
        return expresses;
    }

    /**
     * holds between an anatomical entity and gene or gene product that is expressed there
     * 
     */
    @JsonProperty("expresses")
    public void setExpresses(List<String> expresses) {
        this.expresses = expresses;
    }

    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    public List<String> getInTaxon() {
        return inTaxon;
    }

    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    public void setInTaxon(List<String> inTaxon) {
        this.inTaxon = inTaxon;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("expresses", expresses).append("inTaxon", inTaxon).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(inTaxon).append(expresses).toHashCode();
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
        return new EqualsBuilder().append(inTaxon, rhs.inTaxon).append(expresses, rhs.expresses).isEquals();
    }

}
