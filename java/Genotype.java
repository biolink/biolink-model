import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * Genotype
 * <p>
 * An information content entity that describes a genome by specifying the total variation in genomic sequence and/or gene expression, relative to some extablished background
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "has_zygosity"
})
public class Genotype {

    @JsonProperty("has_zygosity")
    private String hasZygosity;

    @JsonProperty("has_zygosity")
    public String getHasZygosity() {
        return hasZygosity;
    }

    @JsonProperty("has_zygosity")
    public void setHasZygosity(String hasZygosity) {
        this.hasZygosity = hasZygosity;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("hasZygosity", hasZygosity).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasZygosity).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof Genotype) == false) {
            return false;
        }
        Genotype rhs = ((Genotype) other);
        return new EqualsBuilder().append(hasZygosity, rhs.hasZygosity).isEquals();
    }

}
