def maxCoins(nums):
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n, -1, -1):
        for j in range(i+1, n+2):
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
    return dp[0][n+1]

if __name__ == '__main__':
    maxCoins()