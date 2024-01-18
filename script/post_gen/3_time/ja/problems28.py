Synthesizing 10/10 solutions

=======
Suggestion 1

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = -10**5
        for i in range(m):
            for j in range(n):
                for p in range(i, m):
                    for q in range(j, n):
                        total = 0
                        for x in range(i, p+1):
                            for y in range(j, q+1):
                                total += matrix[x][y]
                        if total <= k:
                            ans = max(ans, total)
        return ans

=======
Suggestion 2

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = float("-inf")
        for left in range(n):
            s = [0] * m
            for right in range(left, n):
                for i in range(m):
                    s[i] += matrix[i][right]
                total = 0
                cur_max = float("-inf")
                for i in range(m):
                    total = max(total + s[i], s[i])
                    cur_max = max(cur_max, total)
                    if cur_max == k:
                        return k
                if cur_max < k:
                    ans = max(ans, cur_max)
                else:
                    for i in range(m):
                        total = 0
                        for j in range(i, m):
                            total += s[j]
                            if total < k:
                                ans = max(ans, total)
                            if ans == k:
                                return k
        return ans

=======
Suggestion 3

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        # 行列の行数と列数を取得
        row = len(matrix)
        col = len(matrix[0])
        # 結果の初期値を設定
        res = float('-inf')
        # 行列の上下の境界を設定
        for top in range(row):
            for bottom in range(top, row):
                # 1行分の数値の総和を格納する配列を作成
                arr = [0] * col
                # 行列の左右の境界を設定
                for right in range(col):
                    # 1行分の数値の総和を格納
                    for i in range(top, bottom + 1):
                        arr[right] += matrix[i][right]
                    # 1行分の数値の総和がk以下の最大値を更新
                    for i in range(right+1):
                        s = 0
                        for j in range(i, right+1):
                            s += arr[j]
                            if s <= k:
                                res = max(res, s)
        # 結果を返す
        return res

=======
Suggestion 4

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        #m = len(matrix)
        #n = len(matrix[0])
        #if m > n:
        #    matrix = list(zip(*matrix))
        #    m, n = n, m
        #print(matrix)
        #print(m, n)
        #for i in range(m):
        #    for j in range(n):
        #        if matrix[i][j] > k:
        #            matrix[i][j] = 0
        #print(matrix)
        #ans = 0
        #for i in range(m):
        #    for j in range(n):
        #        if matrix[i][j] > 0:
        #            ans = max(ans, matrix[i][j])
        #            for p in range(i+1, m):
        #                matrix[p][j] += matrix[i][j]
        #                if matrix[p][j] > k:
        #                    matrix[p][j] = 0
        #            for q in range(j+1, n):
        #                matrix[i][q] += matrix[i][j]
        #                if matrix[i][q] > k:
        #                    matrix[i][q] = 0
        #print(matrix)
        #return ans

        m = len(matrix)
        n = len(matrix[0])
        if m > n:
            matrix = list(zip(*matrix))
            m, n = n, m
        ans = -100000
        for i in range(m):
            for j in range(n):
                for p in range(i, m):
                    for q in range(j, n):
                        tmp = 0
                        for r in range(i, p+1):
                            for s in range(j, q+1):
                                tmp += matrix[r][s]
                        if tmp <= k:
                            ans = max(ans, tmp)
        return ans

=======
Suggestion 5

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        #行列の行数
        m = len(matrix)
        #行列の列数
        n = len(matrix[0])

        #行列の行数が列数より大きい場合
        if m > n:
            #行列の行数と列数を入れ替える
            m,n = n,m
            #行列の要素を入れ替える
            matrix = [list(i) for i in zip(*matrix)]

        #行列の行数が列数より小さい場合
        else:
            #行列の要素を入れ替える
            matrix = [list(i) for i in zip(*matrix)]

        #行列の行数が列数と同じ場合
        #行列の行数が列数より小さい場合
        else:
            #行列の要素を入れ替える
            matrix = [list(i) for i in zip(*matrix)]

        #行列の行数が列数と同じ場合
        if m == n:
            #行列の要素を入れ替える
            matrix = [list(i) for i in zip(*matrix)]

        #行列の行数が列数より小さい場合
        else:
            #行列の要素を入れ替える
            matrix = [list(i) for i in zip(*matrix)]

        #行列の行数が列数と同じ場合
        if m == n:
            #行列の要素を入れ替える
            matrix = [list(i) for i in zip(*matrix)]

        #行列の行数が列数より小さい場合
        else:
            #行列の要素を入れ替える
            matrix = [list(i) for i in zip(*matrix)]

        #行列の行数が列数と同じ場合
        if m == n:
            #行列の要素を入れ替える
            matrix = [list(i) for i in zip(*matrix)]

        #行列の行数が列数より小さい場合
        else:
            #行列の要

