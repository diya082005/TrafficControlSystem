import random

def store_original_weights(G):
    for u, v, data in G.edges(data=True):
        if 'original_weight' not in data:
            data['original_weight'] = data['weight']

def reset_weights(G):
    for u, v, data in G.edges(data=True):
        data['weight'] = data['original_weight']

def update_traffic_conditions(G):
    reset_weights(G) 
    for u, v, data in G.edges(data=True):
        congestion_factor = random.uniform(0.5, 2.0) 
        data['weight'] = round(data['original_weight'] * congestion_factor, 2)
        print(f"Updated traffic on road {u}-{v}: New weight = {data['weight']} (Original: {data['original_weight']})")

def congestion_simulation(G, current_iteration):

    print(f"Running congestion simulation for iteration {current_iteration}.")
    store_original_weights(G)
    update_traffic_conditions(G)
    print("---- Traffic updated ----")