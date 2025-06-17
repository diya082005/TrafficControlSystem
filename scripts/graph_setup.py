import networkx as nx

def get_graph():
    G = nx.Graph()

    G.add_node("A", pos=(0, 0))
    G.add_node("B", pos=(1, 2))
    G.add_node("C", pos=(3, 0))
    G.add_node("D", pos=(5, 3))
    G.add_node("P1", pos=(1, 1))
    G.add_node("P2", pos=(3, 1)) 

    G.add_edge("A", "B", weight=2)
    G.add_edge("A", "C", weight=1)
    G.add_edge("B", "C", weight=3)
    G.add_edge("B", "D", weight=2)
    G.add_edge("C", "D", weight=1)

    G.add_edge("A", "P1", weight=1) 
    G.add_edge("B", "P1", weight=1)
    G.add_edge("C", "P2", weight=1)  
    G.add_edge("D", "P2", weight=1)

    pos = nx.get_node_attributes(G, 'pos')
    if not pos:
        pos = nx.spring_layout(G)

    nx.set_node_attributes(G, pos, 'pos')

    return G
G = get_graph()

print(G.nodes())
print(G.edges())
