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
 * GenomicSequenceLocalization
 * <p>
 * A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "association_type",
    "end_interbase_coordinate",
    "genome_build",
    "has_evidence",
    "has_evidence_graph",
    "has_evidence_type",
    "id",
    "label",
    "negated",
    "object",
    "object_extensions",
    "phase",
    "provided_by",
    "publications",
    "qualifiers",
    "relation",
    "start_interbase_coordinate",
    "subject",
    "subject_extensions"
})
public class GenomicSequenceLocalization {

    /**
     * connects an association to the type of association (e.g. gene to phenotype)
     * 
     */
    @JsonProperty("association_type")
    @JsonPropertyDescription("connects an association to the type of association (e.g. gene to phenotype)")
    private String associationType;
    @JsonProperty("end_interbase_coordinate")
    private String endInterbaseCoordinate;
    /**
     * TODO
     * 
     */
    @JsonProperty("genome_build")
    @JsonPropertyDescription("TODO")
    private String genomeBuild;
    /**
     * connects an association to an instance of supporting evidence
     * 
     */
    @JsonProperty("has_evidence")
    @JsonPropertyDescription("connects an association to an instance of supporting evidence")
    private String hasEvidence;
    /**
     * connects an association to a graph object including a path from subject to object
     * 
     */
    @JsonProperty("has_evidence_graph")
    @JsonPropertyDescription("connects an association to a graph object including a path from subject to object")
    private String hasEvidenceGraph;
    /**
     * connects an association to the class of evidence used
     * 
     */
    @JsonProperty("has_evidence_type")
    @JsonPropertyDescription("connects an association to the class of evidence used")
    private String hasEvidenceType;
    @JsonProperty("id")
    private String id;
    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    @JsonPropertyDescription("A human-readable name for a thing")
    private String label;
    /**
     * if set to true, then the association is negated i.e. is not true
     * 
     */
    @JsonProperty("negated")
    @JsonPropertyDescription("if set to true, then the association is negated i.e. is not true")
    private String negated;
    /**
     * connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * 
     */
    @JsonProperty("object")
    @JsonPropertyDescription("connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.")
    private String object;
    /**
     * Additional relationships that are true of the object in the context of the association. For example, if the object is an anatomical term in an expression association, the object extensions may include part-of links
     * 
     */
    @JsonProperty("object_extensions")
    @JsonPropertyDescription("Additional relationships that are true of the object in the context of the association. For example, if the object is an anatomical term in an expression association, the object extensions may include part-of links")
    private List<String> objectExtensions = new ArrayList<String>();
    /**
     * TODO
     * 
     */
    @JsonProperty("phase")
    @JsonPropertyDescription("TODO")
    private String phase;
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
     * 
     */
    @JsonProperty("relation")
    @JsonPropertyDescription("the relationship type by which a subject is connected to an object in an association")
    private String relation;
    @JsonProperty("start_interbase_coordinate")
    private String startInterbaseCoordinate;
    /**
     * connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * 
     */
    @JsonProperty("subject")
    @JsonPropertyDescription("connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.")
    private String subject;
    /**
     * Additional relationships that are true of the subject in the context of the association. For example, if the subject is a gene product in a functional association, the subject extensions may represent  an isoform or a specific post-translational state
     * 
     */
    @JsonProperty("subject_extensions")
    @JsonPropertyDescription("Additional relationships that are true of the subject in the context of the association. For example, if the subject is a gene product in a functional association, the subject extensions may represent  an isoform or a specific post-translational state")
    private List<String> subjectExtensions = new ArrayList<String>();

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

    @JsonProperty("end_interbase_coordinate")
    public String getEndInterbaseCoordinate() {
        return endInterbaseCoordinate;
    }

    @JsonProperty("end_interbase_coordinate")
    public void setEndInterbaseCoordinate(String endInterbaseCoordinate) {
        this.endInterbaseCoordinate = endInterbaseCoordinate;
    }

    /**
     * TODO
     * 
     */
    @JsonProperty("genome_build")
    public String getGenomeBuild() {
        return genomeBuild;
    }

