# game.py
from board import GameBoard
from levels import game_levels

class MagnetGame:
    def __init__(self):
        self.board = GameBoard(game_levels)

    def run_game(self):
        level_index = int(input("Choose level number (from 1 to {}): ".format(len(self.board.game_levels)))) - 1
        self.board.setup_level(level_index)

        while self.board.moves_left > 0:
            print(f"Moves left: {self.board.moves_left}")
            self.board.display_board()

            from_row = int(input("Enter row number to move the magnet from: "))
            from_col = int(input("Enter column number to move the magnet from: "))
            to_row = int(input("Enter new row number: "))
            to_col = int(input("Enter new column number: "))

            if self.board.move_magnet(from_row, from_col, to_row, to_col):
                self.board.moves_left -= 1

                if self.board.check_victory():
                    print("Congratulations! You won!")
                    break
            else:
                print("Try again.")

        if self.board.moves_left == 0:
            print("No more moves left, try again!")
