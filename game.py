from board import GameBoard  
from levels import game_levels

class MagnetGame:
    def __init__(self):
        self.board = GameBoard(game_levels)

    def run_game(self):
        solving_method = input("Choose solving method (manual or auto): ").strip().lower()
        
        try:
            level_index = int(input(f"Choose level number (from 1 to {len(self.board.game_levels)}): ")) - 1
            if not (0 <= level_index < len(self.board.game_levels)):
                print("Invalid level number.")
                return
        except ValueError:
            print("Please enter a valid level number.")
            return

        self.board.setup_level(level_index)

        if solving_method == "auto":
            algorithm_choice = input("Choose algorithm (dfs or bfs): ").strip().lower()
            if algorithm_choice not in ("dfs", "bfs"):
                print("Invalid algorithm choice. Please enter either 'dfs' or 'bfs'.")
                return

            if self.board.solve_with_algorithm(algorithm_choice):
                print("Solution found!")
            else:
                print("")
        else:
            while self.board.moves_left > 0:
                print(f"Moves left: {self.board.moves_left}")
                self.board.display_board()

                try:
                    from_row = int(input("Enter row number to move the magnet from: "))
                    from_col = int(input("Enter column number to move the magnet from: "))
                    to_row = int(input("Enter new row number: "))
                    to_col = int(input("Enter new column number: "))
                except ValueError:
                    print("Please enter numeric values only.")
                    continue

                if self.board.move_magnet(from_row, from_col, to_row, to_col):
                    self.board.moves_left -= 1

                    if self.board.check_victory():
                        print("Congratulations! You won!")
                        break
                else:
                    print("Invalid move. Please try again.")

            if self.board.moves_left == 0:
                print("No moves left. Please try again.")
