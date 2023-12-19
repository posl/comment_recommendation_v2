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
        sums = [0] * n
        for j in range(i, m):
            for c in range(n):
                sums[c] += matrix[j][c]
            maxSum = max(maxSum, maxSumSubarray(sums, k))
    return maxSum

if __name__ == '__main__':
    maxSumSubmatrix()