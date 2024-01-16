Synthesizing 10/10 solutions

=======
Suggestion 1

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = float("-inf")
        for i in range(n):
            sums = [0] * m
            for j in range(i, n):
                for r in range(m):
                    sums[r] += matrix[r][j]
                res = max(res, self.maxSumSubarray(sums, k))
        return res

=======
Suggestion 2

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        max_sum = -float('inf')
        for i in range(n):
            sums = [0]*m
            for j in range(i, n):
                for r in range(m):
                    sums[r] += matrix[r][j]
                max_sum = max(max_sum, self.maxSumSubarray(sums, k))
        return max_sum

=======
Suggestion 3

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')
        for l in range(n):
            rowSum = [0] * m
            for r in range(l, n):
                for i in range(m):
                    rowSum[i] += matrix[i][r]
                ans = max(ans, self.maxSumSubarray(rowSum, k))
                if ans == k:
                    return k
        return ans

=======
Suggestion 4

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')
        for left in range(n):
            rowSum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    rowSum[i] += matrix[i][right]
                ans = max(ans, self.maxSumSubArray(rowSum, k))
                if ans == k:
                    return ans
        return ans

=======
Suggestion 5

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        row_len = len(matrix)
        col_len = len(matrix[0])
        max_sum = float('-inf')
        for l in range(col_len):
            row_sum = [0] * row_len
            for r in range(l, col_len):
                for i in range(row_len):
                    row_sum[i] += matrix[i][r]
                max_sum = max(max_sum, self.maxSumSubArray(row_sum, k))
                if max_sum == k:
                    return max_sum
        return max_sum

=======
Suggestion 6

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        # 1. get the sum of the matrix
        # 2. get the sum of the submatrix
        # 3. compare with k
        # 4. if smaller than k, then update the max value
        # 5. if larger than k, then stop
        # 6. return the max value
        m = len(matrix)
        n = len(matrix[0])
        # 1. get the sum of the matrix
        for i in range(1, m):
            matrix[i][0] += matrix[i - 1][0]
        for j in range(1, n):
            matrix[0][j] += matrix[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]
        # 2. get the sum of the submatrix
        max_value = float('-inf')
        for i in range(m):
            for j in range(n):
                for p in range(i, m):
                    for q in range(j, n):
                        submatrix_sum = matrix[p][q]
                        if i > 0:
                            submatrix_sum -= matrix[i - 1][q]
                        if j > 0:
                            submatrix_sum -= matrix[p][j - 1]
                        if i > 0 and j > 0:
                            submatrix_sum += matrix[i - 1][j - 1]
                        if submatrix_sum <= k:
                            max_value = max(max_value, submatrix_sum)
                            if max_value == k:
                                return k
        return max_value

=======
Suggestion 7

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        def maxSumSubarray(arr: list[int], k: int) -> int:
            prefixSum = 0
            prefixSums = [float('inf')]
            maxSum = float('-inf')
            for num in arr:
                bisect.insort(prefixSums, prefixSum)
                prefixSum += num
                i = bisect.bisect_left(prefixSums, prefixSum - k)
                maxSum = max(maxSum, prefixSum - prefixSums[i])
            return maxSum
        rows = len(matrix)
        cols = len(matrix[0])
        maxSum = float('-inf')
        for left in range(cols):
            rowSums = [0] * rows
            for right in range(left, cols):
                for row in range(rows):
                    rowSums[row] += matrix[row][right]
                maxSum = max(maxSum, maxSumSubarray(rowSums, k))
        return maxSum

=======
Suggestion 8

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        def maxSumSubarray(arr, k):
            max_sum = float("-inf")
            prefix_sum = 0
            prefix_sums = [float("inf")]
            for num in arr:
                bisect.insort(prefix_sums, prefix_sum)
                prefix_sum += num
                i = bisect.bisect_left(prefix_sums, prefix_sum - k)
                max_sum = max(max_sum, prefix_sum - prefix_sums[i])
            return max_sum
        m, n = len(matrix), len(matrix[0])
        max_sum = float("-inf")
        for i in range(n):
            prefix_sum = [0] * m
            for j in range(i, n):
                for k in range(m):
                    prefix_sum[k] += matrix[k][j]
                max_sum = max(max_sum, maxSumSubarray(prefix_sum, k))
        return max_sum

=======
Suggestion 9

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        def maxSumSubarray(arr: list[int]) -> int:
            maxSum = float('-inf')
            prefixSum = 0
            prefixSums = [float('inf')]
            for num in arr:
                bisect.insort(prefixSums, prefixSum)
                prefixSum += num
                i = bisect.bisect_left(prefixSums, prefixSum - k)
                maxSum = max(maxSum, prefixSum - prefixSums[i])
            return maxSum

        maxSum = float('-inf')
        for left in range(len(matrix[0])):
            rowSums = [0] * len(matrix)
            for right in range(left, len(matrix[0])):
                for i in range(len(matrix)):
                    rowSums[i] += matrix[i][right]
                maxSum = max(maxSum, maxSumSubarray(rowSums))
        return maxSum

=======
Suggestion 10

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        def maxSumSubArray(arr, k):
            max_sum = float("-inf")
            prefix_sum = 0
            prefix_sums = []
            prefix_sums.append(0)
            for num in arr:
                prefix_sum += num
                idx = bisect.bisect_left(prefix_sums, prefix_sum - k)
                if idx < len(prefix_sums):
                    max_sum = max(max_sum, prefix_sum - prefix_sums[idx])
                bisect.insort(prefix_sums, prefix_sum)
            return max_sum
        
        def maxSumSubMatrix(matrix, k):
            max_sum = float("-inf")
            for left in range(len(matrix[0])):
                row_sums = [0] * len(matrix)
                for right in range(left, len(matrix[0])):
                    for row in range(len(matrix)):
                        row_sums[row] += matrix[row][right]
                    max_sum = max(max_sum, maxSumSubArray(row_sums, k))
            return max_sum
        
        return maxSumSubMatrix(matrix, k)
