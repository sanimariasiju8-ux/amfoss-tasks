import time


# ---------------------------------------------------------
# 1. READ MATRIX
# ---------------------------------------------------------

def read_matrix(name):
    rows = int(input(f"Enter number of rows for Matrix {name}: "))
    cols = int(input(f"Enter number of columns for Matrix {name}: "))

    matrix = []

    print(f"Enter elements of Matrix {name} row by row:")

    for i in range(rows):
        while True:
            row = list(map(int, input(f"Enter row {i + 1}: ").split()))

            if len(row) == cols:
                matrix.append(row)
                break
            else:
                print(f"Please enter exactly {cols} elements.")

    return matrix, rows, cols


# ---------------------------------------------------------
# 2. NAIVE MATRIX MULTIPLICATION
# ---------------------------------------------------------

def naive_multiply(A, B):

    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


# ---------------------------------------------------------
# 3. MATRIX ADDITION
# ---------------------------------------------------------

def add_matrix(A, B):

    n = len(A)

    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] + B[i][j]

    return result


# ---------------------------------------------------------
# 4. MATRIX SUBTRACTION
# ---------------------------------------------------------

def subtract_matrix(A, B):

    n = len(A)

    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[i][j] = A[i][j] - B[i][j]

    return result


# ---------------------------------------------------------
# 5. DIVIDE AND CONQUER
# ---------------------------------------------------------

def divide_and_conquer(A, B):

    n = len(A)

    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    # Divide A
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    # Divide B
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Recursive multiplication

    M1 = divide_and_conquer(A11, B11)
    M2 = divide_and_conquer(A12, B21)

    M3 = divide_and_conquer(A11, B12)
    M4 = divide_and_conquer(A12, B22)

    M5 = divide_and_conquer(A21, B11)
    M6 = divide_and_conquer(A22, B21)

    M7 = divide_and_conquer(A21, B12)
    M8 = divide_and_conquer(A22, B22)

    # Calculate result blocks

    C11 = add_matrix(M1, M2)
    C12 = add_matrix(M3, M4)
    C21 = add_matrix(M5, M6)
    C22 = add_matrix(M7, M8)

    # Combine the four blocks

    result = []

    for i in range(mid):
        result.append(C11[i] + C12[i])

    for i in range(mid):
        result.append(C21[i] + C22[i])

    return result


# ---------------------------------------------------------
# 6. STRASSEN'S MATRIX MULTIPLICATION
# ---------------------------------------------------------

def strassen(A, B):

    n = len(A)

    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    # Divide A
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    # Divide B
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Strassen's seven products

    P1 = strassen(
        A11,
        subtract_matrix(B12, B22)
    )

    P2 = strassen(
        add_matrix(A11, A12),
        B22
    )

    P3 = strassen(
        add_matrix(A21, A22),
        B11
    )

    P4 = strassen(
        A22,
        subtract_matrix(B21, B11)
    )

    P5 = strassen(
        add_matrix(A11, A22),
        add_matrix(B11, B22)
    )

    P6 = strassen(
        subtract_matrix(A12, A22),
        add_matrix(B21, B22)
    )

    P7 = strassen(
        subtract_matrix(A11, A21),
        add_matrix(B11, B12)
    )

    # Calculate result blocks

    C11 = add_matrix(
        subtract_matrix(
            add_matrix(P5, P4),
            P2
        ),
        P6
    )

    C12 = add_matrix(P1, P2)

    C21 = add_matrix(P3, P4)

    C22 = subtract_matrix(
        subtract_matrix(
            add_matrix(P5, P1),
            P3
        ),
        P7
    )

    # Combine result blocks

    result = []

    for i in range(mid):
        result.append(C11[i] + C12[i])

    for i in range(mid):
        result.append(C21[i] + C22[i])

    return result


# ---------------------------------------------------------
# 7. FIND POWER OF 2
# ---------------------------------------------------------

def next_power_of_two(n):

    power = 1

    while power < n:
        power *= 2

    return power


