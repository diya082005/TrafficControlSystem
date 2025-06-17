class Pedestrian:
    def __init__(self, pedestrian_id, crossing_node):
        self.id = pedestrian_id
        self.crossing_node = crossing_node
        self.is_crossing = False
    def start_crossing(self):
        self.is_crossing = True
        print(f"🚶 Pedestrian {self.id} is crossing at {self.crossing_node}.")
    def stop_crossing(self):
        self.is_crossing = False
        print(f"🚶 Pedestrian {self.id} has finished crossing at {self.crossing_node}.")
    def __repr__(self):
        return f"Pedestrian {self.id} (Crossing at {self.crossing_node})"