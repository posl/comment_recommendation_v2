def maxSumSubmatrix(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    maxSum = -float('inf')
    for i in range(m):
        for j in range(n):
            if i > 0:
                matrix[i][j] += matrix[i - 1][j]
            if j > 0:
                matrix[i][j] += matrix[i][j - 1]
            if i > 0 and j > 0:
                matrix[i][j] -= matrix[i - 1][j - 1]
            for x in range(i + 1):
                for y in range(j + 1):
                    submatrixSum = matrix[i][j]
                    if x > 0:
                        submatrixSum -= matrix[x - 1][j]
                    if y > 0:
                        submatrixSum -= matrix[i][y - 1]
                    if x > 0 and y > 0:
                        submatrixSum += matrix[x - 1][y - 1]
                    if submatrixSum <= k:
                        maxSum = max(maxSum, submatrixSum)
    return maxSum

if __name__ == '__main__':
    maxSumSubmatrix()