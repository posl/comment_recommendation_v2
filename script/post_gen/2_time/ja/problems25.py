Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

def maxCoins(self, nums: list[int]) -> int:
        n = len(nums)
        points = [1] + nums + [1]
        dp = [[0] * (n + 2) for _ in range(n + 2)]

        for i in range(n, -1, -1):
            for j in range(i + 1, n + 2):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], points[i] * points[k] * points[j] + dp[i][k] + dp[k][j])
        return dp[0][n + 1]

=======
Suggestion 3

def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
        return dp[0][n - 1]

=======
Suggestion 4

def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        # dp[left][right] = max coins we can collect
        # if we burst all the balloons between left and right
        for left in range(n - 2, -1, -1):
            for right in range(left + 2, n):
                # same formula to get the best score from bursting
                # balloons between (left, right) as before
                best = 0
                for i in range(left + 1, right):
                    score = nums[left] * nums[i] * nums[right]
                    score += dp[left][i] + dp[i][right]
                    best = max(best, score)
                dp[left][right] = best
        return dp[0][n - 1]

=======
Suggestion 5

def maxCoins(self, nums: list[int]) -> int:
        nums.insert(0,1)
        nums.append(1)
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j],dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
        return dp[0][n-1]

=======
Suggestion 6

def maxCoins(self, nums: list[int]) -> int:
        # とりあえず、先頭と最後に1を追加しておく
        nums = [1] + nums + [1]
        # dp[i][j]は、i番目からj番目までの風船を割った時の最大コイン
        dp = [[0] * len(nums) for _ in range(len(nums))]
        # 風船の数
        n = len(nums)
        # 風船の数が1つの場合は、コインは0
        if n == 1:
            return 0
        # 風船の数が2つの場合は、コインは1つめの風船のコイン
        if n == 2:
            return nums[0]
        # 風船の数が3つの場合は、コインは1つめの風船のコイン+2つめの風船のコイン+1つめの風船と2つめの風船のコイン
        if n == 3:
            return nums[0] * nums[1] * nums[2] + nums[0] * nums[2] + max(nums[0], nums[2])
        # 風船の数が4つ以上の場合は、dpテーブルを埋める
        # 例えば、風船の数が4つの場合は、
        # 1つめの風船を割った時の最大コインは、1つめの風船のコイン+2つめの風船のコイン+1つめの風船と2つめの風船のコイン+1つめの風船と3つめの風船のコイン
        # 2つめの風船を割った時の最大コインは、2つめの風船のコイン+3つめの風船のコイン+1つめの風船と2つめの風船

=======
Suggestion 7

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # 1 <= n <= 300
        # 0 <= nums[i] <= 100
        # 0 <= i <= 299
        # 0 <= j <= 299
        # 0 <= k <= 299
        # 0 <= l <= 299
        # 0 <= m <= 299
        # 0 <= n <= 299
        # 0 <= o <= 299
        # 0 <= p <= 299
        # 0 <= q <= 299
        # 0 <= r <= 299
        # 0 <= s <= 299
        # 0 <= t <= 299
        # 0 <= u <= 299
        # 0 <= v <= 299
        # 0 <= w <= 299
        # 0 <= x <= 299
        # 0 <= y <= 299
        # 0 <= z <= 299
        # 0 <= a <= 299
        # 0 <= b <= 299
        # 0 <= c <= 299
        # 0 <= d <= 299
        # 0 <= e <= 299
        # 0 <= f <= 299
        # 0 <= g <= 299
        # 0 <= h <= 299
        # 0 <= i <= 299
        # 0 <= j <= 299
        # 0 <= k <= 299
        # 0 <= l <= 299
        # 0 <= m <= 299
        # 0 <= n <= 299
        # 0 <= o <= 299
        # 0 <= p <= 299
        # 0 <= q <= 299
        # 0 <= r <= 299
        # 0 <= s <= 299
        # 0 <= t <= 299
        # 0 <= u <= 299
        # 0 <= v <= 299
        # 0 <= w <= 299
        # 0 <= x <= 299
        # 0 <= y <= 299
        # 0 <= z <= 299
        # 0 <= a <= 299
        # 0 <= b <= 299
        # 0 <= c <= 299
        # 0 <= d <=

=======
Suggestion 8

def maxCoins(self, nums: list[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j],
                                   nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])

        return dp[0][-1]

=======
Suggestion 9

def maxCoins(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0] * (len(nums)) for _ in range(len(nums))]
        for i in range(2, len(nums)):
            for j in range(0, len(nums) - i):
                for k in range(j + 1, j + i):
                    dp[j][j + i] = max(dp[j][j + i], dp[j][k] + dp[k][j + i] + nums[j] * nums[k] * nums[j + i])
        return dp[0][len(nums) - 1]
