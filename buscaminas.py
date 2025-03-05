"""
Buscaminas Game
Creators: Annel Camacho & Mariana Barrera
Date: March 4, 2025

This code was developed with assistance from ChatGPT
"""

import random

class Minesweeper:
    def __init__(self, rows=10, cols=10, mines=15):  # Fixed init method
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.initialize_game()
    
    def initialize_game(self):
        self.board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.revealed = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.flags = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.place_mines()
        self.calculate_numbers()

    def place_mines(self):
        mine_positions = random.sample(range(self.rows * self.cols), self.mines)
        for pos in mine_positions:
            r, c = divmod(pos, self.cols)
            self.board[r][c] = -1

    def calculate_numbers(self):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == -1:
                    continue
                count = sum(1 for dr, dc in directions if 0 <= r+dr < self.rows and 0 <= c+dc < self.cols and self.board[r+dr][c+dc] == -1)
                self.board[r][c] = count

    def reveal_cell(self, r, c):
        if self.revealed[r][c] or self.flags[r][c]:
            return
        
        self.revealed[r][c] = True
        if self.board[r][c] == -1:
            print("Boom! You hit a mine! Game Over.")
            self.show_board()
            self.restart_game()
        else:
            print(f"Revealed ({r}, {c}): {self.board[r][c]}")
            if self.board[r][c] == 0:
                for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        self.reveal_cell(nr, nc)

    def flag_cell(self, r, c):
        if self.revealed[r][c]:
            return 
        self.flags[r][c] = not self.flags[r][c]
        print(f"{'Flagged' if self.flags[r][c] else 'Unflagged'} ({r}, {c})")

    def show_board(self):
        print("   " + " ".join(str(c) for c in range(self.cols)))
        print("   " + "-" * (self.cols * 2 - 1))
        for r in range(self.rows):
            row = " ".join(str(self.board[r][c]) if self.revealed[r][c] else ('F' if self.flags[r][c] else 'X') for c in range(self.cols))
            print(f"{r} | {row}")
    
    def restart_game(self):
        choice = input("Do you want to restart? (y/n): ").strip().lower()
        if choice == 'y':
            self.initialize_game()
            self.play()
        else:
            print("Thanks for playing!")
            exit()

    def play(self):
        while True:
            self.show_board()
            action = input("Enter action (r row col to reveal, f row col to flag): ").split()
            if len(action) != 3:
                print("Invalid input, try again.")
                continue
            cmd, r, c = action[0], int(action[1]), int(action[2])
            if cmd == 'r':
                self.reveal_cell(r, c)
            elif cmd == 'f':
                self.flag_cell(r, c)
            else:
                print("Unknown command, use 'r' to reveal or 'f' to flag.")

if __name__ == "_main_":
    game = Minesweeper()
    game.play()
