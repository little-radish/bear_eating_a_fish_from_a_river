import unittest
from src.bear import Bear
from src.fish import Fish

class TestBear(unittest.TestCase):

    def setUp(self):
        self.bear = Bear("John Eldenring", "Runebear")

    def test_bear_name(self):
        self.assertEqual("John Eldenring", self.bear.name)

    def test_bear_type(self):
        self.assertEqual("Runebear", self.bear.type)

    def test_eat_fish(self):
        fish = Fish("Sephiroth")
        self.bear.eat_fish(fish)
        self.assertEqual([fish], self.bear.stomach)

    def test_food_count(self):
        self.assertEqual(0, self.bear.food_count())


