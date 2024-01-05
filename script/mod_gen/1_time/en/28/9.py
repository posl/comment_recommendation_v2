def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    if len(matrix) == 0:
        return 0
    if len(matrix[0]) == 0:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    maxSum = -float('inf')
    for i in range(n):
        rowSum = [0 for _ in range(m)]
        for j in range(i, n):
            for k in range(m):
                rowSum[k] += matrix[k][j]
            maxSum = max(maxSum, maxSumSubarray(rowSum, k))
            if maxSum == k:
                return maxSum
    return maxSum

if __name__ == '__main__':
    matrix = ==========please modify============
    k = int(input())
    a = maxSumSubmatrix(matrix, k)
    print(a)