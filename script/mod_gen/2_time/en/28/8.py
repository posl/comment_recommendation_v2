def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m = len(matrix)
    n = len(matrix[0])
    maxSum = float("-inf")
    for left in range(n):
        rowSum = [0] * m
        for right in range(left, n):
            for i in range(m):
                rowSum[i] += matrix[i][right]
            maxSum = max(maxSum, maxSumSubArray(rowSum, k))
    return maxSum

if __name__ == '__main__':
    maxSumSubmatrix()