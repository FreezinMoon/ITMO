class Solution:
    isSolutionExists = True
    errorMessage = ""

    #
    # Complete the 'solveByGauss' function below.
    #
    # The function is expected to return a DOUBLE_ARRAY.
    # The function accepts following parameters:
    #  1. INTEGER n
    #  2. 2D_DOUBLE_ARRAY matrix
    #
    @staticmethod
    def solveByGauss(n, matrix):
        original_matrix = [[matrix[i][j] for j in range(n + 1)] for i in range(n)]

        for i in range(n):
            max_el = abs(matrix[i][i])
            max_row = i
            for k in range(i + 1, n):
                if abs(matrix[k][i]) > max_el:
                    max_el = abs(matrix[k][i])
                    max_row = k

            if max_el == 0:
                Solution.isSolutionExists = False
                Solution.errorMessage = "The system has no roots of equations or has an infinite set of them."
                return []

            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

            for k in range(i + 1, n):
                c = -matrix[k][i] / matrix[i][i]
                for j in range(i, n + 1):
                    if i == j:
                        matrix[k][j] = 0
                    else:
                        matrix[k][j] += c * matrix[i][j]

        x = [0 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            x[i] = matrix[i][n] / matrix[i][i]
            for k in range(i - 1, -1, -1):
                matrix[k][n] -= matrix[k][i] * x[i]

        residuals = []
        for i in range(n):
            lhs = sum(original_matrix[i][j] * x[j] for j in range(n))
            residual = abs(lhs - original_matrix[i][n])
            residuals.append(residual)

        return x + residuals