import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * Association
 * <p>
 * A typed association between two entities, supported by evidence
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "association_slot",
    "association_type",
    "change_is_catalyzed_by",
    "chi_squared_statistic",
    "clinical_modifier_qualifier",
    "edge_label",
    "frequency_qualifier",
    "has_confidence_level",
    "has_evidence",
    "id",
    "negated",
    "object",
    "onset_qualifier",
    "p_value",
    "provided_by",
    "publications",
    "qualifiers",
    "quantifier_qualifier",
    "relation",
    "sequence_variant_qualifier",
    "severity_qualifier",
    "sex_qualifier",
    "stage_qualifier",
    "subject"
})
public class Association {

    /**
     * any slot that relates an association to another entity
     * 
     */
    @JsonProperty("association_slot")
    @JsonPropertyDescription("any slot that relates an association to another entity")
    private String associationSlot;
    /**
     * connects an association to the type of association (e.g. gene to phenotype)
     * 
     */
    @JsonProperty("association_type")
    @JsonPropertyDescription("connects an association to the type of association (e.g. gene to phenotype)")
    private String associationType;
    /**
     * hyperedge connecting an association between two causally connected entities (for example, two chemical entities, or a chemical entity in that changes location) and the gene product, gene, or complex that enables or catalyzes the change.
     * 
     */
    @JsonProperty("change_is_catalyzed_by")
    @JsonPropertyDescription("hyperedge connecting an association between two causally connected entities (for example, two chemical entities, or a chemical entity in that changes location) and the gene product, gene, or complex that enables or catalyzes the change.")
    private List<String> changeIsCatalyzedBy = new ArrayList<String>();
    /**
     * represents the chi-squared statistic computed from observations
     * 
     */
    @JsonProperty("chi_squared_statistic")
    @JsonPropertyDescription("represents the chi-squared statistic computed from observations")
    private String chiSquaredStatistic;
    /**
     * Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
     * 
     */
    @JsonProperty("clinical_modifier_qualifier")
    @JsonPropertyDescription("Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects")
    private String clinicalModifierQualifier;
    /**
     * A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * (Required)
     * 
     */
    @JsonProperty("edge_label")
    @JsonPropertyDescription("A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.")
    private String edgeLabel;
    /**
     * a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
     * 
     */
    @JsonProperty("frequency_qualifier")
    @JsonPropertyDescription("a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject")
    private String frequencyQualifier;
    /**
     * connects an association to a qualitative term denoting the level of confidence
     * 
     */
    @JsonProperty("has_confidence_level")
    @JsonPropertyDescription("connects an association to a qualitative term denoting the level of confidence")
    private String hasConfidenceLevel;
    /**
     * connects an association to an instance of supporting evidence
     * 
     */
    @JsonProperty("has_evidence")
    @JsonPropertyDescription("connects an association to an instance of supporting evidence")
    private String hasEvidence;
    /**
     * A unique identifier for an association
     * (Required)
     * 
     */
    @JsonProperty("id")
    @JsonPropertyDescription("A unique identifier for an association")
    private String id;
    /**
     * if set to true, then the association is negated i.e. is not true
     * 
     */
    @JsonProperty("negated")
    @JsonPropertyDescription("if set to true, then the association is negated i.e. is not true")
    private String negated;
    /**
     * connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * (Required)
     * 
     */
    @JsonProperty("object")
    @JsonPropertyDescription("connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.")
    private String object;
    /**
     * a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
     * 
     */
    @JsonProperty("onset_qualifier")
    @JsonPropertyDescription("a qualifier used in a phenotypic association to state when the phenotype appears is in the subject")
    private String onsetQualifier;
    /**
     * A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone.
     * 
     */
    @JsonProperty("p_value")
    @JsonPropertyDescription("A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone.")
    private String pValue;
    /**
     * connects an association to the agent (person, organization or group) that provided it
     * 
     */
    @JsonProperty("provided_by")
    @JsonPropertyDescription("connects an association to the agent (person, organization or group) that provided it")
    private List<String> providedBy = new ArrayList<String>();
    /**
     * connects an association to publications supporting the association
     * 
     */
    @JsonProperty("publications")
    @JsonPropertyDescription("connects an association to publications supporting the association")
    private List<String> publications = new ArrayList<String>();
    /**
     * connects an association to qualifiers that modify or qualify the meaning of that association
     * 
     */
    @JsonProperty("qualifiers")
    @JsonPropertyDescription("connects an association to qualifiers that modify or qualify the meaning of that association")
    private List<String> qualifiers = new ArrayList<String>();
    /**
     * A measurable quantity for the object of the association
     * 
     */
    @JsonProperty("quantifier_qualifier")
    @JsonPropertyDescription("A measurable quantity for the object of the association")
    private String quantifierQualifier;
    /**
     * the relationship type by which a subject is connected to an object in an association
     * (Required)
     * 
     */
    @JsonProperty("relation")
    @JsonPropertyDescription("the relationship type by which a subject is connected to an object in an association")
    private String relation;
    /**
     * a qualifier used in an association where the variant
     * 
     */
    @JsonProperty("sequence_variant_qualifier")
    @JsonPropertyDescription("a qualifier used in an association where the variant")
    private String sequenceVariantQualifier;
    /**
     * a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
     * 
     */
    @JsonProperty("severity_qualifier")
    @JsonPropertyDescription("a qualifier used in a phenotypic association to state how severe the phenotype is in the subject")
    private String severityQualifier;
    /**
     * a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
     * 
     */
    @JsonProperty("sex_qualifier")
    @JsonPropertyDescription("a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.")
    private String sexQualifier;
    /**
     * stage at which expression takes place
     * 
     */
    @JsonProperty("stage_qualifier")
    @JsonPropertyDescription("stage at which expression takes place")
    private String stageQualifier;
    /**
     * connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * (Required)
     * 
     */
    @JsonProperty("subject")
    @JsonPropertyDescription("connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.")
    private String subject;

