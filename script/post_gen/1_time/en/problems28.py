Synthesizing 10/10 solutions

=======
Suggestion 1

def maxSumSubmatrix(matrix, k):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    ans = float('-inf')
    for left in range(n):
        rowSum = [0] * m
        for right in range(left, n):
            for i in range(m):
                rowSum[i] += matrix[i][right]
            prefixSum = [0]
            cur = 0
            for r in rowSum:
                cur += r
                idx = bisect.bisect_left(prefixSum, cur - k)
                if idx < len(prefixSum):
                    ans = max(ans, cur - prefixSum[idx])
                bisect.insort(prefixSum, cur)
    return ans

=======
Suggestion 2

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    def maxSumSubarray(arr, k):
        # Find the max sum subarray <= k
        maxSum = float('-inf')
        prefixSum = 0
        prefixSums = [float('inf')]
        for num in arr:
            bisect.insort(prefixSums, prefixSum)
            prefixSum += num
            i = bisect.bisect_left(prefixSums, prefixSum - k)
            maxSum = max(maxSum, prefixSum - prefixSums[i])
        return maxSum

    m, n = len(matrix), len(matrix[0])
    ans = float('-inf')
    for i in range(m):
        arr = [0] * n
        for j in range(i, m):
            for c in range(n):
                arr[c] += matrix[j][c]
            ans = max(ans, maxSumSubarray(arr, k))
    return ans

=======
Suggestion 3

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m = len(matrix)
    n = len(matrix[0])
    max_sum = float('-inf')
    for i in range(m):
        sums = [0] * n
        for j in range(i, m):
            for col in range(n):
                sums[col] += matrix[j][col]
            max_sum = max(max_sum, maxSubArray(sums, k))
            if max_sum == k:
                return k
    return max_sum

=======
Suggestion 4

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    if not matrix or not matrix[0]:
        return 0
    row = len(matrix)
    col = len(matrix[0])
    ans = float('-inf')
    for left in range(col):
        rowSum = [0] * row
        for right in range(left, col):
            for i in range(row):
                rowSum[i] += matrix[i][right]
            ans = max(ans, maxSumSubarray(rowSum, k))
            if ans == k:
                return k
    return ans

=======
Suggestion 5

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

=======
Suggestion 6

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

=======
Suggestion 7

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

=======
Suggestion 8

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    if not matrix:
        return 0
    
    def maxSumSubarray(arr, k):
        maxSum = float('-inf')
        prefixSum = 0
        prefixSums = [float('inf')]
        for num in arr:
            bisect.insort(prefixSums, prefixSum)
            prefixSum += num
            i = bisect.bisect_left(prefixSums, prefixSum - k)
            maxSum = max(maxSum, prefixSum - prefixSums[i])
        return maxSum
    
    m, n = len(matrix), len(matrix[0])
    maxSum = float('-inf')
    for left in range(n):
        rowSums = [0] * m
        for right in range(left, n):
            for i in range(m):
                rowSums[i] += matrix[i][right]
            maxSum = max(maxSum, maxSumSubarray(rowSums, k))
    return maxSum

=======
Suggestion 9

def maxSumSubmatrix(matrix, k):
    import bisect
    m, n = len(matrix), len(matrix[0])
    M, N = max(m, n), min(m, n)
    ans = float('-inf')
    for i in range(N):
        sums = [0] * M
        for j in range(i, N):
            slist, cur = [0], 0
            for k in range(M):
                sums[k] += matrix[k][j] if m > n else matrix[j][k]
                cur += sums[k]
                idx = bisect.bisect_left(slist, cur - k)
                if idx < len(slist): ans = max(ans, cur - slist[idx])
                bisect.insort(slist, cur)
                if ans == k: return ans
    return ans

print(maxSumSubmatrix([[1,0,1],[0,-2,3]], 2)) # 2
print(maxSumSubmatrix([[2,2,-1]], 3)) # 3
print(maxSumSubmatrix([[2,2,-1, 5]], 3)) # 2
print(maxSumSubmatrix([[2,2,-1, 5]], 4)) # 4
print(maxSumSubmatrix([[2,2,-1, 5]], 5)) # 5
print(maxSumSubmatrix([[2,2,-1, 5]], 6)) # 6
print(maxSumSubmatrix([[2,2,-1, 5]], 7)) # 7
print(maxSumSubmatrix([[2,2,-1, 5]], 8)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]], 9)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]], 10)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]], 11)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]], 12)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]], 13)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]], 14)) # 8
print(maxSumSubmatrix([[2,2,-1, 5]],

=======
Suggestion 10

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    if len(matrix) == 0:
        return 0
    if len(matrix[0]) == 0:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    maxSum = -float('inf')
    for i in range(n):
        rowSum = [0 for _ in range(m)]
        for j in range(i, n):
            for k in range(m):
                rowSum[k] += matrix[k][j]
            maxSum = max(maxSum, maxSumSubarray(rowSum, k))
            if maxSum == k:
                return maxSum
    return maxSum
