def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m = len(matrix)
    n = len(matrix[0])
    maxSum = float('-inf')
    for i in range(m):
        for j in range(n):
            if i > 0:
                matrix[i][j] += matrix[i-1][j]
            if j > 0:
                matrix[i][j] += matrix[i][j-1]
            if i > 0 and j > 0:
                matrix[i][j] -= matrix[i-1][j-1]
            for r in range(i+1):
                for c in range(j+1):
                    subRect = matrix[i][j]
                    if r > 0:
                        subRect -= matrix[r-1][j]
                    if c > 0:
                        subRect -= matrix[i][c-1]
                    if r > 0 and c > 0:
                        subRect += matrix[r-1][c-1]
                    if subRect <= k:
                        maxSum = max(maxSum, subRect)
    return maxSum
matrix = [[1,0,1],[0,-2,3]]
k = 2
print(maxSumSubmatrix(matrix, k))
matrix = [[2,2,-1]]
k = 3
print(maxSumSubmatrix(matrix, k))
