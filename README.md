# N-Queens Problem Solver with Hill Climbing Algorithm

This Python script solves the N-Queens problem, where the objective is to place N queens on an NxN chessboard without any two queens threatening each other. It uses a hill climbing algorithm to efficiently find solutions by adjusting queen positions based on a heuristic that minimizes mutual threats.

## Key Features

- **Dynamic Board Configuration**: Initializes an 8x8 board with queens placed in random positions.
- **Heuristic Approach**: Evaluates board configurations based on the number of threatening pairs of queens.
- **Optimization Algorithm**: Uses hill climbing to improve the board configuration by making the best possible move or restarting when necessary.
- **Performance Metrics**: Tracks the number of moves, restarts, and time taken to find a solution.

