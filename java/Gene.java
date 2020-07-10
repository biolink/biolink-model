import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
    private List<String> geneAssociatedWithCondition = new ArrayList<String>();
    /**
     * holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
     * 
     */
    @JsonProperty("genetically_interacts_with")
    @JsonPropertyDescription("holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.")
    private List<String> geneticallyInteractsWith = new ArrayList<String>();
    /**
     * holds between a gene and a transcribed and/or translated product generated from it
     * 
     */
    @JsonProperty("has_gene_product")
    @JsonPropertyDescription("holds between a gene and a transcribed and/or translated product generated from it")
    private List<String> hasGeneProduct = new ArrayList<String>();

    /**
     * holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
     * 
     */
    @JsonProperty("gene_associated_with_condition")
    public List<String> getGeneAssociatedWithCondition() {
        return geneAssociatedWithCondition;
    }

    /**
     * holds between a gene and a disease or phenotypic feature that the gene or its alleles/products may influence, contribute to, or correlate with
     * 
     */
    @JsonProperty("gene_associated_with_condition")
    public void setGeneAssociatedWithCondition(List<String> geneAssociatedWithCondition) {
        this.geneAssociatedWithCondition = geneAssociatedWithCondition;
    }

    /**
     * holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
     * 
     */
    @JsonProperty("genetically_interacts_with")
    public List<String> getGeneticallyInteractsWith() {
        return geneticallyInteractsWith;
    }

    /**
     * holds between two genes whose phenotypic effects are dependent on each other in some way - such that their combined phenotypic effects are the result of some interaction between the activity of their gene products. Examples include epistasis and synthetic lethality.
     * 
     */
    @JsonProperty("genetically_interacts_with")
    public void setGeneticallyInteractsWith(List<String> geneticallyInteractsWith) {
        this.geneticallyInteractsWith = geneticallyInteractsWith;
    }

    /**
     * holds between a gene and a transcribed and/or translated product generated from it
     * 
     */
    @JsonProperty("has_gene_product")
    public List<String> getHasGeneProduct() {
        return hasGeneProduct;
    }

    /**
     * holds between a gene and a transcribed and/or translated product generated from it
     * 
     */
    @JsonProperty("has_gene_product")
    public void setHasGeneProduct(List<String> hasGeneProduct) {
        this.hasGeneProduct = hasGeneProduct;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(Gene.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("geneAssociatedWithCondition");
        sb.append('=');
        sb.append(((this.geneAssociatedWithCondition == null)?"<null>":this.geneAssociatedWithCondition));
        sb.append(',');
        sb.append("geneticallyInteractsWith");
        sb.append('=');
        sb.append(((this.geneticallyInteractsWith == null)?"<null>":this.geneticallyInteractsWith));
        sb.append(',');
        sb.append("hasGeneProduct");
        sb.append('=');
        sb.append(((this.hasGeneProduct == null)?"<null>":this.hasGeneProduct));
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
        result = ((result* 31)+((this.hasGeneProduct == null)? 0 :this.hasGeneProduct.hashCode()));
        result = ((result* 31)+((this.geneAssociatedWithCondition == null)? 0 :this.geneAssociatedWithCondition.hashCode()));
        result = ((result* 31)+((this.geneticallyInteractsWith == null)? 0 :this.geneticallyInteractsWith.hashCode()));
        return result;
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
        return ((((this.hasGeneProduct == rhs.hasGeneProduct)||((this.hasGeneProduct!= null)&&this.hasGeneProduct.equals(rhs.hasGeneProduct)))&&((this.geneAssociatedWithCondition == rhs.geneAssociatedWithCondition)||((this.geneAssociatedWithCondition!= null)&&this.geneAssociatedWithCondition.equals(rhs.geneAssociatedWithCondition))))&&((this.geneticallyInteractsWith == rhs.geneticallyInteractsWith)||((this.geneticallyInteractsWith!= null)&&this.geneticallyInteractsWith.equals(rhs.geneticallyInteractsWith))));
    }

}
