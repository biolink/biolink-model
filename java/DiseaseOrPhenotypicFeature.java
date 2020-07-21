import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * DiseaseOrPhenotypicFeature
 * <p>
 * Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "has_biomarker",
    "in_taxon",
    "treated_by"
})
public class DiseaseOrPhenotypicFeature {

    /**
     * holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("has_biomarker")
    @JsonPropertyDescription("holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.")
    private List<String> hasBiomarker = new ArrayList<String>();
    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    @JsonPropertyDescription("connects a thing to a class representing a taxon")
    private List<String> inTaxon = new ArrayList<String>();
    /**
     * holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition
     * 
     */
    @JsonProperty("treated_by")
    @JsonPropertyDescription("holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition")
    private List<String> treatedBy = new ArrayList<String>();

    /**
     * holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("has_biomarker")
    public List<String> getHasBiomarker() {
        return hasBiomarker;
    }

    /**
     * holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("has_biomarker")
    public void setHasBiomarker(List<String> hasBiomarker) {
        this.hasBiomarker = hasBiomarker;
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

    /**
     * holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition
     * 
     */
    @JsonProperty("treated_by")
    public List<String> getTreatedBy() {
        return treatedBy;
    }

    /**
     * holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition
     * 
     */
    @JsonProperty("treated_by")
    public void setTreatedBy(List<String> treatedBy) {
        this.treatedBy = treatedBy;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(DiseaseOrPhenotypicFeature.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("hasBiomarker");
        sb.append('=');
        sb.append(((this.hasBiomarker == null)?"<null>":this.hasBiomarker));
        sb.append(',');
        sb.append("inTaxon");
        sb.append('=');
        sb.append(((this.inTaxon == null)?"<null>":this.inTaxon));
        sb.append(',');
        sb.append("treatedBy");
        sb.append('=');
        sb.append(((this.treatedBy == null)?"<null>":this.treatedBy));
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
        result = ((result* 31)+((this.hasBiomarker == null)? 0 :this.hasBiomarker.hashCode()));
        result = ((result* 31)+((this.inTaxon == null)? 0 :this.inTaxon.hashCode()));
        result = ((result* 31)+((this.treatedBy == null)? 0 :this.treatedBy.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof DiseaseOrPhenotypicFeature) == false) {
            return false;
        }
        DiseaseOrPhenotypicFeature rhs = ((DiseaseOrPhenotypicFeature) other);
        return ((((this.hasBiomarker == rhs.hasBiomarker)||((this.hasBiomarker!= null)&&this.hasBiomarker.equals(rhs.hasBiomarker)))&&((this.inTaxon == rhs.inTaxon)||((this.inTaxon!= null)&&this.inTaxon.equals(rhs.inTaxon))))&&((this.treatedBy == rhs.treatedBy)||((this.treatedBy!= null)&&this.treatedBy.equals(rhs.treatedBy))));
    }

}
