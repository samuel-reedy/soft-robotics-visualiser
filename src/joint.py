class Joint:
    def __init__(self, max_angle):
        self.max_angle = max_angle
        self.current_angle = 0

    def set_angle(self, angle):
        try:
            if angle < -self.max_angle or angle > self.max_angle:
                raise ValueError(f"Angle {angle} out of bounds for joint")
            self.current_angle = angle
        except ValueError as e:
            print(e)

    def rotate_angle(self, delta_angle):
        new_angle = self.current_angle + delta_angle
        try:
            if new_angle < -self.max_angle or new_angle > self.max_angle:
                raise ValueError(f"Angle {new_angle} out of bounds for joint")
            self.current_angle = new_angle
        except ValueError as e:
            print(e)