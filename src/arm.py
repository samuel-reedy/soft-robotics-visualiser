from .joint import Joint

class Arm:
    def __init__(self):
        self.joints = []

    def add_joint(self, joint):
        self.joints.append(joint)

    def move_joint(self, joint_name, angle):
        for joint in self.joints:
            if joint.name == joint_name:
                joint.bend(angle)
                return
        raise ValueError(f"Joint {joint_name} not found")

    def get_joint_states(self):
        return {joint.name: joint.current_bend for joint in self.joints}

# Example usage
if __name__ == "__main__":
    arm = Arm()
    arm.add_joint(Joint("shoulder", 0, 180))
    arm.add_joint(Joint("elbow", 0, 150))
    
    try:
        print("Before moving joints:")
        for joint in arm.joints:
            print(f"{joint.name} current bend: {joint.current_bend}")
        
        arm.move_joint("shoulder", 90)
        arm.move_joint("elbow", 45)
        
        print("After moving joints:")
        for joint in arm.joints:
            print(f"{joint.name} current bend: {joint.current_bend}")
    except ValueError as e:
        print(e)