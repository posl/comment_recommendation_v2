Synthesizing 9/10 solutions

=======
Suggestion 1

def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for i in range(n, -1, -1):
            for j in range(i + 1, n + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])

        return dp[0][n + 1]

=======
Suggestion 2

def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n + 1]

=======
Suggestion 3

def maxCoins(self, nums: list[int]) -> int:
        #dp[i][j] は、区間 [i, j] で得られる最大のコインの枚数
        #dp[0][n + 1] が答え
        n = len(nums)
        nums.append(1)
        nums.insert(0, 1)
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for k in range(1, n + 1):
            for l in range(1, n + 2 - k):
                r = l + k - 1
                for m in range(l, r + 1):
                    dp[l][r] = max(dp[l][r], dp[l][m - 1] + nums[l - 1] * nums[m] * nums[r + 1] + dp[m + 1][r])

        return dp[1][n]

=======
Suggestion 4

def maxCoins(self, nums: list[int]) -> int:
        # [1] + nums + [1] は、左右の壁を意味する
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[i][j] は、区間 i から j までの最大得点
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                # k は最後に割る風船の番号
                for k in range(i + 1, j):
                    # dp[i][k] と dp[k][j] は、区間 i から k までと k から j までの最大得点
                    dp[i][j] = max(dp[i][j], dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j])
        return dp[0][n - 1]

=======
Suggestion 5

def maxCoins(self, nums: list[int]) -> int:
        #dp[i][j] = i番目からj番目までの最大値
        #dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        #dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        #dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        #dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        #dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        #dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        #dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        #dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for k in range(1, n + 1):
            for i in range(1, n - k + 2):
                j = i + k - 1
                for t in range(i, j + 1):
                    dp[i][j] = max(dp[i][j], dp[i][t - 1] + dp[t + 1][j] + nums[i - 1] * nums[t] * nums[j + 1])
        return dp[1][n]

=======
Suggestion 6

def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for left in range(n - 2, -1, -1):
            for right in range(left + 2, n):
                dp[left][right] = max([dp[left][i] + dp[i][right] + nums[left] * nums[i] * nums[right] for i in range(left + 1, right)])
        return dp[0][n - 1]

=======
Suggestion 7

def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for left in range(n - 2, -1, -1):
            for right in range(left + 2, n):
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right], nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]

=======
Suggestion 8

def maxCoins(self, nums: list[int]) -> int:
        # 1. 0 を左右に追加する
        nums = [1] + nums + [1]
        n = len(nums)
        # 2. dp[i][j] は範囲 i ~ j の最大値を表す
        dp = [[0] * n for _ in range(n)]
        # 3. dp[i][j] を更新していく
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                # 3-1. dp[i][j] は範囲 i ~ j の最大値
                for k in range(i + 1, j):
                    # 3-2. dp[i][j] は範囲 i ~ j の最大値
                    # dp[i][j] は、i ~ j の最後に割る風船を決めたときの最大値
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
        # 4. dp[0][n - 1] が答え
        return dp[0][n - 1]

=======
Suggestion 9

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # 0 から n-1 までのインデックスで示された n 個の風船が与えられる
        # 各風船には配列 nums で表された数字が書かれている
        # i 番目の風船を破裂させると、nums[i - 1] * nums[i] * nums[i + 1]のコインがもらえる
        # i - 1 または i + 1 が配列の範囲外に出た場合は、1 が描かれた風船があるものとして扱う
        # 全ての風船を賢く割って集められるコインの最大値を出力せよ
        # 1 <= n <= 300
        # 0 <= nums[i] <= 100
        # 1 <= i <= n-1
        # 0 <= i-1, i+1 <= n-1
        # 0 <= i-1, i+1 <= 300
        # 0 <= nums[i-1], nums[i], nums[i+1] <= 100
        # 0 <= coins <= 100 * 100 * 100 = 1000000
        # 0 <= coins <= 1000000
        # 0 <= coins <= 1000000
        # 0 <= coins <= 100
