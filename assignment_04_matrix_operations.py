# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

#Helper
def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:5}", end=" ")
        print()
    print()


# Transpose a Matrix
def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = []
    for c in range(cols):
        new_row = []
        for r in range(rows):
            new_row.append(matrix[r][c])
        transposed.append(new_row)

    return transposed


# Add Two Matrices
def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])

    result = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            new_row.append(A[r][c] + B[r][c])
        result.append(new_row)

    return result


#  Multiply Two Matrices
def multiply_matrices(A, B):
    M = len(A)
    N = len(A[0])
    P = len(B[0])

    # Result matrix M x P
    result = []
    for i in range(M):
        new_row = []
        for j in range(P):
            total = 0
            for k in range(N):
                total += A[i][k] * B[k][j]
            new_row.append(total)
        result.append(new_row)

    return result


# Read a matrix from user
def read_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = []
    for r in range(rows):
        row = list(map(int, input(f"Enter row {r+1}: ").split()))
        matrix.append(row)

    return matrix



#The Program

print("=== PART A: TRANSPOSE A MATRIX ===")
A = read_matrix()
print("\nOriginal Matrix:")
print_matrix(A)

T = transpose(A)
print("Transposed Matrix:")
print_matrix(T)

print("=== PART B: ADD TWO MATRICES ===")
print("Enter Matrix 1:")
M1 = read_matrix()
print("Enter Matrix 2:")
M2 = read_matrix()

print("\nSum of Matrices:")
print_matrix(add_matrices(M1, M2))

print("=== PART C: MULTIPLY TWO MATRICES ===")
print("Enter Matrix A:")
A = read_matrix()
print("Enter Matrix B:")
B = read_matrix()

print("\nProduct A × B:")
print_matrix(multiply_matrices(A, B))
