def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    if not matrix or not matrix[0]:
        return 0
    M, N = len(matrix), len(matrix[0])
    res = -float('inf')
    for i in range(N):
        sums = [0] * M
        for j in range(i, N):
            for m in range(M):
                sums[m] += matrix[m][j]
            res = max(res, maxSumSubarray(sums, k))
            if res == k:
                return k
    return res

if __name__ == '__main__':
    maxSumSubmatrix()