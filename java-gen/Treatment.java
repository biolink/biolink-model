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
 * Treatment
 * <p>
 * A treatment is targeted at a disease or phenotype and may involve multiple drug 'exposures'
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "category",
    "has_exposure_parts",
    "id",
    "label",
    "treats"
})
public class Treatment {

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class
     * 
     */
    @JsonProperty("category")
    @JsonPropertyDescription("Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class")
    private String category;
    @JsonProperty("has_exposure_parts")
    private List<String> hasExposureParts = new ArrayList<String>();
    @JsonProperty("id")
    private String id;
    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    @JsonPropertyDescription("A human-readable name for a thing")
    private String label;
    @JsonProperty("treats")
    private String treats;

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

    @JsonProperty("has_exposure_parts")
    public List<String> getHasExposureParts() {
        return hasExposureParts;
    }

    @JsonProperty("has_exposure_parts")
    public void setHasExposureParts(List<String> hasExposureParts) {
        this.hasExposureParts = hasExposureParts;
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

    @JsonProperty("treats")
    public String getTreats() {
        return treats;
    }

    @JsonProperty("treats")
    public void setTreats(String treats) {
        this.treats = treats;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("category", category).append("hasExposureParts", hasExposureParts).append("id", id).append("label", label).append("treats", treats).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(hasExposureParts).append(treats).append(id).append(label).append(category).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof Treatment) == false) {
            return false;
        }
        Treatment rhs = ((Treatment) other);
        return new EqualsBuilder().append(hasExposureParts, rhs.hasExposureParts).append(treats, rhs.treats).append(id, rhs.id).append(label, rhs.label).append(category, rhs.category).isEquals();
    }

}
