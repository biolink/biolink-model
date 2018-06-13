import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * MolecularEntity
 * <p>
 * A gene, gene product, small molecule or macromolecule (including protein complex)
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "biomarker_for",
    "molecularly_interacts_with",
    "regulates_entity_to_entity"
})
public class MolecularEntity {

    /**
     * holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("biomarker_for")
    @JsonPropertyDescription("holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.")
    private String biomarkerFor;
    /**
     * holds between two entities that make physical contact as part of some interaction
     * 
     */
    @JsonProperty("molecularly_interacts_with")
    @JsonPropertyDescription("holds between two entities that make physical contact as part of some interaction")
    private String molecularlyInteractsWith;
    /**
     * describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
     * 
     */
    @JsonProperty("regulates_entity_to_entity")
    @JsonPropertyDescription("describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.")
    private String regulatesEntityToEntity;

    /**
     * holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("biomarker_for")
    public String getBiomarkerFor() {
        return biomarkerFor;
    }

    /**
     * holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("biomarker_for")
    public void setBiomarkerFor(String biomarkerFor) {
        this.biomarkerFor = biomarkerFor;
    }

    /**
     * holds between two entities that make physical contact as part of some interaction
     * 
     */
    @JsonProperty("molecularly_interacts_with")
    public String getMolecularlyInteractsWith() {
        return molecularlyInteractsWith;
    }

    /**
     * holds between two entities that make physical contact as part of some interaction
     * 
     */
    @JsonProperty("molecularly_interacts_with")
    public void setMolecularlyInteractsWith(String molecularlyInteractsWith) {
        this.molecularlyInteractsWith = molecularlyInteractsWith;
    }

    /**
     * describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
     * 
     */
    @JsonProperty("regulates_entity_to_entity")
    public String getRegulatesEntityToEntity() {
        return regulatesEntityToEntity;
    }

    /**
     * describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
     * 
     */
    @JsonProperty("regulates_entity_to_entity")
    public void setRegulatesEntityToEntity(String regulatesEntityToEntity) {
        this.regulatesEntityToEntity = regulatesEntityToEntity;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("biomarkerFor", biomarkerFor).append("molecularlyInteractsWith", molecularlyInteractsWith).append("regulatesEntityToEntity", regulatesEntityToEntity).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(molecularlyInteractsWith).append(biomarkerFor).append(regulatesEntityToEntity).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof MolecularEntity) == false) {
            return false;
        }
        MolecularEntity rhs = ((MolecularEntity) other);
        return new EqualsBuilder().append(molecularlyInteractsWith, rhs.molecularlyInteractsWith).append(biomarkerFor, rhs.biomarkerFor).append(regulatesEntityToEntity, rhs.regulatesEntityToEntity).isEquals();
    }

}