# ---------------------------------------------------------
# 8. PAD MATRIX
# ---------------------------------------------------------

def pad_matrix(matrix, size):

    old_rows = len(matrix)
    old_cols = len(matrix[0])

    padded = [[0] * size for _ in range(size)]

    for i in range(old_rows):
        for j in range(old_cols):
            padded[i][j] = matrix[i][j]

    return padded


# ---------------------------------------------------------
# 9. REMOVE PADDING
# ---------------------------------------------------------

def remove_padding(matrix, rows, cols):

    return [
        row[:cols]
        for row in matrix[:rows]
    ]


# ---------------------------------------------------------
# 10. PRINT MATRIX
# ---------------------------------------------------------

def print_matrix(matrix):

    for row in matrix:
        print(row)


# ---------------------------------------------------------
# 11. MAIN PROGRAM
# ---------------------------------------------------------

print("\n======================================")
print("     MATRIX MULTIPLICATION SHOWDOWN")
print("======================================\n")


# Read Matrix A
A, rows_A, cols_A = read_matrix("A")

print("\nMatrix A:")
print_matrix(A)


# Read Matrix B
print()

B, rows_B, cols_B = read_matrix("B")

print("\nMatrix B:")
print_matrix(B)


# Check whether multiplication is possible

if cols_A != rows_B:

    print("\nMatrix multiplication is NOT possible.")
    print("Number of columns of A must equal number of rows of B.")

else:

    print("\nMatrix multiplication is possible.")

    # -----------------------------------------------------
    # NAIVE
    # -----------------------------------------------------

    start = time.perf_counter()

    naive_result = naive_multiply(A, B)

    naive_time = time.perf_counter() - start


    # -----------------------------------------------------
    # PREPARE MATRICES FOR D&C AND STRASSEN
    # -----------------------------------------------------

    # Find a square size that is a power of 2

    max_dimension = max(
        rows_A,
        cols_A,
        rows_B,
        cols_B
    )

    size = next_power_of_two(max_dimension)

    A_padded = pad_matrix(A, size)
    B_padded = pad_matrix(B, size)


    # -----------------------------------------------------
    # DIVIDE AND CONQUER
    # -----------------------------------------------------

    start = time.perf_counter()

    divide_result_padded = divide_and_conquer(
        A_padded,
        B_padded
    )

    divide_time = time.perf_counter() - start

    divide_result = remove_padding(
        divide_result_padded,
        rows_A,
        cols_B
    )


    # -----------------------------------------------------
    # STRASSEN
    # -----------------------------------------------------

    start = time.perf_counter()

    strassen_result_padded = strassen(
        A_padded,
        B_padded
    )

    strassen_time = time.perf_counter() - start

    strassen_result = remove_padding(
        strassen_result_padded,
        rows_A,
        cols_B
    )


    # -----------------------------------------------------
    # DISPLAY RESULTS
    # -----------------------------------------------------

    print("\n======================================")
    print("          RESULTS")
    print("======================================")

    print("\nNaive Multiplication Result:")
    print_matrix(naive_result)

    print("\nDivide and Conquer Result:")
    print_matrix(divide_result)

    print("\nStrassen Result:")
    print_matrix(strassen_result)


    # -----------------------------------------------------
    # DISPLAY EXECUTION TIMES
    # -----------------------------------------------------

    print("\n======================================")
    print("       EXECUTION TIMES")
    print("======================================")

    print(f"Naive              : {naive_time:.10f} seconds")
    print(f"Divide and Conquer : {divide_time:.10f} seconds")
    print(f"Strassen           : {strassen_time:.10f} seconds")


    # -----------------------------------------------------
    # VERIFY RESULTS
    # -----------------------------------------------------

    print("\n======================================")
    print("          VERIFICATION")
    print("======================================")

    if (
        naive_result == divide_result
        and naive_result == strassen_result
    ):
        print("All three algorithms produced the SAME result.")
        print("Verification successful!")

    else:
        print("Results do NOT match.")
        print("Please check the algorithms.")