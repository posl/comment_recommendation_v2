def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(2, n):
        for j in range(n - i):
            for k in range(j + 1, j + i):
                dp[j][j + i] = max(dp[j][j + i], nums[j] * nums[k] * nums[j + i] + dp[j][k] + dp[k][j + i])
    return dp[0][n - 1]

if __name__ == '__main__':
    maxCoins()