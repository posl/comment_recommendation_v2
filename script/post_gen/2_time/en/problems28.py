Synthesizing 10/10 solutions

=======
Suggestion 1

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        max_sum = float('-inf')
        for i in range(len(matrix[0])):
            row_sum = [0] * len(matrix)
            for j in range(i, len(matrix[0])):
                for k in range(len(matrix)):
                    row_sum[k] += matrix[k][j]
                max_sum = max(max_sum, self.maxSumSubArray(row_sum, k))
        return max_sum

=======
Suggestion 2

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        maxSum = float('-inf')
        for left in range(n):
            rowSum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    rowSum[i] += matrix[i][right]
                maxSum = max(maxSum, self.maxSumSubarray(rowSum, k))
        return maxSum

=======
Suggestion 3

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        M, N = len(matrix), len(matrix[0])
        ans = float('-inf')
        for i in range(N):
            total = [0] * M
            for j in range(i, N):
                for row in range(M):
                    total[row] += matrix[row][j]
                # print(total)
                # ans = max(ans, self.maxSubArray(total, k))
                ans = max(ans, self.maxSubArrayLessThanK(total, k))
        return ans

=======
Suggestion 4

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m < n:
            matrix = list(zip(*matrix))
            m, n = n, m
        ans = -100000
        for i in range(m):
            sums = [0] * n
            for j in range(i, m):
                for c in range(n):
                    sums[c] += matrix[j][c]
                s = 0
                ss = [0]
                for v in sums:
                    s += v
                    idx = bisect.bisect_left(ss, s - k)
                    if idx < len(ss):
                        ans = max(ans, s - ss[idx])
                    bisect.insort(ss, s)
        return ans

=======
Suggestion 5

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')
        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for c in range(n):
                    total[c] += matrix[j][c]
                totalSet = [0]
                curSum = 0
                for v in total:
                    curSum += v
                    idx = bisect.bisect_left(totalSet, curSum - k)
                    if idx < len(totalSet):
                        ans = max(ans, curSum - totalSet[idx])
                    bisect.insort(totalSet, curSum)
        return ans

=======
Suggestion 6

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        ans = float('-inf')
        for i in range(col):
            total = [0] * row
            for j in range(i, col):
                for r in range(row):
                    total[r] += matrix[r][j]
                totalSet = [0]
                cur = 0
                for t in total:
                    cur += t
                    idx = bisect.bisect_left(totalSet, cur - k)
                    if idx < len(totalSet):
                        ans = max(ans, cur - totalSet[idx])
                    bisect.insort(totalSet, cur)
        return ans

=======
Suggestion 7

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_sum = -float("inf")
        for i in range(m):
            for j in range(n):
                for p in range(i, m):
                    for q in range(j, n):
                        cur_sum = 0
                        for r in range(i, p+1):
                            for s in range(j, q+1):
                                cur_sum += matrix[r][s]
                        if cur_sum <= k:
                            max_sum = max(max_sum, cur_sum)
        return max_sum

=======
Suggestion 8

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        #O(m^2*n^2) time and O(mn) space
        #prefix sum
        #sum of submatrix = prefix_sum[x2][y2] - prefix_sum[x2][y1] - prefix_sum[x1][y2] + prefix_sum[x1][y1]
        #x1,y1 = (0,0)
        #x2,y2 = (x,y)
        #x1,y2 = (0,y)
        #x2,y1 = (x,0)
        #x,y = (x2-x1,y2-y1)
        #O(m^2*n^2) time and O(mn) space
        m,n = len(matrix),len(matrix[0])
        prefix_sum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + matrix[i-1][j-1]
        ans = -float('inf')
        for x2 in range(1,m+1):
            for y2 in range(1,n+1):
                for x1 in range(x2):
                    for y1 in range(y2):
                        val = prefix_sum[x2][y2] - prefix_sum[x2][y1] - prefix_sum[x1][y2] + prefix_sum[x1][y1]
                        if val <= k:
                            ans = max(ans,val)
        return ans
        #binary search
        #O(m^2*n*logn) time and O(mn) space
        m,n = len(matrix),len(matrix[0])
        prefix_sum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + matrix[i-1][j-1]
        ans = -float('inf')
        for x2 in range(1,m+1):
            for y2 in range(1,n

=======
Suggestion 9

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        def maxSumSublist(nums: list[int]) -> int:
            maxSum = float('-inf')
            prefixSum = 0
            prefixSums = [float('inf')]
            for num in nums:
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
                for l in range(n):
                    sums[l] += matrix[j][l]
                maxSum = max(maxSum, maxSumSublist(sums))
        return maxSum

=======
Suggestion 10

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        def maxSumSubarray(arr: list[int]) -> int:
            maxSum = arr[0]
            currSum = arr[0]
            for i in range(1, len(arr)):
                currSum = max(arr[i], currSum + arr[i])
                maxSum = max(maxSum, currSum)
            return maxSum
        
        def maxSumSubmatrixHelper(matrix: list[list[int]], k: int) -> int:
            maxSum = float('-inf')
            for left in range(len(matrix[0])):
                arr = [0] * len(matrix)
                for right in range(left, len(matrix[0])):
                    for i in range(len(matrix)):
                        arr[i] += matrix[i][right]
                    maxSum = max(maxSum, maxSumSubarray(arr))
                    if maxSum == k:
                        return k
            return maxSum
        
        maxSum = float('-inf')
        for left in range(len(matrix[0])):
            arr = [0] * len(matrix)
            for right in range(left, len(matrix[0])):
                for i in range(len(matrix)):
                    arr[i] += matrix[i][right]
                maxSum = max(maxSum, maxSumSubarray(arr))
                if maxSum == k:
                    return k
                if maxSum < k:
                    maxSum = max(maxSum, maxSumSubmatrixHelper(matrix, k))
                    if maxSum == k:
                        return k
        return maxSum
