def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m = len(matrix)
    n = len(matrix[0])
    max_sum = -float('inf')
    for i in range(n):
        sums = [0]*m
        for j in range(i, n):
            for r in range(m):
                sums[r] += matrix[r][j]
            max_sum = max(max_sum, maxSumSubarray(sums, k))
    return max_sum

if __name__ == '__main__':
    maxSumSubmatrix()