    /**
     * any slot that relates an association to another entity
     * 
     */
    @JsonProperty("association_slot")
    public String getAssociationSlot() {
        return associationSlot;
    }

    /**
     * any slot that relates an association to another entity
     * 
     */
    @JsonProperty("association_slot")
    public void setAssociationSlot(String associationSlot) {
        this.associationSlot = associationSlot;
    }

    /**
     * connects an association to the type of association (e.g. gene to phenotype)
     * 
     */
    @JsonProperty("association_type")
    public String getAssociationType() {
        return associationType;
    }

    /**
     * connects an association to the type of association (e.g. gene to phenotype)
     * 
     */
    @JsonProperty("association_type")
    public void setAssociationType(String associationType) {
        this.associationType = associationType;
    }

    /**
     * hyperedge connecting an association between two causally connected entities (for example, two chemical entities, or a chemical entity in that changes location) and the gene product, gene, or complex that enables or catalyzes the change.
     * 
     */
    @JsonProperty("change_is_catalyzed_by")
    public List<String> getChangeIsCatalyzedBy() {
        return changeIsCatalyzedBy;
    }

    /**
     * hyperedge connecting an association between two causally connected entities (for example, two chemical entities, or a chemical entity in that changes location) and the gene product, gene, or complex that enables or catalyzes the change.
     * 
     */
    @JsonProperty("change_is_catalyzed_by")
    public void setChangeIsCatalyzedBy(List<String> changeIsCatalyzedBy) {
        this.changeIsCatalyzedBy = changeIsCatalyzedBy;
    }

    /**
     * represents the chi-squared statistic computed from observations
     * 
     */
    @JsonProperty("chi_squared_statistic")
    public String getChiSquaredStatistic() {
        return chiSquaredStatistic;
    }

    /**
     * represents the chi-squared statistic computed from observations
     * 
     */
    @JsonProperty("chi_squared_statistic")
    public void setChiSquaredStatistic(String chiSquaredStatistic) {
        this.chiSquaredStatistic = chiSquaredStatistic;
    }

    /**
     * Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
     * 
     */
    @JsonProperty("clinical_modifier_qualifier")
    public String getClinicalModifierQualifier() {
        return clinicalModifierQualifier;
    }

    /**
     * Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
     * 
     */
    @JsonProperty("clinical_modifier_qualifier")
    public void setClinicalModifierQualifier(String clinicalModifierQualifier) {
        this.clinicalModifierQualifier = clinicalModifierQualifier;
    }

    /**
     * A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * (Required)
     * 
     */
    @JsonProperty("edge_label")
    public String getEdgeLabel() {
        return edgeLabel;
    }

