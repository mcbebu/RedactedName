import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class NodeTest {

    @Test
    public void equalsTest() {
        Node n = new Node(1, 2, "hell");
        Node m = new Node(1, 2, "heaven");
        assertTrue(n.equals(m));
    }
}
