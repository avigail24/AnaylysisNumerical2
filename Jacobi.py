import numpy as np
from numpy.linalg import norm
from matrix_utility import is_diagonally_dominant, DominantDiagonalFix, is_square_matrix, reorder_dominant_diagonal

"""
Performs Jacobi iterations to solve the line system of equations, Ax=b, 
starting from an initial guess, ``x0``.

Terminates when the change in x is less than ``tol``, or
if ``N`` [default=200] iterations have been exceeded.

Receives 5 parameters:
    1.  a, the NxN matrix that method is being performed on.
    2.  b, vector of solution. 
    3.  X0,  the desired initial guess.
        if x is None, the initial guess will bw determined as a vector of 0's.
    4.  TOL, tolerance- the desired limitation of tolerance of solution's anomaly.
        if tolerance is None, the default value will set as 1e-16.
    5.  N, the maxim number of possible iterations to receive the most exact solution.
        if N is None, the default value will set as 200.

Returns variables:
    1.  x, the estimated solution

"""


def jacobi_iterative(matrix, vector_b, vector_0, TOL=1e-16, max_Iteration=200):
    size = len(matrix)
    Iteration = 1

    if is_diagonally_dominant(matrix):
        print('Matrix is diagonally dominant - preforming jacobi algorithm\n')
    else:
        matrix = DominantDiagonalFix(matrix, vector_b)
    print(vector_b)
    print("Iteration" + "\t\t\t".join(
        [" {:>12}".format(var) for var in ["x{}".format(i) for i in range(1, len(matrix) + 1)]]))
    print("-----------------------------------------------------------------------------------------------")

    while Iteration <= max_Iteration:
        x = np.zeros(size, dtype=np.double)
        for i in range(size):
            sigma = 0
            for j in range(size):
                if j != i:
                    sigma += matrix[i][j] * vector_0[j]
            x[i] = (vector_b[i] - sigma) / matrix[i][i]

        print("{:<15} ".format(Iteration) + "\t\t".join(["{:<15} ".format(val) for val in x]))

        if norm(x - vector_0, np.inf) < TOL:
            return tuple(x)

        Iteration += 1
        vector_0 = x.copy()

    print("Maximum number of iterations exceeded")
    return tuple(x)


if __name__ == "__main__":
    A = np.array([2,3,4,5,6], [-5,3,4,-2,3], [4,-5,-2,2,6],[4,5,-1,-2,-3], [5,5,3,-3,5])
    b = np.array([70,20,26,-12,37])

    x = np.zeros_like(b, dtype=np.double)
    solution = jacobi_iterative(A, b, x)

    print("\nApproximate solution:", solution)