    /**
     * A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * (Required)
     * 
     */
    @JsonProperty("edge_label")
    public void setEdgeLabel(String edgeLabel) {
        this.edgeLabel = edgeLabel;
    }

    /**
     * a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
     * 
     */
    @JsonProperty("frequency_qualifier")
    public String getFrequencyQualifier() {
        return frequencyQualifier;
    }

    /**
     * a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
     * 
     */
    @JsonProperty("frequency_qualifier")
    public void setFrequencyQualifier(String frequencyQualifier) {
        this.frequencyQualifier = frequencyQualifier;
    }

    /**
     * connects an association to a qualitative term denoting the level of confidence
     * 
     */
    @JsonProperty("has_confidence_level")
    public String getHasConfidenceLevel() {
        return hasConfidenceLevel;
    }

    /**
     * connects an association to a qualitative term denoting the level of confidence
     * 
     */
    @JsonProperty("has_confidence_level")
    public void setHasConfidenceLevel(String hasConfidenceLevel) {
        this.hasConfidenceLevel = hasConfidenceLevel;
    }

    /**
     * connects an association to an instance of supporting evidence
     * 
     */
    @JsonProperty("has_evidence")
    public String getHasEvidence() {
        return hasEvidence;
    }

    /**
     * connects an association to an instance of supporting evidence
     * 
     */
    @JsonProperty("has_evidence")
    public void setHasEvidence(String hasEvidence) {
        this.hasEvidence = hasEvidence;
    }

    /**
     * A unique identifier for an association
     * (Required)
     * 
     */
    @JsonProperty("id")
    public String getId() {
        return id;
    }

    /**
     * A unique identifier for an association
     * (Required)
     * 
     */
    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    /**
     * if set to true, then the association is negated i.e. is not true
     * 
     */
    @JsonProperty("negated")
    public String getNegated() {
        return negated;
    }

    /**
     * if set to true, then the association is negated i.e. is not true
     * 
     */
    @JsonProperty("negated")
    public void setNegated(String negated) {
        this.negated = negated;
    }

    /**
     * connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * (Required)
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * (Required)
     * 
     */
    @JsonProperty("object")
    public void setObject(String object) {
        this.object = object;
    }

    /**
     * a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
     * 
     */
    @JsonProperty("onset_qualifier")
    public String getOnsetQualifier() {
        return onsetQualifier;
    }

    /**
     * a qualifier used in a phenotypic association to state when the phenotype appears is in the subject
     * 
     */
    @JsonProperty("onset_qualifier")
    public void setOnsetQualifier(String onsetQualifier) {
        this.onsetQualifier = onsetQualifier;
    }

    /**
     * A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone.
     * 
     */
    @JsonProperty("p_value")
    public String getpValue() {
        return pValue;
    }

    /**
     * A quantitative confidence value that represents the probability of obtaining a result at least as extreme as that actually obtained, assuming that the actual value was the result of chance alone.
     * 
     */
    @JsonProperty("p_value")
    public void setpValue(String pValue) {
        this.pValue = pValue;
    }

    /**
     * connects an association to the agent (person, organization or group) that provided it
     * 
     */
    @JsonProperty("provided_by")
    public List<String> getProvidedBy() {
        return providedBy;
    }

    /**
     * connects an association to the agent (person, organization or group) that provided it
     * 
     */
    @JsonProperty("provided_by")
    public void setProvidedBy(List<String> providedBy) {
        this.providedBy = providedBy;
    }

    /**
     * connects an association to publications supporting the association
     * 
     */
    @JsonProperty("publications")
    public List<String> getPublications() {
        return publications;
    }

    /**
     * connects an association to publications supporting the association
     * 
     */
    @JsonProperty("publications")
    public void setPublications(List<String> publications) {
        this.publications = publications;
    }

    /**
     * connects an association to qualifiers that modify or qualify the meaning of that association
     * 
     */
    @JsonProperty("qualifiers")
    public List<String> getQualifiers() {
        return qualifiers;
    }

    /**
     * connects an association to qualifiers that modify or qualify the meaning of that association
     * 
     */
    @JsonProperty("qualifiers")
    public void setQualifiers(List<String> qualifiers) {
        this.qualifiers = qualifiers;
    }

    /**
     * A measurable quantity for the object of the association
     * 
     */
    @JsonProperty("quantifier_qualifier")
    public String getQuantifierQualifier() {
        return quantifierQualifier;
    }

