import random
import networkx as nx

def simulate_accident(G):
    edges = list(G.edges())
    if edges:
        blocked_edge = random.choice(edges)
        G.remove_edge(*blocked_edge) 
        print(f"🚨 Accident on road {blocked_edge}! Road blocked.")
    else:
        print("No roads available to block.")