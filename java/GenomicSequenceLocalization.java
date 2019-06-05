import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import org.apache.commons.lang.builder.EqualsBuilder;
import org.apache.commons.lang.builder.HashCodeBuilder;
import org.apache.commons.lang.builder.ToStringBuilder;


/**
 * GenomicSequenceLocalization
 * <p>
 * A relationship between a sequence feature and an entity it is localized to. The reference entity may be a chromosome, chromosome region or information entity such as a contig
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "end_interbase_coordinate",
    "genome_build",
    "object",
    "phase",
    "start_interbase_coordinate",
    "subject"
})
public class GenomicSequenceLocalization {

    @JsonProperty("end_interbase_coordinate")
    private String endInterbaseCoordinate;
    /**
     * TODO
     * 
     */
    @JsonProperty("genome_build")
    @JsonPropertyDescription("TODO")
    private String genomeBuild;
    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    private String object;
    /**
     * TODO
     * 
     */
    @JsonProperty("phase")
    @JsonPropertyDescription("TODO")
    private String phase;
    @JsonProperty("start_interbase_coordinate")
    private String startInterbaseCoordinate;
    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    private String subject;

    @JsonProperty("end_interbase_coordinate")
    public String getEndInterbaseCoordinate() {
        return endInterbaseCoordinate;
    }

    @JsonProperty("end_interbase_coordinate")
    public void setEndInterbaseCoordinate(String endInterbaseCoordinate) {
        this.endInterbaseCoordinate = endInterbaseCoordinate;
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
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    public String getObject() {
        return object;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("object")
    public void setObject(String object) {
        this.object = object;
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

    @JsonProperty("start_interbase_coordinate")
    public String getStartInterbaseCoordinate() {
        return startInterbaseCoordinate;
    }

    @JsonProperty("start_interbase_coordinate")
    public void setStartInterbaseCoordinate(String startInterbaseCoordinate) {
        this.startInterbaseCoordinate = startInterbaseCoordinate;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    public String getSubject() {
        return subject;
    }

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    public void setSubject(String subject) {
        this.subject = subject;
    }

    @Override
    public String toString() {
        return new ToStringBuilder(this).append("endInterbaseCoordinate", endInterbaseCoordinate).append("genomeBuild", genomeBuild).append("object", object).append("phase", phase).append("startInterbaseCoordinate", startInterbaseCoordinate).append("subject", subject).toString();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder().append(phase).append(genomeBuild).append(subject).append(endInterbaseCoordinate).append(object).append(startInterbaseCoordinate).toHashCode();
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof GenomicSequenceLocalization) == false) {
            return false;
        }
        GenomicSequenceLocalization rhs = ((GenomicSequenceLocalization) other);
        return new EqualsBuilder().append(phase, rhs.phase).append(genomeBuild, rhs.genomeBuild).append(subject, rhs.subject).append(endInterbaseCoordinate, rhs.endInterbaseCoordinate).append(object, rhs.object).append(startInterbaseCoordinate, rhs.startInterbaseCoordinate).isEquals();
    }

}
