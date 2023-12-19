def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for gap in range(2, n):
        for left in range(0, n - gap):
            right = left + gap
            for i in range(left + 1, right):
                dp[left][right] = max(dp[left][right], dp[left][i] + dp[i][right] + nums[left] * nums[i] * nums[right])
    return dp[0][n - 1]

if __name__ == '__main__':
    maxCoins()