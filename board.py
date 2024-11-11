from cell import GameCell

class GameBoard:
    def __init__(self, game_levels):
        self.game_levels = game_levels
        self.current_level = 0
        self.moves_left = 0
        self.grid = None

    def setup_level(self, level_index):
        level = self.game_levels[level_index]
        self.moves_left = level['move_limit']
        self.grid = [[GameCell() for _ in range(6)] for _ in range(5)]

        for target in level['targets']:
            self.grid[target[0]][target[1]] = GameCell('o')

        for piece in level['pieces']:
            self.grid[piece['position'][0]][piece['position'][1]] = GameCell(piece['type'])

    def display_board(self):
        print("   " + " ".join(str(i) for i in range(6)))
        for row_index in range(5):
            print(row_index, " ".join(str(self.grid[row_index][col_index]) for col_index in range(6)))

    def move_magnet(self, from_row, from_col, to_row, to_col):
        if self.grid[from_row][from_col].cell_type not in ('p', 'r', 'purple'):
            print("Invalid move: Not a magnet.")
            return False

        if self.grid[to_row][to_col].cell_type not in ('empty', 'o'):
            print("Invalid move: Destination not empty or target.")
            return False

        self.grid[to_row][to_col], self.grid[from_row][from_col] = self.grid[from_row][from_col], GameCell('empty')

        if self.grid[to_row][to_col].cell_type in ('p', 'purple'):
            self.repel_iron_pieces(to_row, to_col)
        elif self.grid[to_row][to_col].cell_type == 'r':
            self.attract_iron_pieces(to_row, to_col)

        return True

    def repel_iron_pieces(self, to_row, to_col):
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        for direction_row, direction_col in directions:
            row, col = to_row + direction_row, to_col + direction_col
            if 0 <= row < 5 and 0 <= col < 6 and self.grid[row][col].cell_type in ('i', 'gray'):
                new_row, new_col = row + direction_row, col + direction_col
                if 0 <= new_row < 5 and 0 <= new_col < 6 and (self.grid[new_row][new_col].cell_type == 'empty' or self.grid[new_row][new_col].cell_type == 'o'):
                    self.grid[new_row][new_col] = GameCell(self.grid[row][col].cell_type)
                self.grid[row][col] = GameCell('empty')

    def attract_iron_pieces(self, to_row, to_col):
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        for direction_row, direction_col in directions:
            row, col = to_row + direction_row, to_col + direction_col
            new_row, new_col = to_row - direction_row, to_col - direction_col
            if 0 <= row < 5 and 0 <= col < 6 and self.grid[row][col].cell_type in ('i', 'gray'):
                if 0 <= new_row < 5 and 0 <= new_col < 6 and (self.grid[new_row][new_col].cell_type == 'empty' or self.grid[new_row][new_col].cell_type == 'o'):
                    self.grid[new_row][new_col] = GameCell(self.grid[row][col].cell_type)
                    self.grid[row][col] = GameCell('empty')

    def check_victory(self):
        for row in self.grid:
            for cell in row:
                if cell.cell_type == 'o':
                    return False
        return True

    def generate_possible_moves(self, state):
        possible_moves = []
        for row in range(5):
            for col in range(6):
                cell = state[row][col]
                if cell.cell_type in ('p', 'r', 'purple'):
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for direction in directions:
                        new_row = row + direction[0]
                        new_col = col + direction[1]
                        if 0 <= new_row < 5 and 0 <= new_col < 6:
                            if state[new_row][new_col].cell_type in ('empty', 'o'):
                                possible_moves.append(((row, col), (new_row, new_col)))
        return possible_moves

    def grid_to_string(self, grid):
        board_string = ""
        for row in grid:
            for cell in row:
                board_string += str(cell)
            board_string += "\n"
        return board_string

    def apply_move(self, state, move):
        from_row, from_col = move[0]
        to_row, to_col = move[1]
        new_state = [row[:] for row in state]
        new_state[to_row][to_col], new_state[from_row][from_col] = new_state[from_row][from_col], GameCell('empty')
        return new_state

    def solve_with_algorithm(self, algorithm="dfs"):
        stack = [(self.grid, [])]
        queue = [(self.grid, [])]

        if algorithm == "dfs":
            data_structure = stack
            get_next_state = stack.pop
        elif algorithm == "bfs":
            data_structure = queue
            get_next_state = queue.pop
        else:
            print("Invalid algorithm choice! Please choose either 'dfs' or 'bfs'.")
            return False
        
        visited = set()

        while data_structure:
            state, path = get_next_state(0) if algorithm == "bfs" else get_next_state()
            state_string = self.grid_to_string(state)

            if state_string in visited:
                continue
            visited.add(state_string)

            print("Current state of the board:")
            print(self.grid_to_string(state))

            if self.check_victory():
                print("Victory reached!")
                print(f"Solution path: {path}")
                return True

            possible_moves = self.generate_possible_moves(state)
            print(f"Possible moves: {possible_moves}")

            for move in possible_moves:
                new_state = self.apply_move(state, move)
                new_state_string = self.grid_to_string(new_state)

                if new_state_string not in visited:
                    data_structure.append((new_state, path + [move]))

        print("")
        return False
