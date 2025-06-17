def fcfs_scheduling(lanes):
    for lane in lanes:
        if not lane.is_empty():
            vehicle = lane.remove_vehicle()
            print(f"Vehicle {vehicle} from Lane {lane.lane_id} is passing.")
def priority_scheduling(lanes):
    all_vehicles = []
    for lane in lanes:
        all_vehicles.extend(lane.vehicles)
    all_vehicles.sort(key=lambda v: v.priority) 
    for vehicle in all_vehicles:
        print(f"Vehicle {vehicle} (Priority: {vehicle.priority}) is passing.")
        vehicle.move()  
        for lane in lanes:
            if vehicle in lane.vehicles:
                lane.vehicles.remove(vehicle)
                break
def round_robin_scheduling(lanes, time_slice):
    for i in range(len(lanes)):
        lane = lanes[i]
        print(f"Lane {lane.lane_id} gets the green light.")
        for _ in range(time_slice):
            if not lane.is_empty():
                vehicle = lane.remove_vehicle()
                print(f"    Vehicle {vehicle} is passing from Lane {lane.lane_id}.")
            else:
                break