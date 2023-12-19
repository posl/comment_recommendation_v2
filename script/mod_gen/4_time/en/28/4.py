def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m = len(matrix)
    n = len(matrix[0])
    max_sum = -float('inf')
    for i in range(m):
        cum_sum = [0] * n
        for j in range(i, m):
            for col in range(n):
                cum_sum[col] += matrix[j][col]
            max_sum = max(max_sum, maxSumSubarray(cum_sum, k))
    return max_sum

if __name__ == '__main__':
    maxSumSubmatrix()