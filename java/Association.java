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
 * Association
 * <p>
 * A typed association between two entities, supported by evidence
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "association_slot",
    "association_type",
    "clinical_modifier_qualifier",
    "edge_label",
    "has_confidence_level",
    "has_evidence",
    "id",
    "negated",
    "object",
    "provided_by",
    "publications",
    "qualifiers",
    "relation",
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
     * Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects
     * 
     */
    @JsonProperty("clinical_modifier_qualifier")
    @JsonPropertyDescription("Used to characterize and specify the phenotypic abnormalities defined in the Phenotypic abnormality subontology, with respect to severity, laterality, age of onset, and other aspects")
    private String clinicalModifierQualifier;
    /**
     * A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * 
     */
    @JsonProperty("edge_label")
    @JsonPropertyDescription("A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.")
    private String edgeLabel;
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
     * connects an association to the agent (person, organization or group) that provided it
     * 
     */
    @JsonProperty("provided_by")
    @JsonPropertyDescription("connects an association to the agent (person, organization or group) that provided it")
    private String providedBy;
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
     * the relationship type by which a subject is connected to an object in an association
     * (Required)
     * 
     */
    @JsonProperty("relation")
    @JsonPropertyDescription("the relationship type by which a subject is connected to an object in an association")
    private String relation;
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
     * 
     */
    @JsonProperty("edge_label")
    public String getEdgeLabel() {
        return edgeLabel;
    }

    /**
     * A high-level grouping for the relationship type. AKA minimal predicate. This is analogous to category for nodes.
     * 
     */
    @JsonProperty("edge_label")
    public void setEdgeLabel(String edgeLabel) {
        this.edgeLabel = edgeLabel;
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
     * connects an association to the agent (person, organization or group) that provided it
     * 
     */
    @JsonProperty("provided_by")
    public String getProvidedBy() {
        return providedBy;
    }

    /**
     * connects an association to the agent (person, organization or group) that provided it
     * 
     */
    @JsonProperty("provided_by")
    public void setProvidedBy(String providedBy) {
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
        return new ToStringBuilder(this).append("associationSlot", associationSlot).append("associationType", associationType).append("clinicalModifierQualifier", clinicalModifierQualifier).append("edgeLabel", edgeLabel).append("hasConfidenceLevel", hasConfidenceLevel).append("hasEvidence", hasEvidence).append("id", id).append("negated", negated).append("object", object).append("providedBy", providedBy).append("publications", publications).append("qualifiers", qualifiers).append("relation", relation).append("subject", subject).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(providedBy).append(negated).append(associationSlot).append(clinicalModifierQualifier).append(subject).append(associationType).append(qualifiers).append(relation).append(hasConfidenceLevel).append(hasEvidence).append(edgeLabel).append(id).append(object).append(publications).toHashCode();
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
        return new EqualsBuilder().append(providedBy, rhs.providedBy).append(negated, rhs.negated).append(associationSlot, rhs.associationSlot).append(clinicalModifierQualifier, rhs.clinicalModifierQualifier).append(subject, rhs.subject).append(associationType, rhs.associationType).append(qualifiers, rhs.qualifiers).append(relation, rhs.relation).append(hasConfidenceLevel, rhs.hasConfidenceLevel).append(hasEvidence, rhs.hasEvidence).append(edgeLabel, rhs.edgeLabel).append(id, rhs.id).append(object, rhs.object).append(publications, rhs.publications).isEquals();
    }

}
