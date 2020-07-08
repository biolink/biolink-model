import java.util.ArrayList;
import java.util.List;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * NamedThing
 * <p>
 * a databased entity or concept/class
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "actively_involved_in",
    "affects",
    "affects_risk_for",
    "aggregate_statistic",
    "capable_of",
    "category",
    "caused_by",
    "causes",
    "coexists_with",
    "colocalizes_with",
    "contributes_to",
    "correlated_with",
    "creation_date",
    "derives_from",
    "derives_into",
    "description",
    "disrupts",
    "end_interbase_coordinate",
    "filler",
    "full_name",
    "genome_build",
    "has_biological_sequence",
    "has_chemical_formula",
    "has_count",
    "has_drug",
    "has_gene",
    "has_molecular_consequence",
    "has_part",
    "has_percentage",
    "has_quotient",
    "has_total",
    "has_zygosity",
    "homologous_to",
    "id",
    "interacts_with",
    "interbase_coordinate",
    "iri",
    "latitude",
    "located_in",
    "location_of",
    "longitude",
    "manifestation_of",
    "model_of",
    "name",
    "negatively_regulates",
    "node_property",
    "occurs_in",
    "orthologous_to",
    "overlaps",
    "paralogous_to",
    "part_of",
    "participates_in",
    "phase",
    "physically_interacts_with",
    "positively_regulates",
    "predisposes",
    "prevents",
    "produces",
    "regulates",
    "related_to",
    "same_as",
    "start_interbase_coordinate",
    "synonym",
    "systematic_synonym",
    "timepoint",
    "type",
    "update_date",
    "xenologous_to"
})
public class NamedThing {

    /**
     * holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
     * 
     */
    @JsonProperty("actively_involved_in")
    @JsonPropertyDescription("holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes")
    private List<String> activelyInvolvedIn = new ArrayList<String>();
    /**
     * describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
     * 
     */
    @JsonProperty("affects")
    @JsonPropertyDescription("describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.")
    private List<String> affects = new ArrayList<String>();
    /**
     * holds between two entities where exposure to one entity alters the chance of developing the other
     * 
     */
    @JsonProperty("affects_risk_for")
    @JsonPropertyDescription("holds between two entities where exposure to one entity alters the chance of developing the other")
    private List<String> affectsRiskFor = new ArrayList<String>();
    @JsonProperty("aggregate_statistic")
    private String aggregateStatistic;
    /**
     * holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.
     * 
     */
    @JsonProperty("capable_of")
    @JsonPropertyDescription("holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.")
    private List<String> capableOf = new ArrayList<String>();
    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * (Required)
     * 
     */
    @JsonProperty("category")
    @JsonPropertyDescription("Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag")
    private List<String> category = new ArrayList<String>();
    /**
     * holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or  generation of the other
     * 
     */
    @JsonProperty("caused_by")
    @JsonPropertyDescription("holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or  generation of the other")
    private List<String> causedBy = new ArrayList<String>();
    /**
     * holds between two entities where the occurrence, existence, or activity of one causes the occurrence or  generation of the other
     * 
     */
    @JsonProperty("causes")
    @JsonPropertyDescription("holds between two entities where the occurrence, existence, or activity of one causes the occurrence or  generation of the other")
    private List<String> causes = new ArrayList<String>();
    /**
     * holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
     * 
     */
    @JsonProperty("coexists_with")
    @JsonPropertyDescription("holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region")
    private List<String> coexistsWith = new ArrayList<String>();
    /**
     * holds between two entities that are observed to be located in the same place.
     * 
     */
    @JsonProperty("colocalizes_with")
    @JsonPropertyDescription("holds between two entities that are observed to be located in the same place.")
    private List<String> colocalizesWith = new ArrayList<String>();
    /**
     * holds between two entities where the occurrence, existence, or activity of one causes or contributes to the occurrence or generation of the other
     * 
     */
    @JsonProperty("contributes_to")
    @JsonPropertyDescription("holds between two entities where the occurrence, existence, or activity of one causes or contributes to the occurrence or generation of the other")
    private List<String> contributesTo = new ArrayList<String>();
    /**
     * holds between any two named thing entities. For example, correlated_with holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("correlated_with")
    @JsonPropertyDescription("holds between any two named thing entities. For example, correlated_with holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.")
    private List<String> correlatedWith = new ArrayList<String>();
    /**
     * date on which thing was created. This can be applied to nodes or edges
     * 
     */
    @JsonProperty("creation_date")
    @JsonPropertyDescription("date on which thing was created. This can be applied to nodes or edges")
    private String creationDate;
    /**
     * holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
     * 
     */
    @JsonProperty("derives_from")
    @JsonPropertyDescription("holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity")
    private List<String> derivesFrom = new ArrayList<String>();
    /**
     * holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
     * 
     */
    @JsonProperty("derives_into")
    @JsonPropertyDescription("holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity")
    private List<String> derivesInto = new ArrayList<String>();
    /**
     * a human-readable description of a thing
     * 
     */
    @JsonProperty("description")
    @JsonPropertyDescription("a human-readable description of a thing")
    private String description;
    /**
     * describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
     * 
     */
    @JsonProperty("disrupts")
    @JsonPropertyDescription("describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.")
    private List<String> disrupts = new ArrayList<String>();
    @JsonProperty("end_interbase_coordinate")
    private String endInterbaseCoordinate;
    /**
     * The value in a property-value tuple
     * 
     */
    @JsonProperty("filler")
    @JsonPropertyDescription("The value in a property-value tuple")
    private String filler;
    /**
     * a long-form human readable name for a thing
     * 
     */
    @JsonProperty("full_name")
    @JsonPropertyDescription("a long-form human readable name for a thing")
    private String fullName;
    /**
     * TODO
     * 
     */
    @JsonProperty("genome_build")
    @JsonPropertyDescription("TODO")
    private String genomeBuild;
    /**
     * connects a genomic feature to its sequence
     * 
     */
    @JsonProperty("has_biological_sequence")
    @JsonPropertyDescription("connects a genomic feature to its sequence")
    private String hasBiologicalSequence;
    /**
     * description of chemical compound based on element symbols
     * 
     */
    @JsonProperty("has_chemical_formula")
    @JsonPropertyDescription("description of chemical compound based on element symbols")
    private String hasChemicalFormula;
    /**
     * number of things with a particular property
     * 
     */
    @JsonProperty("has_count")
    @JsonPropertyDescription("number of things with a particular property")
    private String hasCount;
    /**
     * connects an entity to a single drug
     * 
     */
    @JsonProperty("has_drug")
    @JsonPropertyDescription("connects an entity to a single drug")
    private String hasDrug;
    /**
     * connects an entity to a single gene
     * 
     */
    @JsonProperty("has_gene")
    @JsonPropertyDescription("connects an entity to a single gene")
    private String hasGene;
    /**
     * connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583
     * 
     */
    @JsonProperty("has_molecular_consequence")
    @JsonPropertyDescription("connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583")
    private List<String> hasMolecularConsequence = new ArrayList<String>();
    /**
     * holds between wholes and their parts (material entities or processes)
     * 
     */
    @JsonProperty("has_part")
    @JsonPropertyDescription("holds between wholes and their parts (material entities or processes)")
    private List<String> hasPart = new ArrayList<String>();
    /**
     * equivalent to has quotient multiplied by 100
     * 
     */
    @JsonProperty("has_percentage")
    @JsonPropertyDescription("equivalent to has quotient multiplied by 100")
    private String hasPercentage;
    @JsonProperty("has_quotient")
    private String hasQuotient;
    /**
     * total number of things in a particular reference set
     * 
     */
    @JsonProperty("has_total")
    @JsonPropertyDescription("total number of things in a particular reference set")
    private String hasTotal;
    @JsonProperty("has_zygosity")
    private String hasZygosity;
    /**
     * holds between two biological entities that have common evolutionary origin
     * 
     */
    @JsonProperty("homologous_to")
    @JsonPropertyDescription("holds between two biological entities that have common evolutionary origin")
    private List<String> homologousTo = new ArrayList<String>();
    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * (Required)
     * 
     */
    @JsonProperty("id")
    @JsonPropertyDescription("A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI")
    private String id;
    /**
     * holds between any two entities that directly or indirectly interact with each other
     * 
     */
    @JsonProperty("interacts_with")
    @JsonPropertyDescription("holds between any two entities that directly or indirectly interact with each other")
    private List<String> interactsWith = new ArrayList<String>();
    /**
     * TODO
     * 
     */
    @JsonProperty("interbase_coordinate")
    @JsonPropertyDescription("TODO")
    private String interbaseCoordinate;
    /**
     * An IRI for the node. This is determined by the id using expansion rules.
     * 
     */
    @JsonProperty("iri")
    @JsonPropertyDescription("An IRI for the node. This is determined by the id using expansion rules.")
    private String iri;
    /**
     * latitude
     * 
     */
    @JsonProperty("latitude")
    @JsonPropertyDescription("latitude")
    private String latitude;
    /**
     * holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)
     * 
     */
    @JsonProperty("located_in")
    @JsonPropertyDescription("holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)")
    private List<String> locatedIn = new ArrayList<String>();
    /**
     * holds between material entity or site and a material entity that is located within it (but not considered a part of it)
     * 
     */
    @JsonProperty("location_of")
    @JsonPropertyDescription("holds between material entity or site and a material entity that is located within it (but not considered a part of it)")
    private List<String> locationOf = new ArrayList<String>();
    /**
     * longitude
     * 
     */
    @JsonProperty("longitude")
    @JsonPropertyDescription("longitude")
    private String longitude;
    /**
     * used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome
     * 
     */
    @JsonProperty("manifestation_of")
    @JsonPropertyDescription("used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome")
    private List<String> manifestationOf = new ArrayList<String>();
    /**
     * holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
     * 
     */
    @JsonProperty("model_of")
    @JsonPropertyDescription("holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.")
    private List<String> modelOf = new ArrayList<String>();
    /**
     * A human-readable name for a thing
     * (Required)
     * 
     */
    @JsonProperty("name")
    @JsonPropertyDescription("A human-readable name for a thing")
    private String name;
    @JsonProperty("negatively_regulates")
    private List<String> negativelyRegulates = new ArrayList<String>();
    /**
     * A grouping for any property that holds between a node and a value
     * 
     */
    @JsonProperty("node_property")
    @JsonPropertyDescription("A grouping for any property that holds between a node and a value")
    private String nodeProperty;
    /**
     * holds between a process and a material entity or site within which the process occurs
     * 
     */
    @JsonProperty("occurs_in")
    @JsonPropertyDescription("holds between a process and a material entity or site within which the process occurs")
    private List<String> occursIn = new ArrayList<String>();
    /**
     * a homology relationship between entities (typically genes) that diverged after a speciation event.
     * 
     */
    @JsonProperty("orthologous_to")
    @JsonPropertyDescription("a homology relationship between entities (typically genes) that diverged after a speciation event.")
    private List<String> orthologousTo = new ArrayList<String>();
    /**
     * holds between entties that overlap in their extents (materials or processes)
     * 
     */
    @JsonProperty("overlaps")
    @JsonPropertyDescription("holds between entties that overlap in their extents (materials or processes)")
    private List<String> overlaps = new ArrayList<String>();
    /**
     * a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
     * 
     */
    @JsonProperty("paralogous_to")
    @JsonPropertyDescription("a homology relationship that holds between entities (typically genes) that diverged after a duplication event.")
    private List<String> paralogousTo = new ArrayList<String>();
    /**
     * holds between parts and wholes (material entities or processes)
     * 
     */
    @JsonProperty("part_of")
    @JsonPropertyDescription("holds between parts and wholes (material entities or processes)")
    private List<String> partOf = new ArrayList<String>();
    /**
     * holds between a continuant and a process, where the continuant is somehow involved in the process
     * 
     */
    @JsonProperty("participates_in")
    @JsonPropertyDescription("holds between a continuant and a process, where the continuant is somehow involved in the process")
    private List<String> participatesIn = new ArrayList<String>();
    /**
     * TODO
     * 
     */
    @JsonProperty("phase")
    @JsonPropertyDescription("TODO")
    private String phase;
    /**
     * holds between two entities that make physical contact as part of some interaction
     * 
     */
    @JsonProperty("physically_interacts_with")
    @JsonPropertyDescription("holds between two entities that make physical contact as part of some interaction")
    private List<String> physicallyInteractsWith = new ArrayList<String>();
    @JsonProperty("positively_regulates")
    private List<String> positivelyRegulates = new ArrayList<String>();
    /**
     * holds between two entities where exposure to one entity increases the chance of developing the other
     * 
     */
    @JsonProperty("predisposes")
    @JsonPropertyDescription("holds between two entities where exposure to one entity increases the chance of developing the other")
    private List<String> predisposes = new ArrayList<String>();
    /**
     * holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical substance, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
     * 
     */
    @JsonProperty("prevents")
    @JsonPropertyDescription("holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical substance, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.")
    private List<String> prevents = new ArrayList<String>();
    /**
     * holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity
     * 
     */
    @JsonProperty("produces")
    @JsonPropertyDescription("holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity")
    private List<String> produces = new ArrayList<String>();
    @JsonProperty("regulates")
    private List<String> regulates = new ArrayList<String>();
    /**
     * A relationship that is asserted between two named things
     * 
     */
    @JsonProperty("related_to")
    @JsonPropertyDescription("A relationship that is asserted between two named things")
    private List<String> relatedTo = new ArrayList<String>();
    /**
     * holds between two entities that are considered equivalent to each other
     * 
     */
    @JsonProperty("same_as")
    @JsonPropertyDescription("holds between two entities that are considered equivalent to each other")
    private List<String> sameAs = new ArrayList<String>();
    @JsonProperty("start_interbase_coordinate")
    private String startInterbaseCoordinate;
    /**
     * Alternate human-readable names for a thing
     * 
     */
    @JsonProperty("synonym")
    @JsonPropertyDescription("Alternate human-readable names for a thing")
    private List<String> synonym = new ArrayList<String>();
    /**
     * more commonly used for gene symbols in yeast
     * 
     */
    @JsonProperty("systematic_synonym")
    @JsonPropertyDescription("more commonly used for gene symbols in yeast")
    private List<String> systematicSynonym = new ArrayList<String>();
    /**
     * a point in time
     * 
     */
    @JsonProperty("timepoint")
    @JsonPropertyDescription("a point in time")
    private String timepoint;
    @JsonProperty("type")
    private String type;
    /**
     * date on which thing was updated. This can be applied to nodes or edges
     * 
     */
    @JsonProperty("update_date")
    @JsonPropertyDescription("date on which thing was updated. This can be applied to nodes or edges")
    private String updateDate;
    /**
     * a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
     * 
     */
    @JsonProperty("xenologous_to")
    @JsonPropertyDescription("a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.")
    private List<String> xenologousTo = new ArrayList<String>();

