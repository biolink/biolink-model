import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * SequenceVariant
 * <p>
 * An allele that varies in its sequence from what is considered the reference allele at that locus.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "category",
    "has_biological_sequence",
    "has_gene",
    "id",
    "in_taxon",
    "name"
})
public class SequenceVariant {

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * 
     */
    @JsonProperty("category")
    @JsonPropertyDescription("Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag")
    private String category;
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
    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * 
     */
    @JsonProperty("id")
    @JsonPropertyDescription("A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI")
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
    @JsonProperty("name")
    @JsonPropertyDescription("A human-readable name for a thing")
    private String name;

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * 
     */
    @JsonProperty("category")
    public String getCategory() {
        return category;
    }

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * 
     */
    @JsonProperty("category")
    public void setCategory(String category) {
        this.category = category;
    }

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

    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * 
     */
    @JsonProperty("id")
    public String getId() {
        return id;
    }

    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * 
     */
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
    @JsonProperty("name")
    public String getName() {
        return name;
    }

    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("name")
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("category", category).append("hasBiologicalSequence", hasBiologicalSequence).append("hasGene", hasGene).append("id", id).append("inTaxon", inTaxon).append("name", name).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(inTaxon).append(name).append(hasBiologicalSequence).append(hasGene).append(id).append(category).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof SequenceVariant) == false) {
            return false;
        }
        SequenceVariant rhs = ((SequenceVariant) other);
        return new EqualsBuilder().append(inTaxon, rhs.inTaxon).append(name, rhs.name).append(hasBiologicalSequence, rhs.hasBiologicalSequence).append(hasGene, rhs.hasGene).append(id, rhs.id).append(category, rhs.category).isEquals();
    }

}
