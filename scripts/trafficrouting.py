import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms import shortest_paths
from congestioncontrol import congestion_simulation

def find_shortest_path(G, source, target):
 
    try:
        path = nx.dijkstra_path(G, source=source, target=target, weight='weight')
        total_cost = sum(G[u][v]['weight'] for u, v in zip(path, path[1:]))
        return path, total_cost
    except nx.NetworkXNoPath:
        return None, None

def visualize_network(G):
    pos = nx.get_node_attributes(G, "pos")
    edge_colors = ['yellow' if G[u][v]['weight'] > 3 else 'green' for u, v in G.edges()]

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, edge_color=edge_colors, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)
    plt.show()

def real_time_simulation(G, source, target, iterations=10):

    for i in range(iterations):
        print(f"\n--- Iteration {i + 1} ---") 
        
        congestion_simulation(G) 
        print("Traffic updated.") 
        
        shortest_path, total_cost = find_shortest_path(G, source, target)
        
        if shortest_path:
            print(f"Shortest path from {source} to {target}: {shortest_path} with total cost: {total_cost:.2f}")
        else:
            print(f"No path found from {source} to {target}.")
        
        visualize_network(G)
