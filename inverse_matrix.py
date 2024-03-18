from matrix_utility import row_addition_elementary_matrix, scalar_multiplication_elementary_matrix, Cond, matrix_multiply
import numpy as np

"""
Function that find the
 inverse of non-singular matrix
The function performs elementary row operations to transform it into the identity matrix.
The resulting identity matrix will be the inverse of the input matrix if it is non-singular.
 If the input matrix is singular (i.e., its diagonal elements become zero during row operations), it raises an error.
"""

def inverse(matrix):
    global matrix_number  # Define global variable to store matrix number
    matrix_number = 0  # Initialize matrix number
    print(f"=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n {matrix}\n")
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)
    counter = 0  # Initialize counter

    # Perform row operations to transform the input matrix into the identity matrix
    for i in range(n):
        # Perform row exchanges if the pivot element is zero
        if matrix[i, i] == 0:
            # Find a row below with a non-zero element in the same column
            for k in range(i + 1, n):
                if matrix[k, i] != 0:
                    # Exchange rows i and k in both the input matrix and the identity matrix
                    matrix[[i, k]] = matrix[[k, i]]
                    identity[[i, k]] = identity[[k, i]]
                    counter += 1  # Increment counter
                    matrix_number += 1  # Increment matrix number
                    print(f"Matrix number after elementary operation: {matrix_number}")
                    break
            else:
                raise ValueError("Matrix is singular, cannot find its inverse.")

        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            scalar = 1.0 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            print(f"elementary matrix to make the diagonal element 1 :\n {elementary_matrix} \n")
            matrix = np.dot(elementary_matrix, matrix)
            print(f"The matrix after elementary operation :\n {matrix}")
            print("------------------------------------------------------------------------------------------------------------------")
            identity = np.dot(elementary_matrix, identity)
            counter += 1  # Increment counter
            matrix_number += 1  # Increment matrix number
            print(f"Matrix number after elementary operation: {matrix_number}")

        # Zero out the elements above and below the diagonal
        for j in range(n):
            if  i < j and matrix[j, i]:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                print(f"elementary matrix for R{j+1} = R{j+1} + ({scalar}R{i+1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                print(f"The matrix after elementary operation :\n {matrix}")
                print("------------------------------------------------------------------------------------------------------------------")
                identity = np.dot(elementary_matrix, identity)
                counter += 1  # Increment counter
                matrix_number += 1  # Increment matrix number
                print(f"Matrix number after elementary operation: {matrix_number}")

    for i in range(n)[::-1]:
        for j in range(n)[::-1]:
            if i > j and matrix[j, i]:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                print(f"elementary matrix for R{j + 1} = R{j + 1} + ({scalar}R{i + 1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                print(f"The matrix after elementary operation :\n {matrix}")
                print(
                    "------------------------------------------------------------------------------------------------------------------")
                identity = np.dot(elementary_matrix, identity)
                counter += 1  # Increment counter
                matrix_number += 1  # Increment matrix number
                print(f"Matrix number after elementary operation: {matrix_number}")

    print("Number of times the matrix was printed after elementary operations:", counter)  # Print counter
    return identity

def print_specific_elementary(matrix, num):
    global matrix_number  # Define global variable to store matrix number
    matrix_number = 0  # Initialize matrix number
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)
    counter = 0  # Initialize counter

    # Perform row operations to transform the input matrix into the identity matrix
    for i in range(n):
        # Perform row exchanges if the pivot element is zero
        if matrix[i, i] == 0:
            # Find a row below with a non-zero element in the same column
            for k in range(i + 1, n):
                if matrix[k, i] != 0:
                    # Exchange rows i and k in both the input matrix and the identity matrix
                    matrix[[i, k]] = matrix[[k, i]]
                    identity[[i, k]] = identity[[k, i]]
                    counter += 1  # Increment counter
                    matrix_number += 1  # Increment matrix number
                    print(f"Matrix number after elementary operation: {matrix_number}")
                    break
            else:
                raise ValueError("Matrix is singular, cannot find its inverse.")

        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            scalar = 1.0 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            if num == matrix_number:
                print(elementary_matrix)
            matrix = np.dot(elementary_matrix, matrix)
            identity = np.dot(elementary_matrix, identity)
            counter += 1  # Increment counter
            matrix_number += 1  # Increment matrix number

        # Zero out the elements above and below the diagonal
        for j in range(n):
            if i < j and matrix[j, i]:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                if num == matrix_number:
                    print(elementary_matrix)
                matrix = np.dot(elementary_matrix, matrix)
                identity = np.dot(elementary_matrix, identity)
                counter += 1  # Increment counter
                matrix_number += 1  # Increment matrix number

    for i in range(n)[::-1]:
        for j in range(n)[::-1]:
            if i > j and matrix[j, i]:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                if num == matrix_number:
                    print(elementary_matrix)
                matrix = np.dot(elementary_matrix, matrix)
                identity = np.dot(elementary_matrix, identity)
                counter += 1  # Increment counter
                matrix_number += 1  # Increment matrix number


def mult_elementaries(matrix, num1, num2):
    elemen1 = []
    elemen2 = []
    global matrix_number  # Define global variable to store matrix number
    matrix_number = 0  # Initialize matrix number
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)
    counter = 0  # Initialize counter

    # Perform row operations to transform the input matrix into the identity matrix
    for i in range(n):
        # Perform row exchanges if the pivot element is zero
        if matrix[i, i] == 0:
            # Find a row below with a non-zero element in the same column
            for k in range(i + 1, n):
                if matrix[k, i] != 0:
                    # Exchange rows i and k in both the input matrix and the identity matrix
                    matrix[[i, k]] = matrix[[k, i]]
                    identity[[i, k]] = identity[[k, i]]
                    counter += 1  # Increment counter
                    matrix_number += 1  # Increment matrix number
                    print(f"Matrix number after elementary operation: {matrix_number}")
                    break
            else:
                raise ValueError("Matrix is singular, cannot find its inverse.")

        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            scalar = 1.0 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            if num1 == matrix_number:
                elemen1 = elementary_matrix
            if num2 == matrix_number:
                elemen2 = elementary_matrix
            matrix = np.dot(elementary_matrix, matrix)
            identity = np.dot(elementary_matrix, identity)
            counter += 1  # Increment counter
            matrix_number += 1  # Increment matrix number

        # Zero out the elements above and below the diagonal
        for j in range(n):
            if i < j and matrix[j, i]:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                if num1 == matrix_number:
                    elemen1 = elementary_matrix
                if num2 == matrix_number:
                    elemen2 = elementary_matrix
                matrix = np.dot(elementary_matrix, matrix)
                identity = np.dot(elementary_matrix, identity)
                counter += 1  # Increment counter
                matrix_number += 1  # Increment matrix number

    for i in range(n)[::-1]:
        for j in range(n)[::-1]:
            if i > j and matrix[j, i]:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                if num1 == matrix_number:
                    elemen1 = elementary_matrix
                if num2 == matrix_number:
                    elemen2 = elementary_matrix
                matrix = np.dot(elementary_matrix, matrix)
                identity = np.dot(elementary_matrix, identity)
                counter += 1  # Increment counter
                matrix_number += 1  # Increment matrix number
    return matrix_multiply(elemen1, elemen2)


# הדפסת טיב ההצגה נמצא בutillity
#מקבלת מטריצה ואת ההופכית שלה
if __name__ == '__main__':

    A = np.array([[1, 1/2 , 1/3],
                  [1/2, 1/3, 1/4],
                  [1/3, 1/4, 1/5]])

    B = np.array([[1, 10, -10],
                  [0, 4, 6],
                  [0, 1, 9]])
    print(inverse(B))
    # print_specific_elementary(A, 0)
    # print("=====================================================================================================================")
    # print_specific_elementary(A, 1)
    # print("=====================================================================================================================")
    # print_specific_elementary(A, 2)
    # print(mult_elementaries(A, 7, 5))
    # try:
    #     A_inverse = inverse(A)
    #     print("\nInverse of matrix A: \n", A_inverse)
    #     print("=====================================================================================================================")
    #
    # except ValueError as e:
    #     print(str(e))

# #אם מפעילים פה COND אז זה מפעיל שוב את ההפיכה
# print(Cond(A,inverse(A)))