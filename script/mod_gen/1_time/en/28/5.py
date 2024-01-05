def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    res = float('-inf')
    for left in range(n):
        sums = [0] * m
        for right in range(left, n):
            for i in range(m):
                sums[i] += matrix[i][right]
            res = max(res, helper(sums, k))
            if res == k:
                return k
    return res

if __name__ == '__main__':
    matrix = ==========please modify============
    k = int(input())
    a = maxSumSubmatrix(matrix, k)
    print(a)