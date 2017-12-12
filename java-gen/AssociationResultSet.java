import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * AssociationResultSet
 * <p>
 * null
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "associations"
})
public class AssociationResultSet {

    @JsonProperty("associations")
    private List<String> associations = new ArrayList<String>();

    @JsonProperty("associations")
    public List<String> getAssociations() {
        return associations;
    }

    @JsonProperty("associations")
    public void setAssociations(List<String> associations) {
        this.associations = associations;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("associations", associations).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(associations).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof AssociationResultSet) == false) {
            return false;
        }
        AssociationResultSet rhs = ((AssociationResultSet) other);
        return new EqualsBuilder().append(associations, rhs.associations).isEquals();
    }

}
