import unittest
from src.arm import Arm
from src.joint import Joint

class TestArm(unittest.TestCase):

    def setUp(self):
        self.arm = Arm()
        self.shoulder = Joint("shoulder", 90)
        self.elbow = Joint("elbow", 45)
        self.arm.add_joint(self.shoulder)
        self.arm.add_joint(self.elbow)

    def test_add_joint(self):
        self.assertEqual(len(self.arm.joints), 2)
        self.assertEqual(self.arm.joints[0].name, "shoulder")
        self.assertEqual(self.arm.joints[1].name, "elbow")

    def test_move_joint(self):
        self.arm.move_joint("shoulder", 45)
        self.assertEqual(self.shoulder.current_bend, 45)

        self.arm.move_joint("elbow", 30)
        self.assertEqual(self.elbow.current_bend, 30)

    def test_move_joint_not_found(self):
        with self.assertRaises(ValueError):
            self.arm.move_joint("wrist", 30)

if __name__ == "__main__":
    unittest.main()