import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * Allele
 * <p>
 * A genomic feature representing one of a set of coexisting sequence variants at a particular genomic locus
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "has_biological_sequence",
    "has_gene",
    "has_zygosity",
    "id",
    "in_taxon",
    "label"
})
public class Allele {

    /**
     * connects a genomic feature to its sequence
     * 
     */
    @JsonProperty("has_biological_sequence")
    @JsonPropertyDescription("connects a genomic feature to its sequence")
    private String hasBiologicalSequence;
    /**
     * connects and entity to a single gene
     * 
     */
    @JsonProperty("has_gene")
    @JsonPropertyDescription("connects and entity to a single gene")
    private String hasGene;
    @JsonProperty("has_zygosity")
    private String hasZygosity;
    @JsonProperty("id")
    private String id;
    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    @JsonPropertyDescription("connects a thing to a class representing a taxon")
    private String inTaxon;
    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    @JsonPropertyDescription("A human-readable name for a thing")
    private String label;

    /**
     * connects a genomic feature to its sequence
     * 
     */
    @JsonProperty("has_biological_sequence")
    public String getHasBiologicalSequence() {
        return hasBiologicalSequence;
    }

    /**
     * connects a genomic feature to its sequence
     * 
     */
    @JsonProperty("has_biological_sequence")
    public void setHasBiologicalSequence(String hasBiologicalSequence) {
        this.hasBiologicalSequence = hasBiologicalSequence;
    }

    /**
     * connects and entity to a single gene
     * 
     */
    @JsonProperty("has_gene")
    public String getHasGene() {
        return hasGene;
    }

    /**
     * connects and entity to a single gene
     * 
     */
    @JsonProperty("has_gene")
    public void setHasGene(String hasGene) {
        this.hasGene = hasGene;
    }

    @JsonProperty("has_zygosity")
    public String getHasZygosity() {
        return hasZygosity;
    }

    @JsonProperty("has_zygosity")
    public void setHasZygosity(String hasZygosity) {
        this.hasZygosity = hasZygosity;
    }

    @JsonProperty("id")
    public String getId() {
        return id;
    }

    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    public String getInTaxon() {
        return inTaxon;
    }

    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    public void setInTaxon(String inTaxon) {
        this.inTaxon = inTaxon;
    }

    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    public String getLabel() {
        return label;
    }

    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    public void setLabel(String label) {
        this.label = label;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("hasBiologicalSequence", hasBiologicalSequence).append("hasGene", hasGene).append("hasZygosity", hasZygosity).append("id", id).append("inTaxon", inTaxon).append("label", label).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(inTaxon).append(hasZygosity).append(hasBiologicalSequence).append(hasGene).append(id).append(label).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof Allele) == false) {
            return false;
        }
        Allele rhs = ((Allele) other);
        return new EqualsBuilder().append(inTaxon, rhs.inTaxon).append(hasZygosity, rhs.hasZygosity).append(hasBiologicalSequence, rhs.hasBiologicalSequence).append(hasGene, rhs.hasGene).append(id, rhs.id).append(label, rhs.label).isEquals();
    }

}
