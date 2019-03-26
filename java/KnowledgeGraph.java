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
 * KnowledgeGraph
 * <p>
 * A collection of knowledge elements definitions
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "default_curi_maps",
    "default_prefix",
    "entities",
    "generation_date",
    "id",
    "kg_source",
    "kg_source_version",
    "kg_version",
    "prefixes",
    "relationship_types"
})
public class KnowledgeGraph {

    /**
     * List of prefixcommon biocontexts to be fetched to resolve id_prefixes and inline prefix variables
     * 
     */
    @JsonProperty("default_curi_maps")
    @JsonPropertyDescription("List of prefixcommon biocontexts to be fetched to resolve id_prefixes and inline prefix variables")
    private List<String> defaultCuriMaps = new ArrayList<String>();
    /**
     * default and base prefix -- used for ':' identifiers, @base and @vocab
     * 
     */
    @JsonProperty("default_prefix")
    @JsonPropertyDescription("default and base prefix -- used for ':' identifiers, @base and @vocab")
    private String defaultPrefix;
    /**
     * the collection of nodes (vertices) that represent entities or concepts
     * 
     */
    @JsonProperty("entities")
    @JsonPropertyDescription("the collection of nodes (vertices) that represent entities or concepts")
    private List<String> entities = new ArrayList<String>();
    /**
     * date that the knowledge graph was loaded/generated.  Supplied by the loader
     * 
     */
    @JsonProperty("generation_date")
    @JsonPropertyDescription("date that the knowledge graph was loaded/generated.  Supplied by the loader")
    private String generationDate;
    /**
     * a globally unique identifier for a knowledge graph
     * 
     */
    @JsonProperty("id")
    @JsonPropertyDescription("a globally unique identifier for a knowledge graph")
    private String id;
    /**
     * name, uri or description of the source of the knowledge source.  Supplied by the loader
     * 
     */
    @JsonProperty("kg_source")
    @JsonPropertyDescription("name, uri or description of the source of the knowledge source.  Supplied by the loader")
    private String kgSource;
    /**
     * version identifier of the knowledge graph.  Supplied by the loader
     * 
     */
    @JsonProperty("kg_source_version")
    @JsonPropertyDescription("version identifier of the knowledge graph.  Supplied by the loader")
    private String kgSourceVersion;
    /**
     * Version of the biolink model used to load the schema. Supplied by the loader
     * 
     */
    @JsonProperty("kg_version")
    @JsonPropertyDescription("Version of the biolink model used to load the schema. Supplied by the loader")
    private String kgVersion;
    /**
     * Additional prefixes to be added to the context beyond those fetched from prefixcommons in id_prefixes
     * 
     */
    @JsonProperty("prefixes")
    @JsonPropertyDescription("Additional prefixes to be added to the context beyond those fetched from prefixcommons in id_prefixes")
    private List<String> prefixes = new ArrayList<String>();
    /**
     * -> the collection of edges that represent relationship types in the knowledge graph
     * 
     */
    @JsonProperty("relationship_types")
    @JsonPropertyDescription("-> the collection of edges that represent relationship types in the knowledge graph")
    private List<String> relationshipTypes = new ArrayList<String>();

    /**
     * List of prefixcommon biocontexts to be fetched to resolve id_prefixes and inline prefix variables
     * 
     */
    @JsonProperty("default_curi_maps")
    public List<String> getDefaultCuriMaps() {
        return defaultCuriMaps;
    }

    /**
     * List of prefixcommon biocontexts to be fetched to resolve id_prefixes and inline prefix variables
     * 
     */
    @JsonProperty("default_curi_maps")
    public void setDefaultCuriMaps(List<String> defaultCuriMaps) {
        this.defaultCuriMaps = defaultCuriMaps;
    }

    /**
     * default and base prefix -- used for ':' identifiers, @base and @vocab
     * 
     */
    @JsonProperty("default_prefix")
    public String getDefaultPrefix() {
        return defaultPrefix;
    }

    /**
     * default and base prefix -- used for ':' identifiers, @base and @vocab
     * 
     */
    @JsonProperty("default_prefix")
    public void setDefaultPrefix(String defaultPrefix) {
        this.defaultPrefix = defaultPrefix;
    }

    /**
     * the collection of nodes (vertices) that represent entities or concepts
     * 
     */
    @JsonProperty("entities")
    public List<String> getEntities() {
        return entities;
    }

