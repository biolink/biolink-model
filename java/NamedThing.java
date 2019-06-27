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
    "causes",
    "coexists_with",
    "colocalizes_with",
    "contributes_to",
    "creation_date",
    "derives_from",
    "derives_into",
    "description",
    "disrupts",
    "filler",
    "full_name",
    "has_chemical_formula",
    "has_molecular_consequence",
    "has_part",
    "homologous_to",
    "id",
    "interacts_with",
    "interbase_coordinate",
    "iri",
    "located_in",
    "location_of",
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
    "physically_interacts_with",
    "positively_regulates",
    "predisposes",
    "prevents",
    "produces",
    "regulates",
    "related_to",
    "same_as",
    "synonym",
    "systematic_synonym",
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
     * holds between a continuant and process or function, where the continuant alone has the ability to carry out the process or function.
     * 
     */
    @JsonProperty("capable_of")
    @JsonPropertyDescription("holds between a continuant and process or function, where the continuant alone has the ability to carry out the process or function.")
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
     * description of chemical compound based on element symbols
     * 
     */
    @JsonProperty("has_chemical_formula")
    @JsonPropertyDescription("description of chemical compound based on element symbols")
    private String hasChemicalFormula;
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
     * used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome
     * 
     */
    @JsonProperty("manifestation_of")
    @JsonPropertyDescription("used in SemMedDB for linking things like dysfunctions and processes to some disease or syndrome")
    private List<String> manifestationOf = new ArrayList<String>();
    /**
     * holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exibiting similar features of the studied entity.
     * 
     */
    @JsonProperty("model_of")
    @JsonPropertyDescription("holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exibiting similar features of the studied entity.")
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
    private String systematicSynonym;
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
     * holds between a continuant and process or function, where the continuant alone has the ability to carry out the process or function.
     * 
     */
    @JsonProperty("capable_of")
    public List<String> getCapableOf() {
        return capableOf;
    }

    /**
     * holds between a continuant and process or function, where the continuant alone has the ability to carry out the process or function.
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
     * holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exibiting similar features of the studied entity.
     * 
     */
    @JsonProperty("model_of")
    public List<String> getModelOf() {
        return modelOf;
    }

    /**
     * holds between an entity and some other entity it approximates for purposes of scientific study, in virtue of its exibiting similar features of the studied entity.
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
        return new ToStringBuilder(this).append("activelyInvolvedIn", activelyInvolvedIn).append("affects", affects).append("affectsRiskFor", affectsRiskFor).append("aggregateStatistic", aggregateStatistic).append("capableOf", capableOf).append("category", category).append("causes", causes).append("coexistsWith", coexistsWith).append("colocalizesWith", colocalizesWith).append("contributesTo", contributesTo).append("creationDate", creationDate).append("derivesFrom", derivesFrom).append("derivesInto", derivesInto).append("description", description).append("disrupts", disrupts).append("filler", filler).append("fullName", fullName).append("hasChemicalFormula", hasChemicalFormula).append("hasMolecularConsequence", hasMolecularConsequence).append("hasPart", hasPart).append("homologousTo", homologousTo).append("id", id).append("interactsWith", interactsWith).append("interbaseCoordinate", interbaseCoordinate).append("iri", iri).append("locatedIn", locatedIn).append("locationOf", locationOf).append("manifestationOf", manifestationOf).append("modelOf", modelOf).append("name", name).append("negativelyRegulates", negativelyRegulates).append("nodeProperty", nodeProperty).append("occursIn", occursIn).append("orthologousTo", orthologousTo).append("overlaps", overlaps).append("paralogousTo", paralogousTo).append("partOf", partOf).append("participatesIn", participatesIn).append("physicallyInteractsWith", physicallyInteractsWith).append("positivelyRegulates", positivelyRegulates).append("predisposes", predisposes).append("prevents", prevents).append("produces", produces).append("regulates", regulates).append("relatedTo", relatedTo).append("sameAs", sameAs).append("synonym", synonym).append("systematicSynonym", systematicSynonym).append("updateDate", updateDate).append("xenologousTo", xenologousTo).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(partOf).append(capableOf).append(systematicSynonym).append(hasChemicalFormula).append(interbaseCoordinate).append(locationOf).append(prevents).append(coexistsWith).append(positivelyRegulates).append(relatedTo).append(interactsWith).append(predisposes).append(overlaps).append(id).append(hasMolecularConsequence).append(nodeProperty).append(hasPart).append(creationDate).append(contributesTo).append(paralogousTo).append(physicallyInteractsWith).append(locatedIn).append(manifestationOf).append(derivesInto).append(name).append(produces).append(modelOf).append(updateDate).append(activelyInvolvedIn).append(description).append(occursIn).append(synonym).append(causes).append(aggregateStatistic).append(affectsRiskFor).append(disrupts).append(iri).append(homologousTo).append(colocalizesWith).append(derivesFrom).append(affects).append(fullName).append(orthologousTo).append(xenologousTo).append(participatesIn).append(regulates).append(negativelyRegulates).append(filler).append(category).append(sameAs).toHashCode();
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
        return new EqualsBuilder().append(partOf, rhs.partOf).append(capableOf, rhs.capableOf).append(systematicSynonym, rhs.systematicSynonym).append(hasChemicalFormula, rhs.hasChemicalFormula).append(interbaseCoordinate, rhs.interbaseCoordinate).append(locationOf, rhs.locationOf).append(prevents, rhs.prevents).append(coexistsWith, rhs.coexistsWith).append(positivelyRegulates, rhs.positivelyRegulates).append(relatedTo, rhs.relatedTo).append(interactsWith, rhs.interactsWith).append(predisposes, rhs.predisposes).append(overlaps, rhs.overlaps).append(id, rhs.id).append(hasMolecularConsequence, rhs.hasMolecularConsequence).append(nodeProperty, rhs.nodeProperty).append(hasPart, rhs.hasPart).append(creationDate, rhs.creationDate).append(contributesTo, rhs.contributesTo).append(paralogousTo, rhs.paralogousTo).append(physicallyInteractsWith, rhs.physicallyInteractsWith).append(locatedIn, rhs.locatedIn).append(manifestationOf, rhs.manifestationOf).append(derivesInto, rhs.derivesInto).append(name, rhs.name).append(produces, rhs.produces).append(modelOf, rhs.modelOf).append(updateDate, rhs.updateDate).append(activelyInvolvedIn, rhs.activelyInvolvedIn).append(description, rhs.description).append(occursIn, rhs.occursIn).append(synonym, rhs.synonym).append(causes, rhs.causes).append(aggregateStatistic, rhs.aggregateStatistic).append(affectsRiskFor, rhs.affectsRiskFor).append(disrupts, rhs.disrupts).append(iri, rhs.iri).append(homologousTo, rhs.homologousTo).append(colocalizesWith, rhs.colocalizesWith).append(derivesFrom, rhs.derivesFrom).append(affects, rhs.affects).append(fullName, rhs.fullName).append(orthologousTo, rhs.orthologousTo).append(xenologousTo, rhs.xenologousTo).append(participatesIn, rhs.participatesIn).append(regulates, rhs.regulates).append(negativelyRegulates, rhs.negativelyRegulates).append(filler, rhs.filler).append(category, rhs.category).append(sameAs, rhs.sameAs).isEquals();
    }

}
