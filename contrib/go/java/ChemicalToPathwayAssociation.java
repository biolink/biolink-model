import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * ChemicalToPathwayAssociation
 * <p>
 * An interaction between a chemical entity and a biological process or pathway
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "object"
})
public class ChemicalToPathwayAssociation {

    /**
     * connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.
     * 
     */
    @JsonProperty("object")
    @JsonPropertyDescription("connects an association to the object of the association. For example, in a gene-to-phenotype association, the gene is subject and phenotype is object.")
    private String object;

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

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("object", object).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(object).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof ChemicalToPathwayAssociation) == false) {
            return false;
        }
        ChemicalToPathwayAssociation rhs = ((ChemicalToPathwayAssociation) other);
        return new EqualsBuilder().append(object, rhs.object).isEquals();
    }

}
