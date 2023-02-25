import java.util.ArrayList;
import java.util.HashMap;

public class Node {
    private long latitude;
    private long longitude;
    private String location;
    private HashMap<Node, Long> hashMap = new HashMap<>();

    public Node(long latitude, long longitude, String location) {
        this.latitude = latitude;
        this.longitude = longitude;
        this.location = location;

    }

    public void addNode(Node node, long value) {
        hashMap.put(node, value);
        if (!node.isAdjacent(this)) {
            node.addNode(this, value);
        }
    }

    public ArrayList<Node> getAdjacentNodes() {
        return new ArrayList<>(hashMap.keySet());
    }

    public boolean isAdjacent(Node node) {
        return hashMap.containsKey(node);
    }



}
