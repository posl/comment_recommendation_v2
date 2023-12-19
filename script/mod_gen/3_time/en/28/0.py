def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    ans = float("-inf")
    for i in range(m):
        total = [0] * n
        for j in range(i, m):
            for c in range(n):
                total[c] += matrix[j][c]
            ans = max(ans, maxSumSubarray(total, k))
    return ans

if __name__ == '__main__':
    maxSumSubmatrix()