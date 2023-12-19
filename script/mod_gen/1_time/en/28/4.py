def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m, n = len(matrix), len(matrix[0])
    res = float('-inf')
    for left in range(n):
        sums = [0] * m
        for right in range(left, n):
            for i in range(m):
                sums[i] += matrix[i][right]
            res = max(res, maxSumSubArray(sums, k))
    return res

if __name__ == '__main__':
    maxSumSubmatrix()