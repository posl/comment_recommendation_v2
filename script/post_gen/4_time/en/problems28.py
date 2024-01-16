Synthesizing 10/10 solutions

=======
Suggestion 1

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')
        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for c in range(n):
                    total[c] += matrix[j][c]
                ans = max(ans, self.maxSumSubarray(total, k))
        return ans

=======
Suggestion 2

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_sum = -float('inf')
        for i in range(m):
            sums = [0] * n
            for j in range(i, m):
                for c in range(n):
                    sums[c] += matrix[j][c]
                max_sum = max(max_sum, self.maxSumSubarray(sums, k))
        return max_sum

=======
Suggestion 3

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = float('-inf')

        for left in range(cols):
            row_sum = [0] * rows
            for right in range(left, cols):
                for row in range(rows):
                    row_sum[row] += matrix[row][right]
                res = max(res, self.maxSumSubArray(row_sum, k))
                if res == k: return res
        return res

=======
Suggestion 4

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        maxSum = float('-inf')
        # O(n^2) time complexity
        for left in range(n):
            temp = [0] * m
            for right in range(left, n):
                for i in range(m):
                    temp[i] += matrix[i][right]
                maxSum = max(maxSum, self.maxSumSubArray(temp, k))
        return maxSum

=======
Suggestion 5

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = float('-inf')
        for left in range(n):
            row_sum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    row_sum[i] += matrix[i][right]
                #print(row_sum)
                ans = max(ans, self.maxSumSubArray(row_sum, k))
                if ans == k:
                    return ans
        return ans

=======
Suggestion 6

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        if matrix is None or len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        maxSum = -math.inf
        for left in range(n):
            sums = [0 for i in range(m)]
            for right in range(left, n):
                for i in range(m):
                    sums[i] += matrix[i][right]
                maxSum = max(maxSum, self.maxSumSubarray(sums, k))
                if maxSum == k:
                    return maxSum
        return maxSum

=======
Suggestion 7

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')

        for left in range(n):
            row_sum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    row_sum[i] += matrix[i][right]

                cur_sum = 0
                cur_max = float('-inf')

                for v in row_sum:
                    cur_sum = max(cur_sum + v, v)
                    cur_max = max(cur_max, cur_sum)
                    if cur_max == k:
                        return k

                if cur_max < k:
                    ans = max(ans, cur_max)
                    continue

                pre_sum = 0
                s = set([0])
                for v in row_sum:
                    pre_sum += v
                    x = bisect.bisect_left(s, pre_sum - k)
                    if x < len(s):
                        ans = max(ans, pre_sum - s[x])
                    bisect.insort(s, pre_sum)

        return ans

=======
Suggestion 8

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float("-inf")

        for left in range(n):
            row_sum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    row_sum[i] += matrix[i][right]

                prefix_sum = [0]
                cur = 0
                for num in row_sum:
                    cur += num
                    idx = bisect.bisect_left(prefix_sum, cur - k)
                    if idx < len(prefix_sum):
                        ans = max(ans, cur - prefix_sum[idx])
                    bisect.insort(prefix_sum, cur)

        return ans

=======
Suggestion 9

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')
        for l in range(n):
            row_sum = [0] * m
            for r in range(l, n):
                for i in range(m):
                    row_sum[i] += matrix[i][r]
                cur_sum = 0
                cur_max = float('-inf')
                for val in row_sum:
                    cur_sum = max(cur_sum + val, val)
                    cur_max = max(cur_max, cur_sum)
                    if cur_max == k:
                        return k
                if cur_max < k:
                    ans = max(ans, cur_max)
                else:
                    for i in range(m):
                        sum_i = 0
                        for j in range(i, m):
                            sum_i += row_sum[j]
                            if sum_i <= k:
                                ans = max(ans, sum_i)
        return ans

=======
Suggestion 10

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] += matrix[i][j - 1]
                
        result = float('-inf')
        for i in range(len(matrix[0])):
            for j in range(i, len(matrix[0])):
                prefix_sums = set()
                prefix_sums.add(0)
                current_sum = 0
                for row in matrix:
                    current_sum += row[j] - (row[i - 1] if i > 0 else 0)
                    target = current_sum - k
                    for prefix_sum in prefix_sums:
                        if prefix_sum <= target:
                            result = max(result, current_sum - prefix_sum)
                    prefix_sums.add(current_sum)
        return result
