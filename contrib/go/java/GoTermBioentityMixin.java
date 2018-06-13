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
 * GoTermBioentityMixin
 * <p>
 * mixes in GO properties to bio-entities
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "isa_partof_closure",
    "isa_partof_closure_label",
    "regulates_closure",
    "regulates_closure_label"
})
public class GoTermBioentityMixin {

    /**
     * Ancestors (reflexive) of the object field following is_a (subClassOf) and part-of links. This is typically used as a query constraint and for faceting. The combination of is_a and part of is a common pattern, and can be used in gene expression queries (finding genes that are expressed in a structure, a subtype, or a part of that structure) or in GO queries (in any of the three branches of GO)
     * 
     */
    @JsonProperty("isa_partof_closure")
    @JsonPropertyDescription("Ancestors (reflexive) of the object field following is_a (subClassOf) and part-of links. This is typically used as a query constraint and for faceting. The combination of is_a and part of is a common pattern, and can be used in gene expression queries (finding genes that are expressed in a structure, a subtype, or a part of that structure) or in GO queries (in any of the three branches of GO)")
    private List<String> isaPartofClosure = new ArrayList<String>();
    /**
     * parent field for fields used for storing the label of the closure concept. See also: closure concept field
     * 
     */
    @JsonProperty("isa_partof_closure_label")
    @JsonPropertyDescription("parent field for fields used for storing the label of the closure concept. See also: closure concept field")
    private List<String> isaPartofClosureLabel = new ArrayList<String>();
    /**
     * Ancestors (reflexive) of the object field following is_a (subClassOf), part-of and regulates (including positive and negative) relationships. This is typically used as a query constraint and for faceting where the range is a biological process
     * 
     */
    @JsonProperty("regulates_closure")
    @JsonPropertyDescription("Ancestors (reflexive) of the object field following is_a (subClassOf), part-of and regulates (including positive and negative) relationships. This is typically used as a query constraint and for faceting where the range is a biological process")
    private List<String> regulatesClosure = new ArrayList<String>();
    /**
     * parent field for fields used for storing the label of the closure concept. See also: closure concept field
     * 
     */
    @JsonProperty("regulates_closure_label")
    @JsonPropertyDescription("parent field for fields used for storing the label of the closure concept. See also: closure concept field")
    private List<String> regulatesClosureLabel = new ArrayList<String>();

    /**
     * Ancestors (reflexive) of the object field following is_a (subClassOf) and part-of links. This is typically used as a query constraint and for faceting. The combination of is_a and part of is a common pattern, and can be used in gene expression queries (finding genes that are expressed in a structure, a subtype, or a part of that structure) or in GO queries (in any of the three branches of GO)
     * 
     */
    @JsonProperty("isa_partof_closure")
    public List<String> getIsaPartofClosure() {
        return isaPartofClosure;
    }

    /**
     * Ancestors (reflexive) of the object field following is_a (subClassOf) and part-of links. This is typically used as a query constraint and for faceting. The combination of is_a and part of is a common pattern, and can be used in gene expression queries (finding genes that are expressed in a structure, a subtype, or a part of that structure) or in GO queries (in any of the three branches of GO)
     * 
     */
    @JsonProperty("isa_partof_closure")
    public void setIsaPartofClosure(List<String> isaPartofClosure) {
        this.isaPartofClosure = isaPartofClosure;
    }

    /**
     * parent field for fields used for storing the label of the closure concept. See also: closure concept field
     * 
     */
    @JsonProperty("isa_partof_closure_label")
    public List<String> getIsaPartofClosureLabel() {
        return isaPartofClosureLabel;
    }

    /**
     * parent field for fields used for storing the label of the closure concept. See also: closure concept field
     * 
     */
    @JsonProperty("isa_partof_closure_label")
    public void setIsaPartofClosureLabel(List<String> isaPartofClosureLabel) {
        this.isaPartofClosureLabel = isaPartofClosureLabel;
    }

    /**
     * Ancestors (reflexive) of the object field following is_a (subClassOf), part-of and regulates (including positive and negative) relationships. This is typically used as a query constraint and for faceting where the range is a biological process
     * 
     */
    @JsonProperty("regulates_closure")
    public List<String> getRegulatesClosure() {
        return regulatesClosure;
    }

    /**
     * Ancestors (reflexive) of the object field following is_a (subClassOf), part-of and regulates (including positive and negative) relationships. This is typically used as a query constraint and for faceting where the range is a biological process
     * 
     */
    @JsonProperty("regulates_closure")
    public void setRegulatesClosure(List<String> regulatesClosure) {
        this.regulatesClosure = regulatesClosure;
    }

    /**
     * parent field for fields used for storing the label of the closure concept. See also: closure concept field
     * 
     */
    @JsonProperty("regulates_closure_label")
    public List<String> getRegulatesClosureLabel() {
        return regulatesClosureLabel;
    }

    /**
     * parent field for fields used for storing the label of the closure concept. See also: closure concept field
     * 
     */
    @JsonProperty("regulates_closure_label")
    public void setRegulatesClosureLabel(List<String> regulatesClosureLabel) {
        this.regulatesClosureLabel = regulatesClosureLabel;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("isaPartofClosure", isaPartofClosure).append("isaPartofClosureLabel", isaPartofClosureLabel).append("regulatesClosure", regulatesClosure).append("regulatesClosureLabel", regulatesClosureLabel).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(regulatesClosureLabel).append(isaPartofClosureLabel).append(isaPartofClosure).append(regulatesClosure).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof GoTermBioentityMixin) == false) {
            return false;
        }
        GoTermBioentityMixin rhs = ((GoTermBioentityMixin) other);
        return new EqualsBuilder().append(regulatesClosureLabel, rhs.regulatesClosureLabel).append(isaPartofClosureLabel, rhs.isaPartofClosureLabel).append(isaPartofClosure, rhs.isaPartofClosure).append(regulatesClosure, rhs.regulatesClosure).isEquals();
    }

}
