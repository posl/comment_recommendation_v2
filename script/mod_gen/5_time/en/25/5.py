def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for i in range(n-2, -1, -1):
        for j in range(i+2, n):
            for k in range(i+1, j):
                dp[i][j] = max(dp[i][j], nums[i]*nums[k]*nums[j] + dp[i][k] + dp[k][j])
    return dp[0][n-1]
print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))
print(maxCoins([1,3,5,8]))
print(maxCoins([9,76,64,21,97,60,5]))
print(maxCoins([2,4,8,4,0,7,8,9,1,2,4,5,0,6,7,8,9,4,3,2,1,2,4,5,6,7,8,9,0,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,0,9,8,7,6,5,4,3,2,1,2,3,4,5,6,7,8,9]))
