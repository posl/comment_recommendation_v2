def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m, n = len(matrix), len(matrix[0])
    res = float('-inf')
    for i in range(n):
        sums = [0] * m
        for j in range(i, n):
            for r in range(m):
                sums[r] += matrix[r][j]
            print(sums)
            # Find the max subarray no more than K
            # Kadane's Algorithm / Maximum Subarray
            max_sum, cur_sum = float('-inf'), 0
            for s in sums:
                cur_sum = max(cur_sum + s, s)
                max_sum = max(max_sum, cur_sum)
                if max_sum == k:
                    return k
            if max_sum < k:
                res = max(res, max_sum)
            else:
                for l in range(m):
                    sums[l] -= matrix[l][i]
    return res
print(maxSumSubmatrix([[1,0,1],[0,-2,3]], 2))
print(maxSumSubmatrix([[2,2,-1]], 3))
print(maxSumSubmatrix([[2,2,-1]], 0))
print(maxSumSubmatrix([[2,2,-1]], -1))
print(maxSumSubmatrix([[2,2,-1]], -2))
print(maxSumSubmatrix([[2,2,-1]], -3))
print(maxSumSubmatrix([[2,2,-1]], -4))
print(maxSumSubmatrix([[2,2,-1]], -5))
print(maxSumSubmatrix([[2,2,-1]], -6))
print(maxSumSubmatrix([[2,2,-1]], -7))
print(maxSumSubmatrix([[2,2,-1]], -8))
print(maxSumSubmatrix([[2,2,-1]], -9))
print(maxSumSubmatrix([[2,2,-1]], -10))
print(maxSumSubmatrix([[2,2,-1]], -11))
print(maxSumSubmatrix([[2,2,-1]], -12))
print(maxSumSubmatrix([[2,2,-1]], -13))
print(maxSumSubmatrix([[2,2,-1]], -14))
print(maxSumSubmatrix([[2,2,-1]], -15))
print(maxSumSubmatrix([[
