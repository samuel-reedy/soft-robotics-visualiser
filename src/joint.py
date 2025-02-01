class Joint:
    def __init__(self, name, max_bend):
        self.name = name
        self.max_bend = max_bend
        self.current_bend = 0

    def bend(self, angle):
        if angle < -self.max_bend or angle > self.max_bend:
            raise ValueError(f"Angle {angle} out of bounds for joint {self.name}")
        self.current_bend = angle

    def __repr__(self):
        return f"Joint(name={self.name}, current_bend={self.current_bend})"