    /**
     * holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
     * 
     */
    @JsonProperty("actively_involved_in")
    public List<String> getActivelyInvolvedIn() {
        return activelyInvolvedIn;
    }

    /**
     * holds between a continuant and a process or function, where the continuant actively contributes to part or all of the process or function it realizes
     * 
     */
    @JsonProperty("actively_involved_in")
    public void setActivelyInvolvedIn(List<String> activelyInvolvedIn) {
        this.activelyInvolvedIn = activelyInvolvedIn;
    }

    /**
     * describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
     * 
     */
    @JsonProperty("affects")
    public List<String> getAffects() {
        return affects;
    }

    /**
     * describes an entity that has a direct affect on the state or quality of another existing entity. Use of the 'affects' predicate implies that the affected entity already exists, unlike predicates such as 'affects risk for' and 'prevents, where the outcome is something that may or may not come to be.
     * 
     */
    @JsonProperty("affects")
    public void setAffects(List<String> affects) {
        this.affects = affects;
    }

    /**
     * holds between two entities where exposure to one entity alters the chance of developing the other
     * 
     */
    @JsonProperty("affects_risk_for")
    public List<String> getAffectsRiskFor() {
        return affectsRiskFor;
    }

    /**
     * holds between two entities where exposure to one entity alters the chance of developing the other
     * 
     */
    @JsonProperty("affects_risk_for")
    public void setAffectsRiskFor(List<String> affectsRiskFor) {
        this.affectsRiskFor = affectsRiskFor;
    }

    @JsonProperty("aggregate_statistic")
    public String getAggregateStatistic() {
        return aggregateStatistic;
    }

    @JsonProperty("aggregate_statistic")
    public void setAggregateStatistic(String aggregateStatistic) {
        this.aggregateStatistic = aggregateStatistic;
    }

    /**
     * holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.
     * 
     */
    @JsonProperty("capable_of")
    public List<String> getCapableOf() {
        return capableOf;
    }

