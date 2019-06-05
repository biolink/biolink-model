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
 * PopulationOfIndividualOrganisms
 * <p>
 * A collection of individuals from the same taxonomic class distinguished by one or more characteristics. Characteristics can include, but are not limited to, shared geographic location, genetics, phenotypes [Alliance for Genome Resources]
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "in_taxon"
})
public class PopulationOfIndividualOrganisms {

    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    @JsonPropertyDescription("connects a thing to a class representing a taxon")
    private List<String> inTaxon = new ArrayList<String>();

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
        return new ToStringBuilder(this).append("inTaxon", inTaxon).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(inTaxon).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof PopulationOfIndividualOrganisms) == false) {
            return false;
        }
        PopulationOfIndividualOrganisms rhs = ((PopulationOfIndividualOrganisms) other);
        return new EqualsBuilder().append(inTaxon, rhs.inTaxon).isEquals();
    }

}
