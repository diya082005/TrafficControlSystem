from collections import deque

class Lane:
    def __init__(self, lane_id):
        self.lane_id = lane_id
        self.vehicles = []
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
    def remove_vehicle(self):
        if self.vehicles:
            return self.vehicles.pop(0)
        return None 
    def is_empty(self):
        return len(self.vehicles) == 0
    def get_vehicle_count(self):
        return len(self.vehicles)