import random
import math
import matplotlib.pyplot as plt
import networkx as nx
from lane import Lane
from trafficlight import TrafficLight
from simulation import simulate_pedestrians, adjust_traffic_lights, collect_traffic_stats
from vehiclemovement import Vehicle
from congestioncontrol import congestion_simulation
from scheduling import priority_scheduling
from accident import simulate_accident
from weather import apply_weather_conditions
from pedestrian import Pedestrian

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
    return G
def find_shortest_path(G, source, target):
    try:
        non_pedestrian_nodes = [node for node in G.nodes() if not node.startswith("P")]
        subgraph = G.subgraph(non_pedestrian_nodes)
        path = nx.dijkstra_path(subgraph, source=source, target=target, weight='weight')
        total_cost = sum(subgraph[u][v]['weight'] for u, v in zip(path, path[1:]))
        return path, total_cost
    except nx.NetworkXNoPath:
        return None, None
def calculate_noise_pollution(vehicles):
    total_noise = 0
    for vehicle in vehicles:
        total_noise += 10 ** (vehicle.noise_level / 10)
    if total_noise > 0:
        total_noise = 10 * math.log10(total_noise)
    else:
        total_noise = 0 
    return total_noise
def display_noise_pollution(noise_level):
    if noise_level < 70:
        print(f"🔇 Noise Pollution: {noise_level:.2f} dB (Low)")
    elif 70 <= noise_level < 90:
        print(f"🔉 Noise Pollution: {noise_level:.2f} dB (Moderate)")
    else:
        print(f"🔊 Noise Pollution: {noise_level:.2f} dB (High)")
def visualize_network(G, pos, vehicles, pedestrians):
    edge_colors = []
    for u, v in G.edges():
        if u.startswith("P") or v.startswith("P"):
            edge_colors.append('blue')
        elif G[u][v]['weight'] > 3:
            edge_colors.append('yellow')
        else:
            edge_colors.append('green')
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=15, edge_color=edge_colors, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)
    for vehicle in vehicles:
        plt.text(pos[vehicle.current_position][0], pos[vehicle.current_position][1], f"V{vehicle.id}",
                 color="red", fontsize=12, fontweight="bold", ha="center")
    for pedestrian in pedestrians:
        if pedestrian.is_crossing:
            plt.text(pos[pedestrian.crossing_node][0], pos[pedestrian.crossing_node][1], f"P{pedestrian.id}",
                     color="purple", fontsize=12, fontweight="bold", ha="center")
    plt.draw()
    plt.pause(1)
def real_time_simulation(G, pos, source, target, iterations=5):
    vehicles = [] 
    shortest_paths = []
    pedestrians = [] 
    lane1 = Lane(1)
    lane2 = Lane(2)
    lane3 = Lane(3)
    lanes = [lane1, lane2, lane3]
    traffic_lights = [TrafficLight() for _ in range(3)]
    pedestrians.append(Pedestrian(1, "P1")) 
    pedestrians.append(Pedestrian(2, "P2")) 
    for i in range(iterations):
        print(f"\n--- Iteration {i + 1} ---")
        vehicles.clear()
        congestion_simulation(G, current_iteration=i + 1)  
        apply_weather_conditions(G)
        if i == 2:  
            simulate_accident(G)
        for light in traffic_lights:
            light.switch_pedestrian() 
        simulate_pedestrians(traffic_lights, pedestrians)  
        num_vehicles = random.randint(2, 5)
        for _ in range(num_vehicles):
            lane = random.choice(lanes)
            vehicle_id = random.randint(1000, 9999)
            vehicle_type = random.choices(["car", "bus", "ambulance"], weights=[3, 3, 4], k=1)[0]
            priority = 1 if vehicle_type == "ambulance" else (2 if vehicle_type == "bus" else 3)
            vehicle = Vehicle(vehicle_id, vehicle_type, priority)
            shortest_path, _ = find_shortest_path(G, source, target)
            if shortest_path:
                vehicle.set_path(shortest_path)
                lane.add_vehicle(vehicle)
                vehicles.append(vehicle)
                print(f"✅ Created Vehicle {vehicle} (Type: {vehicle_type}, Priority: {priority}) in Lane {lane.lane_id}")
            else:
                print(f"❌ No path available for Vehicle {vehicle}. Road blocked.")
        adjust_traffic_lights(lanes, traffic_lights)
        collect_traffic_stats(lanes)
        print("📌 Running Priority Scheduling")
        priority_scheduling(lanes)
        shortest_path, total_cost = find_shortest_path(G, source, target)
        if shortest_path:
            print(f"Iteration {i + 1}: Shortest path: {shortest_path}, Total cost: {total_cost:.2f}")
            shortest_paths.append((shortest_path, total_cost))
        else:
            print(f"Iteration {i + 1}: No path found.")
            shortest_paths.append((None, None))
        for light in traffic_lights:
            light.switch_pedestrian() 
        simulate_pedestrians(traffic_lights, pedestrians)
        noise_level = calculate_noise_pollution(vehicles)
        display_noise_pollution(noise_level)
        visualize_network(G, pos, vehicles, pedestrians)
    print("\n--- Simulation Complete ---")
    for i, (path, cost) in enumerate(shortest_paths, start=1):
        if path:
            print(f"Iteration {i}: Shortest path: {path}, Total cost: {cost:.2f}")
        else:
            print(f"Iteration {i}: No path found.")
    plt.show()
if __name__ == "__main__":
    G = get_graph()
    pos = nx.get_node_attributes(G, 'pos') 
    real_time_simulation(G, pos, source="A", target="D", iterations=10)