from .joint import Joint
import numpy as np

class Arm:
    def __init__(self, joints=None, lengths=None):
        try:
            if joints and lengths and len(lengths) != len(joints):
                raise ValueError(f"Lengths ({len(lengths)}) should equal the number of joints ({len(joints)})")
        except ValueError as e:
            print(f"Initialisation error: {e}")
            joints, lengths = [], []
        self.joints = joints if joints else []
        self.lengths = lengths if lengths else []

    def add_joint(self, joint):
        self.joints.append(joint)

    def add_length(self, length):
        self.lengths.append(length)