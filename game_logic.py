from board import Board

class GameLogic:
    def __init__(self, board):
        self.board = board

    def make_move(self, start_row, start_col, end_row, end_col):
        grid = self.board.grid

        # Check if start position has a peg
        if grid[start_row][start_col] != 1:
            return False

        # Check if end position is empty
        if grid[end_row][end_col] != 0:
            return False

        # Calculate middle position
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2

        # Check if there is a peg to jump over
        if grid[mid_row][mid_col] != 1:
            return False

        # Make move
        grid[start_row][start_col] = 0
        grid[mid_row][mid_col] = 0
        grid[end_row][end_col] = 1

        return True

    def is_game_over(self):
        grid = self.board.grid
        size = self.board.size

        for r in range(size):
            for c in range(size):
                if grid[r][c] == 1:
                    # check right move
                    if c + 2 < size and grid[r][c+1] == 1 and grid[r][c+2] == 0:
                        return False

                    # check down move
                    if r + 2 < size and grid[r+1][c] == 1 and grid[r+2][c] == 0:
                        return False

        return True