    /**
     * TODO
     * 
     */
    @JsonProperty("genome_build")
    public void setGenomeBuild(String genomeBuild) {
        this.genomeBuild = genomeBuild;
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
     * connects an association to a graph object including a path from subject to object
     * 
     */
    @JsonProperty("has_evidence_graph")
    public String getHasEvidenceGraph() {
        return hasEvidenceGraph;
    }

    /**
     * connects an association to a graph object including a path from subject to object
     * 
     */
    @JsonProperty("has_evidence_graph")
    public void setHasEvidenceGraph(String hasEvidenceGraph) {
        this.hasEvidenceGraph = hasEvidenceGraph;
    }

    /**
     * connects an association to the class of evidence used
     * 
     */
    @JsonProperty("has_evidence_type")
    public String getHasEvidenceType() {
        return hasEvidenceType;
    }

    /**
     * connects an association to the class of evidence used
     * 
     */
    @JsonProperty("has_evidence_type")
    public void setHasEvidenceType(String hasEvidenceType) {
        this.hasEvidenceType = hasEvidenceType;
    }

    @JsonProperty("id")
    public String getId() {
        return id;
    }

    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    public String getLabel() {
        return label;
    }

    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    public void setLabel(String label) {
        this.label = label;
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
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * 
     */
    @JsonProperty("object")
    public void setObject(String object) {
        this.object = object;
    }

    /**
     * Additional relationships that are true of the object in the context of the association. For example, if the object is an anatomical term in an expression association, the object extensions may include part-of links
     * 
     */
    @JsonProperty("object_extensions")
    public List<String> getObjectExtensions() {
        return objectExtensions;
    }

    /**
     * Additional relationships that are true of the object in the context of the association. For example, if the object is an anatomical term in an expression association, the object extensions may include part-of links
     * 
     */
    @JsonProperty("object_extensions")
    public void setObjectExtensions(List<String> objectExtensions) {
        this.objectExtensions = objectExtensions;
    }

    /**
     * TODO
     * 
     */
    @JsonProperty("phase")
    public String getPhase() {
        return phase;
    }

    /**
     * TODO
     * 
     */
    @JsonProperty("phase")
    public void setPhase(String phase) {
        this.phase = phase;
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
     * 
     */
    @JsonProperty("relation")
    public String getRelation() {
        return relation;
    }

    /**
     * the relationship type by which a subject is connected to an object in an association
     * 
     */
    @JsonProperty("relation")
    public void setRelation(String relation) {
        this.relation = relation;
    }

    @JsonProperty("start_interbase_coordinate")
    public String getStartInterbaseCoordinate() {
        return startInterbaseCoordinate;
    }

    @JsonProperty("start_interbase_coordinate")
    public void setStartInterbaseCoordinate(String startInterbaseCoordinate) {
        this.startInterbaseCoordinate = startInterbaseCoordinate;
    }

    /**
     * connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * 
     */
    @JsonProperty("subject")
    public void setSubject(String subject) {
        this.subject = subject;
    }

    /**
     * Additional relationships that are true of the subject in the context of the association. For example, if the subject is a gene product in a functional association, the subject extensions may represent  an isoform or a specific post-translational state
     * 
     */
    @JsonProperty("subject_extensions")
    public List<String> getSubjectExtensions() {
        return subjectExtensions;
    }

    /**
     * Additional relationships that are true of the subject in the context of the association. For example, if the subject is a gene product in a functional association, the subject extensions may represent  an isoform or a specific post-translational state
     * 
     */
    @JsonProperty("subject_extensions")
    public void setSubjectExtensions(List<String> subjectExtensions) {
        this.subjectExtensions = subjectExtensions;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("associationType", associationType).append("endInterbaseCoordinate", endInterbaseCoordinate).append("genomeBuild", genomeBuild).append("hasEvidence", hasEvidence).append("hasEvidenceGraph", hasEvidenceGraph).append("hasEvidenceType", hasEvidenceType).append("id", id).append("label", label).append("negated", negated).append("object", object).append("objectExtensions", objectExtensions).append("phase", phase).append("providedBy", providedBy).append("publications", publications).append("qualifiers", qualifiers).append("relation", relation).append("startInterbaseCoordinate", startInterbaseCoordinate).append("subject", subject).append("subjectExtensions", subjectExtensions).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(phase).append(providedBy).append(negated).append(objectExtensions).append(hasEvidenceGraph).append(subject).append(associationType).append(qualifiers).append(label).append(subjectExtensions).append(relation).append(startInterbaseCoordinate).append(hasEvidenceType).append(genomeBuild).append(hasEvidence).append(id).append(endInterbaseCoordinate).append(object).append(publications).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof GenomicSequenceLocalization) == false) {
            return false;
        }
        GenomicSequenceLocalization rhs = ((GenomicSequenceLocalization) other);
        return new EqualsBuilder().append(phase, rhs.phase).append(providedBy, rhs.providedBy).append(negated, rhs.negated).append(objectExtensions, rhs.objectExtensions).append(hasEvidenceGraph, rhs.hasEvidenceGraph).append(subject, rhs.subject).append(associationType, rhs.associationType).append(qualifiers, rhs.qualifiers).append(label, rhs.label).append(subjectExtensions, rhs.subjectExtensions).append(relation, rhs.relation).append(startInterbaseCoordinate, rhs.startInterbaseCoordinate).append(hasEvidenceType, rhs.hasEvidenceType).append(genomeBuild, rhs.genomeBuild).append(hasEvidence, rhs.hasEvidence).append(id, rhs.id).append(endInterbaseCoordinate, rhs.endInterbaseCoordinate).append(object, rhs.object).append(publications, rhs.publications).isEquals();
    }

}
