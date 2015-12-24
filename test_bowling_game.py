import unittest
from bowling_game import Game


class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def roll_many(self, rolls, pins):
        for i in range(rolls):
            self.game.roll(pins)

    def roll_spare(self):
        self.game.roll(2)
        self.game.roll(8)

    def roll_strike(self):
        self.game.roll(10)

    def test_gutter_game(self):
        self.roll_many(rolls=20, pins=0)
        self.assertEqual(self.game.score(), 0)

    def test_all_ones(self):
        self.roll_many(rolls=20, pins=1)
        self.assertEqual(self.game.score(), 20)

    def test_one_spare(self):
        self.roll_spare()
        self.game.roll(3)
        self.roll_many(17, 0)

        self.assertEqual(self.game.score(), 16)

    def test_one_strike(self):
        self.roll_strike()
        self.game.roll(3)
        self.game.roll(4)
        self.roll_many(16, 0)
        self.assertEqual(self.game.score(), 24)

    def test_perfect_game(self):
        self.roll_many(rolls=12, pins=10)
        self.assertEqual(self.game.score(), 300)

if __name__ == '__main__':
    unittest.main()