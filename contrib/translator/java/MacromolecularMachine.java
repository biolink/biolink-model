import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * MacromolecularMachine
 * <p>
 * A union of gene, gene product, and macromolecular complex. These are the basic units of function in a cell. They either carry out individual biological activities, or they encode molecules which do this.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "name"
})
public class MacromolecularMachine {

    /**
     * genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * 
     */
    @JsonProperty("name")
    @JsonPropertyDescription("genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name")
    private String name;

    /**
     * genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * 
     */
    @JsonProperty("name")
    public String getName() {
        return name;
    }

    /**
     * genes are typically designated by a short symbol and a full name. We map the symbol to the default display name and use an additional slot for full name
     * 
     */
    @JsonProperty("name")
    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("name", name).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(name).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof MacromolecularMachine) == false) {
            return false;
        }
        MacromolecularMachine rhs = ((MacromolecularMachine) other);
        return new EqualsBuilder().append(name, rhs.name).isEquals();
    }

}
