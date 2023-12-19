Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def maxSumSubmatrix(matrix, k):
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
Suggestion 3

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    #print(matrix)
    #print(k)
    #print()
    if len(matrix) == 1 and len(matrix[0]) == 1:
        if matrix[0][0] <= k:
            return matrix[0][0]
        else:
            return -1
    elif len(matrix) == 1:
        for i in range(len(matrix[0])):
            matrix[0][i] += matrix[0][i-1]

        if max(matrix[0]) <= k:
            return max(matrix[0])
        else:
            return -1
    elif len(matrix[0]) == 1:
        for i in range(len(matrix)):
            matrix[i][0] += matrix[i-1][0]

        if max(matrix)[0] <= k:
            return max(matrix)[0]
        else:
            return -1
    else:
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] += matrix[i][j-1]
        #print(matrix)
        #print()
        for j in range(len(matrix[0])):
            for i in range(1, len(matrix)):
                matrix[i][j] += matrix[i-1][j]
        #print(matrix)
        #print()
        maxSum = -1000000
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for m in range(i, len(matrix)):
                    for n in range(j, len(matrix[0])):
                        if i == 0 and j == 0:
                            tempSum = matrix[m][n]
                        elif i == 0:
                            tempSum = matrix[m][n] - matrix[m][j-1]
                        elif j == 0:
                            tempSum = matrix[m][n] - matrix[i-1][n]
                        else:
                            tempSum = matrix[m][n] - matrix[i-1][n] - matrix[m][j-1] + matrix[i-1][j-1]
                        if tempSum <= k and tempSum > maxSum:
                            maxSum = tempSum
        if maxSum == -1000000:
            return -1
        else:
            return maxSum

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
    max_sum = float('-inf')
    for i in range(m):
        for j in range(n):
            for x in range(i, m):
                for y in range(j, n):
                    max_sum = max(max_sum, sum(matrix[i][j:y+1]) + sum(matrix[x][j:y+1]))
    return max_sum

=======
Suggestion 5

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

=======
Suggestion 6

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    def maxSumSubArray(arr, k):
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
    for i in range(m):
        sums = [0] * n
        for j in range(i, m):
            for c in range(n):
                sums[c] += matrix[j][c]
            maxSum = max(maxSum, maxSumSubArray(sums, k))
    return maxSum

=======
Suggestion 7

def maxSumSubmatrix(matrix, k):
    rows = len(matrix)
    cols = len(matrix[0])
    maxSum = float('-inf')
    for left in range(cols):
        rowSum = [0] * rows
        for right in range(left, cols):
            for row in range(rows):
                rowSum[row] += matrix[row][right]
            maxSum = max(maxSum, maxSumSubArray(rowSum, k))
            if maxSum == k:
                return k
    return maxSum

=======
Suggestion 8

def maxSumSubmatrix(matrix,k):
    m,n = len(matrix),len(matrix[0])
    ans = float('-inf')
    for i in range(m):
        total = [0] * n
        for j in range(i,m):
            for c in range(n):
                total[c] += matrix[j][c]
            totalSet = [0]
            currSum = 0
            for v in total:
                currSum += v
                idx = bisect.bisect_left(totalSet,currSum-k)
                if idx < len(totalSet):
                    ans = max(ans,currSum-totalSet[idx])
                bisect.insort(totalSet,currSum)
    return ans

=======
Suggestion 9

def maxSumSubmatrix(matrix, k):
    m, n = len(matrix), len(matrix[0])
    res = float('-inf')
    for i in range(m):
        sums = [0] * n
        for j in range(i, m):
            for c in range(n):
                sums[c] += matrix[j][c]
            res = max(res, maxSumSubarray(sums, k))
            if res == k:
                return k
    return res

=======
Suggestion 10

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    def maxSumSubarray(arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        maxSum = float('-inf')
        currSum = 0
        sums = [float('inf')]
        for i in range(len(arr)):
            currSum += arr[i]
            idx = bisect.bisect_left(sums, currSum - k)
            if idx < len(sums):
                maxSum = max(maxSum, currSum - sums[idx])
            bisect.insort(sums, currSum)
        return maxSum
    
    row, col = len(matrix), len(matrix[0])
    maxSum = float('-inf')
    for i in range(col):
        temp = [0] * row
        for j in range(i, col):
            for r in range(row):
                temp[r] += matrix[r][j]
            maxSum = max(maxSum, maxSumSubarray(temp, k))
    return maxSum
