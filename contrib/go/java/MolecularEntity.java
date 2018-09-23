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
    "affects_abundance_of",
    "affects_activity_of",
    "affects_degradation_of",
    "affects_expression_of",
    "affects_folding_of",
    "affects_localization_of",
    "affects_metabolic_processing_of",
    "affects_molecular_modification_of",
    "affects_mutation_rate_of",
    "affects_response_to",
    "affects_secretion_of",
    "affects_splicing_of",
    "affects_stability_of",
    "affects_synthesis_of",
    "affects_transport_of",
    "affects_uptake_of",
    "biomarker_for",
    "decreases_abundance_of",
    "decreases_activity_of",
    "decreases_degradation_of",
    "decreases_expression_of",
    "decreases_folding_of",
    "decreases_localization_of",
    "decreases_metabolic_processing_of",
    "decreases_molecular_modification_of",
    "decreases_mutation_rate_of",
    "decreases_response_to",
    "decreases_secretion_of",
    "decreases_splicing_of",
    "decreases_stability_of",
    "decreases_synthesis_of",
    "decreases_transport_of",
    "decreases_uptake_of",
    "increases_abundance_of",
    "increases_activity_of",
    "increases_degradation_of",
    "increases_expression_of",
    "increases_folding_of",
    "increases_localization_of",
    "increases_metabolic_processing_of",
    "increases_molecular_modification_of",
    "increases_mutation_rate_of",
    "increases_response_to",
    "increases_secretion_of",
    "increases_splicing_of",
    "increases_stability_of",
    "increases_synthesis_of",
    "increases_transport_of",
    "increases_uptake_of",
    "molecularly_interacts_with",
    "regulates_entity_to_entity"
})
public class MolecularEntity {

