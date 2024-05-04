import random
import copy
import time

class Board:
    def __init__(self, n=8):
        self.n = n
        self.array_board = list(range(n))
        random.shuffle(self.array_board)
        self.heuristic = self.calculate_heuristic(self.array_board)
        self.solution_count = 0

    def generate_board(self):
        """Generates a new board configuration."""
        self.array_board = list(range(self.n))
        random.shuffle(self.array_board)
        self.heuristic = self.calculate_heuristic(self.array_board)

    def calculate_heuristic(self, board):
        """Calculates the heuristic value of the board."""
        h = 0  # heuristic
        for i in range(self.n):
            for j in range(i + 1, self.n):
                difference = board[i] - board[j]
                if (difference == 0) or (abs(difference) == j - i):
                    h += 1
        return h

    def print_board(self):
        """Prints the board."""
        for i in range(self.n):
            row = ["Q" if self.array_board[i] == j else "-" for j in range(self.n)]
            print(" ".join(row))

    def algorithm(self):
        """Implements the hill climbing algorithm to solve the board."""
        moves_count = 0
        restarts_count = 0
        start_time = time.time()

        while self.heuristic != 0:
            moves = []
            for i in range(self.n):
                for j in range(self.n):
                    if j != self.array_board[i]:
                        copy_board = copy.deepcopy(self.array_board)
                        copy_board[i] = j
                        moves.append([copy_board, self.calculate_heuristic(copy_board)])
                        moves_count += 1
            moves.sort(key=lambda x: x[1])

            if self.heuristic > moves[0][1]:
                self.array_board, self.heuristic = moves[0][0], moves[0][1]
            else:
                # If at a local maximum, restart
                self.generate_board()
                restarts_count += 1

        end_time = time.time()
        time_taken = end_time - start_time

        self.print_board()
        return (moves_count, restarts_count, time_taken)

def main():
    n = 8
    table = []
    for i in range(9):
        board = Board(n)
        print(f"Solution #{i + 1}")
        moves_count, restarts_count, time_taken = board.algorithm()
        row = [moves_count, restarts_count, time_taken, i]
        table.append(row)

    print("\tMove count\tRestarts count\tElapsed time")
    for row in table:
        print(f"{row[3] + 1}-\t{row[0]}\t\t{row[1]}\t\t\t{row[2]:.4f} seconds")

main()
