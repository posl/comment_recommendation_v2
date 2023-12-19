def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    # Solution 1
    # Time Complexity: O(n^4)
    # Space Complexity: O(1)
    #for i in range(len(matrix)):
    #    for j in range(len(matrix[0])):
    #        if i > 0:
    #            matrix[i][j] += matrix[i - 1][j]
    #        if j > 0:
    #            matrix[i][j] += matrix[i][j - 1]
    #        if i > 0 and j > 0:
    #            matrix[i][j] -= matrix[i - 1][j - 1]
    #res = float('-inf')
    #for i in range(len(matrix)):
    #    for j in range(len(matrix[0])):
    #        for p in range(i, len(matrix)):
    #            for q in range(j, len(matrix[0])):
    #                cur = matrix[p][q]
    #                if i > 0:
    #                    cur -= matrix[i - 1][q]
    #                if j > 0:
    #                    cur -= matrix[p][j - 1]
    #                if i > 0 and j > 0:
    #                    cur += matrix[i - 1][j - 1]
    #                if cur <= k:
    #                    res = max(res, cur)
    #return res
    # Solution 2
    # Time Complexity: O(n^2 * mlog(m))
    # Space Complexity: O(n * m)
    #res = float('-inf')
    #for left in range(len(matrix[0])):
    #    rowSum = [0] * len(matrix)
    #    for right in range(left, len(matrix[0])):
    #        for i in range(len(matrix)):
    #            rowSum[i] += matrix[i][right]
    #        bst, cur = SortedList([0]), 0
    #        for s in rowSum:
    #            cur += s
    #            idx = bisect.bisect_left(bst, cur - k)
    #            if idx < len(bst):
    #                res = max(res, cur - bst[idx])

if __name__ == '__main__':
    maxSumSubmatrix()