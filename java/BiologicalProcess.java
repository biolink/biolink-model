import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * BiologicalProcess
 * <p>
 * One or more causally connected executions of molecular functions
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({

})
public class BiologicalProcess {


    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(BiologicalProcess.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
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
        if ((other instanceof BiologicalProcess) == false) {
            return false;
        }
        BiologicalProcess rhs = ((BiologicalProcess) other);
        return true;
    }

}
