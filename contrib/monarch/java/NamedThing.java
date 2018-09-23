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
    "category",
    "description",
    "full_name",
    "has_alternate_identifier",
    "has_synonym",
    "has_xref",
    "id",
    "iri",
    "name",
    "node_property",
    "related_to",
    "systematic_synonym"
})
public class NamedThing {

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * 
     */
    @JsonProperty("category")
    @JsonPropertyDescription("Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag")
    private List<String> category = new ArrayList<String>();
    /**
     * a human-readable description of a thing
     * 
     */
    @JsonProperty("description")
    @JsonPropertyDescription("a human-readable description of a thing")
    private String description;
    /**
     * a long-form human readable name for a thing
     * 
     */
    @JsonProperty("full_name")
    @JsonPropertyDescription("a long-form human readable name for a thing")
    private String fullName;
    /**
     * An alternate identifier for the entity, provided by the source database
     * 
     */
    @JsonProperty("has_alternate_identifier")
    @JsonPropertyDescription("An alternate identifier for the entity, provided by the source database")
    private List<String> hasAlternateIdentifier = new ArrayList<String>();
    /**
     * Alternate labels for an entity
     * 
     */
    @JsonProperty("has_synonym")
    @JsonPropertyDescription("Alternate labels for an entity")
    private List<String> hasSynonym = new ArrayList<String>();
    /**
     * A database cross-reference for the entity, provided by a separate database
     * 
     */
    @JsonProperty("has_xref")
    @JsonPropertyDescription("A database cross-reference for the entity, provided by a separate database")
    private List<String> hasXref = new ArrayList<String>();
    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * 
     */
    @JsonProperty("id")
    @JsonPropertyDescription("A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI")
    private String id;
    /**
     * An IRI for the node. This is determined by the id using expansion rules.
     * 
     */
    @JsonProperty("iri")
    @JsonPropertyDescription("An IRI for the node. This is determined by the id using expansion rules.")
    private String iri;
    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("name")
    @JsonPropertyDescription("A human-readable name for a thing")
    private String name;
    /**
     * A grouping for any property that holds between a node and a value
     * 
     */
    @JsonProperty("node_property")
    @JsonPropertyDescription("A grouping for any property that holds between a node and a value")
    private String nodeProperty;
    /**
     * A grouping for any relationship type that holds between any two things
     * 
     */
    @JsonProperty("related_to")
    @JsonPropertyDescription("A grouping for any relationship type that holds between any two things")
    private String relatedTo;
    /**
     * more commonly used for gene symbols in yeast
     * 
     */
    @JsonProperty("systematic_synonym")
    @JsonPropertyDescription("more commonly used for gene symbols in yeast")
    private String systematicSynonym;

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * 
     */
    @JsonProperty("category")
    public List<String> getCategory() {
        return category;
    }

    /**
     * Name of the high level ontology class in which this entity is categorized. Corresponds to the label for the biolink entity type class. In a neo4j database this MAY correspond to the neo4j label tag
     * 
     */
    @JsonProperty("category")
    public void setCategory(List<String> category) {
        this.category = category;
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
     * An alternate identifier for the entity, provided by the source database
     * 
     */
    @JsonProperty("has_alternate_identifier")
    public List<String> getHasAlternateIdentifier() {
        return hasAlternateIdentifier;
    }

    /**
     * An alternate identifier for the entity, provided by the source database
     * 
     */
    @JsonProperty("has_alternate_identifier")
    public void setHasAlternateIdentifier(List<String> hasAlternateIdentifier) {
        this.hasAlternateIdentifier = hasAlternateIdentifier;
    }

    /**
     * Alternate labels for an entity
     * 
     */
    @JsonProperty("has_synonym")
    public List<String> getHasSynonym() {
        return hasSynonym;
    }

    /**
     * Alternate labels for an entity
     * 
     */
    @JsonProperty("has_synonym")
    public void setHasSynonym(List<String> hasSynonym) {
        this.hasSynonym = hasSynonym;
    }

    /**
     * A database cross-reference for the entity, provided by a separate database
     * 
     */
    @JsonProperty("has_xref")
    public List<String> getHasXref() {
        return hasXref;
    }

    /**
     * A database cross-reference for the entity, provided by a separate database
     * 
     */
    @JsonProperty("has_xref")
    public void setHasXref(List<String> hasXref) {
        this.hasXref = hasXref;
    }

    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * 
     */
    @JsonProperty("id")
    public String getId() {
        return id;
    }

    /**
     * A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
     * 
     */
    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
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
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("name")
    public String getName() {
        return name;
    }

    /**
     * A human-readable name for a thing
     * 
     */
    @JsonProperty("name")
    public void setName(String name) {
        this.name = name;
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
     * A grouping for any relationship type that holds between any two things
     * 
     */
    @JsonProperty("related_to")
    public String getRelatedTo() {
        return relatedTo;
    }

    /**
     * A grouping for any relationship type that holds between any two things
     * 
     */
    @JsonProperty("related_to")
    public void setRelatedTo(String relatedTo) {
        this.relatedTo = relatedTo;
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
        return new ToStringBuilder(this).append("category", category).append("description", description).append("fullName", fullName).append("hasAlternateIdentifier", hasAlternateIdentifier).append("hasSynonym", hasSynonym).append("hasXref", hasXref).append("id", id).append("iri", iri).append("name", name).append("nodeProperty", nodeProperty).append("relatedTo", relatedTo).append("systematicSynonym", systematicSynonym).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(iri).append(nodeProperty).append(hasAlternateIdentifier).append(systematicSynonym).append(description).append(fullName).append(hasSynonym).append(relatedTo).append(name).append(hasXref).append(id).append(category).toHashCode();
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
        return new EqualsBuilder().append(iri, rhs.iri).append(nodeProperty, rhs.nodeProperty).append(hasAlternateIdentifier, rhs.hasAlternateIdentifier).append(systematicSynonym, rhs.systematicSynonym).append(description, rhs.description).append(fullName, rhs.fullName).append(hasSynonym, rhs.hasSynonym).append(relatedTo, rhs.relatedTo).append(name, rhs.name).append(hasXref, rhs.hasXref).append(id, rhs.id).append(category, rhs.category).isEquals();
    }

}
