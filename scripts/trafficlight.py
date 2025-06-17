class TrafficLight:
    def __init__(self):
        self.state = "red"
        self.pedestrian_state = "don't walk"
        self.timer = 0
    def switch(self):
        self.state = "green" if self.state == "red" else "red"
        print(f"🚦 Traffic light is now {self.state}.")
    def switch_pedestrian(self):
        self.pedestrian_state = "walk" if self.pedestrian_state == "don't walk" else "don't walk"
        if self.pedestrian_state == "walk":
            print(f"🚶 Pedestrian light is now **WALK**. Pedestrians may cross.")
        else:
            print(f"🚶 Pedestrian light is now **DON'T WALK**. Pedestrians must wait.")
        print(f"DEBUG: Pedestrian light state = {self.pedestrian_state}") 
    def set_timer(self, timer):
        self.timer = timer
        print(f"🚦 Traffic light timer set to {self.timer} seconds.")
    def get_state(self):
        return self.state
    def get_pedestrian_state(self):
        return self.pedestrian_state