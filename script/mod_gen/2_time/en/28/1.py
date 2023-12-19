def maxSumSubmatrix(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    res = float('-inf')
    for i in range(m):
        for j in range(1, n):
            matrix[i][j] += matrix[i][j-1]
                
    for i in range(n):
        for j in range(i, n):
            cur = 0
            preSum = {0:0}
            for l in range(m):
                cur += matrix[l][j] - (matrix[l][i-1] if i > 0 else 0)
                if cur - k in preSum:
                    res = max(res, cur - preSum[cur-k])
                preSum[cur] = cur
    return res
matrix = [[1,0,1],[0,-2,3]]
k = 2
print(maxSumSubmatrix(matrix, k))
matrix = [[2,2,-1]]
k = 3
print(maxSumSubmatrix(matrix, k))
