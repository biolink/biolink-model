import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * MolecularEvent
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "downstream_causal_relationship",
    "enabled_by",
    "occurs_in",
    "part_of",
    "upstream_causal_relationship"
})
public class MolecularEvent {

    @JsonProperty("downstream_causal_relationship")
    private String downstreamCausalRelationship;
    @JsonProperty("enabled_by")
    private String enabledBy;
    /**
     * holds between a process and a material entity or site within which the process occurs
     * 
     */
    @JsonProperty("occurs_in")
    @JsonPropertyDescription("holds between a process and a material entity or site within which the process occurs")
    private String occursIn;
    /**
     * holds between parts and wholes (material entities or processes)
     * 
     */
    @JsonProperty("part_of")
    @JsonPropertyDescription("holds between parts and wholes (material entities or processes)")
    private String partOf;
    @JsonProperty("upstream_causal_relationship")
    private String upstreamCausalRelationship;

    @JsonProperty("downstream_causal_relationship")
    public String getDownstreamCausalRelationship() {
        return downstreamCausalRelationship;
    }

    @JsonProperty("downstream_causal_relationship")
    public void setDownstreamCausalRelationship(String downstreamCausalRelationship) {
        this.downstreamCausalRelationship = downstreamCausalRelationship;
    }

    @JsonProperty("enabled_by")
    public String getEnabledBy() {
        return enabledBy;
    }

    @JsonProperty("enabled_by")
    public void setEnabledBy(String enabledBy) {
        this.enabledBy = enabledBy;
    }

    /**
     * holds between a process and a material entity or site within which the process occurs
     * 
     */
    @JsonProperty("occurs_in")
    public String getOccursIn() {
        return occursIn;
    }

    /**
     * holds between a process and a material entity or site within which the process occurs
     * 
     */
    @JsonProperty("occurs_in")
    public void setOccursIn(String occursIn) {
        this.occursIn = occursIn;
    }

    /**
     * holds between parts and wholes (material entities or processes)
     * 
     */
    @JsonProperty("part_of")
    public String getPartOf() {
        return partOf;
    }

    /**
     * holds between parts and wholes (material entities or processes)
     * 
     */
    @JsonProperty("part_of")
    public void setPartOf(String partOf) {
        this.partOf = partOf;
    }

    @JsonProperty("upstream_causal_relationship")
    public String getUpstreamCausalRelationship() {
        return upstreamCausalRelationship;
    }

    @JsonProperty("upstream_causal_relationship")
    public void setUpstreamCausalRelationship(String upstreamCausalRelationship) {
        this.upstreamCausalRelationship = upstreamCausalRelationship;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("downstreamCausalRelationship", downstreamCausalRelationship).append("enabledBy", enabledBy).append("occursIn", occursIn).append("partOf", partOf).append("upstreamCausalRelationship", upstreamCausalRelationship).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(enabledBy).append(partOf).append(upstreamCausalRelationship).append(downstreamCausalRelationship).append(occursIn).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof MolecularEvent) == false) {
            return false;
        }
        MolecularEvent rhs = ((MolecularEvent) other);
        return new EqualsBuilder().append(enabledBy, rhs.enabledBy).append(partOf, rhs.partOf).append(upstreamCausalRelationship, rhs.upstreamCausalRelationship).append(downstreamCausalRelationship, rhs.downstreamCausalRelationship).append(occursIn, rhs.occursIn).isEquals();
    }

}
