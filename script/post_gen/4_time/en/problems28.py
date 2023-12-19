Synthesizing 10/10 solutions

=======
Suggestion 1

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    global_max = float('-inf')
    for i in range(len(matrix[0])):
        row_sum = [0 for _ in range(len(matrix))]
        for j in range(i, len(matrix[0])):
            for row in range(len(matrix)):
                row_sum[row] += matrix[row][j]
            global_max = max(global_max, kadane(row_sum, k))
    return global_max

=======
Suggestion 2

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    def maxSumSubarray(arr, k):
        max_sum = float('-inf')
        prefix_sum = 0
        prefix_sums = [float('inf')]
        for num in arr:
            bisect.insort(prefix_sums, prefix_sum)
            prefix_sum += num
            i = bisect.bisect_left(prefix_sums, prefix_sum - k)
            max_sum = max(max_sum, prefix_sum - prefix_sums[i])
        return max_sum

    max_sum = float('-inf')
    for i in range(len(matrix[0])):
        arr = [0] * len(matrix)
        for j in range(i, len(matrix[0])):
            for k in range(len(matrix)):
                arr[k] += matrix[k][j]
            max_sum = max(max_sum, maxSumSubarray(arr, k))
    return max_sum

=======
Suggestion 3

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    if not matrix:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    result = float("-inf")
    for left in range(cols):
        rowSum = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                rowSum[i] += matrix[i][right]
            result = max(result, maxSumSubArray(rowSum, k))
            if result == k:
                return k
    return result

=======
Suggestion 4

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m = len(matrix)
    n = len(matrix[0])
    ans = -float('inf')
    for l in range(n):
        rowSum = [0] * m
        for r in range(l, n):
            for i in range(m):
                rowSum[i] += matrix[i][r]
            ans = max(ans, maxSumSubArray(rowSum, k))
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

=======
Suggestion 6

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

=======
Suggestion 7

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    def maxSumSubarray(arr):
        maxSum = float("-inf")
        prefixSum = 0
        prefixSums = [float("inf")]
        for num in arr:
            bisect.insort(prefixSums, prefixSum)
            prefixSum += num
            i = bisect.bisect_left(prefixSums, prefixSum - k)
            maxSum = max(maxSum, prefixSum - prefixSums[i])
        return maxSum
    maxSum = float("-inf")
    for left in range(len(matrix[0])):
        rowSums = [0] * len(matrix)
        for right in range(left, len(matrix[0])):
            for i in range(len(matrix)):
                rowSums[i] += matrix[i][right]
            maxSum = max(maxSum, maxSumSubarray(rowSums))
    return maxSum

=======
Suggestion 8

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
        for j in range(n):
            if i > 0:
                matrix[i][j] += matrix[i-1][j]
            if j > 0:
                matrix[i][j] += matrix[i][j-1]
            if i > 0 and j > 0:
                matrix[i][j] -= matrix[i-1][j-1]
            for r in range(i+1):
                for c in range(j+1):
                    subRect = matrix[i][j]
                    if r > 0:
                        subRect -= matrix[r-1][j]
                    if c > 0:
                        subRect -= matrix[i][c-1]
                    if r > 0 and c > 0:
                        subRect += matrix[r-1][c-1]
                    if subRect <= k:
                        maxSum = max(maxSum, subRect)
    return maxSum

matrix = [[1,0,1],[0,-2,3]]
k = 2
print(maxSumSubmatrix(matrix, k))

matrix = [[2,2,-1]]
k = 3
print(maxSumSubmatrix(matrix, k))

=======
Suggestion 9

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
        for j in range(n):
            for p in range(i, m):
                for q in range(j, n):
                    curr_sum = 0
                    for x in range(i, p+1):
                        for y in range(j, q+1):
                            curr_sum += matrix[x][y]
                    if curr_sum <= k:
                        if curr_sum > max_sum:
                            max_sum = curr_sum
    return max_sum

=======
Suggestion 10

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