=======
Suggestion 6

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        #dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        ans = -9999999999999999
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0:
                    matrix[i][j] += matrix[i - 1][j]
                ans = max(ans, matrix[i][j])
                if j > 0:
                    matrix[i][j] += matrix[i][j - 1]
                ans = max(ans, matrix[i][j])
                if i > 0 and j > 0:
                    matrix[i][j] -= matrix[i - 1][j - 1]
                ans = max(ans, matrix[i][j])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for k in range(i, len(matrix)):
                    for l in range(j, len(matrix[0])):
                        tmp = matrix[k][l]
                        if i > 0:
                            tmp -= matrix[i - 1][l]
                        if j > 0:
                            tmp -= matrix[k][j - 1]
                        if i > 0 and j > 0:
                            tmp += matrix[i - 1][j - 1]
                        if tmp <= k:
                            ans = max(ans, tmp)
        return ans

=======
Suggestion 7

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        max_v = -100000000000000
        for i in range(m):
            for j in range(n):
                for p in range(i,m):
                    for q in range(j,n):
                        tmp = 0
                        for r in range(i,p+1):
                            for s in range(j,q+1):
                                tmp += matrix[r][s]
                        if tmp <= k:
                            max_v = max(max_v,tmp)
        return max_v

=======
Suggestion 8

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        # 二次元累積和
        # 行ごとに累積和を取る
        # 行ごとに列を固定して、その行から下の行までの累積和を取る
        # その累積和の中からk以下の最大値を取る
        # 列ごとに行を固定して、その列から右の列までの累積和を取る
        # その累積和の中からk以下の最大値を取る
        # 行と列を固定して、その行列から右下の行列までの累積和を取る
        # その累積和の中からk以下の最大値を取る
        # 時間複雑度はO(m^2*n^2)
        # 空間複雑度はO(m*n)
        m = len(matrix)
        n = len(matrix[0])
        # 行ごとの累積和を取る
        for i in range(m):
            for j in range(1, n):
                matrix[i][j] += matrix[i][j - 1]
        # 列ごとの累積和を取る
        for j in range(n):
            for i in range(1, m):
                matrix[i][j] += matrix[i - 1][j]
        # 行と列を固定して、その行列から右下の行列までの累積和を取る
        ans = -float("inf")
        for i in range(m):
            for j in range(n):
                for x in range(i, m):
                    for y in range(j, n):
                        # その行列の累積和を取る
                        s = matrix[x][y]
                        if i > 0:
                            s -= matrix[i - 1][y]
                        if j > 0:
                            s -= matrix[x][j - 1]
                        if i > 0 and j > 0:
                            s += matrix[i - 1][j - 1

=======
Suggestion 9

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        # 二次元累積和を計算
        m, n = len(matrix), len(matrix[0])
        sum_matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                sum_matrix[i + 1][j + 1] = sum_matrix[i][j + 1] + sum_matrix[i + 1][j] - sum_matrix[i][j] + matrix[i][j]

        # 累積和を利用して、長方形の和を計算
        res = float('-inf')
        for i in range(m):
            for j in range(n):
                for p in range(i, m):
                    for q in range(j, n):
                        area = sum_matrix[p + 1][q + 1] - sum_matrix[p + 1][j] - sum_matrix[i][q + 1] + sum_matrix[i][j]
                        if area <= k:
                            res = max(res, area)
        return res

=======
Suggestion 10

def maxSumSubmatrix(self, matrix: list[list[int]], k: int) -> int:
        # 2次元累積和
        # 累積和の計算
        # 左上からの累積和
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0:
                    matrix[i][j] += matrix[i-1][j]
                if j > 0:
                    matrix[i][j] += matrix[i][j-1]
                if i > 0 and j > 0:
                    matrix[i][j] -= matrix[i-1][j-1]
        ans = -float("inf")
        # 面積を固定して、高さを変えていく
        for top in range(len(matrix)):
            for bottom in range(top, len(matrix)):
                # 高さを固定して、面積を変えていく
                for left in range(len(matrix[0])):
                    for right in range(left, len(matrix[0])):
                        # 面積を求める
                        area = matrix[bottom][right]
                        if top > 0:
                            area -= matrix[top-1][right]
                        if left > 0:
                            area -= matrix[bottom][left-1]
                        if top > 0 and left > 0:
                            area += matrix[top-1][left-1]
                        # 面積がk以下の時、最大値を更新する
                        if area <= k:
                            ans = max(ans, area)
        return ans
