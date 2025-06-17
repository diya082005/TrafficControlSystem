import random
import time
from lane import Lane
from vehiclemovement import Vehicle
from trafficlight import TrafficLight
from scheduling import fcfs_scheduling, priority_scheduling, round_robin_scheduling
def simulate_traffic_flow(lanes, traffic_lights, scheduling_algorithm, time_slice=3, iterations=10):
    print("\n🚦 Traffic Simulation Started 🚦")
    if not lanes:
        print("❌ ERROR: No lanes found!")
        return
    if not traffic_lights:
        print("❌ ERROR: No traffic lights found!")
        return
    for i in range(iterations):
        print(f"\n--- Iteration {i + 1} ---")
        num_vehicles = random.randint(2, 5)
        for _ in range(num_vehicles):
            lane = random.choice(lanes)
            vehicle_id = random.randint(1000, 9999)
            vehicle_type = random.choices(["car", "bus", "ambulance"], weights=[3, 3, 4], k=1)[0]
            priority = 1 if vehicle_type == "ambulance" else (2 if vehicle_type == "bus" else 3)
            vehicle = Vehicle(vehicle_id, vehicle_type, priority)
            lane.add_vehicle(vehicle)
            print(f"✅ Created Vehicle {vehicle} (Type: {vehicle_type}, Priority: {priority}) in Lane {lane.lane_id}")
        if scheduling_algorithm == 'fcfs':
            print("📌 Running FCFS Scheduling")
            fcfs_scheduling(lanes)
        elif scheduling_algorithm == 'priority':
            print("📌 Running Priority Scheduling")
            priority_scheduling(lanes)
        elif scheduling_algorithm == 'round_robin':
            print("📌 Running Round Robin Scheduling")
            round_robin_scheduling(lanes, time_slice)
        else:
            print(f"❌ ERROR: Invalid scheduling algorithm '{scheduling_algorithm}'")
        for light in traffic_lights:
            light.switch()
        print("🚦 Traffic updated.")
        time.sleep(1)
def simulate_pedestrians(traffic_lights, pedestrians):
    for light in traffic_lights:
        if light.get_pedestrian_state() == "walk":
            for pedestrian in pedestrians:
                    pedestrian.start_crossing()
        else:
            for pedestrian in pedestrians:
                if pedestrian.is_crossing: 
                    pedestrian.stop_crossing()
def adjust_traffic_lights(lanes, traffic_lights):
    for lane, light in zip(lanes, traffic_lights):
        vehicle_count = lane.get_vehicle_count()
        if vehicle_count > 3: 
            light.set_timer(10) 
        else:
            light.set_timer(5)
def collect_traffic_stats(lanes):
    total_vehicles = sum(lane.get_vehicle_count() for lane in lanes)
    avg_wait_time = total_vehicles * 0.5 
    print(f"Total vehicles: {total_vehicles}, Avg wait time: {avg_wait_time:.2f} mins")