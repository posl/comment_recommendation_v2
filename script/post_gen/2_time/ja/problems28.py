Synthesizing 10/10 solutions

=======
Suggestion 1

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = float('-inf')
        for left in range(n):
            sums = [0] * m
            for right in range(left, n):
                for i in range(m):
                    sums[i] += matrix[i][right]
                res = max(res, self.helper(sums, k))
        return res

=======
Suggestion 2

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = -10 ** 5
        for i in range(m):
            arr = [0] * n
            for j in range(i, m):
                for l in range(n):
                    arr[l] += matrix[j][l]
                ans = max(ans, self.maxSumSubarray(arr, k))
        return ans

=======
Suggestion 3

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = -100000
        for i in range(m):
            for j in range(1,n):
                matrix[i][j] += matrix[i][j-1]
        for i in range(n):
            for j in range(i,n):
                d = {0:-100000}
                s = 0
                for l in range(m):
                    s += matrix[l][j] - (matrix[l][i-1] if i > 0 else 0)
                    it = d.bisect_left(s-k)
                    if it != len(d):
                        ans = max(ans, s-d[it])
                    d.bisect_left(s)
        return ans

=======
Suggestion 4

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        # 二次元累積和を求める
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                s[i + 1][j + 1] = s[i + 1][j] + matrix[i][j]
        for j in range(n):
            for i in range(m):
                s[i + 1][j + 1] += s[i][j + 1]

        # 二次元累積和の中から、和が k 以下となる最大の長方形の和を求める
        ans = -float('inf')
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for x in range(i):
                    for y in range(j):
                        if (i - x) * (j - y) == 1:
                            continue
                        if s[i][j] - s[x][j] - s[i][y] + s[x][y] <= k:
                            ans = max(ans, s[i][j] - s[x][j] - s[i][y] + s[x][y])

        return ans

=======
Suggestion 5

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        result = -100000
        for i in range(0, m):
            for j in range(0, n):
                for p in range(i, m):
                    for q in range(j, n):
                        sum = 0
                        for a in range(i, p+1):
                            for b in range(j, q+1):
                                sum += matrix[a][b]
                        if sum <= k and result < sum:
                            result = sum
        return result

=======
Suggestion 6

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        # 2次元累積和の計算
        m, n = len(matrix), len(matrix[0])
        cum = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                cum[i+1][j+1] = cum[i+1][j] + cum[i][j+1] - cum[i][j] + matrix[i][j]
        
        # 累積和を用いて、長方形の和がK以下となる最大の長方形を探す
        ans = float('-inf')
        for i in range(1, m+1):
            for j in range(i, m+1):
                # 累積和の差分をとることで、長方形の和を求める
                diff_cum = [cum[j][l] - cum[i-1][l] for l in range(n+1)]
                # 累積和の差分を用いて、和がK以下となる最大の長方形を探す
                # 二分探索を用いて、和がK以下となる最大の長方形を探す
                s = 0
                cand = float('-inf')
                for l in range(n+1):
                    r = bisect.bisect_left(diff_cum, s+k)
                    if r <= n:
                        cand = max(cand, diff_cum[r] - s)
                    s += diff_cum[l]
                ans = max(ans, cand)
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
                i = bisect.bisect_left(prefixSums, prefixSum - k)
                maxSum = max(maxSum, prefixSum - prefixSums[i])
            return maxSum

        maxSum = float('-inf')
        for i in range(len(matrix)):
            arr = [0] * len(matrix[0])
            for j in range(i, len(matrix)):
                for l in range(len(matrix[0])):
                    arr[l] += matrix[j][l]
                maxSum = max(maxSum, maxSumSubarray(arr))
        return maxSum

=======
Suggestion 8

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
Suggestion 9

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_sum = -1000000
        for i in range(m):
            for j in range(n):
                for p in range(i, m):
                    for q in range(j, n):
                        sum = 0
                        for r in range(i, p+1):
                            for s in range(j, q+1):
                                sum += matrix[r][s]
                        if sum <= k and max_sum < sum:
                            max_sum = sum
        return max_sum

=======
Suggestion 10

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        # 行列の行数と列数を取得
        row = len(matrix)
        col = len(matrix[0])
        # 答えとなる最大値を初期化
        ans = -1000000
        # 列方向に累積和を取る
        for i in range(row):
            for j in range(col-1):
                matrix[i][j+1] += matrix[i][j]
        # 列方向に累積和を取った行列の、行方向に累積和を取る
        for j in range(col):
            for i in range(row-1):
                matrix[i+1][j] += matrix[i][j]
        # 列方向に累積和を取った行列の、行方向に累積和を取った行列の、左上から右下にかけての長方形の和を全探索する
        for i1 in range(row):
            for j1 in range(col):
                for i2 in range(i1, row):
                    for j2 in range(j1, col):
                        # 長方形の和を取得
                        total = matrix[i2][j2]
                        if i1 > 0:
                            total -= matrix[i1-1][j2]
                        if j1 > 0:
                            total -= matrix[i2][j1-1]
                        if i1 > 0 and j1 > 0:
                            total += matrix[i1-1][j1-1]
                        # 長方形の和が k 以下の場合は、最大値を更新する
                        if total <= k:
                            ans = max(ans, total)
        return ans