    /**
     * A measurable quantity for the object of the association
     * 
     */
    @JsonProperty("quantifier_qualifier")
    public void setQuantifierQualifier(String quantifierQualifier) {
        this.quantifierQualifier = quantifierQualifier;
    }

    /**
     * the relationship type by which a subject is connected to an object in an association
     * (Required)
     * 
     */
    @JsonProperty("relation")
    public String getRelation() {
        return relation;
    }

    /**
     * the relationship type by which a subject is connected to an object in an association
     * (Required)
     * 
     */
    @JsonProperty("relation")
    public void setRelation(String relation) {
        this.relation = relation;
    }

    /**
     * a qualifier used in an association where the variant
     * 
     */
    @JsonProperty("sequence_variant_qualifier")
    public String getSequenceVariantQualifier() {
        return sequenceVariantQualifier;
    }

    /**
     * a qualifier used in an association where the variant
     * 
     */
    @JsonProperty("sequence_variant_qualifier")
    public void setSequenceVariantQualifier(String sequenceVariantQualifier) {
        this.sequenceVariantQualifier = sequenceVariantQualifier;
    }

    /**
     * a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
     * 
     */
    @JsonProperty("severity_qualifier")
    public String getSeverityQualifier() {
        return severityQualifier;
    }

    /**
     * a qualifier used in a phenotypic association to state how severe the phenotype is in the subject
     * 
     */
    @JsonProperty("severity_qualifier")
    public void setSeverityQualifier(String severityQualifier) {
        this.severityQualifier = severityQualifier;
    }

    /**
     * a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
     * 
     */
    @JsonProperty("sex_qualifier")
    public String getSexQualifier() {
        return sexQualifier;
    }

    /**
     * a qualifier used in a phenotypic association to state whether the association is specific to a particular sex.
     * 
     */
    @JsonProperty("sex_qualifier")
    public void setSexQualifier(String sexQualifier) {
        this.sexQualifier = sexQualifier;
    }

    /**
     * stage at which expression takes place
     * 
     */
    @JsonProperty("stage_qualifier")
    public String getStageQualifier() {
        return stageQualifier;
    }

    /**
     * stage at which expression takes place
     * 
     */
    @JsonProperty("stage_qualifier")
    public void setStageQualifier(String stageQualifier) {
        this.stageQualifier = stageQualifier;
    }

