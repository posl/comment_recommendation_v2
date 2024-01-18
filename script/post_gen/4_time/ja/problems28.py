Synthesizing 9/10 solutions

=======
Suggestion 1

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        pass

=======
Suggestion 2

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

=======
Suggestion 3

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for i in range(n):
            sums = [0] * m
            for j in range(i, n):
                for row in range(m):
                    sums[row] += matrix[row][j]
                res = max(res, self.helper(sums, k))
        return res

=======
Suggestion 4

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        #まずは縦横の長さを取得
        m = len(matrix)
        n = len(matrix[0])
        #行の数が列の数よりずっと大きい場合はどうなるか？
        if m > n:
            m, n = n, m
        #最大値を格納する変数を用意
        max_value = -100000
        #行の数が列の数よりずっと大きい場合はどうなるか？の場合分け
        if m == len(matrix):
            #行の数が列の数よりずっと大きい場合はどうなるか？の場合分け
            #行の数が列の数よりずっと大きい場合はどうなるか？の場合分け
            for i in range(m):
                for j in range(n):
                    #縦方向にどれだけの長さがあるか
                    for k in range(m):
                        #横方向にどれだけの長さがあるか
                        for l in range(n):
                            #最大値を格納する変数を用意
                            max_value = max(max_value, sum(matrix[i][j:k+1][l]))
        else:
            #行の数が列の数よりずっと大きい場合はどうなるか？の場合分け
            for i in range(m):
                for j in range(n):
                    #縦方向にどれだけの長さがあるか
                    for k in range(m):
                        #横方向にどれだけの長さがあるか
                        for l in range(n):
                            #最大値を格納する変数を用意
                            max_value = max(max_value, sum(matrix[i][j:k+1][l]))
        return max_value

=======
Suggestion 5

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        # 二次元累積和を求める
        m,n = len(matrix),len(matrix[0])
        s = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                s[i+1][j+1] = s[i+1][j] + s[i][j+1] - s[i][j] + matrix[i][j]
        ans = -float('inf')
        # 左上の座標を全探索
        for i in range(m):
            for j in range(n):
                # 右下の座標を全探索
                for x in range(i+1,m+1):
                    for y in range(j+1,n+1):
                        # 面積を求める
                        area = s[x][y] - s[i][y] - s[x][j] + s[i][j]
                        # 面積が k 以下のとき、最大値を更新
                        if area <= k:
                            ans = max(ans,area)
        return ans

=======
Suggestion 6

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = -10 ** 5
        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for l in range(n):
                    total[l] += matrix[j][l]
                totalSet = [0]
                cur = 0
                for num in total:
                    cur += num
                    idx = bisect.bisect_left(totalSet, cur - k)
                    if idx < len(totalSet):
                        ans = max(ans, cur - totalSet[idx])
                    bisect.insort(totalSet, cur)
        return ans

=======
Suggestion 7

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        def maxSumSubarray(arr: list[int]) -> int:
            maxSum = float('-inf')
            prefixSum = 0
            prefixSums = [float('inf')]
            for num in arr:
                bisect.insort(prefixSums, prefixSum)
                prefixSum += num
                idx = bisect.bisect_left(prefixSums, prefixSum - k)
                maxSum = max(maxSum, prefixSum - prefixSums[idx])
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
Suggestion 8

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])

        if m > n:
            matrix = list(zip(*matrix))
            m, n = n, m

        ans = -100000
        for i in range(m):
            rowsum = [0] * n
            for j in range(i, m):
                for l in range(n):
                    rowsum[l] += matrix[j][l]
                st = [0]
                cur = 0
                for r in rowsum:
                    cur += r
                    idx = bisect.bisect_left(st, cur - k)
                    if idx < len(st):
                        ans = max(ans, cur - st[idx])
                    bisect.insort(st, cur)
        return ans

=======
Suggestion 9

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        ans = -10 ** 5
        for l in range(len(matrix[0])):
            row_sums = [0] * len(matrix)
            for r in range(l, len(matrix[0])):
                for i in range(len(matrix)):
                    row_sums[i] += matrix[i][r]
                print(row_sums)
                cur_sum = 0
                cur_max = -10 ** 5
                for row_sum in row_sums:
                    if cur_sum < 0:
                        cur_sum = row_sum
                    else:
                        cur_sum += row_sum
                    cur_max = max(cur_max, cur_sum)
                if cur_max <= k:
                    ans = max(ans, cur_max)
                else:
                    cur_sum = 0
                    cur_max = -10 ** 5
                    for row_sum in row_sums:
                        cur_sum += row_sum
                        if cur_sum == k:
                            return k
                        elif cur_sum < k:
                            cur_max = max(cur_max, cur_sum)
                        else:
                            cur_sum -= row_sum
                            cur_max = max(cur_max, cur_sum)
                            l = r
                            break
                    ans = max(ans, cur_max)
        return ans
