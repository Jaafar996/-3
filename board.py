# board.py
from cell import Cell

class GameBoard:
    def __init__(self, game_levels):
        self.game_levels = game_levels
        self.current_level = 0
        self.moves_left = 0
        self.grid = None

    def setup_level(self, level_index):
        level = self.game_levels[level_index]
        self.moves_left = level['move_limit']
        self.grid = [[Cell() for _ in range(6)] for _ in range(5)]

        for target in level['targets']:
            self.grid[target[0]][target[1]] = Cell('o')

        for piece in level['pieces']:
            self.grid[piece['position'][0]][piece['position'][1]] = Cell(piece['type'])

    def display_board(self):
        print("   " + " ".join(str(i) for i in range(6)))
        for row_index in range(5):
            print(row_index, " ".join(str(self.grid[row_index][col_index]) for col_index in range(6)))

    def move_magnet(self, from_row, from_col, to_row, to_col):
        if self.grid[from_row][from_col].cell_type != 'p':
            print("Invalid move: Not a magnet.")
            return False

        if self.grid[to_row][to_col].cell_type != 'empty' and self.grid[to_row][to_col].cell_type != 'o':
            print("Invalid move: Destination not empty or target.")
            return False

        self.grid[to_row][to_col], self.grid[from_row][from_col] = self.grid[from_row][from_col], Cell('empty')
        self.repel_iron_pieces(to_row, to_col)
        
        return True

    def repel_iron_pieces(self, to_row, to_col):
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]
        for direction_row, direction_col in directions:
            row, col = to_row + direction_row, to_col + direction_col
            if 0 <= row < 5 and 0 <= col < 6 and self.grid[row][col].cell_type == 'i':
                new_row, new_col = row + direction_row, col + direction_col
                if 0 <= new_row < 5 and 0 <= new_col < 6 and (self.grid[new_row][new_col].cell_type == 'empty' or self.grid[new_row][new_col].cell_type == 'o'):
                    self.grid[new_row][new_col] = Cell('i')
                self.grid[row][col] = Cell('empty')

    def check_victory(self):
        for row in self.grid:
            for cell in row:
                if cell.cell_type == 'o':
                    return False
        return True