    /**
     * connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * (Required)
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * (Required)
     * 
     */
    @JsonProperty("subject")
    public void setSubject(String subject) {
        this.subject = subject;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(Association.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("associationSlot");
        sb.append('=');
        sb.append(((this.associationSlot == null)?"<null>":this.associationSlot));
        sb.append(',');
        sb.append("associationType");
        sb.append('=');
        sb.append(((this.associationType == null)?"<null>":this.associationType));
        sb.append(',');
        sb.append("changeIsCatalyzedBy");
        sb.append('=');
        sb.append(((this.changeIsCatalyzedBy == null)?"<null>":this.changeIsCatalyzedBy));
        sb.append(',');
        sb.append("chiSquaredStatistic");
        sb.append('=');
        sb.append(((this.chiSquaredStatistic == null)?"<null>":this.chiSquaredStatistic));
        sb.append(',');
        sb.append("clinicalModifierQualifier");
        sb.append('=');
        sb.append(((this.clinicalModifierQualifier == null)?"<null>":this.clinicalModifierQualifier));
        sb.append(',');
        sb.append("edgeLabel");
        sb.append('=');
        sb.append(((this.edgeLabel == null)?"<null>":this.edgeLabel));
        sb.append(',');
        sb.append("frequencyQualifier");
        sb.append('=');
        sb.append(((this.frequencyQualifier == null)?"<null>":this.frequencyQualifier));
        sb.append(',');
        sb.append("hasConfidenceLevel");
        sb.append('=');
        sb.append(((this.hasConfidenceLevel == null)?"<null>":this.hasConfidenceLevel));
        sb.append(',');
        sb.append("hasEvidence");
        sb.append('=');
        sb.append(((this.hasEvidence == null)?"<null>":this.hasEvidence));
        sb.append(',');
        sb.append("id");
        sb.append('=');
        sb.append(((this.id == null)?"<null>":this.id));
        sb.append(',');
        sb.append("negated");
        sb.append('=');
        sb.append(((this.negated == null)?"<null>":this.negated));
        sb.append(',');
        sb.append("object");
        sb.append('=');
        sb.append(((this.object == null)?"<null>":this.object));
        sb.append(',');
        sb.append("onsetQualifier");
        sb.append('=');
        sb.append(((this.onsetQualifier == null)?"<null>":this.onsetQualifier));
        sb.append(',');
        sb.append("pValue");
        sb.append('=');
        sb.append(((this.pValue == null)?"<null>":this.pValue));
        sb.append(',');
        sb.append("providedBy");
        sb.append('=');
        sb.append(((this.providedBy == null)?"<null>":this.providedBy));
        sb.append(',');
        sb.append("publications");
        sb.append('=');
        sb.append(((this.publications == null)?"<null>":this.publications));
        sb.append(',');
        sb.append("qualifiers");
        sb.append('=');
        sb.append(((this.qualifiers == null)?"<null>":this.qualifiers));
        sb.append(',');
        sb.append("quantifierQualifier");
        sb.append('=');
        sb.append(((this.quantifierQualifier == null)?"<null>":this.quantifierQualifier));
        sb.append(',');
        sb.append("relation");
        sb.append('=');
        sb.append(((this.relation == null)?"<null>":this.relation));
        sb.append(',');
        sb.append("sequenceVariantQualifier");
        sb.append('=');
        sb.append(((this.sequenceVariantQualifier == null)?"<null>":this.sequenceVariantQualifier));
        sb.append(',');
        sb.append("severityQualifier");
        sb.append('=');
        sb.append(((this.severityQualifier == null)?"<null>":this.severityQualifier));
        sb.append(',');
        sb.append("sexQualifier");
        sb.append('=');
        sb.append(((this.sexQualifier == null)?"<null>":this.sexQualifier));
        sb.append(',');
        sb.append("stageQualifier");
        sb.append('=');
        sb.append(((this.stageQualifier == null)?"<null>":this.stageQualifier));
        sb.append(',');
        sb.append("subject");
        sb.append('=');
        sb.append(((this.subject == null)?"<null>":this.subject));
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
        result = ((result* 31)+((this.negated == null)? 0 :this.negated.hashCode()));
        result = ((result* 31)+((this.sequenceVariantQualifier == null)? 0 :this.sequenceVariantQualifier.hashCode()));
        result = ((result* 31)+((this.subject == null)? 0 :this.subject.hashCode()));
        result = ((result* 31)+((this.chiSquaredStatistic == null)? 0 :this.chiSquaredStatistic.hashCode()));
        result = ((result* 31)+((this.relation == null)? 0 :this.relation.hashCode()));
        result = ((result* 31)+((this.onsetQualifier == null)? 0 :this.onsetQualifier.hashCode()));
        result = ((result* 31)+((this.stageQualifier == null)? 0 :this.stageQualifier.hashCode()));
        result = ((result* 31)+((this.id == null)? 0 :this.id.hashCode()));
        result = ((result* 31)+((this.providedBy == null)? 0 :this.providedBy.hashCode()));
        result = ((result* 31)+((this.sexQualifier == null)? 0 :this.sexQualifier.hashCode()));
        result = ((result* 31)+((this.associationSlot == null)? 0 :this.associationSlot.hashCode()));
        result = ((result* 31)+((this.clinicalModifierQualifier == null)? 0 :this.clinicalModifierQualifier.hashCode()));
        result = ((result* 31)+((this.associationType == null)? 0 :this.associationType.hashCode()));
        result = ((result* 31)+((this.frequencyQualifier == null)? 0 :this.frequencyQualifier.hashCode()));
        result = ((result* 31)+((this.pValue == null)? 0 :this.pValue.hashCode()));
        result = ((result* 31)+((this.qualifiers == null)? 0 :this.qualifiers.hashCode()));
        result = ((result* 31)+((this.severityQualifier == null)? 0 :this.severityQualifier.hashCode()));
        result = ((result* 31)+((this.hasConfidenceLevel == null)? 0 :this.hasConfidenceLevel.hashCode()));
        result = ((result* 31)+((this.quantifierQualifier == null)? 0 :this.quantifierQualifier.hashCode()));
        result = ((result* 31)+((this.changeIsCatalyzedBy == null)? 0 :this.changeIsCatalyzedBy.hashCode()));
        result = ((result* 31)+((this.hasEvidence == null)? 0 :this.hasEvidence.hashCode()));
        result = ((result* 31)+((this.edgeLabel == null)? 0 :this.edgeLabel.hashCode()));
        result = ((result* 31)+((this.object == null)? 0 :this.object.hashCode()));
        result = ((result* 31)+((this.publications == null)? 0 :this.publications.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof Association) == false) {
            return false;
        }
        Association rhs = ((Association) other);
        return (((((((((((((((((((((((((this.negated == rhs.negated)||((this.negated!= null)&&this.negated.equals(rhs.negated)))&&((this.sequenceVariantQualifier == rhs.sequenceVariantQualifier)||((this.sequenceVariantQualifier!= null)&&this.sequenceVariantQualifier.equals(rhs.sequenceVariantQualifier))))&&((this.subject == rhs.subject)||((this.subject!= null)&&this.subject.equals(rhs.subject))))&&((this.chiSquaredStatistic == rhs.chiSquaredStatistic)||((this.chiSquaredStatistic!= null)&&this.chiSquaredStatistic.equals(rhs.chiSquaredStatistic))))&&((this.relation == rhs.relation)||((this.relation!= null)&&this.relation.equals(rhs.relation))))&&((this.onsetQualifier == rhs.onsetQualifier)||((this.onsetQualifier!= null)&&this.onsetQualifier.equals(rhs.onsetQualifier))))&&((this.stageQualifier == rhs.stageQualifier)||((this.stageQualifier!= null)&&this.stageQualifier.equals(rhs.stageQualifier))))&&((this.id == rhs.id)||((this.id!= null)&&this.id.equals(rhs.id))))&&((this.providedBy == rhs.providedBy)||((this.providedBy!= null)&&this.providedBy.equals(rhs.providedBy))))&&((this.sexQualifier == rhs.sexQualifier)||((this.sexQualifier!= null)&&this.sexQualifier.equals(rhs.sexQualifier))))&&((this.associationSlot == rhs.associationSlot)||((this.associationSlot!= null)&&this.associationSlot.equals(rhs.associationSlot))))&&((this.clinicalModifierQualifier == rhs.clinicalModifierQualifier)||((this.clinicalModifierQualifier!= null)&&this.clinicalModifierQualifier.equals(rhs.clinicalModifierQualifier))))&&((this.associationType == rhs.associationType)||((this.associationType!= null)&&this.associationType.equals(rhs.associationType))))&&((this.frequencyQualifier == rhs.frequencyQualifier)||((this.frequencyQualifier!= null)&&this.frequencyQualifier.equals(rhs.frequencyQualifier))))&&((this.pValue == rhs.pValue)||((this.pValue!= null)&&this.pValue.equals(rhs.pValue))))&&((this.qualifiers == rhs.qualifiers)||((this.qualifiers!= null)&&this.qualifiers.equals(rhs.qualifiers))))&&((this.severityQualifier == rhs.severityQualifier)||((this.severityQualifier!= null)&&this.severityQualifier.equals(rhs.severityQualifier))))&&((this.hasConfidenceLevel == rhs.hasConfidenceLevel)||((this.hasConfidenceLevel!= null)&&this.hasConfidenceLevel.equals(rhs.hasConfidenceLevel))))&&((this.quantifierQualifier == rhs.quantifierQualifier)||((this.quantifierQualifier!= null)&&this.quantifierQualifier.equals(rhs.quantifierQualifier))))&&((this.changeIsCatalyzedBy == rhs.changeIsCatalyzedBy)||((this.changeIsCatalyzedBy!= null)&&this.changeIsCatalyzedBy.equals(rhs.changeIsCatalyzedBy))))&&((this.hasEvidence == rhs.hasEvidence)||((this.hasEvidence!= null)&&this.hasEvidence.equals(rhs.hasEvidence))))&&((this.edgeLabel == rhs.edgeLabel)||((this.edgeLabel!= null)&&this.edgeLabel.equals(rhs.edgeLabel))))&&((this.object == rhs.object)||((this.object!= null)&&this.object.equals(rhs.object))))&&((this.publications == rhs.publications)||((this.publications!= null)&&this.publications.equals(rhs.publications))));
    }

}
