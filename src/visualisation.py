class Visualizer:
    def __init__(self, arm):
        self.arm = arm

    def display(self):
        import matplotlib.pyplot as plt
        import numpy as np

        plt.figure()
        ax = plt.subplot(111, polar=True)
        angles = [joint.current_bend for joint in self.arm.joints]
        names = [joint.name for joint in self.arm.joints]

        # Create a radial plot for the joint angles
        theta = np.linspace(0, 2 * np.pi, len(angles), endpoint=False).tolist()
        angles += angles[:1]
        theta += theta[:1]

        ax.fill(theta, angles, color='blue', alpha=0.1)
        ax.set_xticks(theta[:-1])
        ax.set_xticklabels(names)
        ax.set_title("Robotic Arm Joint Angles")
        plt.show()