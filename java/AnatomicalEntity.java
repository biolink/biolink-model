import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
        StringBuilder sb = new StringBuilder();
        sb.append(AnatomicalEntity.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("expresses");
        sb.append('=');
        sb.append(((this.expresses == null)?"<null>":this.expresses));
        sb.append(',');
        sb.append("inTaxon");
        sb.append('=');
        sb.append(((this.inTaxon == null)?"<null>":this.inTaxon));
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
        result = ((result* 31)+((this.inTaxon == null)? 0 :this.inTaxon.hashCode()));
        result = ((result* 31)+((this.expresses == null)? 0 :this.expresses.hashCode()));
        return result;
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
        return (((this.inTaxon == rhs.inTaxon)||((this.inTaxon!= null)&&this.inTaxon.equals(rhs.inTaxon)))&&((this.expresses == rhs.expresses)||((this.expresses!= null)&&this.expresses.equals(rhs.expresses))));
    }

}
