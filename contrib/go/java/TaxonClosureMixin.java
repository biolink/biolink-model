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
 * TaxonClosureMixin
 * <p>
 * An association that includes flattened inlined objects, such as subject_taxon_closure
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "object_taxon",
    "object_taxon_closure",
    "object_taxon_closure_label",
    "object_taxon_label",
    "subject_taxon",
    "subject_taxon_closure",
    "subject_taxon_closure_label",
    "subject_taxon_label"
})
public class TaxonClosureMixin {

    /**
     * the taxonomic class of the entity in the object slot
     * 
     */
    @JsonProperty("object_taxon")
    @JsonPropertyDescription("the taxonomic class of the entity in the object slot")
    private String objectTaxon;
    /**
     * The taxon class or ancestor class for the object
     * 
     */
    @JsonProperty("object_taxon_closure")
    @JsonPropertyDescription("The taxon class or ancestor class for the object")
    private List<String> objectTaxonClosure = new ArrayList<String>();
    /**
     * The label for the taxon class or ancestor class for the object
     * 
     */
    @JsonProperty("object_taxon_closure_label")
    @JsonPropertyDescription("The label for the taxon class or ancestor class for the object")
    private List<String> objectTaxonClosureLabel = new ArrayList<String>();
    @JsonProperty("object_taxon_label")
    private String objectTaxonLabel;
    /**
     * the taxonomic class of the entity in the object slot
     * 
     */
    @JsonProperty("subject_taxon")
    @JsonPropertyDescription("the taxonomic class of the entity in the object slot")
    private String subjectTaxon;
    /**
     * The taxon class or ancestor class for the subject
     * 
     */
    @JsonProperty("subject_taxon_closure")
    @JsonPropertyDescription("The taxon class or ancestor class for the subject")
    private List<String> subjectTaxonClosure = new ArrayList<String>();
    /**
     * The label for the taxon class or ancestor class for the subject
     * 
     */
    @JsonProperty("subject_taxon_closure_label")
    @JsonPropertyDescription("The label for the taxon class or ancestor class for the subject")
    private List<String> subjectTaxonClosureLabel = new ArrayList<String>();
    @JsonProperty("subject_taxon_label")
    private String subjectTaxonLabel;

    /**
     * the taxonomic class of the entity in the object slot
     * 
     */
    @JsonProperty("object_taxon")
    public String getObjectTaxon() {
        return objectTaxon;
    }

    /**
     * the taxonomic class of the entity in the object slot
     * 
     */
    @JsonProperty("object_taxon")
    public void setObjectTaxon(String objectTaxon) {
        this.objectTaxon = objectTaxon;
    }

    /**
     * The taxon class or ancestor class for the object
     * 
     */
    @JsonProperty("object_taxon_closure")
    public List<String> getObjectTaxonClosure() {
        return objectTaxonClosure;
    }

    /**
     * The taxon class or ancestor class for the object
     * 
     */
    @JsonProperty("object_taxon_closure")
    public void setObjectTaxonClosure(List<String> objectTaxonClosure) {
        this.objectTaxonClosure = objectTaxonClosure;
    }

    /**
     * The label for the taxon class or ancestor class for the object
     * 
     */
    @JsonProperty("object_taxon_closure_label")
    public List<String> getObjectTaxonClosureLabel() {
        return objectTaxonClosureLabel;
    }

    /**
     * The label for the taxon class or ancestor class for the object
     * 
     */
    @JsonProperty("object_taxon_closure_label")
    public void setObjectTaxonClosureLabel(List<String> objectTaxonClosureLabel) {
        this.objectTaxonClosureLabel = objectTaxonClosureLabel;
    }

    @JsonProperty("object_taxon_label")
    public String getObjectTaxonLabel() {
        return objectTaxonLabel;
    }

    @JsonProperty("object_taxon_label")
    public void setObjectTaxonLabel(String objectTaxonLabel) {
        this.objectTaxonLabel = objectTaxonLabel;
    }

    /**
     * the taxonomic class of the entity in the object slot
     * 
     */
    @JsonProperty("subject_taxon")
    public String getSubjectTaxon() {
        return subjectTaxon;
    }

    /**
     * the taxonomic class of the entity in the object slot
     * 
     */
    @JsonProperty("subject_taxon")
    public void setSubjectTaxon(String subjectTaxon) {
        this.subjectTaxon = subjectTaxon;
    }

    /**
     * The taxon class or ancestor class for the subject
     * 
     */
    @JsonProperty("subject_taxon_closure")
    public List<String> getSubjectTaxonClosure() {
        return subjectTaxonClosure;
    }

    /**
     * The taxon class or ancestor class for the subject
     * 
     */
    @JsonProperty("subject_taxon_closure")
    public void setSubjectTaxonClosure(List<String> subjectTaxonClosure) {
        this.subjectTaxonClosure = subjectTaxonClosure;
    }

    /**
     * The label for the taxon class or ancestor class for the subject
     * 
     */
    @JsonProperty("subject_taxon_closure_label")
    public List<String> getSubjectTaxonClosureLabel() {
        return subjectTaxonClosureLabel;
    }

    /**
     * The label for the taxon class or ancestor class for the subject
     * 
     */
    @JsonProperty("subject_taxon_closure_label")
    public void setSubjectTaxonClosureLabel(List<String> subjectTaxonClosureLabel) {
        this.subjectTaxonClosureLabel = subjectTaxonClosureLabel;
    }

    @JsonProperty("subject_taxon_label")
    public String getSubjectTaxonLabel() {
        return subjectTaxonLabel;
    }

    @JsonProperty("subject_taxon_label")
    public void setSubjectTaxonLabel(String subjectTaxonLabel) {
        this.subjectTaxonLabel = subjectTaxonLabel;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("objectTaxon", objectTaxon).append("objectTaxonClosure", objectTaxonClosure).append("objectTaxonClosureLabel", objectTaxonClosureLabel).append("objectTaxonLabel", objectTaxonLabel).append("subjectTaxon", subjectTaxon).append("subjectTaxonClosure", subjectTaxonClosure).append("subjectTaxonClosureLabel", subjectTaxonClosureLabel).append("subjectTaxonLabel", subjectTaxonLabel).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(subjectTaxonClosureLabel).append(objectTaxon).append(subjectTaxonLabel).append(objectTaxonLabel).append(subjectTaxon).append(objectTaxonClosureLabel).append(objectTaxonClosure).append(subjectTaxonClosure).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof TaxonClosureMixin) == false) {
            return false;
        }
        TaxonClosureMixin rhs = ((TaxonClosureMixin) other);
        return new EqualsBuilder().append(subjectTaxonClosureLabel, rhs.subjectTaxonClosureLabel).append(objectTaxon, rhs.objectTaxon).append(subjectTaxonLabel, rhs.subjectTaxonLabel).append(objectTaxonLabel, rhs.objectTaxonLabel).append(subjectTaxon, rhs.subjectTaxon).append(objectTaxonClosureLabel, rhs.objectTaxonClosureLabel).append(objectTaxonClosure, rhs.objectTaxonClosure).append(subjectTaxonClosure, rhs.subjectTaxonClosure).isEquals();
    }

}
