import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * DataSetVersion
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "distribution",
    "source_data_file",
    "title",
    "type",
    "versionOf"
})
public class DataSetVersion {

    @JsonProperty("distribution")
    private String distribution;
    @JsonProperty("source_data_file")
    private String sourceDataFile;
    @JsonProperty("title")
    private String title;
    @JsonProperty("type")
    private String type;
    @JsonProperty("versionOf")
    private String versionOf;

    @JsonProperty("distribution")
    public String getDistribution() {
        return distribution;
    }

    @JsonProperty("distribution")
    public void setDistribution(String distribution) {
        this.distribution = distribution;
    }

    @JsonProperty("source_data_file")
    public String getSourceDataFile() {
        return sourceDataFile;
    }

    @JsonProperty("source_data_file")
    public void setSourceDataFile(String sourceDataFile) {
        this.sourceDataFile = sourceDataFile;
    }

    @JsonProperty("title")
    public String getTitle() {
        return title;
    }

    @JsonProperty("title")
    public void setTitle(String title) {
        this.title = title;
    }

    @JsonProperty("type")
    public String getType() {
        return type;
    }

    @JsonProperty("type")
    public void setType(String type) {
        this.type = type;
    }

    @JsonProperty("versionOf")
    public String getVersionOf() {
        return versionOf;
    }

    @JsonProperty("versionOf")
    public void setVersionOf(String versionOf) {
        this.versionOf = versionOf;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(DataSetVersion.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("distribution");
        sb.append('=');
        sb.append(((this.distribution == null)?"<null>":this.distribution));
        sb.append(',');
        sb.append("sourceDataFile");
        sb.append('=');
        sb.append(((this.sourceDataFile == null)?"<null>":this.sourceDataFile));
        sb.append(',');
        sb.append("title");
        sb.append('=');
        sb.append(((this.title == null)?"<null>":this.title));
        sb.append(',');
        sb.append("type");
        sb.append('=');
        sb.append(((this.type == null)?"<null>":this.type));
        sb.append(',');
        sb.append("versionOf");
        sb.append('=');
        sb.append(((this.versionOf == null)?"<null>":this.versionOf));
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
        result = ((result* 31)+((this.distribution == null)? 0 :this.distribution.hashCode()));
        result = ((result* 31)+((this.title == null)? 0 :this.title.hashCode()));
        result = ((result* 31)+((this.type == null)? 0 :this.type.hashCode()));
        result = ((result* 31)+((this.versionOf == null)? 0 :this.versionOf.hashCode()));
        result = ((result* 31)+((this.sourceDataFile == null)? 0 :this.sourceDataFile.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof DataSetVersion) == false) {
            return false;
        }
        DataSetVersion rhs = ((DataSetVersion) other);
        return ((((((this.distribution == rhs.distribution)||((this.distribution!= null)&&this.distribution.equals(rhs.distribution)))&&((this.title == rhs.title)||((this.title!= null)&&this.title.equals(rhs.title))))&&((this.type == rhs.type)||((this.type!= null)&&this.type.equals(rhs.type))))&&((this.versionOf == rhs.versionOf)||((this.versionOf!= null)&&this.versionOf.equals(rhs.versionOf))))&&((this.sourceDataFile == rhs.sourceDataFile)||((this.sourceDataFile!= null)&&this.sourceDataFile.equals(rhs.sourceDataFile))));
    }

}