    /**
     * holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest
     * 
     */
    @JsonProperty("affects_abundance_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest")
    private String affectsAbundanceOf;
    /**
     * holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest
     * 
     */
    @JsonProperty("affects_activity_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest")
    private String affectsActivityOf;
    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("affects_degradation_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest")
    private String affectsDegradationOf;
    /**
     * holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("affects_expression_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest")
    private String affectsExpressionOf;
    /**
     * holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other 
     * 
     */
    @JsonProperty("affects_folding_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other ")
    private String affectsFoldingOf;
    /**
     * holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest
     * 
     */
    @JsonProperty("affects_localization_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest")
    private String affectsLocalizationOf;
    /**
     * holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("affects_metabolic_processing_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest")
    private String affectsMetabolicProcessingOf;
    /**
     * holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("affects_molecular_modification_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)")
    private String affectsMolecularModificationOf;
    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("affects_mutation_rate_of")
    @JsonPropertyDescription("holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest")
    private String affectsMutationRateOf;
    /**
     * holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("affects_response_to")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other")
    private String affectsResponseTo;
    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("affects_secretion_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ")
    private String affectsSecretionOf;
    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA
     * 
     */
    @JsonProperty("affects_splicing_of")
    @JsonPropertyDescription("holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA")
    private String affectsSplicingOf;
    /**
     * holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest
     * 
     */
    @JsonProperty("affects_stability_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest")
    private String affectsStabilityOf;
    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("affects_synthesis_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other")
    private String affectsSynthesisOf;
    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("affects_transport_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest")
    private String affectsTransportOf;
    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("affects_uptake_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ")
    private String affectsUptakeOf;
    /**
     * holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("biomarker_for")
    @JsonPropertyDescription("holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.")
    private String biomarkerFor;
    /**
     * holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_abundance_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest")
    private String decreasesAbundanceOf;
    /**
     * holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_activity_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest")
    private String decreasesActivityOf;
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_degradation_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest")
    private String decreasesDegradationOf;
    /**
     * holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_expression_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest")
    private String decreasesExpressionOf;
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other 
     * 
     */
    @JsonProperty("decreases_folding_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other ")
    private String decreasesFoldingOf;
    /**
     * holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_localization_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest")
    private String decreasesLocalizationOf;
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_metabolic_processing_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest")
    private String decreasesMetabolicProcessingOf;
    /**
     * holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("decreases_molecular_modification_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)")
    private String decreasesMolecularModificationOf;
    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("decreases_mutation_rate_of")
    @JsonPropertyDescription("holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest")
    private String decreasesMutationRateOf;
    /**
     * holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("decreases_response_to")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other")
    private String decreasesResponseTo;
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("decreases_secretion_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ")
    private String decreasesSecretionOf;
    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
     * 
     */
    @JsonProperty("decreases_splicing_of")
    @JsonPropertyDescription("holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA")
    private String decreasesSplicingOf;
    /**
     * holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_stability_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest")
    private String decreasesStabilityOf;
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("decreases_synthesis_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other")
    private String decreasesSynthesisOf;
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("decreases_transport_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest")
    private String decreasesTransportOf;
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("decreases_uptake_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ")
    private String decreasesUptakeOf;
    /**
     * holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
     * 
     */
    @JsonProperty("increases_abundance_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest")
    private String increasesAbundanceOf;
    /**
     * holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
     * 
     */
    @JsonProperty("increases_activity_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest")
    private String increasesActivityOf;
    /**
     * holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("increases_degradation_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest")
    private String increasesDegradationOf;
    /**
     * holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("increases_expression_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest")
    private String increasesExpressionOf;
    /**
     * holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other 
     * 
     */
    @JsonProperty("increases_folding_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other ")
    private String increasesFoldingOf;
    /**
     * holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
     * 
     */
    @JsonProperty("increases_localization_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest")
    private String increasesLocalizationOf;
    /**
     * holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("increases_metabolic_processing_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest")
    private String increasesMetabolicProcessingOf;
    /**
     * holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("increases_molecular_modification_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)")
    private String increasesMolecularModificationOf;
    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("increases_mutation_rate_of")
    @JsonPropertyDescription("holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest")
    private String increasesMutationRateOf;
    /**
     * holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("increases_response_to")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other")
    private String increasesResponseTo;
    /**
     * holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("increases_secretion_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ")
    private String increasesSecretionOf;
    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
     * 
     */
    @JsonProperty("increases_splicing_of")
    @JsonPropertyDescription("holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA")
    private String increasesSplicingOf;
    /**
     * holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
     * 
     */
    @JsonProperty("increases_stability_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest")
    private String increasesStabilityOf;
    /**
     * holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("increases_synthesis_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other")
    private String increasesSynthesisOf;
    /**
     * holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("increases_transport_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest")
    private String increasesTransportOf;
    /**
     * holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("increases_uptake_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ")
    private String increasesUptakeOf;
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
     * holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest
     * 
     */
    @JsonProperty("affects_abundance_of")
    public String getAffectsAbundanceOf() {
        return affectsAbundanceOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest
     * 
     */
    @JsonProperty("affects_abundance_of")
    public void setAffectsAbundanceOf(String affectsAbundanceOf) {
        this.affectsAbundanceOf = affectsAbundanceOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest
     * 
     */
    @JsonProperty("affects_activity_of")
    public String getAffectsActivityOf() {
        return affectsActivityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest
     * 
     */
    @JsonProperty("affects_activity_of")
    public void setAffectsActivityOf(String affectsActivityOf) {
        this.affectsActivityOf = affectsActivityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("affects_degradation_of")
    public String getAffectsDegradationOf() {
        return affectsDegradationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("affects_degradation_of")
    public void setAffectsDegradationOf(String affectsDegradationOf) {
        this.affectsDegradationOf = affectsDegradationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("affects_expression_of")
    public String getAffectsExpressionOf() {
        return affectsExpressionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("affects_expression_of")
    public void setAffectsExpressionOf(String affectsExpressionOf) {
        this.affectsExpressionOf = affectsExpressionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other 
     * 
     */
    @JsonProperty("affects_folding_of")
    public String getAffectsFoldingOf() {
        return affectsFoldingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other 
     * 
     */
    @JsonProperty("affects_folding_of")
    public void setAffectsFoldingOf(String affectsFoldingOf) {
        this.affectsFoldingOf = affectsFoldingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest
     * 
     */
    @JsonProperty("affects_localization_of")
    public String getAffectsLocalizationOf() {
        return affectsLocalizationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest
     * 
     */
    @JsonProperty("affects_localization_of")
    public void setAffectsLocalizationOf(String affectsLocalizationOf) {
        this.affectsLocalizationOf = affectsLocalizationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("affects_metabolic_processing_of")
    public String getAffectsMetabolicProcessingOf() {
        return affectsMetabolicProcessingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("affects_metabolic_processing_of")
    public void setAffectsMetabolicProcessingOf(String affectsMetabolicProcessingOf) {
        this.affectsMetabolicProcessingOf = affectsMetabolicProcessingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("affects_molecular_modification_of")
    public String getAffectsMolecularModificationOf() {
        return affectsMolecularModificationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("affects_molecular_modification_of")
    public void setAffectsMolecularModificationOf(String affectsMolecularModificationOf) {
        this.affectsMolecularModificationOf = affectsMolecularModificationOf;
    }

    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("affects_mutation_rate_of")
    public String getAffectsMutationRateOf() {
        return affectsMutationRateOf;
    }

    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("affects_mutation_rate_of")
    public void setAffectsMutationRateOf(String affectsMutationRateOf) {
        this.affectsMutationRateOf = affectsMutationRateOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("affects_response_to")
    public String getAffectsResponseTo() {
        return affectsResponseTo;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("affects_response_to")
    public void setAffectsResponseTo(String affectsResponseTo) {
        this.affectsResponseTo = affectsResponseTo;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("affects_secretion_of")
    public String getAffectsSecretionOf() {
        return affectsSecretionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("affects_secretion_of")
    public void setAffectsSecretionOf(String affectsSecretionOf) {
        this.affectsSecretionOf = affectsSecretionOf;
    }

    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA
     * 
     */
    @JsonProperty("affects_splicing_of")
    public String getAffectsSplicingOf() {
        return affectsSplicingOf;
    }

    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA
     * 
     */
    @JsonProperty("affects_splicing_of")
    public void setAffectsSplicingOf(String affectsSplicingOf) {
        this.affectsSplicingOf = affectsSplicingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest
     * 
     */
    @JsonProperty("affects_stability_of")
    public String getAffectsStabilityOf() {
        return affectsStabilityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest
     * 
     */
    @JsonProperty("affects_stability_of")
    public void setAffectsStabilityOf(String affectsStabilityOf) {
        this.affectsStabilityOf = affectsStabilityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("affects_synthesis_of")
    public String getAffectsSynthesisOf() {
        return affectsSynthesisOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("affects_synthesis_of")
    public void setAffectsSynthesisOf(String affectsSynthesisOf) {
        this.affectsSynthesisOf = affectsSynthesisOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("affects_transport_of")
    public String getAffectsTransportOf() {
        return affectsTransportOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("affects_transport_of")
    public void setAffectsTransportOf(String affectsTransportOf) {
        this.affectsTransportOf = affectsTransportOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("affects_uptake_of")
    public String getAffectsUptakeOf() {
        return affectsUptakeOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("affects_uptake_of")
    public void setAffectsUptakeOf(String affectsUptakeOf) {
        this.affectsUptakeOf = affectsUptakeOf;
    }

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
     * holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_abundance_of")
    public String getDecreasesAbundanceOf() {
        return decreasesAbundanceOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_abundance_of")
    public void setDecreasesAbundanceOf(String decreasesAbundanceOf) {
        this.decreasesAbundanceOf = decreasesAbundanceOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_activity_of")
    public String getDecreasesActivityOf() {
        return decreasesActivityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_activity_of")
    public void setDecreasesActivityOf(String decreasesActivityOf) {
        this.decreasesActivityOf = decreasesActivityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_degradation_of")
    public String getDecreasesDegradationOf() {
        return decreasesDegradationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_degradation_of")
    public void setDecreasesDegradationOf(String decreasesDegradationOf) {
        this.decreasesDegradationOf = decreasesDegradationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_expression_of")
    public String getDecreasesExpressionOf() {
        return decreasesExpressionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_expression_of")
    public void setDecreasesExpressionOf(String decreasesExpressionOf) {
        this.decreasesExpressionOf = decreasesExpressionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other 
     * 
     */
    @JsonProperty("decreases_folding_of")
    public String getDecreasesFoldingOf() {
        return decreasesFoldingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other 
     * 
     */
    @JsonProperty("decreases_folding_of")
    public void setDecreasesFoldingOf(String decreasesFoldingOf) {
        this.decreasesFoldingOf = decreasesFoldingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_localization_of")
    public String getDecreasesLocalizationOf() {
        return decreasesLocalizationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_localization_of")
    public void setDecreasesLocalizationOf(String decreasesLocalizationOf) {
        this.decreasesLocalizationOf = decreasesLocalizationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_metabolic_processing_of")
    public String getDecreasesMetabolicProcessingOf() {
        return decreasesMetabolicProcessingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_metabolic_processing_of")
    public void setDecreasesMetabolicProcessingOf(String decreasesMetabolicProcessingOf) {
        this.decreasesMetabolicProcessingOf = decreasesMetabolicProcessingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("decreases_molecular_modification_of")
    public String getDecreasesMolecularModificationOf() {
        return decreasesMolecularModificationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("decreases_molecular_modification_of")
    public void setDecreasesMolecularModificationOf(String decreasesMolecularModificationOf) {
        this.decreasesMolecularModificationOf = decreasesMolecularModificationOf;
    }

    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("decreases_mutation_rate_of")
    public String getDecreasesMutationRateOf() {
        return decreasesMutationRateOf;
    }

    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("decreases_mutation_rate_of")
    public void setDecreasesMutationRateOf(String decreasesMutationRateOf) {
        this.decreasesMutationRateOf = decreasesMutationRateOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("decreases_response_to")
    public String getDecreasesResponseTo() {
        return decreasesResponseTo;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("decreases_response_to")
    public void setDecreasesResponseTo(String decreasesResponseTo) {
        this.decreasesResponseTo = decreasesResponseTo;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("decreases_secretion_of")
    public String getDecreasesSecretionOf() {
        return decreasesSecretionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("decreases_secretion_of")
    public void setDecreasesSecretionOf(String decreasesSecretionOf) {
        this.decreasesSecretionOf = decreasesSecretionOf;
    }

    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
     * 
     */
    @JsonProperty("decreases_splicing_of")
    public String getDecreasesSplicingOf() {
        return decreasesSplicingOf;
    }

    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
     * 
     */
    @JsonProperty("decreases_splicing_of")
    public void setDecreasesSplicingOf(String decreasesSplicingOf) {
        this.decreasesSplicingOf = decreasesSplicingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_stability_of")
    public String getDecreasesStabilityOf() {
        return decreasesStabilityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_stability_of")
    public void setDecreasesStabilityOf(String decreasesStabilityOf) {
        this.decreasesStabilityOf = decreasesStabilityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("decreases_synthesis_of")
    public String getDecreasesSynthesisOf() {
        return decreasesSynthesisOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("decreases_synthesis_of")
    public void setDecreasesSynthesisOf(String decreasesSynthesisOf) {
        this.decreasesSynthesisOf = decreasesSynthesisOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("decreases_transport_of")
    public String getDecreasesTransportOf() {
        return decreasesTransportOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("decreases_transport_of")
    public void setDecreasesTransportOf(String decreasesTransportOf) {
        this.decreasesTransportOf = decreasesTransportOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("decreases_uptake_of")
    public String getDecreasesUptakeOf() {
        return decreasesUptakeOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("decreases_uptake_of")
    public void setDecreasesUptakeOf(String decreasesUptakeOf) {
        this.decreasesUptakeOf = decreasesUptakeOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
     * 
     */
    @JsonProperty("increases_abundance_of")
    public String getIncreasesAbundanceOf() {
        return increasesAbundanceOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
     * 
     */
    @JsonProperty("increases_abundance_of")
    public void setIncreasesAbundanceOf(String increasesAbundanceOf) {
        this.increasesAbundanceOf = increasesAbundanceOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
     * 
     */
    @JsonProperty("increases_activity_of")
    public String getIncreasesActivityOf() {
        return increasesActivityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
     * 
     */
    @JsonProperty("increases_activity_of")
    public void setIncreasesActivityOf(String increasesActivityOf) {
        this.increasesActivityOf = increasesActivityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("increases_degradation_of")
    public String getIncreasesDegradationOf() {
        return increasesDegradationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("increases_degradation_of")
    public void setIncreasesDegradationOf(String increasesDegradationOf) {
        this.increasesDegradationOf = increasesDegradationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("increases_expression_of")
    public String getIncreasesExpressionOf() {
        return increasesExpressionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("increases_expression_of")
    public void setIncreasesExpressionOf(String increasesExpressionOf) {
        this.increasesExpressionOf = increasesExpressionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other 
     * 
     */
    @JsonProperty("increases_folding_of")
    public String getIncreasesFoldingOf() {
        return increasesFoldingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other 
     * 
     */
    @JsonProperty("increases_folding_of")
    public void setIncreasesFoldingOf(String increasesFoldingOf) {
        this.increasesFoldingOf = increasesFoldingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
     * 
     */
    @JsonProperty("increases_localization_of")
    public String getIncreasesLocalizationOf() {
        return increasesLocalizationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
     * 
     */
    @JsonProperty("increases_localization_of")
    public void setIncreasesLocalizationOf(String increasesLocalizationOf) {
        this.increasesLocalizationOf = increasesLocalizationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("increases_metabolic_processing_of")
    public String getIncreasesMetabolicProcessingOf() {
        return increasesMetabolicProcessingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("increases_metabolic_processing_of")
    public void setIncreasesMetabolicProcessingOf(String increasesMetabolicProcessingOf) {
        this.increasesMetabolicProcessingOf = increasesMetabolicProcessingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("increases_molecular_modification_of")
    public String getIncreasesMolecularModificationOf() {
        return increasesMolecularModificationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("increases_molecular_modification_of")
    public void setIncreasesMolecularModificationOf(String increasesMolecularModificationOf) {
        this.increasesMolecularModificationOf = increasesMolecularModificationOf;
    }

    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("increases_mutation_rate_of")
    public String getIncreasesMutationRateOf() {
        return increasesMutationRateOf;
    }

    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("increases_mutation_rate_of")
    public void setIncreasesMutationRateOf(String increasesMutationRateOf) {
        this.increasesMutationRateOf = increasesMutationRateOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("increases_response_to")
    public String getIncreasesResponseTo() {
        return increasesResponseTo;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("increases_response_to")
    public void setIncreasesResponseTo(String increasesResponseTo) {
        this.increasesResponseTo = increasesResponseTo;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("increases_secretion_of")
    public String getIncreasesSecretionOf() {
        return increasesSecretionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("increases_secretion_of")
    public void setIncreasesSecretionOf(String increasesSecretionOf) {
        this.increasesSecretionOf = increasesSecretionOf;
    }

    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
     * 
     */
    @JsonProperty("increases_splicing_of")
    public String getIncreasesSplicingOf() {
        return increasesSplicingOf;
    }

    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
     * 
     */
    @JsonProperty("increases_splicing_of")
    public void setIncreasesSplicingOf(String increasesSplicingOf) {
        this.increasesSplicingOf = increasesSplicingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
     * 
     */
    @JsonProperty("increases_stability_of")
    public String getIncreasesStabilityOf() {
        return increasesStabilityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
     * 
     */
    @JsonProperty("increases_stability_of")
    public void setIncreasesStabilityOf(String increasesStabilityOf) {
        this.increasesStabilityOf = increasesStabilityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("increases_synthesis_of")
    public String getIncreasesSynthesisOf() {
        return increasesSynthesisOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("increases_synthesis_of")
    public void setIncreasesSynthesisOf(String increasesSynthesisOf) {
        this.increasesSynthesisOf = increasesSynthesisOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("increases_transport_of")
    public String getIncreasesTransportOf() {
        return increasesTransportOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("increases_transport_of")
    public void setIncreasesTransportOf(String increasesTransportOf) {
        this.increasesTransportOf = increasesTransportOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("increases_uptake_of")
    public String getIncreasesUptakeOf() {
        return increasesUptakeOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("increases_uptake_of")
    public void setIncreasesUptakeOf(String increasesUptakeOf) {
        this.increasesUptakeOf = increasesUptakeOf;
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
        return new ToStringBuilder(this).append("affectsAbundanceOf", affectsAbundanceOf).append("affectsActivityOf", affectsActivityOf).append("affectsDegradationOf", affectsDegradationOf).append("affectsExpressionOf", affectsExpressionOf).append("affectsFoldingOf", affectsFoldingOf).append("affectsLocalizationOf", affectsLocalizationOf).append("affectsMetabolicProcessingOf", affectsMetabolicProcessingOf).append("affectsMolecularModificationOf", affectsMolecularModificationOf).append("affectsMutationRateOf", affectsMutationRateOf).append("affectsResponseTo", affectsResponseTo).append("affectsSecretionOf", affectsSecretionOf).append("affectsSplicingOf", affectsSplicingOf).append("affectsStabilityOf", affectsStabilityOf).append("affectsSynthesisOf", affectsSynthesisOf).append("affectsTransportOf", affectsTransportOf).append("affectsUptakeOf", affectsUptakeOf).append("biomarkerFor", biomarkerFor).append("decreasesAbundanceOf", decreasesAbundanceOf).append("decreasesActivityOf", decreasesActivityOf).append("decreasesDegradationOf", decreasesDegradationOf).append("decreasesExpressionOf", decreasesExpressionOf).append("decreasesFoldingOf", decreasesFoldingOf).append("decreasesLocalizationOf", decreasesLocalizationOf).append("decreasesMetabolicProcessingOf", decreasesMetabolicProcessingOf).append("decreasesMolecularModificationOf", decreasesMolecularModificationOf).append("decreasesMutationRateOf", decreasesMutationRateOf).append("decreasesResponseTo", decreasesResponseTo).append("decreasesSecretionOf", decreasesSecretionOf).append("decreasesSplicingOf", decreasesSplicingOf).append("decreasesStabilityOf", decreasesStabilityOf).append("decreasesSynthesisOf", decreasesSynthesisOf).append("decreasesTransportOf", decreasesTransportOf).append("decreasesUptakeOf", decreasesUptakeOf).append("increasesAbundanceOf", increasesAbundanceOf).append("increasesActivityOf", increasesActivityOf).append("increasesDegradationOf", increasesDegradationOf).append("increasesExpressionOf", increasesExpressionOf).append("increasesFoldingOf", increasesFoldingOf).append("increasesLocalizationOf", increasesLocalizationOf).append("increasesMetabolicProcessingOf", increasesMetabolicProcessingOf).append("increasesMolecularModificationOf", increasesMolecularModificationOf).append("increasesMutationRateOf", increasesMutationRateOf).append("increasesResponseTo", increasesResponseTo).append("increasesSecretionOf", increasesSecretionOf).append("increasesSplicingOf", increasesSplicingOf).append("increasesStabilityOf", increasesStabilityOf).append("increasesSynthesisOf", increasesSynthesisOf).append("increasesTransportOf", increasesTransportOf).append("increasesUptakeOf", increasesUptakeOf).append("molecularlyInteractsWith", molecularlyInteractsWith).append("regulatesEntityToEntity", regulatesEntityToEntity).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(affectsMetabolicProcessingOf).append(decreasesFoldingOf).append(increasesSecretionOf).append(decreasesLocalizationOf).append(affectsUptakeOf).append(decreasesResponseTo).append(decreasesTransportOf).append(molecularlyInteractsWith).append(decreasesExpressionOf).append(increasesStabilityOf).append(decreasesSecretionOf).append(decreasesStabilityOf).append(increasesAbundanceOf).append(increasesMutationRateOf).append(affectsMutationRateOf).append(increasesExpressionOf).append(affectsLocalizationOf).append(affectsAbundanceOf).append(increasesMolecularModificationOf).append(decreasesDegradationOf).append(increasesFoldingOf).append(decreasesMutationRateOf).append(decreasesSynthesisOf).append(affectsFoldingOf).append(decreasesUptakeOf).append(increasesMetabolicProcessingOf).append(decreasesActivityOf).append(affectsSecretionOf).append(decreasesSplicingOf).append(decreasesMetabolicProcessingOf).append(increasesUptakeOf).append(affectsActivityOf).append(affectsStabilityOf).append(increasesSplicingOf).append(biomarkerFor).append(increasesLocalizationOf).append(increasesDegradationOf).append(affectsResponseTo).append(affectsExpressionOf).append(affectsTransportOf).append(decreasesAbundanceOf).append(affectsSynthesisOf).append(affectsDegradationOf).append(affectsSplicingOf).append(affectsMolecularModificationOf).append(decreasesMolecularModificationOf).append(increasesTransportOf).append(increasesSynthesisOf).append(increasesResponseTo).append(increasesActivityOf).append(regulatesEntityToEntity).toHashCode();
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
        return new EqualsBuilder().append(affectsMetabolicProcessingOf, rhs.affectsMetabolicProcessingOf).append(decreasesFoldingOf, rhs.decreasesFoldingOf).append(increasesSecretionOf, rhs.increasesSecretionOf).append(decreasesLocalizationOf, rhs.decreasesLocalizationOf).append(affectsUptakeOf, rhs.affectsUptakeOf).append(decreasesResponseTo, rhs.decreasesResponseTo).append(decreasesTransportOf, rhs.decreasesTransportOf).append(molecularlyInteractsWith, rhs.molecularlyInteractsWith).append(decreasesExpressionOf, rhs.decreasesExpressionOf).append(increasesStabilityOf, rhs.increasesStabilityOf).append(decreasesSecretionOf, rhs.decreasesSecretionOf).append(decreasesStabilityOf, rhs.decreasesStabilityOf).append(increasesAbundanceOf, rhs.increasesAbundanceOf).append(increasesMutationRateOf, rhs.increasesMutationRateOf).append(affectsMutationRateOf, rhs.affectsMutationRateOf).append(increasesExpressionOf, rhs.increasesExpressionOf).append(affectsLocalizationOf, rhs.affectsLocalizationOf).append(affectsAbundanceOf, rhs.affectsAbundanceOf).append(increasesMolecularModificationOf, rhs.increasesMolecularModificationOf).append(decreasesDegradationOf, rhs.decreasesDegradationOf).append(increasesFoldingOf, rhs.increasesFoldingOf).append(decreasesMutationRateOf, rhs.decreasesMutationRateOf).append(decreasesSynthesisOf, rhs.decreasesSynthesisOf).append(affectsFoldingOf, rhs.affectsFoldingOf).append(decreasesUptakeOf, rhs.decreasesUptakeOf).append(increasesMetabolicProcessingOf, rhs.increasesMetabolicProcessingOf).append(decreasesActivityOf, rhs.decreasesActivityOf).append(affectsSecretionOf, rhs.affectsSecretionOf).append(decreasesSplicingOf, rhs.decreasesSplicingOf).append(decreasesMetabolicProcessingOf, rhs.decreasesMetabolicProcessingOf).append(increasesUptakeOf, rhs.increasesUptakeOf).append(affectsActivityOf, rhs.affectsActivityOf).append(affectsStabilityOf, rhs.affectsStabilityOf).append(increasesSplicingOf, rhs.increasesSplicingOf).append(biomarkerFor, rhs.biomarkerFor).append(increasesLocalizationOf, rhs.increasesLocalizationOf).append(increasesDegradationOf, rhs.increasesDegradationOf).append(affectsResponseTo, rhs.affectsResponseTo).append(affectsExpressionOf, rhs.affectsExpressionOf).append(affectsTransportOf, rhs.affectsTransportOf).append(decreasesAbundanceOf, rhs.decreasesAbundanceOf).append(affectsSynthesisOf, rhs.affectsSynthesisOf).append(affectsDegradationOf, rhs.affectsDegradationOf).append(affectsSplicingOf, rhs.affectsSplicingOf).append(affectsMolecularModificationOf, rhs.affectsMolecularModificationOf).append(decreasesMolecularModificationOf, rhs.decreasesMolecularModificationOf).append(increasesTransportOf, rhs.increasesTransportOf).append(increasesSynthesisOf, rhs.increasesSynthesisOf).append(increasesResponseTo, rhs.increasesResponseTo).append(increasesActivityOf, rhs.increasesActivityOf).append(regulatesEntityToEntity, rhs.regulatesEntityToEntity).isEquals();
    }

}
