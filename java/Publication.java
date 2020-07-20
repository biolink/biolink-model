import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * Publication
 * <p>
 * Any published piece of information. Can refer to a whole publication, or to a part of it (e.g. a figure, figure legend, or section highlighted by NLP). The scope is intended to be general and include information published on the web as well as journals.
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class Publication {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(Publication.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof Publication) == false) {
            return false;
        }
        Publication rhs = ((Publication) other);
        return true;
    }

}