    /**
     * holds between a physical entity and process or function, where the continuant alone has the ability to carry out the process or function.
     * 
     */
    @JsonProperty("capable_of")
    public void setCapableOf(List<String> capableOf) {
        this.capableOf = capableOf;
    }

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * (Required)
     * 
     */
    @JsonProperty("category")
    public List<String> getCategory() {
        return category;
    }

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * (Required)
     * 
     */
    @JsonProperty("category")
    public void setCategory(List<String> category) {
        this.category = category;
    }

    /**
     * holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or  generation of the other
     * 
     */
    @JsonProperty("caused_by")
    public List<String> getCausedBy() {
        return causedBy;
    }

    /**
     * holds between two entities where the occurrence, existence, or activity of one is caused by the occurrence or  generation of the other
     * 
     */
    @JsonProperty("caused_by")
    public void setCausedBy(List<String> causedBy) {
        this.causedBy = causedBy;
    }

    /**
     * holds between two entities where the occurrence, existence, or activity of one causes the occurrence or  generation of the other
     * 
     */
    @JsonProperty("causes")
    public List<String> getCauses() {
        return causes;
    }

    /**
     * holds between two entities where the occurrence, existence, or activity of one causes the occurrence or  generation of the other
     * 
     */
    @JsonProperty("causes")
    public void setCauses(List<String> causes) {
        this.causes = causes;
    }

    /**
     * holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
     * 
     */
    @JsonProperty("coexists_with")
    public List<String> getCoexistsWith() {
        return coexistsWith;
    }

    /**
     * holds between two entities that are co-located in the same aggregate object, process, or spatio-temporal region
     * 
     */
    @JsonProperty("coexists_with")
    public void setCoexistsWith(List<String> coexistsWith) {
        this.coexistsWith = coexistsWith;
    }

    /**
     * holds between two entities that are observed to be located in the same place.
     * 
     */
    @JsonProperty("colocalizes_with")
    public List<String> getColocalizesWith() {
        return colocalizesWith;
    }

    /**
     * holds between two entities that are observed to be located in the same place.
     * 
     */
    @JsonProperty("colocalizes_with")
    public void setColocalizesWith(List<String> colocalizesWith) {
        this.colocalizesWith = colocalizesWith;
    }

    /**
     * holds between two entities where the occurrence, existence, or activity of one causes or contributes to the occurrence or generation of the other
     * 
     */
    @JsonProperty("contributes_to")
    public List<String> getContributesTo() {
        return contributesTo;
    }

    /**
     * holds between two entities where the occurrence, existence, or activity of one causes or contributes to the occurrence or generation of the other
     * 
     */
    @JsonProperty("contributes_to")
    public void setContributesTo(List<String> contributesTo) {
        this.contributesTo = contributesTo;
    }

    /**
     * holds between any two named thing entities. For example, correlated_with holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("correlated_with")
    public List<String> getCorrelatedWith() {
        return correlatedWith;
    }

    /**
     * holds between any two named thing entities. For example, correlated_with holds between a disease or phenotypic feature and a measurable molecular entity that is used as an indicator of the presence or state of the disease or feature.
     * 
     */
    @JsonProperty("correlated_with")
    public void setCorrelatedWith(List<String> correlatedWith) {
        this.correlatedWith = correlatedWith;
    }

    /**
     * date on which thing was created. This can be applied to nodes or edges
     * 
     */
    @JsonProperty("creation_date")
    public String getCreationDate() {
        return creationDate;
    }

    /**
     * date on which thing was created. This can be applied to nodes or edges
     * 
     */
    @JsonProperty("creation_date")
    public void setCreationDate(String creationDate) {
        this.creationDate = creationDate;
    }

    /**
     * holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
     * 
     */
    @JsonProperty("derives_from")
    public List<String> getDerivesFrom() {
        return derivesFrom;
    }

    /**
     * holds between two distinct material entities, the new entity and the old entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
     * 
     */
    @JsonProperty("derives_from")
    public void setDerivesFrom(List<String> derivesFrom) {
        this.derivesFrom = derivesFrom;
    }

    /**
     * holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
     * 
     */
    @JsonProperty("derives_into")
    public List<String> getDerivesInto() {
        return derivesInto;
    }

    /**
     * holds between two distinct material entities, the old entity and the new entity, in which the new entity begins to exist when the old entity ceases to exist, and the new entity inherits the significant portion of the matter of the old entity
     * 
     */
    @JsonProperty("derives_into")
    public void setDerivesInto(List<String> derivesInto) {
        this.derivesInto = derivesInto;
    }

    /**
     * a human-readable description of a thing
     * 
     */
    @JsonProperty("description")
    public String getDescription() {
        return description;
    }

    /**
     * a human-readable description of a thing
     * 
     */
    @JsonProperty("description")
    public void setDescription(String description) {
        this.description = description;
    }

    /**
     * describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
     * 
     */
    @JsonProperty("disrupts")
    public List<String> getDisrupts() {
        return disrupts;
    }

    /**
     * describes a relationship where one entity degrades or interferes with the structure, function, or occurrence of another.
     * 
     */
    @JsonProperty("disrupts")
    public void setDisrupts(List<String> disrupts) {
        this.disrupts = disrupts;
    }

    @JsonProperty("end_interbase_coordinate")
    public String getEndInterbaseCoordinate() {
        return endInterbaseCoordinate;
    }

    @JsonProperty("end_interbase_coordinate")
    public void setEndInterbaseCoordinate(String endInterbaseCoordinate) {
        this.endInterbaseCoordinate = endInterbaseCoordinate;
    }

    /**
     * The value in a property-value tuple
     * 
     */
    @JsonProperty("filler")
    public String getFiller() {
        return filler;
    }

    /**
     * The value in a property-value tuple
     * 
     */
    @JsonProperty("filler")
    public void setFiller(String filler) {
        this.filler = filler;
    }

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

    /**
     * TODO
     * 
     */
    @JsonProperty("genome_build")
    public String getGenomeBuild() {
        return genomeBuild;
    }

    /**
     * TODO
     * 
     */
    @JsonProperty("genome_build")
    public void setGenomeBuild(String genomeBuild) {
        this.genomeBuild = genomeBuild;
    }

    /**
     * connects a genomic feature to its sequence
     * 
     */
    @JsonProperty("has_biological_sequence")
    public String getHasBiologicalSequence() {
        return hasBiologicalSequence;
    }

    /**
     * connects a genomic feature to its sequence
     * 
     */
    @JsonProperty("has_biological_sequence")
    public void setHasBiologicalSequence(String hasBiologicalSequence) {
        this.hasBiologicalSequence = hasBiologicalSequence;
    }

    /**
     * description of chemical compound based on element symbols
     * 
     */
    @JsonProperty("has_chemical_formula")
    public String getHasChemicalFormula() {
        return hasChemicalFormula;
    }

    /**
     * description of chemical compound based on element symbols
     * 
     */
    @JsonProperty("has_chemical_formula")
    public void setHasChemicalFormula(String hasChemicalFormula) {
        this.hasChemicalFormula = hasChemicalFormula;
    }

    /**
     * number of things with a particular property
     * 
     */
    @JsonProperty("has_count")
    public String getHasCount() {
        return hasCount;
    }

    /**
     * number of things with a particular property
     * 
     */
    @JsonProperty("has_count")
    public void setHasCount(String hasCount) {
        this.hasCount = hasCount;
    }

    /**
     * connects an entity to a single drug
     * 
     */
    @JsonProperty("has_drug")
    public String getHasDrug() {
        return hasDrug;
    }

    /**
     * connects an entity to a single drug
     * 
     */
    @JsonProperty("has_drug")
    public void setHasDrug(String hasDrug) {
        this.hasDrug = hasDrug;
    }

    /**
     * connects an entity to a single gene
     * 
     */
    @JsonProperty("has_gene")
    public String getHasGene() {
        return hasGene;
    }

    /**
     * connects an entity to a single gene
     * 
     */
    @JsonProperty("has_gene")
    public void setHasGene(String hasGene) {
        this.hasGene = hasGene;
    }

    /**
     * connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583
     * 
     */
    @JsonProperty("has_molecular_consequence")
    public List<String> getHasMolecularConsequence() {
        return hasMolecularConsequence;
    }

    /**
     * connects a sequence variant to a class describing the molecular consequence. E.g.  SO:0001583
     * 
     */
    @JsonProperty("has_molecular_consequence")
    public void setHasMolecularConsequence(List<String> hasMolecularConsequence) {
        this.hasMolecularConsequence = hasMolecularConsequence;
    }

