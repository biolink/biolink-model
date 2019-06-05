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
 * GeneOrGeneProduct
 * <p>
 * a union of genes or gene products. Frequently an identifier for one will be used as proxy for another
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "expressed_in",
    "in_cell_population_with",
    "in_complex_with",
    "in_pathway_with"
})
public class GeneOrGeneProduct {

    /**
     * holds between a gene or gene product and an anatomical entity in which it is expressed
     * 
     */
    @JsonProperty("expressed_in")
    @JsonPropertyDescription("holds between a gene or gene product and an anatomical entity in which it is expressed")
    private List<String> expressedIn = new ArrayList<String>();
    /**
     * holds between two genes or gene products that are expressed in the same cell type or population
     * 
     */
    @JsonProperty("in_cell_population_with")
    @JsonPropertyDescription("holds between two genes or gene products that are expressed in the same cell type or population")
    private List<String> inCellPopulationWith = new ArrayList<String>();
    /**
     * holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
     * 
     */
    @JsonProperty("in_complex_with")
    @JsonPropertyDescription("holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex")
    private List<String> inComplexWith = new ArrayList<String>();
    /**
     * holds between two genes or gene products that are part of in the same biological pathway
     * 
     */
    @JsonProperty("in_pathway_with")
    @JsonPropertyDescription("holds between two genes or gene products that are part of in the same biological pathway")
    private List<String> inPathwayWith = new ArrayList<String>();

    /**
     * holds between a gene or gene product and an anatomical entity in which it is expressed
     * 
     */
    @JsonProperty("expressed_in")
    public List<String> getExpressedIn() {
        return expressedIn;
    }

    /**
     * holds between a gene or gene product and an anatomical entity in which it is expressed
     * 
     */
    @JsonProperty("expressed_in")
    public void setExpressedIn(List<String> expressedIn) {
        this.expressedIn = expressedIn;
    }

    /**
     * holds between two genes or gene products that are expressed in the same cell type or population
     * 
     */
    @JsonProperty("in_cell_population_with")
    public List<String> getInCellPopulationWith() {
        return inCellPopulationWith;
    }

    /**
     * holds between two genes or gene products that are expressed in the same cell type or population
     * 
     */
    @JsonProperty("in_cell_population_with")
    public void setInCellPopulationWith(List<String> inCellPopulationWith) {
        this.inCellPopulationWith = inCellPopulationWith;
    }

    /**
     * holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
     * 
     */
    @JsonProperty("in_complex_with")
    public List<String> getInComplexWith() {
        return inComplexWith;
    }

    /**
     * holds between two genes or gene products that are part of (or code for products that are part of) in the same macromolecular complex
     * 
     */
    @JsonProperty("in_complex_with")
    public void setInComplexWith(List<String> inComplexWith) {
        this.inComplexWith = inComplexWith;
    }

    /**
     * holds between two genes or gene products that are part of in the same biological pathway
     * 
     */
    @JsonProperty("in_pathway_with")
    public List<String> getInPathwayWith() {
        return inPathwayWith;
    }

    /**
     * holds between two genes or gene products that are part of in the same biological pathway
     * 
     */
    @JsonProperty("in_pathway_with")
    public void setInPathwayWith(List<String> inPathwayWith) {
        this.inPathwayWith = inPathwayWith;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("expressedIn", expressedIn).append("inCellPopulationWith", inCellPopulationWith).append("inComplexWith", inComplexWith).append("inPathwayWith", inPathwayWith).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(expressedIn).append(inCellPopulationWith).append(inComplexWith).append(inPathwayWith).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof GeneOrGeneProduct) == false) {
            return false;
        }
        GeneOrGeneProduct rhs = ((GeneOrGeneProduct) other);
        return new EqualsBuilder().append(expressedIn, rhs.expressedIn).append(inCellPopulationWith, rhs.inCellPopulationWith).append(inComplexWith, rhs.inComplexWith).append(inPathwayWith, rhs.inPathwayWith).isEquals();
    }

}
