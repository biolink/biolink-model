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
    "treated_by"
})
public class DiseaseOrPhenotypicFeature {

    /**
     * holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("correlated_with")
    @JsonPropertyDescription("holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.")
    private String correlatedWith;
    /**
     * holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("has_biomarker")
    @JsonPropertyDescription("holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.")
    private String hasBiomarker;
    /**
     * holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition 
     * 
     */
    @JsonProperty("treated_by")
    @JsonPropertyDescription("holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition ")
    private String treatedBy;

    /**
     * holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("correlated_with")
    public String getCorrelatedWith() {
        return correlatedWith;
    }

    /**
     * holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("correlated_with")
    public void setCorrelatedWith(String correlatedWith) {
        this.correlatedWith = correlatedWith;
    }

    /**
     * holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("has_biomarker")
    public String getHasBiomarker() {
        return hasBiomarker;
    }

    /**
     * holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("has_biomarker")
    public void setHasBiomarker(String hasBiomarker) {
        this.hasBiomarker = hasBiomarker;
    }

    /**
     * holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition 
     * 
     */
    @JsonProperty("treated_by")
    public String getTreatedBy() {
        return treatedBy;
    }

    /**
     * holds between a disease or phenotypic feature and a therapeutic process or chemical substance that is used to treat the condition 
     * 
     */
    @JsonProperty("treated_by")
    public void setTreatedBy(String treatedBy) {
        this.treatedBy = treatedBy;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("correlatedWith", correlatedWith).append("hasBiomarker", hasBiomarker).append("treatedBy", treatedBy).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasBiomarker).append(correlatedWith).append(treatedBy).toHashCode();
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
        return new EqualsBuilder().append(hasBiomarker, rhs.hasBiomarker).append(correlatedWith, rhs.correlatedWith).append(treatedBy, rhs.treatedBy).isEquals();
    }

}