    /**
     * holds between wholes and their parts (material entities or processes)
     * 
     */
    @JsonProperty("has_part")
    public List<String> getHasPart() {
        return hasPart;
    }

    /**
     * holds between wholes and their parts (material entities or processes)
     * 
     */
    @JsonProperty("has_part")
    public void setHasPart(List<String> hasPart) {
        this.hasPart = hasPart;
    }

    /**
     * equivalent to has quotient multiplied by 100
     * 
     */
    @JsonProperty("has_percentage")
    public String getHasPercentage() {
        return hasPercentage;
    }

    /**
     * equivalent to has quotient multiplied by 100
     * 
     */
    @JsonProperty("has_percentage")
    public void setHasPercentage(String hasPercentage) {
        this.hasPercentage = hasPercentage;
    }

    @JsonProperty("has_quotient")
    public String getHasQuotient() {
        return hasQuotient;
    }

    @JsonProperty("has_quotient")
    public void setHasQuotient(String hasQuotient) {
        this.hasQuotient = hasQuotient;
    }

    /**
     * total number of things in a particular reference set
     * 
     */
    @JsonProperty("has_total")
    public String getHasTotal() {
        return hasTotal;
    }

    /**
     * total number of things in a particular reference set
     * 
     */
    @JsonProperty("has_total")
    public void setHasTotal(String hasTotal) {
        this.hasTotal = hasTotal;
    }

    @JsonProperty("has_zygosity")
    public String getHasZygosity() {
        return hasZygosity;
    }

    @JsonProperty("has_zygosity")
    public void setHasZygosity(String hasZygosity) {
        this.hasZygosity = hasZygosity;
    }

    /**
     * holds between two biological entities that have common evolutionary origin
     * 
     */
    @JsonProperty("homologous_to")
    public List<String> getHomologousTo() {
        return homologousTo;
    }

    /**
     * holds between two biological entities that have common evolutionary origin
     * 
     */
    @JsonProperty("homologous_to")
    public void setHomologousTo(List<String> homologousTo) {
        this.homologousTo = homologousTo;
    }

    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * (Required)
     * 
     */
    @JsonProperty("id")
    public String getId() {
        return id;
    }

    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * (Required)
     * 
     */
    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    /**
     * holds between any two entities that directly or indirectly interact with each other
     * 
     */
    @JsonProperty("interacts_with")
    public List<String> getInteractsWith() {
        return interactsWith;
    }

    /**
     * holds between any two entities that directly or indirectly interact with each other
     * 
     */
    @JsonProperty("interacts_with")
    public void setInteractsWith(List<String> interactsWith) {
        this.interactsWith = interactsWith;
    }

    /**
     * TODO
     * 
     */
    @JsonProperty("interbase_coordinate")
    public String getInterbaseCoordinate() {
        return interbaseCoordinate;
    }

    /**
     * TODO
     * 
     */
    @JsonProperty("interbase_coordinate")
    public void setInterbaseCoordinate(String interbaseCoordinate) {
        this.interbaseCoordinate = interbaseCoordinate;
    }

    /**
     * An IRI for the node. This is determined by the id using expansion rules.
     * 
     */
    @JsonProperty("iri")
    public String getIri() {
        return iri;
    }

    /**
     * An IRI for the node. This is determined by the id using expansion rules.
     * 
     */
    @JsonProperty("iri")
    public void setIri(String iri) {
        this.iri = iri;
    }

    /**
     * latitude
     * 
     */
    @JsonProperty("latitude")
    public String getLatitude() {
        return latitude;
    }

