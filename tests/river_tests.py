import unittest
from src.river import River
from src.fish import Fish

class TestRiver(unittest.TestCase):

    def setUp(self):
        self.river = River("Amazon")
        self.inhabitants = []

    def test_river_name(self):
        self.assertEqual("Amazon", self.river.name)