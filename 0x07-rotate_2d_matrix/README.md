# Rotate 2D Matrix Inplace

This is a readme file for a github project that implements an algorithm to rotate a 2D matrix inplace.

## Problem Statement

Given a 2D array of integers, rotate the array by 90 degrees in place.

## Solution

The following algorithm can be used to rotate a 2D matrix inplace:

1. Start by iterating through the matrix from left to right, top to bottom.
2. For each element in the matrix, swap it with the element that is directly below it.
3. After iterating through the entire matrix, the matrix will be rotated by 90 degrees.

## Implementation

The following code implements the algorithm described above:

```python
def rotate_matrix(matrix):
  """Rotates a 2D matrix inplace by 90 degrees."""

  n = len(matrix)

  for i in range(n // 2):
    for j in range(n):
      matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]

```

## Testing

The following code can be used to test the implementation of the algorithm:

```python
def test_rotate_matrix():
  """Tests the rotate_matrix function."""

  matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

  rotate_matrix(matrix)

  assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

```

## Conclusion

The algorithm described in this readme file can be used to rotate a 2D matrix inplace by 90 degrees. The implementation of the algorithm is provided in the code block above. The algorithm can be tested using the code block below.