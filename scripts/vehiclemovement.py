class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, priority):
        self.id = vehicle_id
        self.vehicle_type = vehicle_type
        self.priority = priority
        self.current_position = "A" 
        self.path = []
        if self.vehicle_type == "car":
            self.noise_level = 70
        elif self.vehicle_type == "bus":
            self.noise_level = 80
        elif self.vehicle_type == "ambulance":
            self.noise_level = 90 
    def set_path(self, path):
        self.path = path
    def move(self):
        if self.path:
            self.current_position = self.path.pop(0) 
            print(f"Vehicle {self.id} moved to {self.current_position}.")
        else:
            print(f"Vehicle {self.id} has reached its destination.")
    def __repr__(self):
        return f"Vehicle {self.id} ({self.vehicle_type})"