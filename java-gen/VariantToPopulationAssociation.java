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
 * VariantToPopulationAssociation
 * <p>
 * An association between a variant and a population, where the variant has particular frequency in the population
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "association_type",
    "category",
    "frequency_qualifier",
    "has_count",
    "has_percentage",
    "has_quotient",
    "has_total",
    "id",
    "label",
    "negated",
    "object",
    "provided_by",
    "publications",
    "qualifiers",
    "relation",
    "subject"
})
public class VariantToPopulationAssociation {

    /**
     * connects an association to the type of association (e.g. gene to phenotype)
     * 
     */
    @JsonProperty("association_type")
    @JsonPropertyDescription("connects an association to the type of association (e.g. gene to phenotype)")
    private String associationType;
    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class
     * 
     */
    @JsonProperty("category")
    @JsonPropertyDescription("Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class")
    private String category;
    /**
     * a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject
     * 
     */
    @JsonProperty("frequency_qualifier")
    @JsonPropertyDescription("a qualifier used in a phenotypic association to state how frequent the phenotype is observed in the subject")
    private String frequencyQualifier;
    /**
     * number of things with a particular property
     * 
     */
    @JsonProperty("has_count")
    @JsonPropertyDescription("number of things with a particular property")
    private String hasCount;
    /**
     * equivalent to has quotient multiplied by 100
     * 
     */
    @JsonProperty("has_percentage")
    @JsonPropertyDescription("equivalent to has quotient multiplied by 100")
    private String hasPercentage;
    @JsonProperty("has_quotient")
    private String hasQuotient;
    /**
     * total number of things in a particular reference set
     * 
     */
    @JsonProperty("has_total")
    @JsonPropertyDescription("total number of things in a particular reference set")
    private String hasTotal;
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
    /**
     * connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * 
     */
    @JsonProperty("subject")
    @JsonPropertyDescription("connects an association to the subject of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.")
    private String subject;

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
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class
     * 
     */
    @JsonProperty("category")
    public String getCategory() {
        return category;
    }

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class
     * 
     */
    @JsonProperty("category")
    public void setCategory(String category) {
        this.category = category;
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
     * number of things with a particular property
     * 
     */
    @JsonProperty("has_count")
    public String getHasCount() {
        return hasCount;
    }

    /**
     * number of things with a particular property
     * 
     */
    @JsonProperty("has_count")
    public void setHasCount(String hasCount) {
        this.hasCount = hasCount;
    }

    /**
     * equivalent to has quotient multiplied by 100
     * 
     */
    @JsonProperty("has_percentage")
    public String getHasPercentage() {
        return hasPercentage;
    }

    /**
     * equivalent to has quotient multiplied by 100
     * 
     */
    @JsonProperty("has_percentage")
    public void setHasPercentage(String hasPercentage) {
        this.hasPercentage = hasPercentage;
    }

    @JsonProperty("has_quotient")
    public String getHasQuotient() {
        return hasQuotient;
    }

    @JsonProperty("has_quotient")
    public void setHasQuotient(String hasQuotient) {
        this.hasQuotient = hasQuotient;
    }

    /**
     * total number of things in a particular reference set
     * 
     */
    @JsonProperty("has_total")
    public String getHasTotal() {
        return hasTotal;
    }

    /**
     * total number of things in a particular reference set
     * 
     */
    @JsonProperty("has_total")
    public void setHasTotal(String hasTotal) {
        this.hasTotal = hasTotal;
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

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("associationType", associationType).append("category", category).append("frequencyQualifier", frequencyQualifier).append("hasCount", hasCount).append("hasPercentage", hasPercentage).append("hasQuotient", hasQuotient).append("hasTotal", hasTotal).append("id", id).append("label", label).append("negated", negated).append("object", object).append("providedBy", providedBy).append("publications", publications).append("qualifiers", qualifiers).append("relation", relation).append("subject", subject).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(providedBy).append(negated).append(subject).append(associationType).append(frequencyQualifier).append(qualifiers).append(label).append(hasCount).append(hasTotal).append(relation).append(hasPercentage).append(hasQuotient).append(id).append(category).append(object).append(publications).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof VariantToPopulationAssociation) == false) {
            return false;
        }
        VariantToPopulationAssociation rhs = ((VariantToPopulationAssociation) other);
        return new EqualsBuilder().append(providedBy, rhs.providedBy).append(negated, rhs.negated).append(subject, rhs.subject).append(associationType, rhs.associationType).append(frequencyQualifier, rhs.frequencyQualifier).append(qualifiers, rhs.qualifiers).append(label, rhs.label).append(hasCount, rhs.hasCount).append(hasTotal, rhs.hasTotal).append(relation, rhs.relation).append(hasPercentage, rhs.hasPercentage).append(hasQuotient, rhs.hasQuotient).append(id, rhs.id).append(category, rhs.category).append(object, rhs.object).append(publications, rhs.publications).isEquals();
    }

}
