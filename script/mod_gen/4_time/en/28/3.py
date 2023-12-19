def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m = len(matrix)
    n = len(matrix[0])
    ans = -float('inf')
    for l in range(n):
        rowSum = [0] * m
        for r in range(l, n):
            for i in range(m):
                rowSum[i] += matrix[i][r]
            ans = max(ans, maxSumSubArray(rowSum, k))
            if ans == k:
                return k
    return ans

if __name__ == '__main__':
    maxSumSubmatrix()