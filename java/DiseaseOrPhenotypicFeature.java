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
 * DiseaseOrPhenotypicFeature
 * <p>
 * Either one of a disease or an individual phenotypic feature. Some knowledge resources such as Monarch treat these as distinct, others such as MESH conflate.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "correlated_with",
    "has_biomarker",
    "in_taxon",
    "treated_by"
})
public class DiseaseOrPhenotypicFeature {

    /**
     * holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("correlated_with")
    @JsonPropertyDescription("holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.")
    private List<String> correlatedWith = new ArrayList<String>();
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
    @JsonProperty("correlated_with")
    public List<String> getCorrelatedWith() {
        return correlatedWith;
    }

    /**
     * holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("correlated_with")
    public void setCorrelatedWith(List<String> correlatedWith) {
        this.correlatedWith = correlatedWith;
    }

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
        return new ToStringBuilder(this).append("correlatedWith", correlatedWith).append("hasBiomarker", hasBiomarker).append("inTaxon", inTaxon).append("treatedBy", treatedBy).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasBiomarker).append(correlatedWith).append(inTaxon).append(treatedBy).toHashCode();
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
        return new EqualsBuilder().append(hasBiomarker, rhs.hasBiomarker).append(correlatedWith, rhs.correlatedWith).append(inTaxon, rhs.inTaxon).append(treatedBy, rhs.treatedBy).isEquals();
    }

}
