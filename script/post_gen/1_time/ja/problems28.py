Synthesizing 10/10 solutions

=======
Suggestion 1

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
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
        m, n = len(matrix), len(matrix[0])
        ans = -float('inf')
        for l in range(n):
            row_sum = [0] * m
            for r in range(l, n):
                for i in range(m):
                    row_sum[i] += matrix[i][r]
                ans = max(ans, self.maxSumSubArray(row_sum, k))
        return ans

=======
Suggestion 3

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = float('-inf')
        for l in range(n):
            row_sum = [0] * m
            for r in range(l, n):
                for i in range(m):
                    row_sum[i] += matrix[i][r]
                ans = max(ans, self.maxSumSubarray(row_sum, k))
                if ans == k:
                    return k
        return ans

=======
Suggestion 4

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        #行列の行数
        m = len(matrix)
        #行列の列数
        n = len(matrix[0])
        #最大値
        ans = -10**5
        #行列の行数分ループ
        for i in range(m):
            #行列の列数分ループ
            for j in range(n):
                #行列の行数分ループ
                for p in range(i, m):
                    #行列の列数分ループ
                    for q in range(j, n):
                        #最大値と、和がkよりも大きくないような長方形の和の最大値を比較して、大きい方を最大値とする
                        ans = max(ans, self.sum(matrix, i, j, p, q, k))
        return ans

=======
Suggestion 5

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        # 二次元累積和を求める
        # 二次元累積和を求めるときは、左上の点から右下の点までの範囲の和を求める
        # 二次元累積和を求めるときは、左上の点から右下の点までの範囲の和を求める
        # 二次元累積和を求めるときは、左上の点から右下の点までの範囲の和を求める
        # 二次元累積和を求めるときは、左上の点から右下の点までの範囲の和を求める
        # 二次元累積和を求めるときは、左上の点から右下の点までの範囲の和を求める
        # 二次元累積和を求めるときは、左上の点から右下の点までの範囲の和を求める
        # 二次元累積和を求めるときは、左上の点から右下の点までの範囲の和を求める
        # 二次元累積和を求めるときは、左上の点から右下の点までの範囲の和を求める
        # 二次元累積和を求めるときは、左上の点から右下の点までの範囲の和を求める
        m = len(matrix)
        n = len(matrix[0])
        sum_matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                sum_matrix[i + 1][j + 1] = sum_matrix[i + 1][j] + sum_matrix[i][j + 1] - sum_matrix[i][j] + matrix[i][j]
        # 二分探

=======
Suggestion 6

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')
        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for c in range(n):
                    total[c] += matrix[j][c]
                totalSet = [0]
                cur = 0
                for v in total:
                    cur += v
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
        ans = -10 ** 9
        for l in range(n):
            row_sum = [0] * m
            for r in range(l, n):
                for i in range(m):
                    row_sum[i] += matrix[i][r]
                st = [0]
                cur = 0
                for num in row_sum:
                    cur += num
                    idx = bisect.bisect_left(st, cur - k)
                    if idx < len(st):
                        ans = max(ans, cur - st[idx])
                    bisect.insort(st, cur)
        return ans

=======
Suggestion 8

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = -10**5 - 1
        for i in range(n):
            s = [0] * m
            for j in range(i, n):
                for l in range(m):
                    s[l] += matrix[l][j]
                st = set()
                st.add(0)
                cur = 0
                for l in range(m):
                    cur += s[l]
                    it = st.bisect_left(cur - k)
                    if it != len(st):
                        ans = max(ans, cur - st[it])
                    st.add(cur)
        return ans

=======
Suggestion 9

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = float('-inf')
        for left in range(n):
            row_sum = [0] * m
            for right in range(left, n):
                for i in range(m):
                    row_sum[i] += matrix[i][right]
                # 1D Kadane's
                cur_sum = 0
                cur_max = float('-inf')
                for v in row_sum:
                    cur_sum = max(cur_sum + v, v)
                    cur_max = max(cur_max, cur_sum)
                    if cur_max == k:
                        return k
                if cur_max < k:
                    ans = max(ans, cur_max)
                else:
                    # cur_max is the largest sum <= k
                    # => cur_max + x <= k, 0 <= x
                    # => x <= k - cur_max
                    # => ans <= k - cur_max + cur_max
                    # => ans <= k
                    for i in range(m):
                        sum = 0
                        for j in range(i, m):
                            sum += row_sum[j]
                            if cur_max < sum <= k:
                                return k
                            if sum <= k:
                                ans = max(ans, sum)
        return ans

=======
Suggestion 10

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        ans = float('-inf')
        m, n = len(matrix), len(matrix[0])
        for l in range(n):
            rowsum = [0] * m
            for r in range(l, n):
                for i in range(m):
                    rowsum[i] += matrix[i][r]
                accsum = [0]
                cursum = 0
                for v in rowsum:
                    cursum += v
                    idx = bisect.bisect_left(accsum, cursum - k)
                    if idx != len(accsum):
                        ans = max(ans, cursum - accsum[idx])
                    bisect.insort(accsum, cursum)
        return ans
