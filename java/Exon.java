import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * Exon
 * <p>
 * A region of the transcript sequence within a gene which is not removed from the primary RNA transcript by RNA splicing
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class Exon {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(Exon.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof Exon) == false) {
            return false;
        }
        Exon rhs = ((Exon) other);
        return true;
    }

}
