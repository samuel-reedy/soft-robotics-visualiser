from src.joint import Joint
from src.arm import Arm
import numpy as np
import tkinter as tk
from tkinter import ttk

shoulder = Joint(90)
elbow = Joint(45)

arm = Arm([shoulder, elbow], [100, 50])

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_circle(canvas, position, radius, color="blue"):
    canvas.create_oval(position.x - radius, position.y - radius, position.x + radius, position.y + radius, outline=color, fill=color)

def draw_line(canvas, start_position, end_position, color="black"):
    canvas.create_line(start_position.x, start_position.y, end_position.x, end_position.y, fill=color)

window = tk.Tk()          

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

def draw_arm(canvas, arm, base_position):
    canvas.delete("all")
    current_position = base_position
    cumulative_angle = 0
    for i in range(len(arm.joints)):
        joint = arm.joints[i]
        cumulative_angle += joint.current_angle
        angle = np.deg2rad(cumulative_angle)
        length = arm.lengths[i]
        next_position = Position(
            current_position.x + length * np.cos(angle),
            current_position.y - length * np.sin(angle)
        )
        draw_circle(canvas, current_position, 5)
        draw_line(canvas, current_position, next_position)
        current_position = next_position
    draw_circle(canvas, current_position, 5)

def update_joint_angle(joint, angle):
    joint.set_angle(angle)
    draw_arm(canvas, arm, base_position)

base_position = Position(200, 200)
draw_arm(canvas, arm, base_position)

# Create sliders for each joint
for i, joint in enumerate(arm.joints):
    slider = tk.Scale(window, from_=-joint.max_angle, to=joint.max_angle, orient=tk.HORIZONTAL, command=lambda angle, j=joint: update_joint_angle(j, float(angle)))
    slider.set(joint.current_angle)
    slider.pack()

window.mainloop()