    /**
     * the collection of nodes (vertices) that represent entities or concepts
     * 
     */
    @JsonProperty("entities")
    public void setEntities(List<String> entities) {
        this.entities = entities;
    }

    /**
     * date that the knowledge graph was loaded/generated.  Supplied by the loader
     * 
     */
    @JsonProperty("generation_date")
    public String getGenerationDate() {
        return generationDate;
    }

    /**
     * date that the knowledge graph was loaded/generated.  Supplied by the loader
     * 
     */
    @JsonProperty("generation_date")
    public void setGenerationDate(String generationDate) {
        this.generationDate = generationDate;
    }

    /**
     * a globally unique identifier for a knowledge graph
     * 
     */
    @JsonProperty("id")
    public String getId() {
        return id;
    }

    /**
     * a globally unique identifier for a knowledge graph
     * 
     */
    @JsonProperty("id")
    public void setId(String id) {
        this.id = id;
    }

    /**
     * name, uri or description of the source of the knowledge source.  Supplied by the loader
     * 
     */
    @JsonProperty("kg_source")
    public String getKgSource() {
        return kgSource;
    }

    /**
     * name, uri or description of the source of the knowledge source.  Supplied by the loader
     * 
     */
    @JsonProperty("kg_source")
    public void setKgSource(String kgSource) {
        this.kgSource = kgSource;
    }

    /**
     * version identifier of the knowledge graph.  Supplied by the loader
     * 
     */
    @JsonProperty("kg_source_version")
    public String getKgSourceVersion() {
        return kgSourceVersion;
    }

    /**
     * version identifier of the knowledge graph.  Supplied by the loader
     * 
     */
    @JsonProperty("kg_source_version")
    public void setKgSourceVersion(String kgSourceVersion) {
        this.kgSourceVersion = kgSourceVersion;
    }

    /**
     * Version of the biolink model used to load the schema. Supplied by the loader
     * 
     */
    @JsonProperty("kg_version")
    public String getKgVersion() {
        return kgVersion;
    }

    /**
     * Version of the biolink model used to load the schema. Supplied by the loader
     * 
     */
    @JsonProperty("kg_version")
    public void setKgVersion(String kgVersion) {
        this.kgVersion = kgVersion;
    }

    /**
     * Additional prefixes to be added to the context beyond those fetched from prefixcommons in id_prefixes
     * 
     */
    @JsonProperty("prefixes")
    public List<String> getPrefixes() {
        return prefixes;
    }

    /**
     * Additional prefixes to be added to the context beyond those fetched from prefixcommons in id_prefixes
     * 
     */
    @JsonProperty("prefixes")
    public void setPrefixes(List<String> prefixes) {
        this.prefixes = prefixes;
    }

    /**
     * -> the collection of edges that represent relationship types in the knowledge graph
     * 
     */
    @JsonProperty("relationship_types")
    public List<String> getRelationshipTypes() {
        return relationshipTypes;
    }

    /**
     * -> the collection of edges that represent relationship types in the knowledge graph
     * 
     */
    @JsonProperty("relationship_types")
    public void setRelationshipTypes(List<String> relationshipTypes) {
        this.relationshipTypes = relationshipTypes;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("defaultCuriMaps", defaultCuriMaps).append("defaultPrefix", defaultPrefix).append("entities", entities).append("generationDate", generationDate).append("id", id).append("kgSource", kgSource).append("kgSourceVersion", kgSourceVersion).append("kgVersion", kgVersion).append("prefixes", prefixes).append("relationshipTypes", relationshipTypes).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(prefixes).append(kgSource).append(entities).append(generationDate).append(defaultPrefix).append(kgSourceVersion).append(defaultCuriMaps).append(id).append(relationshipTypes).append(kgVersion).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof KnowledgeGraph) == false) {
            return false;
        }
        KnowledgeGraph rhs = ((KnowledgeGraph) other);
        return new EqualsBuilder().append(prefixes, rhs.prefixes).append(kgSource, rhs.kgSource).append(entities, rhs.entities).append(generationDate, rhs.generationDate).append(defaultPrefix, rhs.defaultPrefix).append(kgSourceVersion, rhs.kgSourceVersion).append(defaultCuriMaps, rhs.defaultCuriMaps).append(id, rhs.id).append(relationshipTypes, rhs.relationshipTypes).append(kgVersion, rhs.kgVersion).isEquals();
    }

}
