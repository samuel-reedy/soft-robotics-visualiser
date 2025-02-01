import unittest
from src.joint import Joint

class TestJoint(unittest.TestCase):

    def setUp(self):
        self.joint = Joint("elbow", max_bend=90)

    def test_initialization(self):
        self.assertEqual(self.joint.name, "elbow")
        self.assertEqual(self.joint.current_bend, 0)
        self.assertEqual(self.joint.max_bend, 90)

    def test_bend(self):
        self.joint.bend(45)
        self.assertEqual(self.joint.current_bend, 45)

    def test_bend_exceeds_max(self):
        joint = Joint("elbow", 90)
        with self.assertRaises(ValueError):
            joint.bend(100)  # This should raise a ValueError

if __name__ == '__main__':
    unittest.main()