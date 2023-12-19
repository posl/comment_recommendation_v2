def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 1. DP
    # dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + dp[k+1][j] for k in range(i, j+1))
    # Time: O(n^3)
    # Space: O(n^2)
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0]*n for _ in range(n)]
    for i in range(n-2, -1, -1):
        for j in range(i+2, n):
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], dp[i][k-1] + nums[i]*nums[k]*nums[j] + dp[k+1][j])
    return dp[0][n-1]

if __name__ == '__main__':
    maxCoins()