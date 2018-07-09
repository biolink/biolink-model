import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * Gene
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "gene_associated_with_condition",
    "genetically_interacts_with",
    "has_gene_product"
})
public class Gene {

    /**
     * holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
     * 
     */
    @JsonProperty("gene_associated_with_condition")
    @JsonPropertyDescription("holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with")
    private String geneAssociatedWithCondition;
    /**
     * holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
     * 
     */
    @JsonProperty("genetically_interacts_with")
    @JsonPropertyDescription("holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.")
    private String geneticallyInteractsWith;
    /**
     * holds between a gene and a transcribed and/or translated product generated from it
     * 
     */
    @JsonProperty("has_gene_product")
    @JsonPropertyDescription("holds between a gene and a transcribed and/or translated product generated from it")
    private String hasGeneProduct;

    /**
     * holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
     * 
     */
    @JsonProperty("gene_associated_with_condition")
    public String getGeneAssociatedWithCondition() {
        return geneAssociatedWithCondition;
    }

    /**
     * holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
     * 
     */
    @JsonProperty("gene_associated_with_condition")
    public void setGeneAssociatedWithCondition(String geneAssociatedWithCondition) {
        this.geneAssociatedWithCondition = geneAssociatedWithCondition;
    }

    /**
     * holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
     * 
     */
    @JsonProperty("genetically_interacts_with")
    public String getGeneticallyInteractsWith() {
        return geneticallyInteractsWith;
    }

    /**
     * holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
     * 
     */
    @JsonProperty("genetically_interacts_with")
    public void setGeneticallyInteractsWith(String geneticallyInteractsWith) {
        this.geneticallyInteractsWith = geneticallyInteractsWith;
    }

    /**
     * holds between a gene and a transcribed and/or translated product generated from it
     * 
     */
    @JsonProperty("has_gene_product")
    public String getHasGeneProduct() {
        return hasGeneProduct;
    }

    /**
     * holds between a gene and a transcribed and/or translated product generated from it
     * 
     */
    @JsonProperty("has_gene_product")
    public void setHasGeneProduct(String hasGeneProduct) {
        this.hasGeneProduct = hasGeneProduct;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("geneAssociatedWithCondition", geneAssociatedWithCondition).append("geneticallyInteractsWith", geneticallyInteractsWith).append("hasGeneProduct", hasGeneProduct).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasGeneProduct).append(geneAssociatedWithCondition).append(geneticallyInteractsWith).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof Gene) == false) {
            return false;
        }
        Gene rhs = ((Gene) other);
        return new EqualsBuilder().append(hasGeneProduct, rhs.hasGeneProduct).append(geneAssociatedWithCondition, rhs.geneAssociatedWithCondition).append(geneticallyInteractsWith, rhs.geneticallyInteractsWith).isEquals();
    }

}
