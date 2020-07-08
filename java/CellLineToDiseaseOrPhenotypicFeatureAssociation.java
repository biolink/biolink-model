import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * CellLineToDiseaseOrPhenotypicFeatureAssociation
 * <p>
 * An relationship between a cell line and a disease or a phenotype, where the cell line is derived from an individual with that disease or phenotype
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "subject"
})
public class CellLineToDiseaseOrPhenotypicFeatureAssociation {

    /**
     * 
     * (Required)
     * 
     */
    @JsonProperty("subject")
    private String subject;

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
        StringBuilder sb = new StringBuilder();
        sb.append(CellLineToDiseaseOrPhenotypicFeatureAssociation.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("subject");
        sb.append('=');
        sb.append(((this.subject == null)?"<null>":this.subject));
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
        result = ((result* 31)+((this.subject == null)? 0 :this.subject.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof CellLineToDiseaseOrPhenotypicFeatureAssociation) == false) {
            return false;
        }
        CellLineToDiseaseOrPhenotypicFeatureAssociation rhs = ((CellLineToDiseaseOrPhenotypicFeatureAssociation) other);
        return ((this.subject == rhs.subject)||((this.subject!= null)&&this.subject.equals(rhs.subject)));
    }

}
