import unittest
from board import Board
from game_logic import GameLogic


class TestGameLogic(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.game = GameLogic(self.board)

    def test_valid_move(self):
        # Move from (3,1) to (3,3)
        result = self.game.make_move(3, 1, 3, 3)
        self.assertTrue(result)

    def test_invalid_move(self):
        # Try invalid move (no peg jump)
        result = self.game.make_move(0, 0, 0, 2)
        self.assertFalse(result)

    def test_game_not_over_initially(self):
        self.assertFalse(self.game.is_game_over())


if __name__ == "__main__":
    unittest.main()