    /**
     * latitude
     * 
     */
    @JsonProperty("latitude")
    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }

    /**
     * holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)
     * 
     */
    @JsonProperty("located_in")
    public List<String> getLocatedIn() {
        return locatedIn;
    }

    /**
     * holds between a material entity and a material entity or site within which it is located (but of which it is not considered a part)
     * 
     */
    @JsonProperty("located_in")
    public void setLocatedIn(List<String> locatedIn) {
        this.locatedIn = locatedIn;
    }

    /**
     * holds between material entity or site and a material entity that is located within it (but not considered a part of it)
     * 
     */
    @JsonProperty("location_of")
    public List<String> getLocationOf() {
        return locationOf;
    }

    /**
     * holds between material entity or site and a material entity that is located within it (but not considered a part of it)
     * 
     */
    @JsonProperty("location_of")
    public void setLocationOf(List<String> locationOf) {
        this.locationOf = locationOf;
    }

    /**
     * longitude
     * 
     */
    @JsonProperty("longitude")
    public String getLongitude() {
        return longitude;
    }

    /**
     * longitude
     * 
     */
    @JsonProperty("longitude")
    public void setLongitude(String longitude) {
        this.longitude = longitude;
    }

    /**
     * used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome
     * 
     */
    @JsonProperty("manifestation_of")
    public List<String> getManifestationOf() {
        return manifestationOf;
    }

    /**
     * used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome
     * 
     */
    @JsonProperty("manifestation_of")
    public void setManifestationOf(List<String> manifestationOf) {
        this.manifestationOf = manifestationOf;
    }

    /**
     * holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
     * 
     */
    @JsonProperty("model_of")
    public List<String> getModelOf() {
        return modelOf;
    }

    /**
     * holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exhibiting similar features of the studied entity.
     * 
     */
    @JsonProperty("model_of")
    public void setModelOf(List<String> modelOf) {
        this.modelOf = modelOf;
    }

    /**
     * A human-readable name for a thing
     * (Required)
     * 
     */
    @JsonProperty("name")
    public String getName() {
        return name;
    }

    /**
     * A human-readable name for a thing
     * (Required)
     * 
     */
    @JsonProperty("name")
    public void setName(String name) {
        this.name = name;
    }

    @JsonProperty("negatively_regulates")
    public List<String> getNegativelyRegulates() {
        return negativelyRegulates;
    }

    @JsonProperty("negatively_regulates")
    public void setNegativelyRegulates(List<String> negativelyRegulates) {
        this.negativelyRegulates = negativelyRegulates;
    }

    /**
     * A grouping for any property that holds between a node and a value
     * 
     */
    @JsonProperty("node_property")
    public String getNodeProperty() {
        return nodeProperty;
    }

    /**
     * A grouping for any property that holds between a node and a value
     * 
     */
    @JsonProperty("node_property")
    public void setNodeProperty(String nodeProperty) {
        this.nodeProperty = nodeProperty;
    }

    /**
     * holds between a process and a material entity or site within which the process occurs
     * 
     */
    @JsonProperty("occurs_in")
    public List<String> getOccursIn() {
        return occursIn;
    }

    /**
     * holds between a process and a material entity or site within which the process occurs
     * 
     */
    @JsonProperty("occurs_in")
    public void setOccursIn(List<String> occursIn) {
        this.occursIn = occursIn;
    }

    /**
     * a homology relationship between entities (typically genes) that diverged after a speciation event.
     * 
     */
    @JsonProperty("orthologous_to")
    public List<String> getOrthologousTo() {
        return orthologousTo;
    }

    /**
     * a homology relationship between entities (typically genes) that diverged after a speciation event.
     * 
     */
    @JsonProperty("orthologous_to")
    public void setOrthologousTo(List<String> orthologousTo) {
        this.orthologousTo = orthologousTo;
    }

    /**
     * holds between entties that overlap in their extents (materials or processes)
     * 
     */
    @JsonProperty("overlaps")
    public List<String> getOverlaps() {
        return overlaps;
    }

    /**
     * holds between entties that overlap in their extents (materials or processes)
     * 
     */
    @JsonProperty("overlaps")
    public void setOverlaps(List<String> overlaps) {
        this.overlaps = overlaps;
    }

    /**
     * a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
     * 
     */
    @JsonProperty("paralogous_to")
    public List<String> getParalogousTo() {
        return paralogousTo;
    }

    /**
     * a homology relationship that holds between entities (typically genes) that diverged after a duplication event.
     * 
     */
    @JsonProperty("paralogous_to")
    public void setParalogousTo(List<String> paralogousTo) {
        this.paralogousTo = paralogousTo;
    }

    /**
     * holds between parts and wholes (material entities or processes)
     * 
     */
    @JsonProperty("part_of")
    public List<String> getPartOf() {
        return partOf;
    }

    /**
     * holds between parts and wholes (material entities or processes)
     * 
     */
    @JsonProperty("part_of")
    public void setPartOf(List<String> partOf) {
        this.partOf = partOf;
    }

    /**
     * holds between a continuant and a process, where the continuant is somehow involved in the process
     * 
     */
    @JsonProperty("participates_in")
    public List<String> getParticipatesIn() {
        return participatesIn;
    }

    /**
     * holds between a continuant and a process, where the continuant is somehow involved in the process
     * 
     */
    @JsonProperty("participates_in")
    public void setParticipatesIn(List<String> participatesIn) {
        this.participatesIn = participatesIn;
    }

    /**
     * TODO
     * 
     */
    @JsonProperty("phase")
    public String getPhase() {
        return phase;
    }

    /**
     * TODO
     * 
     */
    @JsonProperty("phase")
    public void setPhase(String phase) {
        this.phase = phase;
    }

    /**
     * holds between two entities that make physical contact as part of some interaction
     * 
     */
    @JsonProperty("physically_interacts_with")
    public List<String> getPhysicallyInteractsWith() {
        return physicallyInteractsWith;
    }

    /**
     * holds between two entities that make physical contact as part of some interaction
     * 
     */
    @JsonProperty("physically_interacts_with")
    public void setPhysicallyInteractsWith(List<String> physicallyInteractsWith) {
        this.physicallyInteractsWith = physicallyInteractsWith;
    }

    @JsonProperty("positively_regulates")
    public List<String> getPositivelyRegulates() {
        return positivelyRegulates;
    }

    @JsonProperty("positively_regulates")
    public void setPositivelyRegulates(List<String> positivelyRegulates) {
        this.positivelyRegulates = positivelyRegulates;
    }

    /**
     * holds between two entities where exposure to one entity increases the chance of developing the other
     * 
     */
    @JsonProperty("predisposes")
    public List<String> getPredisposes() {
        return predisposes;
    }

    /**
     * holds between two entities where exposure to one entity increases the chance of developing the other
     * 
     */
    @JsonProperty("predisposes")
    public void setPredisposes(List<String> predisposes) {
        this.predisposes = predisposes;
    }

    /**
     * holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical substance, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
     * 
     */
    @JsonProperty("prevents")
    public List<String> getPrevents() {
        return prevents;
    }

    /**
     * holds between an entity whose application or use reduces the likelihood of a potential outcome. Typically used to associate a chemical substance, exposure, activity, or medical intervention that can prevent the onset a disease or phenotypic feature.
     * 
     */
    @JsonProperty("prevents")
    public void setPrevents(List<String> prevents) {
        this.prevents = prevents;
    }

    /**
     * holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity
     * 
     */
    @JsonProperty("produces")
    public List<String> getProduces() {
        return produces;
    }

    /**
     * holds between a material entity and a product that is generated through the intentional actions or functioning of the material entity
     * 
     */
    @JsonProperty("produces")
    public void setProduces(List<String> produces) {
        this.produces = produces;
    }

    @JsonProperty("regulates")
    public List<String> getRegulates() {
        return regulates;
    }

    @JsonProperty("regulates")
    public void setRegulates(List<String> regulates) {
        this.regulates = regulates;
    }

    /**
     * A relationship that is asserted between two named things
     * 
     */
    @JsonProperty("related_to")
    public List<String> getRelatedTo() {
        return relatedTo;
    }

    /**
     * A relationship that is asserted between two named things
     * 
     */
    @JsonProperty("related_to")
    public void setRelatedTo(List<String> relatedTo) {
        this.relatedTo = relatedTo;
    }

    /**
     * holds between two entities that are considered equivalent to each other
     * 
     */
    @JsonProperty("same_as")
    public List<String> getSameAs() {
        return sameAs;
    }

    /**
     * holds between two entities that are considered equivalent to each other
     * 
     */
    @JsonProperty("same_as")
    public void setSameAs(List<String> sameAs) {
        this.sameAs = sameAs;
    }

    @JsonProperty("start_interbase_coordinate")
    public String getStartInterbaseCoordinate() {
        return startInterbaseCoordinate;
    }

    @JsonProperty("start_interbase_coordinate")
    public void setStartInterbaseCoordinate(String startInterbaseCoordinate) {
        this.startInterbaseCoordinate = startInterbaseCoordinate;
    }

    /**
     * Alternate human-readable names for a thing
     * 
     */
    @JsonProperty("synonym")
    public List<String> getSynonym() {
        return synonym;
    }

    /**
     * Alternate human-readable names for a thing
     * 
     */
    @JsonProperty("synonym")
    public void setSynonym(List<String> synonym) {
        this.synonym = synonym;
    }

    /**
     * more commonly used for gene symbols in yeast
     * 
     */
    @JsonProperty("systematic_synonym")
    public List<String> getSystematicSynonym() {
        return systematicSynonym;
    }

    /**
     * more commonly used for gene symbols in yeast
     * 
     */
    @JsonProperty("systematic_synonym")
    public void setSystematicSynonym(List<String> systematicSynonym) {
        this.systematicSynonym = systematicSynonym;
    }

    /**
     * a point in time
     * 
     */
    @JsonProperty("timepoint")
    public String getTimepoint() {
        return timepoint;
    }

    /**
     * a point in time
     * 
     */
    @JsonProperty("timepoint")
    public void setTimepoint(String timepoint) {
        this.timepoint = timepoint;
    }

    @JsonProperty("type")
    public String getType() {
        return type;
    }

    @JsonProperty("type")
    public void setType(String type) {
        this.type = type;
    }

    /**
     * date on which thing was updated. This can be applied to nodes or edges
     * 
     */
    @JsonProperty("update_date")
    public String getUpdateDate() {
        return updateDate;
    }

    /**
     * date on which thing was updated. This can be applied to nodes or edges
     * 
     */
    @JsonProperty("update_date")
    public void setUpdateDate(String updateDate) {
        this.updateDate = updateDate;
    }

    /**
     * a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
     * 
     */
    @JsonProperty("xenologous_to")
    public List<String> getXenologousTo() {
        return xenologousTo;
    }

    /**
     * a homology relationship characterized by an interspecies (horizontal) transfer since the common ancestor.
     * 
     */
    @JsonProperty("xenologous_to")
    public void setXenologousTo(List<String> xenologousTo) {
        this.xenologousTo = xenologousTo;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(NamedThing.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("activelyInvolvedIn");
        sb.append('=');
        sb.append(((this.activelyInvolvedIn == null)?"<null>":this.activelyInvolvedIn));
        sb.append(',');
        sb.append("affects");
        sb.append('=');
        sb.append(((this.affects == null)?"<null>":this.affects));
        sb.append(',');
        sb.append("affectsRiskFor");
        sb.append('=');
        sb.append(((this.affectsRiskFor == null)?"<null>":this.affectsRiskFor));
        sb.append(',');
        sb.append("aggregateStatistic");
        sb.append('=');
        sb.append(((this.aggregateStatistic == null)?"<null>":this.aggregateStatistic));
        sb.append(',');
        sb.append("capableOf");
        sb.append('=');
        sb.append(((this.capableOf == null)?"<null>":this.capableOf));
        sb.append(',');
        sb.append("category");
        sb.append('=');
        sb.append(((this.category == null)?"<null>":this.category));
        sb.append(',');
        sb.append("causedBy");
        sb.append('=');
        sb.append(((this.causedBy == null)?"<null>":this.causedBy));
        sb.append(',');
        sb.append("causes");
        sb.append('=');
        sb.append(((this.causes == null)?"<null>":this.causes));
        sb.append(',');
        sb.append("coexistsWith");
        sb.append('=');
        sb.append(((this.coexistsWith == null)?"<null>":this.coexistsWith));
        sb.append(',');
        sb.append("colocalizesWith");
        sb.append('=');
        sb.append(((this.colocalizesWith == null)?"<null>":this.colocalizesWith));
        sb.append(',');
        sb.append("contributesTo");
        sb.append('=');
        sb.append(((this.contributesTo == null)?"<null>":this.contributesTo));
        sb.append(',');
        sb.append("correlatedWith");
        sb.append('=');
        sb.append(((this.correlatedWith == null)?"<null>":this.correlatedWith));
        sb.append(',');
        sb.append("creationDate");
        sb.append('=');
        sb.append(((this.creationDate == null)?"<null>":this.creationDate));
        sb.append(',');
        sb.append("derivesFrom");
        sb.append('=');
        sb.append(((this.derivesFrom == null)?"<null>":this.derivesFrom));
        sb.append(',');
        sb.append("derivesInto");
        sb.append('=');
        sb.append(((this.derivesInto == null)?"<null>":this.derivesInto));
        sb.append(',');
        sb.append("description");
        sb.append('=');
        sb.append(((this.description == null)?"<null>":this.description));
        sb.append(',');
        sb.append("disrupts");
        sb.append('=');
        sb.append(((this.disrupts == null)?"<null>":this.disrupts));
        sb.append(',');
        sb.append("endInterbaseCoordinate");
        sb.append('=');
        sb.append(((this.endInterbaseCoordinate == null)?"<null>":this.endInterbaseCoordinate));
        sb.append(',');
        sb.append("filler");
        sb.append('=');
        sb.append(((this.filler == null)?"<null>":this.filler));
        sb.append(',');
        sb.append("fullName");
        sb.append('=');
        sb.append(((this.fullName == null)?"<null>":this.fullName));
        sb.append(',');
        sb.append("genomeBuild");
        sb.append('=');
        sb.append(((this.genomeBuild == null)?"<null>":this.genomeBuild));
        sb.append(',');
        sb.append("hasBiologicalSequence");
        sb.append('=');
        sb.append(((this.hasBiologicalSequence == null)?"<null>":this.hasBiologicalSequence));
        sb.append(',');
        sb.append("hasChemicalFormula");
        sb.append('=');
        sb.append(((this.hasChemicalFormula == null)?"<null>":this.hasChemicalFormula));
        sb.append(',');
        sb.append("hasCount");
        sb.append('=');
        sb.append(((this.hasCount == null)?"<null>":this.hasCount));
        sb.append(',');
        sb.append("hasDrug");
        sb.append('=');
        sb.append(((this.hasDrug == null)?"<null>":this.hasDrug));
        sb.append(',');
        sb.append("hasGene");
        sb.append('=');
        sb.append(((this.hasGene == null)?"<null>":this.hasGene));
        sb.append(',');
        sb.append("hasMolecularConsequence");
        sb.append('=');
        sb.append(((this.hasMolecularConsequence == null)?"<null>":this.hasMolecularConsequence));
        sb.append(',');
        sb.append("hasPart");
        sb.append('=');
        sb.append(((this.hasPart == null)?"<null>":this.hasPart));
        sb.append(',');
        sb.append("hasPercentage");
        sb.append('=');
        sb.append(((this.hasPercentage == null)?"<null>":this.hasPercentage));
        sb.append(',');
        sb.append("hasQuotient");
        sb.append('=');
        sb.append(((this.hasQuotient == null)?"<null>":this.hasQuotient));
        sb.append(',');
        sb.append("hasTotal");
        sb.append('=');
        sb.append(((this.hasTotal == null)?"<null>":this.hasTotal));
        sb.append(',');
        sb.append("hasZygosity");
        sb.append('=');
        sb.append(((this.hasZygosity == null)?"<null>":this.hasZygosity));
        sb.append(',');
        sb.append("homologousTo");
        sb.append('=');
        sb.append(((this.homologousTo == null)?"<null>":this.homologousTo));
        sb.append(',');
        sb.append("id");
        sb.append('=');
        sb.append(((this.id == null)?"<null>":this.id));
        sb.append(',');
        sb.append("interactsWith");
        sb.append('=');
        sb.append(((this.interactsWith == null)?"<null>":this.interactsWith));
        sb.append(',');
        sb.append("interbaseCoordinate");
        sb.append('=');
        sb.append(((this.interbaseCoordinate == null)?"<null>":this.interbaseCoordinate));
        sb.append(',');
        sb.append("iri");
        sb.append('=');
        sb.append(((this.iri == null)?"<null>":this.iri));
        sb.append(',');
        sb.append("latitude");
        sb.append('=');
        sb.append(((this.latitude == null)?"<null>":this.latitude));
        sb.append(',');
        sb.append("locatedIn");
        sb.append('=');
        sb.append(((this.locatedIn == null)?"<null>":this.locatedIn));
        sb.append(',');
        sb.append("locationOf");
        sb.append('=');
        sb.append(((this.locationOf == null)?"<null>":this.locationOf));
        sb.append(',');
        sb.append("longitude");
        sb.append('=');
        sb.append(((this.longitude == null)?"<null>":this.longitude));
        sb.append(',');
        sb.append("manifestationOf");
        sb.append('=');
        sb.append(((this.manifestationOf == null)?"<null>":this.manifestationOf));
        sb.append(',');
        sb.append("modelOf");
        sb.append('=');
        sb.append(((this.modelOf == null)?"<null>":this.modelOf));
        sb.append(',');
        sb.append("name");
        sb.append('=');
        sb.append(((this.name == null)?"<null>":this.name));
        sb.append(',');
        sb.append("negativelyRegulates");
        sb.append('=');
        sb.append(((this.negativelyRegulates == null)?"<null>":this.negativelyRegulates));
        sb.append(',');
        sb.append("nodeProperty");
        sb.append('=');
        sb.append(((this.nodeProperty == null)?"<null>":this.nodeProperty));
        sb.append(',');
        sb.append("occursIn");
        sb.append('=');
        sb.append(((this.occursIn == null)?"<null>":this.occursIn));
        sb.append(',');
        sb.append("orthologousTo");
        sb.append('=');
        sb.append(((this.orthologousTo == null)?"<null>":this.orthologousTo));
        sb.append(',');
        sb.append("overlaps");
        sb.append('=');
        sb.append(((this.overlaps == null)?"<null>":this.overlaps));
        sb.append(',');
        sb.append("paralogousTo");
        sb.append('=');
        sb.append(((this.paralogousTo == null)?"<null>":this.paralogousTo));
        sb.append(',');
        sb.append("partOf");
        sb.append('=');
        sb.append(((this.partOf == null)?"<null>":this.partOf));
        sb.append(',');
        sb.append("participatesIn");
        sb.append('=');
        sb.append(((this.participatesIn == null)?"<null>":this.participatesIn));
        sb.append(',');
        sb.append("phase");
        sb.append('=');
        sb.append(((this.phase == null)?"<null>":this.phase));
        sb.append(',');
        sb.append("physicallyInteractsWith");
        sb.append('=');
        sb.append(((this.physicallyInteractsWith == null)?"<null>":this.physicallyInteractsWith));
        sb.append(',');
        sb.append("positivelyRegulates");
        sb.append('=');
        sb.append(((this.positivelyRegulates == null)?"<null>":this.positivelyRegulates));
        sb.append(',');
        sb.append("predisposes");
        sb.append('=');
        sb.append(((this.predisposes == null)?"<null>":this.predisposes));
        sb.append(',');
        sb.append("prevents");
        sb.append('=');
        sb.append(((this.prevents == null)?"<null>":this.prevents));
        sb.append(',');
        sb.append("produces");
        sb.append('=');
        sb.append(((this.produces == null)?"<null>":this.produces));
        sb.append(',');
        sb.append("regulates");
        sb.append('=');
        sb.append(((this.regulates == null)?"<null>":this.regulates));
        sb.append(',');
        sb.append("relatedTo");
        sb.append('=');
        sb.append(((this.relatedTo == null)?"<null>":this.relatedTo));
        sb.append(',');
        sb.append("sameAs");
        sb.append('=');
        sb.append(((this.sameAs == null)?"<null>":this.sameAs));
        sb.append(',');
        sb.append("startInterbaseCoordinate");
        sb.append('=');
        sb.append(((this.startInterbaseCoordinate == null)?"<null>":this.startInterbaseCoordinate));
        sb.append(',');
        sb.append("synonym");
        sb.append('=');
        sb.append(((this.synonym == null)?"<null>":this.synonym));
        sb.append(',');
        sb.append("systematicSynonym");
        sb.append('=');
        sb.append(((this.systematicSynonym == null)?"<null>":this.systematicSynonym));
        sb.append(',');
        sb.append("timepoint");
        sb.append('=');
        sb.append(((this.timepoint == null)?"<null>":this.timepoint));
        sb.append(',');
        sb.append("type");
        sb.append('=');
        sb.append(((this.type == null)?"<null>":this.type));
        sb.append(',');
        sb.append("updateDate");
        sb.append('=');
        sb.append(((this.updateDate == null)?"<null>":this.updateDate));
        sb.append(',');
        sb.append("xenologousTo");
        sb.append('=');
        sb.append(((this.xenologousTo == null)?"<null>":this.xenologousTo));
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
        result = ((result* 31)+((this.partOf == null)? 0 :this.partOf.hashCode()));
        result = ((result* 31)+((this.capableOf == null)? 0 :this.capableOf.hashCode()));
        result = ((result* 31)+((this.systematicSynonym == null)? 0 :this.systematicSynonym.hashCode()));
        result = ((result* 31)+((this.hasChemicalFormula == null)? 0 :this.hasChemicalFormula.hashCode()));
        result = ((result* 31)+((this.interbaseCoordinate == null)? 0 :this.interbaseCoordinate.hashCode()));
        result = ((result* 31)+((this.locationOf == null)? 0 :this.locationOf.hashCode()));
        result = ((result* 31)+((this.prevents == null)? 0 :this.prevents.hashCode()));
        result = ((result* 31)+((this.coexistsWith == null)? 0 :this.coexistsWith.hashCode()));
        result = ((result* 31)+((this.positivelyRegulates == null)? 0 :this.positivelyRegulates.hashCode()));
        result = ((result* 31)+((this.type == null)? 0 :this.type.hashCode()));
        result = ((result* 31)+((this.hasTotal == null)? 0 :this.hasTotal.hashCode()));
        result = ((result* 31)+((this.relatedTo == null)? 0 :this.relatedTo.hashCode()));
        result = ((result* 31)+((this.interactsWith == null)? 0 :this.interactsWith.hashCode()));
        result = ((result* 31)+((this.predisposes == null)? 0 :this.predisposes.hashCode()));
        result = ((result* 31)+((this.overlaps == null)? 0 :this.overlaps.hashCode()));
        result = ((result* 31)+((this.id == null)? 0 :this.id.hashCode()));
        result = ((result* 31)+((this.hasMolecularConsequence == null)? 0 :this.hasMolecularConsequence.hashCode()));
        result = ((result* 31)+((this.longitude == null)? 0 :this.longitude.hashCode()));
        result = ((result* 31)+((this.phase == null)? 0 :this.phase.hashCode()));
        result = ((result* 31)+((this.nodeProperty == null)? 0 :this.nodeProperty.hashCode()));
        result = ((result* 31)+((this.hasPart == null)? 0 :this.hasPart.hashCode()));
        result = ((result* 31)+((this.causedBy == null)? 0 :this.causedBy.hashCode()));
        result = ((result* 31)+((this.creationDate == null)? 0 :this.creationDate.hashCode()));
        result = ((result* 31)+((this.contributesTo == null)? 0 :this.contributesTo.hashCode()));
        result = ((result* 31)+((this.paralogousTo == null)? 0 :this.paralogousTo.hashCode()));
        result = ((result* 31)+((this.physicallyInteractsWith == null)? 0 :this.physicallyInteractsWith.hashCode()));
        result = ((result* 31)+((this.locatedIn == null)? 0 :this.locatedIn.hashCode()));
        result = ((result* 31)+((this.manifestationOf == null)? 0 :this.manifestationOf.hashCode()));
        result = ((result* 31)+((this.derivesInto == null)? 0 :this.derivesInto.hashCode()));
        result = ((result* 31)+((this.name == null)? 0 :this.name.hashCode()));
        result = ((result* 31)+((this.produces == null)? 0 :this.produces.hashCode()));
        result = ((result* 31)+((this.modelOf == null)? 0 :this.modelOf.hashCode()));
        result = ((result* 31)+((this.correlatedWith == null)? 0 :this.correlatedWith.hashCode()));
        result = ((result* 31)+((this.updateDate == null)? 0 :this.updateDate.hashCode()));
        result = ((result* 31)+((this.latitude == null)? 0 :this.latitude.hashCode()));
        result = ((result* 31)+((this.activelyInvolvedIn == null)? 0 :this.activelyInvolvedIn.hashCode()));
        result = ((result* 31)+((this.description == null)? 0 :this.description.hashCode()));
        result = ((result* 31)+((this.hasGene == null)? 0 :this.hasGene.hashCode()));
        result = ((result* 31)+((this.hasCount == null)? 0 :this.hasCount.hashCode()));
        result = ((result* 31)+((this.occursIn == null)? 0 :this.occursIn.hashCode()));
        result = ((result* 31)+((this.startInterbaseCoordinate == null)? 0 :this.startInterbaseCoordinate.hashCode()));
        result = ((result* 31)+((this.synonym == null)? 0 :this.synonym.hashCode()));
        result = ((result* 31)+((this.hasQuotient == null)? 0 :this.hasQuotient.hashCode()));
        result = ((result* 31)+((this.causes == null)? 0 :this.causes.hashCode()));
        result = ((result* 31)+((this.hasBiologicalSequence == null)? 0 :this.hasBiologicalSequence.hashCode()));
        result = ((result* 31)+((this.hasDrug == null)? 0 :this.hasDrug.hashCode()));
        result = ((result* 31)+((this.aggregateStatistic == null)? 0 :this.aggregateStatistic.hashCode()));
        result = ((result* 31)+((this.affectsRiskFor == null)? 0 :this.affectsRiskFor.hashCode()));
        result = ((result* 31)+((this.endInterbaseCoordinate == null)? 0 :this.endInterbaseCoordinate.hashCode()));
        result = ((result* 31)+((this.disrupts == null)? 0 :this.disrupts.hashCode()));
        result = ((result* 31)+((this.iri == null)? 0 :this.iri.hashCode()));
        result = ((result* 31)+((this.homologousTo == null)? 0 :this.homologousTo.hashCode()));
        result = ((result* 31)+((this.colocalizesWith == null)? 0 :this.colocalizesWith.hashCode()));
        result = ((result* 31)+((this.derivesFrom == null)? 0 :this.derivesFrom.hashCode()));
        result = ((result* 31)+((this.affects == null)? 0 :this.affects.hashCode()));
        result = ((result* 31)+((this.fullName == null)? 0 :this.fullName.hashCode()));
        result = ((result* 31)+((this.orthologousTo == null)? 0 :this.orthologousTo.hashCode()));
        result = ((result* 31)+((this.xenologousTo == null)? 0 :this.xenologousTo.hashCode()));
        result = ((result* 31)+((this.hasPercentage == null)? 0 :this.hasPercentage.hashCode()));
        result = ((result* 31)+((this.participatesIn == null)? 0 :this.participatesIn.hashCode()));
        result = ((result* 31)+((this.regulates == null)? 0 :this.regulates.hashCode()));
        result = ((result* 31)+((this.genomeBuild == null)? 0 :this.genomeBuild.hashCode()));
        result = ((result* 31)+((this.hasZygosity == null)? 0 :this.hasZygosity.hashCode()));
        result = ((result* 31)+((this.negativelyRegulates == null)? 0 :this.negativelyRegulates.hashCode()));
        result = ((result* 31)+((this.filler == null)? 0 :this.filler.hashCode()));
        result = ((result* 31)+((this.category == null)? 0 :this.category.hashCode()));
        result = ((result* 31)+((this.sameAs == null)? 0 :this.sameAs.hashCode()));
        result = ((result* 31)+((this.timepoint == null)? 0 :this.timepoint.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof NamedThing) == false) {
            return false;
        }
        NamedThing rhs = ((NamedThing) other);
        return (((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((this.partOf == rhs.partOf)||((this.partOf!= null)&&this.partOf.equals(rhs.partOf)))&&((this.capableOf == rhs.capableOf)||((this.capableOf!= null)&&this.capableOf.equals(rhs.capableOf))))&&((this.systematicSynonym == rhs.systematicSynonym)||((this.systematicSynonym!= null)&&this.systematicSynonym.equals(rhs.systematicSynonym))))&&((this.hasChemicalFormula == rhs.hasChemicalFormula)||((this.hasChemicalFormula!= null)&&this.hasChemicalFormula.equals(rhs.hasChemicalFormula))))&&((this.interbaseCoordinate == rhs.interbaseCoordinate)||((this.interbaseCoordinate!= null)&&this.interbaseCoordinate.equals(rhs.interbaseCoordinate))))&&((this.locationOf == rhs.locationOf)||((this.locationOf!= null)&&this.locationOf.equals(rhs.locationOf))))&&((this.prevents == rhs.prevents)||((this.prevents!= null)&&this.prevents.equals(rhs.prevents))))&&((this.coexistsWith == rhs.coexistsWith)||((this.coexistsWith!= null)&&this.coexistsWith.equals(rhs.coexistsWith))))&&((this.positivelyRegulates == rhs.positivelyRegulates)||((this.positivelyRegulates!= null)&&this.positivelyRegulates.equals(rhs.positivelyRegulates))))&&((this.type == rhs.type)||((this.type!= null)&&this.type.equals(rhs.type))))&&((this.hasTotal == rhs.hasTotal)||((this.hasTotal!= null)&&this.hasTotal.equals(rhs.hasTotal))))&&((this.relatedTo == rhs.relatedTo)||((this.relatedTo!= null)&&this.relatedTo.equals(rhs.relatedTo))))&&((this.interactsWith == rhs.interactsWith)||((this.interactsWith!= null)&&this.interactsWith.equals(rhs.interactsWith))))&&((this.predisposes == rhs.predisposes)||((this.predisposes!= null)&&this.predisposes.equals(rhs.predisposes))))&&((this.overlaps == rhs.overlaps)||((this.overlaps!= null)&&this.overlaps.equals(rhs.overlaps))))&&((this.id == rhs.id)||((this.id!= null)&&this.id.equals(rhs.id))))&&((this.hasMolecularConsequence == rhs.hasMolecularConsequence)||((this.hasMolecularConsequence!= null)&&this.hasMolecularConsequence.equals(rhs.hasMolecularConsequence))))&&((this.longitude == rhs.longitude)||((this.longitude!= null)&&this.longitude.equals(rhs.longitude))))&&((this.phase == rhs.phase)||((this.phase!= null)&&this.phase.equals(rhs.phase))))&&((this.nodeProperty == rhs.nodeProperty)||((this.nodeProperty!= null)&&this.nodeProperty.equals(rhs.nodeProperty))))&&((this.hasPart == rhs.hasPart)||((this.hasPart!= null)&&this.hasPart.equals(rhs.hasPart))))&&((this.causedBy == rhs.causedBy)||((this.causedBy!= null)&&this.causedBy.equals(rhs.causedBy))))&&((this.creationDate == rhs.creationDate)||((this.creationDate!= null)&&this.creationDate.equals(rhs.creationDate))))&&((this.contributesTo == rhs.contributesTo)||((this.contributesTo!= null)&&this.contributesTo.equals(rhs.contributesTo))))&&((this.paralogousTo == rhs.paralogousTo)||((this.paralogousTo!= null)&&this.paralogousTo.equals(rhs.paralogousTo))))&&((this.physicallyInteractsWith == rhs.physicallyInteractsWith)||((this.physicallyInteractsWith!= null)&&this.physicallyInteractsWith.equals(rhs.physicallyInteractsWith))))&&((this.locatedIn == rhs.locatedIn)||((this.locatedIn!= null)&&this.locatedIn.equals(rhs.locatedIn))))&&((this.manifestationOf == rhs.manifestationOf)||((this.manifestationOf!= null)&&this.manifestationOf.equals(rhs.manifestationOf))))&&((this.derivesInto == rhs.derivesInto)||((this.derivesInto!= null)&&this.derivesInto.equals(rhs.derivesInto))))&&((this.name == rhs.name)||((this.name!= null)&&this.name.equals(rhs.name))))&&((this.produces == rhs.produces)||((this.produces!= null)&&this.produces.equals(rhs.produces))))&&((this.modelOf == rhs.modelOf)||((this.modelOf!= null)&&this.modelOf.equals(rhs.modelOf))))&&((this.correlatedWith == rhs.correlatedWith)||((this.correlatedWith!= null)&&this.correlatedWith.equals(rhs.correlatedWith))))&&((this.updateDate == rhs.updateDate)||((this.updateDate!= null)&&this.updateDate.equals(rhs.updateDate))))&&((this.latitude == rhs.latitude)||((this.latitude!= null)&&this.latitude.equals(rhs.latitude))))&&((this.activelyInvolvedIn == rhs.activelyInvolvedIn)||((this.activelyInvolvedIn!= null)&&this.activelyInvolvedIn.equals(rhs.activelyInvolvedIn))))&&((this.description == rhs.description)||((this.description!= null)&&this.description.equals(rhs.description))))&&((this.hasGene == rhs.hasGene)||((this.hasGene!= null)&&this.hasGene.equals(rhs.hasGene))))&&((this.hasCount == rhs.hasCount)||((this.hasCount!= null)&&this.hasCount.equals(rhs.hasCount))))&&((this.occursIn == rhs.occursIn)||((this.occursIn!= null)&&this.occursIn.equals(rhs.occursIn))))&&((this.startInterbaseCoordinate == rhs.startInterbaseCoordinate)||((this.startInterbaseCoordinate!= null)&&this.startInterbaseCoordinate.equals(rhs.startInterbaseCoordinate))))&&((this.synonym == rhs.synonym)||((this.synonym!= null)&&this.synonym.equals(rhs.synonym))))&&((this.hasQuotient == rhs.hasQuotient)||((this.hasQuotient!= null)&&this.hasQuotient.equals(rhs.hasQuotient))))&&((this.causes == rhs.causes)||((this.causes!= null)&&this.causes.equals(rhs.causes))))&&((this.hasBiologicalSequence == rhs.hasBiologicalSequence)||((this.hasBiologicalSequence!= null)&&this.hasBiologicalSequence.equals(rhs.hasBiologicalSequence))))&&((this.hasDrug == rhs.hasDrug)||((this.hasDrug!= null)&&this.hasDrug.equals(rhs.hasDrug))))&&((this.aggregateStatistic == rhs.aggregateStatistic)||((this.aggregateStatistic!= null)&&this.aggregateStatistic.equals(rhs.aggregateStatistic))))&&((this.affectsRiskFor == rhs.affectsRiskFor)||((this.affectsRiskFor!= null)&&this.affectsRiskFor.equals(rhs.affectsRiskFor))))&&((this.endInterbaseCoordinate == rhs.endInterbaseCoordinate)||((this.endInterbaseCoordinate!= null)&&this.endInterbaseCoordinate.equals(rhs.endInterbaseCoordinate))))&&((this.disrupts == rhs.disrupts)||((this.disrupts!= null)&&this.disrupts.equals(rhs.disrupts))))&&((this.iri == rhs.iri)||((this.iri!= null)&&this.iri.equals(rhs.iri))))&&((this.homologousTo == rhs.homologousTo)||((this.homologousTo!= null)&&this.homologousTo.equals(rhs.homologousTo))))&&((this.colocalizesWith == rhs.colocalizesWith)||((this.colocalizesWith!= null)&&this.colocalizesWith.equals(rhs.colocalizesWith))))&&((this.derivesFrom == rhs.derivesFrom)||((this.derivesFrom!= null)&&this.derivesFrom.equals(rhs.derivesFrom))))&&((this.affects == rhs.affects)||((this.affects!= null)&&this.affects.equals(rhs.affects))))&&((this.fullName == rhs.fullName)||((this.fullName!= null)&&this.fullName.equals(rhs.fullName))))&&((this.orthologousTo == rhs.orthologousTo)||((this.orthologousTo!= null)&&this.orthologousTo.equals(rhs.orthologousTo))))&&((this.xenologousTo == rhs.xenologousTo)||((this.xenologousTo!= null)&&this.xenologousTo.equals(rhs.xenologousTo))))&&((this.hasPercentage == rhs.hasPercentage)||((this.hasPercentage!= null)&&this.hasPercentage.equals(rhs.hasPercentage))))&&((this.participatesIn == rhs.participatesIn)||((this.participatesIn!= null)&&this.participatesIn.equals(rhs.participatesIn))))&&((this.regulates == rhs.regulates)||((this.regulates!= null)&&this.regulates.equals(rhs.regulates))))&&((this.genomeBuild == rhs.genomeBuild)||((this.genomeBuild!= null)&&this.genomeBuild.equals(rhs.genomeBuild))))&&((this.hasZygosity == rhs.hasZygosity)||((this.hasZygosity!= null)&&this.hasZygosity.equals(rhs.hasZygosity))))&&((this.negativelyRegulates == rhs.negativelyRegulates)||((this.negativelyRegulates!= null)&&this.negativelyRegulates.equals(rhs.negativelyRegulates))))&&((this.filler == rhs.filler)||((this.filler!= null)&&this.filler.equals(rhs.filler))))&&((this.category == rhs.category)||((this.category!= null)&&this.category.equals(rhs.category))))&&((this.sameAs == rhs.sameAs)||((this.sameAs!= null)&&this.sameAs.equals(rhs.sameAs))))&&((this.timepoint == rhs.timepoint)||((this.timepoint!= null)&&this.timepoint.equals(rhs.timepoint))));
    }

}
