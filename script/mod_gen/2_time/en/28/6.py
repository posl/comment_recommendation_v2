def maxSumSubmatrix(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    max_sum = -1e9
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
                    sub_sum = matrix[i][j]
                    if r > 0:
                        sub_sum -= matrix[r-1][j]
                    if c > 0:
                        sub_sum -= matrix[i][c-1]
                    if r > 0 and c > 0:
                        sub_sum += matrix[r-1][c-1]
                    if sub_sum <= k:
                        max_sum = max(max_sum, sub_sum)
    return max_sum
matrix = [[1,0,1],[0,-2,3]]
k = 2
print(maxSumSubmatrix(matrix, k))
