import networkx as nx
import matplotlib.pyplot as plt

# User-defined vertices (defined by programmer)
vertices = ["A", "B", "C", "D", "E"]   # Must be more than 3
# Check condition
if len(vertices) <= 3:
    print("Number of vertices must be greater than 3.")
else:
    # Create empty graph
    G = nx.Graph()
    # Add vertices
    G.add_nodes_from(vertices)
    # Add edges to make it complete
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            G.add_edge(vertices[i], vertices[j])
    # Draw graph
    nx.draw(
        G,
        with_labels=True,
        node_color="lightblue",
        node_size=1000,
        font_size=12
    )
    plt.title("Complete Graph")
    plt.show()
