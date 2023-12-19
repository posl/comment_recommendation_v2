Synthesizing 10/10 solutions

=======
Suggestion 1

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    row = len(matrix)
    col = len(matrix[0])
    max_sum = -float('inf')
    for left in range(col):
        _sum = [0] * row
        for right in range(left, col):
            for i in range(row):
                _sum[i] += matrix[i][right]
            print(_sum)
            print("left: ", left, "right: ", right)
            print("max_sum: ", max_sum)
            print("k: ", k, "sum: ", _sum)
            print()
            max_sum = max(max_sum, maxSubArray(_sum, k))
    return max_sum

=======
Suggestion 2

def maxSumSubmatrix(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    res = float('-inf')
    for i in range(m):
        for j in range(1, n):
            matrix[i][j] += matrix[i][j-1]
                
    for i in range(n):
        for j in range(i, n):
            cur = 0
            preSum = {0:0}
            for l in range(m):
                cur += matrix[l][j] - (matrix[l][i-1] if i > 0 else 0)
                if cur - k in preSum:
                    res = max(res, cur - preSum[cur-k])
                preSum[cur] = cur
    return res

matrix = [[1,0,1],[0,-2,3]]
k = 2
print(maxSumSubmatrix(matrix, k))

matrix = [[2,2,-1]]
k = 3
print(maxSumSubmatrix(matrix, k))

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

    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = float('-inf')

    for left in range(cols):
        row_sums = [0] * rows
        for right in range(left, cols):
            for row in range(rows):
                row_sums[row] += matrix[row][right]

            max_sum = max(max_sum, max_sum_subarray(row_sums, k))

    return max_sum

=======
Suggestion 4

def maxSumSubmatrix(matrix, k):
    m, n = len(matrix), len(matrix[0])
    M = max(m, n)
    N = min(m, n)
    ans = float("-inf")
    for x in range(N):
        sums = [0] * M
        for y in range(x, N):
            slist, num = [], 0
            for z in range(M):
                sums[z] += matrix[z][y] if m > n else matrix[y][z]
                num += sums[z]
                if num <= k:
                    ans = max(ans, num)
                i = bisect.bisect_left(slist, num - k)
                if i != len(slist):
                    ans = max(ans, num - slist[i])
                bisect.insort(slist, num)
    return ans

=======
Suggestion 5

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    m=len(matrix)
    n=len(matrix[0])
    maxSum=-1000000
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:
                matrix[i][j]=matrix[i][j]
            elif i==0:
                matrix[i][j]=matrix[i][j]+matrix[i][j-1]
            elif j==0:
                matrix[i][j]=matrix[i][j]+matrix[i-1][j]
            else:
                matrix[i][j]=matrix[i][j]+matrix[i-1][j]+matrix[i][j-1]-matrix[i-1][j-1]
    for i in range(m):
        for j in range(n):
            for p in range(i,m):
                for q in range(j,n):
                    if i==0 and j==0:
                        sum=matrix[p][q]
                    elif i==0:
                        sum=matrix[p][q]-matrix[p][j-1]
                    elif j==0:
                        sum=matrix[p][q]-matrix[i-1][q]
                    else:
                        sum=matrix[p][q]-matrix[p][j-1]-matrix[i-1][q]+matrix[i-1][j-1]
                    if sum<=k:
                        maxSum=max(maxSum,sum)
    return maxSum

matrix = [[1,0,1],[0,-2,3]]
k = 2
print(maxSumSubmatrix(matrix,k))

matrix = [[2,2,-1]]
k = 3
print(maxSumSubmatrix(matrix,k))

=======
Suggestion 6

def maxSumSubmatrix(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    result = float("-inf")
    for left in range(n):
        sums = [0] * m
        for right in range(left, n):
            for i in range(m):
                sums[i] += matrix[i][right]
            result = max(result, maxSumSubArray(sums, k))
    return result

=======
Suggestion 7

def maxSumSubmatrix(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    max_sum = -1e9
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
                    sub_sum = matrix[i][j]
                    if r > 0:
                        sub_sum -= matrix[r-1][j]
                    if c > 0:
                        sub_sum -= matrix[i][c-1]
                    if r > 0 and c > 0:
                        sub_sum += matrix[r-1][c-1]
                    if sub_sum <= k:
                        max_sum = max(max_sum, sub_sum)
    return max_sum

matrix = [[1,0,1],[0,-2,3]]
k = 2
print(maxSumSubmatrix(matrix, k))

=======
Suggestion 8

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """

    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = None

    for left in range(cols):
        row_sums = [0] * rows
        for right in range(left, cols):
            for row in range(rows):
                row_sums[row] += matrix[row][right]
            max_sum = max(max_sum, maxSumSubarray(row_sums, k))

    return max_sum

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
    maxSum = float("-inf")
    for left in range(n):
        rowSum = [0] * m
        for right in range(left, n):
            for i in range(m):
                rowSum[i] += matrix[i][right]
            maxSum = max(maxSum, maxSumSubArray(rowSum, k))
    return maxSum

=======
Suggestion 10

def maxSumSubmatrix(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    # M1. 暴力法
    # 1. 遍历所有的子矩阵，计算每个子矩阵的和
    # 2. 保留所有不大于k的子矩阵的和
    # 3. 返回最大的和
    # O(m^2 * n^2)
    # O(mn)
    # 优化：提前终止
    # 1. 当前的sum > k，直接跳出循环
    # 2. 当前的sum == k，直接返回k
    # 3. 当前的sum < k，更新最大值
    # 4. 当前的sum == k，直接返回k
    # O(m^2 * n^2)
    # O(mn)
    # 优化：前缀和
    # 1. 求出每个矩形的前缀和
    # 2. 遍历所有的子矩阵，计算每个子矩阵的和
    # 3. 保留所有不大于k的子矩阵的和
    # 4. 返回最大的和
    # O(m^2 * n^2)
    # O(mn)
    # 优化：前缀和 + 二分法
    # 1. 求出每个矩形的前缀和
    # 2. 遍历所有的子矩阵，计算每个子矩阵的和
    # 3. 保留所有不大于k的子矩阵的和
    # 4. 返回最大的和
    # O(m^2 * nlogn)
    # O(mn)
    # 优化：前缀和 + 二分法 + 优先队列
    # 1. 求出每个矩
