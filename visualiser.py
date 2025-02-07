import numpy as np
import tkinter as tk
from tkinter import ttk
from src.joint import Joint
from src.arm import Arm

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def draw_circle(canvas, position, radius, color="blue"):
    canvas.create_oval(position.x - radius, position.y - radius, position.x + radius, position.y + radius, outline=color, fill=color)

def draw_line(canvas, start_position, end_position, color="black"):
    canvas.create_line(start_position.x, start_position.y, end_position.x, end_position.y, fill=color)

def draw_x(canvas, position, size=5, color="red"):
    canvas.create_line(position.x - size, position.y - size, position.x + size, position.y + size, fill=color)
    canvas.create_line(position.x - size, position.y + size, position.x + size, position.y - size, fill=color)

def calculate_reach_envelope(base_position, arm):
    points = []
    for shoulder_angle in range(0, 361, 5):
        for elbow_angle in range(0, 181, 5):
            try:
                arm.joints[0].set_angle(shoulder_angle)
                arm.joints[1].set_angle(elbow_angle)
            except ValueError:
                continue
            cumulative_angle = 0
            current_position = base_position
            for i in range(len(arm.joints)):
                joint = arm.joints[i]
                cumulative_angle += joint.current_angle
                angle = np.deg2rad(cumulative_angle)
                length = arm.lengths[i]
                next_position = Position(
                    current_position.x + length * np.cos(angle),
                    current_position.y - length * np.sin(angle)
                )
                current_position = next_position
            points.append((current_position.x, current_position.y))
    return points

def draw_reach_envelope(canvas, points):
    for point in points:
        draw_circle(canvas, Position(point[0], point[1]), 1, color="gray")

window = tk.Tk()          

canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

def draw_arm(canvas, arm, base_position):
    canvas.delete("all")
    draw_reach_envelope(canvas, reach_envelope_points)
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

def inverse_kinematics(x, y, arm):
    l1, l2 = arm.lengths
    d = np.sqrt(x**2 + y**2)
    if d > l1 + l2:
        return None  # Target is unreachable

    a = np.arctan2(y, x)
    b = np.arccos((l1**2 + d**2 - l2**2) / (2 * l1 * d))
    theta1 = np.rad2deg(a - b)

    c = np.arccos((l1**2 + l2**2 - d**2) / (2 * l1 * l2))
    theta2 = 180 - np.rad2deg(c)

    return theta1, theta2

def update_position(x, y):
    arm_max_length = sum(arm.lengths)
    if np.sqrt(x**2 + y**2) > arm_max_length:
        angle = np.arctan2(y, x)
        x = arm_max_length * np.cos(angle)
        y = arm_max_length * np.sin(angle)

    angles = inverse_kinematics(x, y, arm)
    if angles:
        shoulder_angle, elbow_angle = angles
        arm.joints[0].set_angle(shoulder_angle)
        arm.joints[1].set_angle(elbow_angle)
    draw_arm(canvas, arm, base_position)
    draw_x(canvas, Position(base_position.x + x, base_position.y - y))
    draw_x(canvas, Position(base_position.x + x_slider.get(), base_position.y - y_slider.get()), color="green")

base_position = Position(200, 200)
shoulder = Joint(180)
elbow = Joint(135)
arm = Arm([shoulder, elbow], [100, 50])
reach_envelope_points = calculate_reach_envelope(base_position, arm)
draw_arm(canvas, arm, base_position)

# Create sliders for x and y positions
x_slider = tk.Scale(window, from_=-200, to=200, orient=tk.HORIZONTAL, label="X Position", command=lambda x: update_position(float(x), y_slider.get()))
x_slider.set(0)
x_slider.pack()

y_slider = tk.Scale(window, from_=-200, to=200, orient=tk.VERTICAL, label="Y Position", command=lambda y: update_position(x_slider.get(), float(y)))
y_slider.set(0)
y_slider.pack()

window.mainloop()