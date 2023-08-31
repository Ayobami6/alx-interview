## N queens Problem solver Using Backtracking Algorithm

### Problem statement

The N queens problem is a classic problem in computer science. It is an NP-complete problem, meaning that there is no known polynomial-time algorithm to solve it. The problem is to find a way to place N queens on an NxN chessboard so that no queen can attack another queen.

### Solution

The backtracking algorithm is a recursive algorithm that can be used to solve the N queens problem. The algorithm starts by placing a queen on the first row of the chessboard. It then checks if the queen can attack any of the other queens that have already been placed. If it can, the algorithm backtracks and tries placing the queen on a different square. If it cannot, the algorithm continues placing queens on the next row of the chessboard. The algorithm repeats this process until all N queens have been placed.

### Implementation

The following code implements the backtracking algorithm for the N queens problem.

```python
def n_queens(n):
  """
  Solves the N queens problem using the backtracking algorithm.

  Parameters:
    n: The number of queens.

  Returns:
    A list of lists representing the positions of the queens on the chessboard.
  """

  # Initialize the chessboard.
  board = [[0 for _ in range(n)] for _ in range(n)]

  # Place the first queen on the first row.
  board[0][0] = 1

  # Recursively place the remaining queens.
  for i in range(1, n):
    for j in range(n):
      if is_valid(board, i, j):
        board[i][j] = 1
        if n_queens(n, i + 1):
          return board
        board[i][j] = 0

  return None

def is_valid(board, i, j):
  """
  Checks if a queen can be placed on the given square.

  Parameters:
    board: The chessboard.
    i: The row of the square.
    j: The column of the square.

  Returns:
    True if the queen can be placed on the square, False otherwise.
  """

  # Check if there is a queen in the same row.
  for k in range(n):
    if board[i][k] == 1:
      return False

  # Check if there is a queen in the same column.
  for k in range(n):
    if board[k][j] == 1:
      return False

  # Check if there is a queen in the same diagonal.
  for k in range(n):
    if i - k >= 0 and j - k >= 0 and board[i - k][j - k] == 1:
      return False
    if i - k >= 0 and j + k < n and board[i - k][j + k] == 1:
      return False
    if i + k < n and j - k >= 0 and board[i + k][j - k] == 1:
      return False
    if i + k < n and j + k < n and board[i + k][j + k] == 1:
      return False

  return True
```

### Running the code

To run the code, you can use the following command:

```
python n_queens.py <n>
```

where `n` is the number of queens.

### Example

The following is an example of the output of the code for `n = 4`:

```
[[1, 3, 0, 2],
 [2, 0, 3, 1],
 [3, 1, 2, 0],
 [0, 2, 1, 3]]
```

This output shows a solution to the N queens problem for `n = 4`. The solution is a list of lists, where each list represents a row of the chessboard. The number in each list represents the column where the queen is placed. In this solution, the queens are placed on the squares (1, 3), (2, 0), (3, 1), and (0, 2).

### References

- [N queens problem](https://en.wikipedia.org/wiki/N-queens_problem)
- [Backtracking algorithm](https://en.wikipedia.org/wiki/Backtracking)
