def maxCoins(nums):
    # dp[i][j] is the max coins we can get by bursting all the balloons between i and j
    # dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + nums[i-1] * nums[k] * nums[j+1]) for i <= k <= j
    # dp[i][j] = 0 if i > j
    # dp[i][i] = nums[i-1] * nums[i] * nums[i+1]
    # dp[i][i+1] = max(nums[i-1] * nums[i] * nums[i+1], nums[i] * nums[i+1] * nums[i+2])
    # dp[i][i+2] = max(nums[i-1] * nums[i] * nums[i+1] + nums[i-1] * nums[i+1] * nums[i+2], nums[i] * nums[i+1] * nums[i+2] + nums[i] * nums[i+2] * nums[i+3])
    # dp[i][i+3] = max(nums[i-1] * nums[i] * nums[i+1] + nums[i-1] * nums[i+1] * nums[i+2] + nums[i-1] * nums[i+2] * nums[i+3], nums[i] * nums[i+1] * nums[i+2] + nums[i] * nums[i+2] * nums[i+3] + nums[i] * nums[i+3] * nums[i+4])
    # dp[i][i+4] = max(nums[i-1] * nums[i] * nums[i+1] + nums[i-1] * nums[i+1] * nums[i+2] + nums[i-1] * nums[i+2] * nums[i+3] + nums[i-1] * nums[i+3] * nums[i+4], nums[i] * nums[i+1] * nums[i+2] + nums[i] * nums[i+2] * nums[i+3] + nums[i] * nums[i+3] * nums[i+4] + nums[i] * nums[i+4] * nums[i+5])
    # dp[i][i+5] = max(nums[i-1] * nums[i

if __name__ == '__main__':
    maxCoins()