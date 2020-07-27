import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(Genotype.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("hasZygosity");
        sb.append('=');
        sb.append(((this.hasZygosity == null)?"<null>":this.hasZygosity));
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
        result = ((result* 31)+((this.hasZygosity == null)? 0 :this.hasZygosity.hashCode()));
        return result;
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
        return ((this.hasZygosity == rhs.hasZygosity)||((this.hasZygosity!= null)&&this.hasZygosity.equals(rhs.hasZygosity)));
    }

}
