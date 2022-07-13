import unittest
from src.fish import Fish

class TestFish(unittest.TestCase):

    def setUp(self):
        self.fish = Fish("Sephiroth")

    def test_bear_name(self):
        self.assertEqual("Sephiroth", self.fish.name)