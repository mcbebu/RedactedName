import com.sun.source.tree.Tree;

import java.util.ArrayList;

public class TreeHandler {
    private ArrayList<Node> nodes;
    private int threshold;

    public TreeHandler(ArrayList<Node> nodes, int threshold) {
        this.nodes = nodes;
        this.threshold = threshold;
    }

    public void generateCompleteGraph () {
        for (Node node1: nodes) {
            for (Node node2: nodes) {
                if (node1.equals(node2)) {

                }
            }
        }
    }

    public ArrayList<Cluster> generateClusters() {
        int unvisitedNodes = nodes.size();
        ArrayList<Cluster> clusters = new ArrayList<>();

        while (unvisitedNodes > 0) {
            unvisitedNodes --;
        }
        return null;
    }
}
