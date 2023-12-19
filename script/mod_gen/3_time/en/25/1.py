def maxCoins(nums):
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for length in range(1, n + 1):
        for left in range(1, n - length + 2):
            right = left + length - 1
            for i in range(left, right + 1):
                dp[left][right] = max(dp[left][right],
                                      nums[left - 1] * nums[i] * nums[right + 1] + dp[left][i - 1] + dp[i + 1][right])
    return dp[1][n]
nums = [3,1,5,8]
print(maxCoins(nums))
