import numpy as np


def split_matrix(matrix):
    row, col = matrix.shape
    mid_row, mid_col = row // 2, col // 2
    return matrix[:mid_row, :mid_col], matrix[:mid_row, mid_col:], matrix[mid_row:, :mid_col], matrix[mid_row:,
                                                                                               mid_col:]


def matrix_multiply(A, B):
    if A.shape == (2, 2) and B.shape == (2, 2):
        C = np.zeros((2, 2))
        C[0, 0] = A[0, 0] * B[0, 0] + A[0, 1] * B[1, 0]
        C[0, 1] = A[0, 0] * B[0, 1] + A[0, 1] * B[1, 1]
        C[1, 0] = A[1, 0] * B[0, 0] + A[1, 1] * B[1, 0]
        C[1, 1] = A[1, 0] * B[0, 1] + A[1, 1] * B[1, 1]
        return C

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    C11 = matrix_multiply(A11, B11) + matrix_multiply(A12, B21)
    C12 = matrix_multiply(A11, B12) + matrix_multiply(A12, B22)
    C21 = matrix_multiply(A21, B11) + matrix_multiply(A22, B21)
    C22 = matrix_multiply(A21, B12) + matrix_multiply(A22, B22)

    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    return np.vstack((top, bottom))


A = np.array([[1, 2, 5, 6],
              [3, 4, 3, 4],
              [5, 2, 1, 2],
              [7, 2, 4, 3]])
B = np.array([[5, 6, 1, 2],
              [7, 8, 1, 2],
              [3, 1, 1, 2],
              [4, 2, 21, 1]])

result = matrix_multiply(A, B)
print("Result of matrix multiplication:\n", result)
print(A @ B)
