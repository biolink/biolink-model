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
    "in_taxon",
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
    "negatively_regulates_entity_to_entity",
    "positively_regulates_entity_to_entity",
    "regulates_entity_to_entity"
})
public class MolecularEntity {

    /**
     * holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest
     * 
     */
    @JsonProperty("affects_abundance_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest")
    private List<String> affectsAbundanceOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest
     * 
     */
    @JsonProperty("affects_activity_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest")
    private List<String> affectsActivityOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("affects_degradation_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest")
    private List<String> affectsDegradationOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("affects_expression_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest")
    private List<String> affectsExpressionOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other
     * 
     */
    @JsonProperty("affects_folding_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other")
    private List<String> affectsFoldingOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest
     * 
     */
    @JsonProperty("affects_localization_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest")
    private List<String> affectsLocalizationOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("affects_metabolic_processing_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest")
    private List<String> affectsMetabolicProcessingOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("affects_molecular_modification_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)")
    private List<String> affectsMolecularModificationOf = new ArrayList<String>();
    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("affects_mutation_rate_of")
    @JsonPropertyDescription("holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest")
    private List<String> affectsMutationRateOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("affects_response_to")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other")
    private List<String> affectsResponseTo = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("affects_secretion_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ")
    private List<String> affectsSecretionOf = new ArrayList<String>();
    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA
     * 
     */
    @JsonProperty("affects_splicing_of")
    @JsonPropertyDescription("holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA")
    private List<String> affectsSplicingOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest
     * 
     */
    @JsonProperty("affects_stability_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest")
    private List<String> affectsStabilityOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("affects_synthesis_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other")
    private List<String> affectsSynthesisOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("affects_transport_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest")
    private List<String> affectsTransportOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("affects_uptake_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ")
    private List<String> affectsUptakeOf = new ArrayList<String>();
    /**
     * holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("biomarker_for")
    @JsonPropertyDescription("holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.")
    private List<String> biomarkerFor = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_abundance_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest")
    private List<String> decreasesAbundanceOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_activity_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest")
    private List<String> decreasesActivityOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_degradation_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest")
    private List<String> decreasesDegradationOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_expression_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest")
    private List<String> decreasesExpressionOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other
     * 
     */
    @JsonProperty("decreases_folding_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other")
    private List<String> decreasesFoldingOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_localization_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest")
    private List<String> decreasesLocalizationOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_metabolic_processing_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest")
    private List<String> decreasesMetabolicProcessingOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("decreases_molecular_modification_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)")
    private List<String> decreasesMolecularModificationOf = new ArrayList<String>();
    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("decreases_mutation_rate_of")
    @JsonPropertyDescription("holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest")
    private List<String> decreasesMutationRateOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("decreases_response_to")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other")
    private List<String> decreasesResponseTo = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("decreases_secretion_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ")
    private List<String> decreasesSecretionOf = new ArrayList<String>();
    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
     * 
     */
    @JsonProperty("decreases_splicing_of")
    @JsonPropertyDescription("holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA")
    private List<String> decreasesSplicingOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_stability_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest")
    private List<String> decreasesStabilityOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("decreases_synthesis_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other")
    private List<String> decreasesSynthesisOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("decreases_transport_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest")
    private List<String> decreasesTransportOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("decreases_uptake_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ")
    private List<String> decreasesUptakeOf = new ArrayList<String>();
    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    @JsonPropertyDescription("connects a thing to a class representing a taxon")
    private List<String> inTaxon = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
     * 
     */
    @JsonProperty("increases_abundance_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest")
    private List<String> increasesAbundanceOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
     * 
     */
    @JsonProperty("increases_activity_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest")
    private List<String> increasesActivityOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("increases_degradation_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest")
    private List<String> increasesDegradationOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("increases_expression_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest")
    private List<String> increasesExpressionOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other
     * 
     */
    @JsonProperty("increases_folding_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other")
    private List<String> increasesFoldingOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
     * 
     */
    @JsonProperty("increases_localization_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest")
    private List<String> increasesLocalizationOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("increases_metabolic_processing_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest")
    private List<String> increasesMetabolicProcessingOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("increases_molecular_modification_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)")
    private List<String> increasesMolecularModificationOf = new ArrayList<String>();
    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("increases_mutation_rate_of")
    @JsonPropertyDescription("holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest")
    private List<String> increasesMutationRateOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("increases_response_to")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other")
    private List<String> increasesResponseTo = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("increases_secretion_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ")
    private List<String> increasesSecretionOf = new ArrayList<String>();
    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
     * 
     */
    @JsonProperty("increases_splicing_of")
    @JsonPropertyDescription("holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA")
    private List<String> increasesSplicingOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
     * 
     */
    @JsonProperty("increases_stability_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest")
    private List<String> increasesStabilityOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("increases_synthesis_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other")
    private List<String> increasesSynthesisOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("increases_transport_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest")
    private List<String> increasesTransportOf = new ArrayList<String>();
    /**
     * holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("increases_uptake_of")
    @JsonPropertyDescription("holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ")
    private List<String> increasesUptakeOf = new ArrayList<String>();
    @JsonProperty("molecularly_interacts_with")
    private List<String> molecularlyInteractsWith = new ArrayList<String>();
    @JsonProperty("negatively_regulates_entity_to_entity")
    private List<String> negativelyRegulatesEntityToEntity = new ArrayList<String>();
    @JsonProperty("positively_regulates_entity_to_entity")
    private List<String> positivelyRegulatesEntityToEntity = new ArrayList<String>();
    @JsonProperty("regulates_entity_to_entity")
    private List<String> regulatesEntityToEntity = new ArrayList<String>();

    /**
     * holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest
     * 
     */
    @JsonProperty("affects_abundance_of")
    public List<String> getAffectsAbundanceOf() {
        return affectsAbundanceOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the amount of the other within a system of interest
     * 
     */
    @JsonProperty("affects_abundance_of")
    public void setAffectsAbundanceOf(List<String> affectsAbundanceOf) {
        this.affectsAbundanceOf = affectsAbundanceOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest
     * 
     */
    @JsonProperty("affects_activity_of")
    public List<String> getAffectsActivityOf() {
        return affectsActivityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the activity of the other within a system of interest
     * 
     */
    @JsonProperty("affects_activity_of")
    public void setAffectsActivityOf(List<String> affectsActivityOf) {
        this.affectsActivityOf = affectsActivityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("affects_degradation_of")
    public List<String> getAffectsDegradationOf() {
        return affectsDegradationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("affects_degradation_of")
    public void setAffectsDegradationOf(List<String> affectsDegradationOf) {
        this.affectsDegradationOf = affectsDegradationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("affects_expression_of")
    public List<String> getAffectsExpressionOf() {
        return affectsExpressionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("affects_expression_of")
    public void setAffectsExpressionOf(List<String> affectsExpressionOf) {
        this.affectsExpressionOf = affectsExpressionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other
     * 
     */
    @JsonProperty("affects_folding_of")
    public List<String> getAffectsFoldingOf() {
        return affectsFoldingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the rate or quality of folding of the other
     * 
     */
    @JsonProperty("affects_folding_of")
    public void setAffectsFoldingOf(List<String> affectsFoldingOf) {
        this.affectsFoldingOf = affectsFoldingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest
     * 
     */
    @JsonProperty("affects_localization_of")
    public List<String> getAffectsLocalizationOf() {
        return affectsLocalizationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one changes the localization of the other within a system of interest
     * 
     */
    @JsonProperty("affects_localization_of")
    public void setAffectsLocalizationOf(List<String> affectsLocalizationOf) {
        this.affectsLocalizationOf = affectsLocalizationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("affects_metabolic_processing_of")
    public List<String> getAffectsMetabolicProcessingOf() {
        return affectsMetabolicProcessingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("affects_metabolic_processing_of")
    public void setAffectsMetabolicProcessingOf(List<String> affectsMetabolicProcessingOf) {
        this.affectsMetabolicProcessingOf = affectsMetabolicProcessingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("affects_molecular_modification_of")
    public List<String> getAffectsMolecularModificationOf() {
        return affectsMolecularModificationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one leads changes in the molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("affects_molecular_modification_of")
    public void setAffectsMolecularModificationOf(List<String> affectsMolecularModificationOf) {
        this.affectsMolecularModificationOf = affectsMolecularModificationOf;
    }

    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("affects_mutation_rate_of")
    public List<String> getAffectsMutationRateOf() {
        return affectsMutationRateOf;
    }

    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity impacts the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("affects_mutation_rate_of")
    public void setAffectsMutationRateOf(List<String> affectsMutationRateOf) {
        this.affectsMutationRateOf = affectsMutationRateOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("affects_response_to")
    public List<String> getAffectsResponseTo() {
        return affectsResponseTo;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("affects_response_to")
    public void setAffectsResponseTo(List<String> affectsResponseTo) {
        this.affectsResponseTo = affectsResponseTo;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("affects_secretion_of")
    public List<String> getAffectsSecretionOf() {
        return affectsSecretionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("affects_secretion_of")
    public void setAffectsSecretionOf(List<String> affectsSecretionOf) {
        this.affectsSecretionOf = affectsSecretionOf;
    }

    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA
     * 
     */
    @JsonProperty("affects_splicing_of")
    public List<String> getAffectsSplicingOf() {
        return affectsSplicingOf;
    }

    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity impacts the splicing of the mRNA
     * 
     */
    @JsonProperty("affects_splicing_of")
    public void setAffectsSplicingOf(List<String> affectsSplicingOf) {
        this.affectsSplicingOf = affectsSplicingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest
     * 
     */
    @JsonProperty("affects_stability_of")
    public List<String> getAffectsStabilityOf() {
        return affectsStabilityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the stability of the other within a system of interest
     * 
     */
    @JsonProperty("affects_stability_of")
    public void setAffectsStabilityOf(List<String> affectsStabilityOf) {
        this.affectsStabilityOf = affectsStabilityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("affects_synthesis_of")
    public List<String> getAffectsSynthesisOf() {
        return affectsSynthesisOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("affects_synthesis_of")
    public void setAffectsSynthesisOf(List<String> affectsSynthesisOf) {
        this.affectsSynthesisOf = affectsSynthesisOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("affects_transport_of")
    public List<String> getAffectsTransportOf() {
        return affectsTransportOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("affects_transport_of")
    public void setAffectsTransportOf(List<String> affectsTransportOf) {
        this.affectsTransportOf = affectsTransportOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("affects_uptake_of")
    public List<String> getAffectsUptakeOf() {
        return affectsUptakeOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one impacts the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("affects_uptake_of")
    public void setAffectsUptakeOf(List<String> affectsUptakeOf) {
        this.affectsUptakeOf = affectsUptakeOf;
    }

    /**
     * holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("biomarker_for")
    public List<String> getBiomarkerFor() {
        return biomarkerFor;
    }

    /**
     * holds between a measurable molecular entity and a disease or phenotypic feature, where the entity is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("biomarker_for")
    public void setBiomarkerFor(List<String> biomarkerFor) {
        this.biomarkerFor = biomarkerFor;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_abundance_of")
    public List<String> getDecreasesAbundanceOf() {
        return decreasesAbundanceOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the amount of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_abundance_of")
    public void setDecreasesAbundanceOf(List<String> decreasesAbundanceOf) {
        this.decreasesAbundanceOf = decreasesAbundanceOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_activity_of")
    public List<String> getDecreasesActivityOf() {
        return decreasesActivityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the activity of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_activity_of")
    public void setDecreasesActivityOf(List<String> decreasesActivityOf) {
        this.decreasesActivityOf = decreasesActivityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_degradation_of")
    public List<String> getDecreasesDegradationOf() {
        return decreasesDegradationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_degradation_of")
    public void setDecreasesDegradationOf(List<String> decreasesDegradationOf) {
        this.decreasesDegradationOf = decreasesDegradationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_expression_of")
    public List<String> getDecreasesExpressionOf() {
        return decreasesExpressionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_expression_of")
    public void setDecreasesExpressionOf(List<String> decreasesExpressionOf) {
        this.decreasesExpressionOf = decreasesExpressionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other
     * 
     */
    @JsonProperty("decreases_folding_of")
    public List<String> getDecreasesFoldingOf() {
        return decreasesFoldingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate or quality of folding of the other
     * 
     */
    @JsonProperty("decreases_folding_of")
    public void setDecreasesFoldingOf(List<String> decreasesFoldingOf) {
        this.decreasesFoldingOf = decreasesFoldingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_localization_of")
    public List<String> getDecreasesLocalizationOf() {
        return decreasesLocalizationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the proper localization of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_localization_of")
    public void setDecreasesLocalizationOf(List<String> decreasesLocalizationOf) {
        this.decreasesLocalizationOf = decreasesLocalizationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_metabolic_processing_of")
    public List<String> getDecreasesMetabolicProcessingOf() {
        return decreasesMetabolicProcessingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_metabolic_processing_of")
    public void setDecreasesMetabolicProcessingOf(List<String> decreasesMetabolicProcessingOf) {
        this.decreasesMetabolicProcessingOf = decreasesMetabolicProcessingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("decreases_molecular_modification_of")
    public List<String> getDecreasesMolecularModificationOf() {
        return decreasesMolecularModificationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one leads to decreased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("decreases_molecular_modification_of")
    public void setDecreasesMolecularModificationOf(List<String> decreasesMolecularModificationOf) {
        this.decreasesMolecularModificationOf = decreasesMolecularModificationOf;
    }

    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("decreases_mutation_rate_of")
    public List<String> getDecreasesMutationRateOf() {
        return decreasesMutationRateOf;
    }

    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity decreases the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("decreases_mutation_rate_of")
    public void setDecreasesMutationRateOf(List<String> decreasesMutationRateOf) {
        this.decreasesMutationRateOf = decreasesMutationRateOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("decreases_response_to")
    public List<String> getDecreasesResponseTo() {
        return decreasesResponseTo;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("decreases_response_to")
    public void setDecreasesResponseTo(List<String> decreasesResponseTo) {
        this.decreasesResponseTo = decreasesResponseTo;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("decreases_secretion_of")
    public List<String> getDecreasesSecretionOf() {
        return decreasesSecretionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("decreases_secretion_of")
    public void setDecreasesSecretionOf(List<String> decreasesSecretionOf) {
        this.decreasesSecretionOf = decreasesSecretionOf;
    }

    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
     * 
     */
    @JsonProperty("decreases_splicing_of")
    public List<String> getDecreasesSplicingOf() {
        return decreasesSplicingOf;
    }

    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity decreases the proper splicing of the mRNA
     * 
     */
    @JsonProperty("decreases_splicing_of")
    public void setDecreasesSplicingOf(List<String> decreasesSplicingOf) {
        this.decreasesSplicingOf = decreasesSplicingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_stability_of")
    public List<String> getDecreasesStabilityOf() {
        return decreasesStabilityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the stability of the other within a system of interest
     * 
     */
    @JsonProperty("decreases_stability_of")
    public void setDecreasesStabilityOf(List<String> decreasesStabilityOf) {
        this.decreasesStabilityOf = decreasesStabilityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("decreases_synthesis_of")
    public List<String> getDecreasesSynthesisOf() {
        return decreasesSynthesisOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("decreases_synthesis_of")
    public void setDecreasesSynthesisOf(List<String> decreasesSynthesisOf) {
        this.decreasesSynthesisOf = decreasesSynthesisOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("decreases_transport_of")
    public List<String> getDecreasesTransportOf() {
        return decreasesTransportOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("decreases_transport_of")
    public void setDecreasesTransportOf(List<String> decreasesTransportOf) {
        this.decreasesTransportOf = decreasesTransportOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("decreases_uptake_of")
    public List<String> getDecreasesUptakeOf() {
        return decreasesUptakeOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one decreases the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("decreases_uptake_of")
    public void setDecreasesUptakeOf(List<String> decreasesUptakeOf) {
        this.decreasesUptakeOf = decreasesUptakeOf;
    }

    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    public List<String> getInTaxon() {
        return inTaxon;
    }

    /**
     * connects a thing to a class representing a taxon
     * 
     */
    @JsonProperty("in_taxon")
    public void setInTaxon(List<String> inTaxon) {
        this.inTaxon = inTaxon;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
     * 
     */
    @JsonProperty("increases_abundance_of")
    public List<String> getIncreasesAbundanceOf() {
        return increasesAbundanceOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the amount of the other within a system of interest
     * 
     */
    @JsonProperty("increases_abundance_of")
    public void setIncreasesAbundanceOf(List<String> increasesAbundanceOf) {
        this.increasesAbundanceOf = increasesAbundanceOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
     * 
     */
    @JsonProperty("increases_activity_of")
    public List<String> getIncreasesActivityOf() {
        return increasesActivityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the activity of the other within a system of interest
     * 
     */
    @JsonProperty("increases_activity_of")
    public void setIncreasesActivityOf(List<String> increasesActivityOf) {
        this.increasesActivityOf = increasesActivityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("increases_degradation_of")
    public List<String> getIncreasesDegradationOf() {
        return increasesDegradationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of degradation of the other within a system of interest
     * 
     */
    @JsonProperty("increases_degradation_of")
    public void setIncreasesDegradationOf(List<String> increasesDegradationOf) {
        this.increasesDegradationOf = increasesDegradationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("increases_expression_of")
    public List<String> getIncreasesExpressionOf() {
        return increasesExpressionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the level of expression of the other within a system of interest
     * 
     */
    @JsonProperty("increases_expression_of")
    public void setIncreasesExpressionOf(List<String> increasesExpressionOf) {
        this.increasesExpressionOf = increasesExpressionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other
     * 
     */
    @JsonProperty("increases_folding_of")
    public List<String> getIncreasesFoldingOf() {
        return increasesFoldingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate or quality of folding of the other
     * 
     */
    @JsonProperty("increases_folding_of")
    public void setIncreasesFoldingOf(List<String> increasesFoldingOf) {
        this.increasesFoldingOf = increasesFoldingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
     * 
     */
    @JsonProperty("increases_localization_of")
    public List<String> getIncreasesLocalizationOf() {
        return increasesLocalizationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the proper localization of the other within a system of interest
     * 
     */
    @JsonProperty("increases_localization_of")
    public void setIncreasesLocalizationOf(List<String> increasesLocalizationOf) {
        this.increasesLocalizationOf = increasesLocalizationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("increases_metabolic_processing_of")
    public List<String> getIncreasesMetabolicProcessingOf() {
        return increasesMetabolicProcessingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of metabolic processing of the other within a system of interest
     * 
     */
    @JsonProperty("increases_metabolic_processing_of")
    public void setIncreasesMetabolicProcessingOf(List<String> increasesMetabolicProcessingOf) {
        this.increasesMetabolicProcessingOf = increasesMetabolicProcessingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("increases_molecular_modification_of")
    public List<String> getIncreasesMolecularModificationOf() {
        return increasesMolecularModificationOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one leads to increased molecular modification(s) of the other (e.g. via post-translational modifications of proteins such as the addition of phosphoryl group, or via redox reaction that adds or subtracts electrons)
     * 
     */
    @JsonProperty("increases_molecular_modification_of")
    public void setIncreasesMolecularModificationOf(List<String> increasesMolecularModificationOf) {
        this.increasesMolecularModificationOf = increasesMolecularModificationOf;
    }

    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("increases_mutation_rate_of")
    public List<String> getIncreasesMutationRateOf() {
        return increasesMutationRateOf;
    }

    /**
     * holds between a molecular entity and a genomic entity where the action or effect of the molecular entity increases the rate of mutation of the genomic entity within a system of interest
     * 
     */
    @JsonProperty("increases_mutation_rate_of")
    public void setIncreasesMutationRateOf(List<String> increasesMutationRateOf) {
        this.increasesMutationRateOf = increasesMutationRateOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("increases_response_to")
    public List<String> getIncreasesResponseTo() {
        return increasesResponseTo;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the susceptibility of a biological entity or system (e.g. an organism, cell, cellular component, macromolecular machine, biological or pathological process) to the other
     * 
     */
    @JsonProperty("increases_response_to")
    public void setIncreasesResponseTo(List<String> increasesResponseTo) {
        this.increasesResponseTo = increasesResponseTo;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("increases_secretion_of")
    public List<String> getIncreasesSecretionOf() {
        return increasesSecretionOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of secretion of the other out of a cell, gland, or organ
     * 
     */
    @JsonProperty("increases_secretion_of")
    public void setIncreasesSecretionOf(List<String> increasesSecretionOf) {
        this.increasesSecretionOf = increasesSecretionOf;
    }

    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
     * 
     */
    @JsonProperty("increases_splicing_of")
    public List<String> getIncreasesSplicingOf() {
        return increasesSplicingOf;
    }

    /**
     * holds between a molecular entity and an mRNA where the action or effect of the molecular entity increases the proper splicing of the mRNA
     * 
     */
    @JsonProperty("increases_splicing_of")
    public void setIncreasesSplicingOf(List<String> increasesSplicingOf) {
        this.increasesSplicingOf = increasesSplicingOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
     * 
     */
    @JsonProperty("increases_stability_of")
    public List<String> getIncreasesStabilityOf() {
        return increasesStabilityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the stability of the other within a system of interest
     * 
     */
    @JsonProperty("increases_stability_of")
    public void setIncreasesStabilityOf(List<String> increasesStabilityOf) {
        this.increasesStabilityOf = increasesStabilityOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("increases_synthesis_of")
    public List<String> getIncreasesSynthesisOf() {
        return increasesSynthesisOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of chemical synthesis of the other
     * 
     */
    @JsonProperty("increases_synthesis_of")
    public void setIncreasesSynthesisOf(List<String> increasesSynthesisOf) {
        this.increasesSynthesisOf = increasesSynthesisOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("increases_transport_of")
    public List<String> getIncreasesTransportOf() {
        return increasesTransportOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of transport of the other across some boundary in a system of interest
     * 
     */
    @JsonProperty("increases_transport_of")
    public void setIncreasesTransportOf(List<String> increasesTransportOf) {
        this.increasesTransportOf = increasesTransportOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("increases_uptake_of")
    public List<String> getIncreasesUptakeOf() {
        return increasesUptakeOf;
    }

    /**
     * holds between two molecular entities where the action or effect of one increases the rate of uptake of the other into of a cell, gland, or organ
     * 
     */
    @JsonProperty("increases_uptake_of")
    public void setIncreasesUptakeOf(List<String> increasesUptakeOf) {
        this.increasesUptakeOf = increasesUptakeOf;
    }

    @JsonProperty("molecularly_interacts_with")
    public List<String> getMolecularlyInteractsWith() {
        return molecularlyInteractsWith;
    }

    @JsonProperty("molecularly_interacts_with")
    public void setMolecularlyInteractsWith(List<String> molecularlyInteractsWith) {
        this.molecularlyInteractsWith = molecularlyInteractsWith;
    }

    @JsonProperty("negatively_regulates_entity_to_entity")
    public List<String> getNegativelyRegulatesEntityToEntity() {
        return negativelyRegulatesEntityToEntity;
    }

    @JsonProperty("negatively_regulates_entity_to_entity")
    public void setNegativelyRegulatesEntityToEntity(List<String> negativelyRegulatesEntityToEntity) {
        this.negativelyRegulatesEntityToEntity = negativelyRegulatesEntityToEntity;
    }

    @JsonProperty("positively_regulates_entity_to_entity")
    public List<String> getPositivelyRegulatesEntityToEntity() {
        return positivelyRegulatesEntityToEntity;
    }

    @JsonProperty("positively_regulates_entity_to_entity")
    public void setPositivelyRegulatesEntityToEntity(List<String> positivelyRegulatesEntityToEntity) {
        this.positivelyRegulatesEntityToEntity = positivelyRegulatesEntityToEntity;
    }

    @JsonProperty("regulates_entity_to_entity")
    public List<String> getRegulatesEntityToEntity() {
        return regulatesEntityToEntity;
    }

    @JsonProperty("regulates_entity_to_entity")
    public void setRegulatesEntityToEntity(List<String> regulatesEntityToEntity) {
        this.regulatesEntityToEntity = regulatesEntityToEntity;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("affectsAbundanceOf", affectsAbundanceOf).append("affectsActivityOf", affectsActivityOf).append("affectsDegradationOf", affectsDegradationOf).append("affectsExpressionOf", affectsExpressionOf).append("affectsFoldingOf", affectsFoldingOf).append("affectsLocalizationOf", affectsLocalizationOf).append("affectsMetabolicProcessingOf", affectsMetabolicProcessingOf).append("affectsMolecularModificationOf", affectsMolecularModificationOf).append("affectsMutationRateOf", affectsMutationRateOf).append("affectsResponseTo", affectsResponseTo).append("affectsSecretionOf", affectsSecretionOf).append("affectsSplicingOf", affectsSplicingOf).append("affectsStabilityOf", affectsStabilityOf).append("affectsSynthesisOf", affectsSynthesisOf).append("affectsTransportOf", affectsTransportOf).append("affectsUptakeOf", affectsUptakeOf).append("biomarkerFor", biomarkerFor).append("decreasesAbundanceOf", decreasesAbundanceOf).append("decreasesActivityOf", decreasesActivityOf).append("decreasesDegradationOf", decreasesDegradationOf).append("decreasesExpressionOf", decreasesExpressionOf).append("decreasesFoldingOf", decreasesFoldingOf).append("decreasesLocalizationOf", decreasesLocalizationOf).append("decreasesMetabolicProcessingOf", decreasesMetabolicProcessingOf).append("decreasesMolecularModificationOf", decreasesMolecularModificationOf).append("decreasesMutationRateOf", decreasesMutationRateOf).append("decreasesResponseTo", decreasesResponseTo).append("decreasesSecretionOf", decreasesSecretionOf).append("decreasesSplicingOf", decreasesSplicingOf).append("decreasesStabilityOf", decreasesStabilityOf).append("decreasesSynthesisOf", decreasesSynthesisOf).append("decreasesTransportOf", decreasesTransportOf).append("decreasesUptakeOf", decreasesUptakeOf).append("inTaxon", inTaxon).append("increasesAbundanceOf", increasesAbundanceOf).append("increasesActivityOf", increasesActivityOf).append("increasesDegradationOf", increasesDegradationOf).append("increasesExpressionOf", increasesExpressionOf).append("increasesFoldingOf", increasesFoldingOf).append("increasesLocalizationOf", increasesLocalizationOf).append("increasesMetabolicProcessingOf", increasesMetabolicProcessingOf).append("increasesMolecularModificationOf", increasesMolecularModificationOf).append("increasesMutationRateOf", increasesMutationRateOf).append("increasesResponseTo", increasesResponseTo).append("increasesSecretionOf", increasesSecretionOf).append("increasesSplicingOf", increasesSplicingOf).append("increasesStabilityOf", increasesStabilityOf).append("increasesSynthesisOf", increasesSynthesisOf).append("increasesTransportOf", increasesTransportOf).append("increasesUptakeOf", increasesUptakeOf).append("molecularlyInteractsWith", molecularlyInteractsWith).append("negativelyRegulatesEntityToEntity", negativelyRegulatesEntityToEntity).append("positivelyRegulatesEntityToEntity", positivelyRegulatesEntityToEntity).append("regulatesEntityToEntity", regulatesEntityToEntity).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(affectsMetabolicProcessingOf).append(decreasesFoldingOf).append(increasesSecretionOf).append(decreasesLocalizationOf).append(affectsUptakeOf).append(decreasesResponseTo).append(decreasesTransportOf).append(molecularlyInteractsWith).append(decreasesExpressionOf).append(increasesStabilityOf).append(decreasesSecretionOf).append(decreasesStabilityOf).append(increasesAbundanceOf).append(increasesMutationRateOf).append(affectsMutationRateOf).append(increasesExpressionOf).append(affectsLocalizationOf).append(affectsAbundanceOf).append(increasesMolecularModificationOf).append(decreasesDegradationOf).append(increasesFoldingOf).append(decreasesMutationRateOf).append(decreasesSynthesisOf).append(affectsFoldingOf).append(decreasesUptakeOf).append(increasesMetabolicProcessingOf).append(decreasesActivityOf).append(affectsSecretionOf).append(decreasesSplicingOf).append(decreasesMetabolicProcessingOf).append(increasesUptakeOf).append(negativelyRegulatesEntityToEntity).append(inTaxon).append(affectsActivityOf).append(affectsStabilityOf).append(increasesSplicingOf).append(biomarkerFor).append(increasesLocalizationOf).append(increasesDegradationOf).append(affectsResponseTo).append(affectsExpressionOf).append(affectsTransportOf).append(decreasesAbundanceOf).append(affectsSynthesisOf).append(affectsDegradationOf).append(affectsSplicingOf).append(affectsMolecularModificationOf).append(decreasesMolecularModificationOf).append(increasesTransportOf).append(increasesSynthesisOf).append(increasesResponseTo).append(increasesActivityOf).append(regulatesEntityToEntity).append(positivelyRegulatesEntityToEntity).toHashCode();
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
        return new EqualsBuilder().append(affectsMetabolicProcessingOf, rhs.affectsMetabolicProcessingOf).append(decreasesFoldingOf, rhs.decreasesFoldingOf).append(increasesSecretionOf, rhs.increasesSecretionOf).append(decreasesLocalizationOf, rhs.decreasesLocalizationOf).append(affectsUptakeOf, rhs.affectsUptakeOf).append(decreasesResponseTo, rhs.decreasesResponseTo).append(decreasesTransportOf, rhs.decreasesTransportOf).append(molecularlyInteractsWith, rhs.molecularlyInteractsWith).append(decreasesExpressionOf, rhs.decreasesExpressionOf).append(increasesStabilityOf, rhs.increasesStabilityOf).append(decreasesSecretionOf, rhs.decreasesSecretionOf).append(decreasesStabilityOf, rhs.decreasesStabilityOf).append(increasesAbundanceOf, rhs.increasesAbundanceOf).append(increasesMutationRateOf, rhs.increasesMutationRateOf).append(affectsMutationRateOf, rhs.affectsMutationRateOf).append(increasesExpressionOf, rhs.increasesExpressionOf).append(affectsLocalizationOf, rhs.affectsLocalizationOf).append(affectsAbundanceOf, rhs.affectsAbundanceOf).append(increasesMolecularModificationOf, rhs.increasesMolecularModificationOf).append(decreasesDegradationOf, rhs.decreasesDegradationOf).append(increasesFoldingOf, rhs.increasesFoldingOf).append(decreasesMutationRateOf, rhs.decreasesMutationRateOf).append(decreasesSynthesisOf, rhs.decreasesSynthesisOf).append(affectsFoldingOf, rhs.affectsFoldingOf).append(decreasesUptakeOf, rhs.decreasesUptakeOf).append(increasesMetabolicProcessingOf, rhs.increasesMetabolicProcessingOf).append(decreasesActivityOf, rhs.decreasesActivityOf).append(affectsSecretionOf, rhs.affectsSecretionOf).append(decreasesSplicingOf, rhs.decreasesSplicingOf).append(decreasesMetabolicProcessingOf, rhs.decreasesMetabolicProcessingOf).append(increasesUptakeOf, rhs.increasesUptakeOf).append(negativelyRegulatesEntityToEntity, rhs.negativelyRegulatesEntityToEntity).append(inTaxon, rhs.inTaxon).append(affectsActivityOf, rhs.affectsActivityOf).append(affectsStabilityOf, rhs.affectsStabilityOf).append(increasesSplicingOf, rhs.increasesSplicingOf).append(biomarkerFor, rhs.biomarkerFor).append(increasesLocalizationOf, rhs.increasesLocalizationOf).append(increasesDegradationOf, rhs.increasesDegradationOf).append(affectsResponseTo, rhs.affectsResponseTo).append(affectsExpressionOf, rhs.affectsExpressionOf).append(affectsTransportOf, rhs.affectsTransportOf).append(decreasesAbundanceOf, rhs.decreasesAbundanceOf).append(affectsSynthesisOf, rhs.affectsSynthesisOf).append(affectsDegradationOf, rhs.affectsDegradationOf).append(affectsSplicingOf, rhs.affectsSplicingOf).append(affectsMolecularModificationOf, rhs.affectsMolecularModificationOf).append(decreasesMolecularModificationOf, rhs.decreasesMolecularModificationOf).append(increasesTransportOf, rhs.increasesTransportOf).append(increasesSynthesisOf, rhs.increasesSynthesisOf).append(increasesResponseTo, rhs.increasesResponseTo).append(increasesActivityOf, rhs.increasesActivityOf).append(regulatesEntityToEntity, rhs.regulatesEntityToEntity).append(positivelyRegulatesEntityToEntity, rhs.positivelyRegulatesEntityToEntity).isEquals();
    }

}
