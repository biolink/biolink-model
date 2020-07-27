import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


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
    "decreases_molecular_interaction",
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
    "increases_molecular_interaction",
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
     * indicates that the source decreases the molecular interaction between the target and some other molecular entity
     * 
     */
    @JsonProperty("decreases_molecular_interaction")
    @JsonPropertyDescription("indicates that the source decreases the molecular interaction between the target and some other molecular entity")
    private List<String> decreasesMolecularInteraction = new ArrayList<String>();
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
     * indicates that the source increases the molecular interaction between the target and some other molecular entity
     * 
     */
    @JsonProperty("increases_molecular_interaction")
    @JsonPropertyDescription("indicates that the source increases the molecular interaction between the target and some other molecular entity")
    private List<String> increasesMolecularInteraction = new ArrayList<String>();
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
     * indicates that the source decreases the molecular interaction between the target and some other molecular entity
     * 
     */
    @JsonProperty("decreases_molecular_interaction")
    public List<String> getDecreasesMolecularInteraction() {
        return decreasesMolecularInteraction;
    }

    /**
     * indicates that the source decreases the molecular interaction between the target and some other molecular entity
     * 
     */
    @JsonProperty("decreases_molecular_interaction")
    public void setDecreasesMolecularInteraction(List<String> decreasesMolecularInteraction) {
        this.decreasesMolecularInteraction = decreasesMolecularInteraction;
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
     * indicates that the source increases the molecular interaction between the target and some other molecular entity
     * 
     */
    @JsonProperty("increases_molecular_interaction")
    public List<String> getIncreasesMolecularInteraction() {
        return increasesMolecularInteraction;
    }

    /**
     * indicates that the source increases the molecular interaction between the target and some other molecular entity
     * 
     */
    @JsonProperty("increases_molecular_interaction")
    public void setIncreasesMolecularInteraction(List<String> increasesMolecularInteraction) {
        this.increasesMolecularInteraction = increasesMolecularInteraction;
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
        StringBuilder sb = new StringBuilder();
        sb.append(MolecularEntity.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("affectsAbundanceOf");
        sb.append('=');
        sb.append(((this.affectsAbundanceOf == null)?"<null>":this.affectsAbundanceOf));
        sb.append(',');
        sb.append("affectsActivityOf");
        sb.append('=');
        sb.append(((this.affectsActivityOf == null)?"<null>":this.affectsActivityOf));
        sb.append(',');
        sb.append("affectsDegradationOf");
        sb.append('=');
        sb.append(((this.affectsDegradationOf == null)?"<null>":this.affectsDegradationOf));
        sb.append(',');
        sb.append("affectsExpressionOf");
        sb.append('=');
        sb.append(((this.affectsExpressionOf == null)?"<null>":this.affectsExpressionOf));
        sb.append(',');
        sb.append("affectsFoldingOf");
        sb.append('=');
        sb.append(((this.affectsFoldingOf == null)?"<null>":this.affectsFoldingOf));
        sb.append(',');
        sb.append("affectsLocalizationOf");
        sb.append('=');
        sb.append(((this.affectsLocalizationOf == null)?"<null>":this.affectsLocalizationOf));
        sb.append(',');
        sb.append("affectsMetabolicProcessingOf");
        sb.append('=');
        sb.append(((this.affectsMetabolicProcessingOf == null)?"<null>":this.affectsMetabolicProcessingOf));
        sb.append(',');
        sb.append("affectsMolecularModificationOf");
        sb.append('=');
        sb.append(((this.affectsMolecularModificationOf == null)?"<null>":this.affectsMolecularModificationOf));
        sb.append(',');
        sb.append("affectsMutationRateOf");
        sb.append('=');
        sb.append(((this.affectsMutationRateOf == null)?"<null>":this.affectsMutationRateOf));
        sb.append(',');
        sb.append("affectsResponseTo");
        sb.append('=');
        sb.append(((this.affectsResponseTo == null)?"<null>":this.affectsResponseTo));
        sb.append(',');
        sb.append("affectsSecretionOf");
        sb.append('=');
        sb.append(((this.affectsSecretionOf == null)?"<null>":this.affectsSecretionOf));
        sb.append(',');
        sb.append("affectsSplicingOf");
        sb.append('=');
        sb.append(((this.affectsSplicingOf == null)?"<null>":this.affectsSplicingOf));
        sb.append(',');
        sb.append("affectsStabilityOf");
        sb.append('=');
        sb.append(((this.affectsStabilityOf == null)?"<null>":this.affectsStabilityOf));
        sb.append(',');
        sb.append("affectsSynthesisOf");
        sb.append('=');
        sb.append(((this.affectsSynthesisOf == null)?"<null>":this.affectsSynthesisOf));
        sb.append(',');
        sb.append("affectsTransportOf");
        sb.append('=');
        sb.append(((this.affectsTransportOf == null)?"<null>":this.affectsTransportOf));
        sb.append(',');
        sb.append("affectsUptakeOf");
        sb.append('=');
        sb.append(((this.affectsUptakeOf == null)?"<null>":this.affectsUptakeOf));
        sb.append(',');
        sb.append("biomarkerFor");
        sb.append('=');
        sb.append(((this.biomarkerFor == null)?"<null>":this.biomarkerFor));
        sb.append(',');
        sb.append("decreasesAbundanceOf");
        sb.append('=');
        sb.append(((this.decreasesAbundanceOf == null)?"<null>":this.decreasesAbundanceOf));
        sb.append(',');
        sb.append("decreasesActivityOf");
        sb.append('=');
        sb.append(((this.decreasesActivityOf == null)?"<null>":this.decreasesActivityOf));
        sb.append(',');
        sb.append("decreasesDegradationOf");
        sb.append('=');
        sb.append(((this.decreasesDegradationOf == null)?"<null>":this.decreasesDegradationOf));
        sb.append(',');
        sb.append("decreasesExpressionOf");
        sb.append('=');
        sb.append(((this.decreasesExpressionOf == null)?"<null>":this.decreasesExpressionOf));
        sb.append(',');
        sb.append("decreasesFoldingOf");
        sb.append('=');
        sb.append(((this.decreasesFoldingOf == null)?"<null>":this.decreasesFoldingOf));
        sb.append(',');
        sb.append("decreasesLocalizationOf");
        sb.append('=');
        sb.append(((this.decreasesLocalizationOf == null)?"<null>":this.decreasesLocalizationOf));
        sb.append(',');
        sb.append("decreasesMetabolicProcessingOf");
        sb.append('=');
        sb.append(((this.decreasesMetabolicProcessingOf == null)?"<null>":this.decreasesMetabolicProcessingOf));
        sb.append(',');
        sb.append("decreasesMolecularInteraction");
        sb.append('=');
        sb.append(((this.decreasesMolecularInteraction == null)?"<null>":this.decreasesMolecularInteraction));
        sb.append(',');
        sb.append("decreasesMolecularModificationOf");
        sb.append('=');
        sb.append(((this.decreasesMolecularModificationOf == null)?"<null>":this.decreasesMolecularModificationOf));
        sb.append(',');
        sb.append("decreasesMutationRateOf");
        sb.append('=');
        sb.append(((this.decreasesMutationRateOf == null)?"<null>":this.decreasesMutationRateOf));
        sb.append(',');
        sb.append("decreasesResponseTo");
        sb.append('=');
        sb.append(((this.decreasesResponseTo == null)?"<null>":this.decreasesResponseTo));
        sb.append(',');
        sb.append("decreasesSecretionOf");
        sb.append('=');
        sb.append(((this.decreasesSecretionOf == null)?"<null>":this.decreasesSecretionOf));
        sb.append(',');
        sb.append("decreasesSplicingOf");
        sb.append('=');
        sb.append(((this.decreasesSplicingOf == null)?"<null>":this.decreasesSplicingOf));
        sb.append(',');
        sb.append("decreasesStabilityOf");
        sb.append('=');
        sb.append(((this.decreasesStabilityOf == null)?"<null>":this.decreasesStabilityOf));
        sb.append(',');
        sb.append("decreasesSynthesisOf");
        sb.append('=');
        sb.append(((this.decreasesSynthesisOf == null)?"<null>":this.decreasesSynthesisOf));
        sb.append(',');
        sb.append("decreasesTransportOf");
        sb.append('=');
        sb.append(((this.decreasesTransportOf == null)?"<null>":this.decreasesTransportOf));
        sb.append(',');
        sb.append("decreasesUptakeOf");
        sb.append('=');
        sb.append(((this.decreasesUptakeOf == null)?"<null>":this.decreasesUptakeOf));
        sb.append(',');
        sb.append("inTaxon");
        sb.append('=');
        sb.append(((this.inTaxon == null)?"<null>":this.inTaxon));
        sb.append(',');
        sb.append("increasesAbundanceOf");
        sb.append('=');
        sb.append(((this.increasesAbundanceOf == null)?"<null>":this.increasesAbundanceOf));
        sb.append(',');
        sb.append("increasesActivityOf");
        sb.append('=');
        sb.append(((this.increasesActivityOf == null)?"<null>":this.increasesActivityOf));
        sb.append(',');
        sb.append("increasesDegradationOf");
        sb.append('=');
        sb.append(((this.increasesDegradationOf == null)?"<null>":this.increasesDegradationOf));
        sb.append(',');
        sb.append("increasesExpressionOf");
        sb.append('=');
        sb.append(((this.increasesExpressionOf == null)?"<null>":this.increasesExpressionOf));
        sb.append(',');
        sb.append("increasesFoldingOf");
        sb.append('=');
        sb.append(((this.increasesFoldingOf == null)?"<null>":this.increasesFoldingOf));
        sb.append(',');
        sb.append("increasesLocalizationOf");
        sb.append('=');
        sb.append(((this.increasesLocalizationOf == null)?"<null>":this.increasesLocalizationOf));
        sb.append(',');
        sb.append("increasesMetabolicProcessingOf");
        sb.append('=');
        sb.append(((this.increasesMetabolicProcessingOf == null)?"<null>":this.increasesMetabolicProcessingOf));
        sb.append(',');
        sb.append("increasesMolecularInteraction");
        sb.append('=');
        sb.append(((this.increasesMolecularInteraction == null)?"<null>":this.increasesMolecularInteraction));
        sb.append(',');
        sb.append("increasesMolecularModificationOf");
        sb.append('=');
        sb.append(((this.increasesMolecularModificationOf == null)?"<null>":this.increasesMolecularModificationOf));
        sb.append(',');
        sb.append("increasesMutationRateOf");
        sb.append('=');
        sb.append(((this.increasesMutationRateOf == null)?"<null>":this.increasesMutationRateOf));
        sb.append(',');
        sb.append("increasesResponseTo");
        sb.append('=');
        sb.append(((this.increasesResponseTo == null)?"<null>":this.increasesResponseTo));
        sb.append(',');
        sb.append("increasesSecretionOf");
        sb.append('=');
        sb.append(((this.increasesSecretionOf == null)?"<null>":this.increasesSecretionOf));
        sb.append(',');
        sb.append("increasesSplicingOf");
        sb.append('=');
        sb.append(((this.increasesSplicingOf == null)?"<null>":this.increasesSplicingOf));
        sb.append(',');
        sb.append("increasesStabilityOf");
        sb.append('=');
        sb.append(((this.increasesStabilityOf == null)?"<null>":this.increasesStabilityOf));
        sb.append(',');
        sb.append("increasesSynthesisOf");
        sb.append('=');
        sb.append(((this.increasesSynthesisOf == null)?"<null>":this.increasesSynthesisOf));
        sb.append(',');
        sb.append("increasesTransportOf");
        sb.append('=');
        sb.append(((this.increasesTransportOf == null)?"<null>":this.increasesTransportOf));
        sb.append(',');
        sb.append("increasesUptakeOf");
        sb.append('=');
        sb.append(((this.increasesUptakeOf == null)?"<null>":this.increasesUptakeOf));
        sb.append(',');
        sb.append("molecularlyInteractsWith");
        sb.append('=');
        sb.append(((this.molecularlyInteractsWith == null)?"<null>":this.molecularlyInteractsWith));
        sb.append(',');
        sb.append("negativelyRegulatesEntityToEntity");
        sb.append('=');
        sb.append(((this.negativelyRegulatesEntityToEntity == null)?"<null>":this.negativelyRegulatesEntityToEntity));
        sb.append(',');
        sb.append("positivelyRegulatesEntityToEntity");
        sb.append('=');
        sb.append(((this.positivelyRegulatesEntityToEntity == null)?"<null>":this.positivelyRegulatesEntityToEntity));
        sb.append(',');
        sb.append("regulatesEntityToEntity");
        sb.append('=');
        sb.append(((this.regulatesEntityToEntity == null)?"<null>":this.regulatesEntityToEntity));
        sb.append(',');
        if (sb.charAt((sb.length()- 1)) == ',') {
            sb.setCharAt((sb.length()- 1), ']');
        } else {
            sb.append(']');
        }
        return sb.toString();
    }

    @Override
    public int hashCode() {
        int result = 1;
        result = ((result* 31)+((this.affectsMetabolicProcessingOf == null)? 0 :this.affectsMetabolicProcessingOf.hashCode()));
        result = ((result* 31)+((this.decreasesFoldingOf == null)? 0 :this.decreasesFoldingOf.hashCode()));
        result = ((result* 31)+((this.increasesSecretionOf == null)? 0 :this.increasesSecretionOf.hashCode()));
        result = ((result* 31)+((this.decreasesLocalizationOf == null)? 0 :this.decreasesLocalizationOf.hashCode()));
        result = ((result* 31)+((this.affectsUptakeOf == null)? 0 :this.affectsUptakeOf.hashCode()));
        result = ((result* 31)+((this.decreasesResponseTo == null)? 0 :this.decreasesResponseTo.hashCode()));
        result = ((result* 31)+((this.decreasesTransportOf == null)? 0 :this.decreasesTransportOf.hashCode()));
        result = ((result* 31)+((this.molecularlyInteractsWith == null)? 0 :this.molecularlyInteractsWith.hashCode()));
        result = ((result* 31)+((this.decreasesExpressionOf == null)? 0 :this.decreasesExpressionOf.hashCode()));
        result = ((result* 31)+((this.increasesStabilityOf == null)? 0 :this.increasesStabilityOf.hashCode()));
        result = ((result* 31)+((this.decreasesSecretionOf == null)? 0 :this.decreasesSecretionOf.hashCode()));
        result = ((result* 31)+((this.decreasesStabilityOf == null)? 0 :this.decreasesStabilityOf.hashCode()));
        result = ((result* 31)+((this.increasesAbundanceOf == null)? 0 :this.increasesAbundanceOf.hashCode()));
        result = ((result* 31)+((this.increasesMutationRateOf == null)? 0 :this.increasesMutationRateOf.hashCode()));
        result = ((result* 31)+((this.affectsMutationRateOf == null)? 0 :this.affectsMutationRateOf.hashCode()));
        result = ((result* 31)+((this.increasesExpressionOf == null)? 0 :this.increasesExpressionOf.hashCode()));
        result = ((result* 31)+((this.affectsLocalizationOf == null)? 0 :this.affectsLocalizationOf.hashCode()));
        result = ((result* 31)+((this.affectsAbundanceOf == null)? 0 :this.affectsAbundanceOf.hashCode()));
        result = ((result* 31)+((this.increasesMolecularModificationOf == null)? 0 :this.increasesMolecularModificationOf.hashCode()));
        result = ((result* 31)+((this.decreasesDegradationOf == null)? 0 :this.decreasesDegradationOf.hashCode()));
        result = ((result* 31)+((this.increasesFoldingOf == null)? 0 :this.increasesFoldingOf.hashCode()));
        result = ((result* 31)+((this.decreasesMutationRateOf == null)? 0 :this.decreasesMutationRateOf.hashCode()));
        result = ((result* 31)+((this.decreasesSynthesisOf == null)? 0 :this.decreasesSynthesisOf.hashCode()));
        result = ((result* 31)+((this.affectsFoldingOf == null)? 0 :this.affectsFoldingOf.hashCode()));
        result = ((result* 31)+((this.decreasesUptakeOf == null)? 0 :this.decreasesUptakeOf.hashCode()));
        result = ((result* 31)+((this.increasesMetabolicProcessingOf == null)? 0 :this.increasesMetabolicProcessingOf.hashCode()));
        result = ((result* 31)+((this.increasesMolecularInteraction == null)? 0 :this.increasesMolecularInteraction.hashCode()));
        result = ((result* 31)+((this.decreasesActivityOf == null)? 0 :this.decreasesActivityOf.hashCode()));
        result = ((result* 31)+((this.affectsSecretionOf == null)? 0 :this.affectsSecretionOf.hashCode()));
        result = ((result* 31)+((this.decreasesSplicingOf == null)? 0 :this.decreasesSplicingOf.hashCode()));
        result = ((result* 31)+((this.decreasesMetabolicProcessingOf == null)? 0 :this.decreasesMetabolicProcessingOf.hashCode()));
        result = ((result* 31)+((this.increasesUptakeOf == null)? 0 :this.increasesUptakeOf.hashCode()));
        result = ((result* 31)+((this.negativelyRegulatesEntityToEntity == null)? 0 :this.negativelyRegulatesEntityToEntity.hashCode()));
        result = ((result* 31)+((this.inTaxon == null)? 0 :this.inTaxon.hashCode()));
        result = ((result* 31)+((this.affectsActivityOf == null)? 0 :this.affectsActivityOf.hashCode()));
        result = ((result* 31)+((this.affectsStabilityOf == null)? 0 :this.affectsStabilityOf.hashCode()));
        result = ((result* 31)+((this.increasesSplicingOf == null)? 0 :this.increasesSplicingOf.hashCode()));
        result = ((result* 31)+((this.biomarkerFor == null)? 0 :this.biomarkerFor.hashCode()));
        result = ((result* 31)+((this.increasesLocalizationOf == null)? 0 :this.increasesLocalizationOf.hashCode()));
        result = ((result* 31)+((this.increasesDegradationOf == null)? 0 :this.increasesDegradationOf.hashCode()));
        result = ((result* 31)+((this.affectsResponseTo == null)? 0 :this.affectsResponseTo.hashCode()));
        result = ((result* 31)+((this.decreasesMolecularInteraction == null)? 0 :this.decreasesMolecularInteraction.hashCode()));
        result = ((result* 31)+((this.affectsExpressionOf == null)? 0 :this.affectsExpressionOf.hashCode()));
        result = ((result* 31)+((this.affectsTransportOf == null)? 0 :this.affectsTransportOf.hashCode()));
        result = ((result* 31)+((this.decreasesAbundanceOf == null)? 0 :this.decreasesAbundanceOf.hashCode()));
        result = ((result* 31)+((this.affectsSynthesisOf == null)? 0 :this.affectsSynthesisOf.hashCode()));
        result = ((result* 31)+((this.affectsDegradationOf == null)? 0 :this.affectsDegradationOf.hashCode()));
        result = ((result* 31)+((this.affectsSplicingOf == null)? 0 :this.affectsSplicingOf.hashCode()));
        result = ((result* 31)+((this.affectsMolecularModificationOf == null)? 0 :this.affectsMolecularModificationOf.hashCode()));
        result = ((result* 31)+((this.decreasesMolecularModificationOf == null)? 0 :this.decreasesMolecularModificationOf.hashCode()));
        result = ((result* 31)+((this.increasesTransportOf == null)? 0 :this.increasesTransportOf.hashCode()));
        result = ((result* 31)+((this.increasesSynthesisOf == null)? 0 :this.increasesSynthesisOf.hashCode()));
        result = ((result* 31)+((this.increasesResponseTo == null)? 0 :this.increasesResponseTo.hashCode()));
        result = ((result* 31)+((this.increasesActivityOf == null)? 0 :this.increasesActivityOf.hashCode()));
        result = ((result* 31)+((this.regulatesEntityToEntity == null)? 0 :this.regulatesEntityToEntity.hashCode()));
        result = ((result* 31)+((this.positivelyRegulatesEntityToEntity == null)? 0 :this.positivelyRegulatesEntityToEntity.hashCode()));
        return result;
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
        return (((((((((((((((((((((((((((((((((((((((((((((((((((((((((this.affectsMetabolicProcessingOf == rhs.affectsMetabolicProcessingOf)||((this.affectsMetabolicProcessingOf!= null)&&this.affectsMetabolicProcessingOf.equals(rhs.affectsMetabolicProcessingOf)))&&((this.decreasesFoldingOf == rhs.decreasesFoldingOf)||((this.decreasesFoldingOf!= null)&&this.decreasesFoldingOf.equals(rhs.decreasesFoldingOf))))&&((this.increasesSecretionOf == rhs.increasesSecretionOf)||((this.increasesSecretionOf!= null)&&this.increasesSecretionOf.equals(rhs.increasesSecretionOf))))&&((this.decreasesLocalizationOf == rhs.decreasesLocalizationOf)||((this.decreasesLocalizationOf!= null)&&this.decreasesLocalizationOf.equals(rhs.decreasesLocalizationOf))))&&((this.affectsUptakeOf == rhs.affectsUptakeOf)||((this.affectsUptakeOf!= null)&&this.affectsUptakeOf.equals(rhs.affectsUptakeOf))))&&((this.decreasesResponseTo == rhs.decreasesResponseTo)||((this.decreasesResponseTo!= null)&&this.decreasesResponseTo.equals(rhs.decreasesResponseTo))))&&((this.decreasesTransportOf == rhs.decreasesTransportOf)||((this.decreasesTransportOf!= null)&&this.decreasesTransportOf.equals(rhs.decreasesTransportOf))))&&((this.molecularlyInteractsWith == rhs.molecularlyInteractsWith)||((this.molecularlyInteractsWith!= null)&&this.molecularlyInteractsWith.equals(rhs.molecularlyInteractsWith))))&&((this.decreasesExpressionOf == rhs.decreasesExpressionOf)||((this.decreasesExpressionOf!= null)&&this.decreasesExpressionOf.equals(rhs.decreasesExpressionOf))))&&((this.increasesStabilityOf == rhs.increasesStabilityOf)||((this.increasesStabilityOf!= null)&&this.increasesStabilityOf.equals(rhs.increasesStabilityOf))))&&((this.decreasesSecretionOf == rhs.decreasesSecretionOf)||((this.decreasesSecretionOf!= null)&&this.decreasesSecretionOf.equals(rhs.decreasesSecretionOf))))&&((this.decreasesStabilityOf == rhs.decreasesStabilityOf)||((this.decreasesStabilityOf!= null)&&this.decreasesStabilityOf.equals(rhs.decreasesStabilityOf))))&&((this.increasesAbundanceOf == rhs.increasesAbundanceOf)||((this.increasesAbundanceOf!= null)&&this.increasesAbundanceOf.equals(rhs.increasesAbundanceOf))))&&((this.increasesMutationRateOf == rhs.increasesMutationRateOf)||((this.increasesMutationRateOf!= null)&&this.increasesMutationRateOf.equals(rhs.increasesMutationRateOf))))&&((this.affectsMutationRateOf == rhs.affectsMutationRateOf)||((this.affectsMutationRateOf!= null)&&this.affectsMutationRateOf.equals(rhs.affectsMutationRateOf))))&&((this.increasesExpressionOf == rhs.increasesExpressionOf)||((this.increasesExpressionOf!= null)&&this.increasesExpressionOf.equals(rhs.increasesExpressionOf))))&&((this.affectsLocalizationOf == rhs.affectsLocalizationOf)||((this.affectsLocalizationOf!= null)&&this.affectsLocalizationOf.equals(rhs.affectsLocalizationOf))))&&((this.affectsAbundanceOf == rhs.affectsAbundanceOf)||((this.affectsAbundanceOf!= null)&&this.affectsAbundanceOf.equals(rhs.affectsAbundanceOf))))&&((this.increasesMolecularModificationOf == rhs.increasesMolecularModificationOf)||((this.increasesMolecularModificationOf!= null)&&this.increasesMolecularModificationOf.equals(rhs.increasesMolecularModificationOf))))&&((this.decreasesDegradationOf == rhs.decreasesDegradationOf)||((this.decreasesDegradationOf!= null)&&this.decreasesDegradationOf.equals(rhs.decreasesDegradationOf))))&&((this.increasesFoldingOf == rhs.increasesFoldingOf)||((this.increasesFoldingOf!= null)&&this.increasesFoldingOf.equals(rhs.increasesFoldingOf))))&&((this.decreasesMutationRateOf == rhs.decreasesMutationRateOf)||((this.decreasesMutationRateOf!= null)&&this.decreasesMutationRateOf.equals(rhs.decreasesMutationRateOf))))&&((this.decreasesSynthesisOf == rhs.decreasesSynthesisOf)||((this.decreasesSynthesisOf!= null)&&this.decreasesSynthesisOf.equals(rhs.decreasesSynthesisOf))))&&((this.affectsFoldingOf == rhs.affectsFoldingOf)||((this.affectsFoldingOf!= null)&&this.affectsFoldingOf.equals(rhs.affectsFoldingOf))))&&((this.decreasesUptakeOf == rhs.decreasesUptakeOf)||((this.decreasesUptakeOf!= null)&&this.decreasesUptakeOf.equals(rhs.decreasesUptakeOf))))&&((this.increasesMetabolicProcessingOf == rhs.increasesMetabolicProcessingOf)||((this.increasesMetabolicProcessingOf!= null)&&this.increasesMetabolicProcessingOf.equals(rhs.increasesMetabolicProcessingOf))))&&((this.increasesMolecularInteraction == rhs.increasesMolecularInteraction)||((this.increasesMolecularInteraction!= null)&&this.increasesMolecularInteraction.equals(rhs.increasesMolecularInteraction))))&&((this.decreasesActivityOf == rhs.decreasesActivityOf)||((this.decreasesActivityOf!= null)&&this.decreasesActivityOf.equals(rhs.decreasesActivityOf))))&&((this.affectsSecretionOf == rhs.affectsSecretionOf)||((this.affectsSecretionOf!= null)&&this.affectsSecretionOf.equals(rhs.affectsSecretionOf))))&&((this.decreasesSplicingOf == rhs.decreasesSplicingOf)||((this.decreasesSplicingOf!= null)&&this.decreasesSplicingOf.equals(rhs.decreasesSplicingOf))))&&((this.decreasesMetabolicProcessingOf == rhs.decreasesMetabolicProcessingOf)||((this.decreasesMetabolicProcessingOf!= null)&&this.decreasesMetabolicProcessingOf.equals(rhs.decreasesMetabolicProcessingOf))))&&((this.increasesUptakeOf == rhs.increasesUptakeOf)||((this.increasesUptakeOf!= null)&&this.increasesUptakeOf.equals(rhs.increasesUptakeOf))))&&((this.negativelyRegulatesEntityToEntity == rhs.negativelyRegulatesEntityToEntity)||((this.negativelyRegulatesEntityToEntity!= null)&&this.negativelyRegulatesEntityToEntity.equals(rhs.negativelyRegulatesEntityToEntity))))&&((this.inTaxon == rhs.inTaxon)||((this.inTaxon!= null)&&this.inTaxon.equals(rhs.inTaxon))))&&((this.affectsActivityOf == rhs.affectsActivityOf)||((this.affectsActivityOf!= null)&&this.affectsActivityOf.equals(rhs.affectsActivityOf))))&&((this.affectsStabilityOf == rhs.affectsStabilityOf)||((this.affectsStabilityOf!= null)&&this.affectsStabilityOf.equals(rhs.affectsStabilityOf))))&&((this.increasesSplicingOf == rhs.increasesSplicingOf)||((this.increasesSplicingOf!= null)&&this.increasesSplicingOf.equals(rhs.increasesSplicingOf))))&&((this.biomarkerFor == rhs.biomarkerFor)||((this.biomarkerFor!= null)&&this.biomarkerFor.equals(rhs.biomarkerFor))))&&((this.increasesLocalizationOf == rhs.increasesLocalizationOf)||((this.increasesLocalizationOf!= null)&&this.increasesLocalizationOf.equals(rhs.increasesLocalizationOf))))&&((this.increasesDegradationOf == rhs.increasesDegradationOf)||((this.increasesDegradationOf!= null)&&this.increasesDegradationOf.equals(rhs.increasesDegradationOf))))&&((this.affectsResponseTo == rhs.affectsResponseTo)||((this.affectsResponseTo!= null)&&this.affectsResponseTo.equals(rhs.affectsResponseTo))))&&((this.decreasesMolecularInteraction == rhs.decreasesMolecularInteraction)||((this.decreasesMolecularInteraction!= null)&&this.decreasesMolecularInteraction.equals(rhs.decreasesMolecularInteraction))))&&((this.affectsExpressionOf == rhs.affectsExpressionOf)||((this.affectsExpressionOf!= null)&&this.affectsExpressionOf.equals(rhs.affectsExpressionOf))))&&((this.affectsTransportOf == rhs.affectsTransportOf)||((this.affectsTransportOf!= null)&&this.affectsTransportOf.equals(rhs.affectsTransportOf))))&&((this.decreasesAbundanceOf == rhs.decreasesAbundanceOf)||((this.decreasesAbundanceOf!= null)&&this.decreasesAbundanceOf.equals(rhs.decreasesAbundanceOf))))&&((this.affectsSynthesisOf == rhs.affectsSynthesisOf)||((this.affectsSynthesisOf!= null)&&this.affectsSynthesisOf.equals(rhs.affectsSynthesisOf))))&&((this.affectsDegradationOf == rhs.affectsDegradationOf)||((this.affectsDegradationOf!= null)&&this.affectsDegradationOf.equals(rhs.affectsDegradationOf))))&&((this.affectsSplicingOf == rhs.affectsSplicingOf)||((this.affectsSplicingOf!= null)&&this.affectsSplicingOf.equals(rhs.affectsSplicingOf))))&&((this.affectsMolecularModificationOf == rhs.affectsMolecularModificationOf)||((this.affectsMolecularModificationOf!= null)&&this.affectsMolecularModificationOf.equals(rhs.affectsMolecularModificationOf))))&&((this.decreasesMolecularModificationOf == rhs.decreasesMolecularModificationOf)||((this.decreasesMolecularModificationOf!= null)&&this.decreasesMolecularModificationOf.equals(rhs.decreasesMolecularModificationOf))))&&((this.increasesTransportOf == rhs.increasesTransportOf)||((this.increasesTransportOf!= null)&&this.increasesTransportOf.equals(rhs.increasesTransportOf))))&&((this.increasesSynthesisOf == rhs.increasesSynthesisOf)||((this.increasesSynthesisOf!= null)&&this.increasesSynthesisOf.equals(rhs.increasesSynthesisOf))))&&((this.increasesResponseTo == rhs.increasesResponseTo)||((this.increasesResponseTo!= null)&&this.increasesResponseTo.equals(rhs.increasesResponseTo))))&&((this.increasesActivityOf == rhs.increasesActivityOf)||((this.increasesActivityOf!= null)&&this.increasesActivityOf.equals(rhs.increasesActivityOf))))&&((this.regulatesEntityToEntity == rhs.regulatesEntityToEntity)||((this.regulatesEntityToEntity!= null)&&this.regulatesEntityToEntity.equals(rhs.regulatesEntityToEntity))))&&((this.positivelyRegulatesEntityToEntity == rhs.positivelyRegulatesEntityToEntity)||((this.positivelyRegulatesEntityToEntity!= null)&&this.positivelyRegulatesEntityToEntity.equals(rhs.positivelyRegulatesEntityToEntity))));
    }

}
