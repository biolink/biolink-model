import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(GeneOrGeneProduct.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("expressedIn");
        sb.append('=');
        sb.append(((this.expressedIn == null)?"<null>":this.expressedIn));
        sb.append(',');
        sb.append("inCellPopulationWith");
        sb.append('=');
        sb.append(((this.inCellPopulationWith == null)?"<null>":this.inCellPopulationWith));
        sb.append(',');
        sb.append("inComplexWith");
        sb.append('=');
        sb.append(((this.inComplexWith == null)?"<null>":this.inComplexWith));
        sb.append(',');
        sb.append("inPathwayWith");
        sb.append('=');
        sb.append(((this.inPathwayWith == null)?"<null>":this.inPathwayWith));
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
        result = ((result* 31)+((this.expressedIn == null)? 0 :this.expressedIn.hashCode()));
        result = ((result* 31)+((this.inCellPopulationWith == null)? 0 :this.inCellPopulationWith.hashCode()));
        result = ((result* 31)+((this.inComplexWith == null)? 0 :this.inComplexWith.hashCode()));
        result = ((result* 31)+((this.inPathwayWith == null)? 0 :this.inPathwayWith.hashCode()));
        return result;
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
        return (((((this.expressedIn == rhs.expressedIn)||((this.expressedIn!= null)&&this.expressedIn.equals(rhs.expressedIn)))&&((this.inCellPopulationWith == rhs.inCellPopulationWith)||((this.inCellPopulationWith!= null)&&this.inCellPopulationWith.equals(rhs.inCellPopulationWith))))&&((this.inComplexWith == rhs.inComplexWith)||((this.inComplexWith!= null)&&this.inComplexWith.equals(rhs.inComplexWith))))&&((this.inPathwayWith == rhs.inPathwayWith)||((this.inPathwayWith!= null)&&this.inPathwayWith.equals(rhs.inPathwayWith))));
    }

}
