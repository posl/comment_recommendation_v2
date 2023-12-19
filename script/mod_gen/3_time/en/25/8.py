def maxCoins(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j])
    return dp[0][n - 1]
nums = [3,1,5,8]
print(maxCoins(nums))
nums = [1,5]
print(maxCoins(nums))
