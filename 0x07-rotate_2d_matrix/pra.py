matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def rotate_matrix(matrix):
    n = len(matrix)
    temp = []
    tmp = list(matrix)
    for j in range(n):
        for i in range(n - 1, -1, -1):
            temp.append(tmp[i][j])
        matrix[j] = temp
        temp = []

    # def rotate_matrix(matrix):
    #     """Rotates a 2D matrix inplace by 90 degrees."""

    #     n = len(matrix)

    #     for i in range(n // 2):
    #         print(i, "this is i")
    #         for j in range(n):
    #             print(matrix[i][j])
    #             print(matrix[n - i - 1][j])
    #             matrix[i][j], matrix[n - i -
    #                                  1][j] = matrix[n - i - 1][j], matrix[i][j]


# print(matrix[2][0])

rotate_matrix(matrix)
print(matrix)
