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
 * BioentityWithGoTerms
 * <p>
 * this serves as exemplar for the time being, corresponding to the bioentity document type in amigo, which has a single entry per bioentity, with associated GO information
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "full_name",
    "id",
    "in_taxon",
    "isa_partof_closure",
    "label",
    "regulates_closure",
    "systematic_synonym"
})
public class BioentityWithGoTerms {

    /**
     * a long-form human readable name for a thing
     * 
     */
    @JsonProperty("full_name")
    @JsonPropertyDescription("a long-form human readable name for a thing")
    private String fullName;
    @JsonProperty("id")
    private String id;
    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    @JsonPropertyDescription("connects a thing to a class representing a taxon")
    private String inTaxon;
    /**
     * Ancestors (reflexive) of the object field following is_a (subClassOf) and part-of links. This is typically used as a query constraint and for faceting. The combination of is_a and part of is a common pattern, and can be used in gene expression queries (finding genes that are expressed in a structure, a subtype, or a part of that structure) or in GO queries (in any of the three branches of GO)
     * 
     */
    @JsonProperty("isa_partof_closure")
    @JsonPropertyDescription("Ancestors (reflexive) of the object field following is_a (subClassOf) and part-of links. This is typically used as a query constraint and for faceting. The combination of is_a and part of is a common pattern, and can be used in gene expression queries (finding genes that are expressed in a structure, a subtype, or a part of that structure) or in GO queries (in any of the three branches of GO)")
    private List<String> isaPartofClosure = new ArrayList<String>();
    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("label")
    @JsonPropertyDescription("A human-readable name for a thing")
    private String label;
    /**
     * Ancestors (reflexive) of the object field following is_a (subClassOf), part-of and regulates (including positive and negative) relationships. This is typically used as a query constraint and for faceting where the range is a biological process
     * 
     */
    @JsonProperty("regulates_closure")
    @JsonPropertyDescription("Ancestors (reflexive) of the object field following is_a (subClassOf), part-of and regulates (including positive and negative) relationships. This is typically used as a query constraint and for faceting where the range is a biological process")
    private List<String> regulatesClosure = new ArrayList<String>();
    /**
     * more commonly used for gene symbols in yeast
     * 
     */
    @JsonProperty("systematic_synonym")
    @JsonPropertyDescription("more commonly used for gene symbols in yeast")
    private String systematicSynonym;

    /**
     * a long-form human readable name for a thing
     * 
     */
    @JsonProperty("full_name")
    public String getFullName() {
        return fullName;
    }

    /**
     * a long-form human readable name for a thing
     * 
     */
    @JsonProperty("full_name")
    public void setFullName(String fullName) {
        this.fullName = fullName;
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
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    public String getInTaxon() {
        return inTaxon;
    }

    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    public void setInTaxon(String inTaxon) {
        this.inTaxon = inTaxon;
    }

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
     * more commonly used for gene symbols in yeast
     * 
     */
    @JsonProperty("systematic_synonym")
    public String getSystematicSynonym() {
        return systematicSynonym;
    }

    /**
     * more commonly used for gene symbols in yeast
     * 
     */
    @JsonProperty("systematic_synonym")
    public void setSystematicSynonym(String systematicSynonym) {
        this.systematicSynonym = systematicSynonym;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("fullName", fullName).append("id", id).append("inTaxon", inTaxon).append("isaPartofClosure", isaPartofClosure).append("label", label).append("regulatesClosure", regulatesClosure).append("systematicSynonym", systematicSynonym).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(systematicSynonym).append(inTaxon).append(regulatesClosure).append(fullName).append(id).append(isaPartofClosure).append(label).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof BioentityWithGoTerms) == false) {
            return false;
        }
        BioentityWithGoTerms rhs = ((BioentityWithGoTerms) other);
        return new EqualsBuilder().append(systematicSynonym, rhs.systematicSynonym).append(inTaxon, rhs.inTaxon).append(regulatesClosure, rhs.regulatesClosure).append(fullName, rhs.fullName).append(id, rhs.id).append(isaPartofClosure, rhs.isaPartofClosure).append(label, rhs.label).isEquals();
    }

}
