def maxCoins(nums):
    n = len(nums)
    nums = [1] + nums + [1]
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for length in range(1, n + 1):
        for left in range(1, n - length + 2):
            right = left + length - 1
            for k in range(left, right + 1):
                dp[left][right] = max(dp[left][right], dp[left][k - 1] + nums[left - 1] * nums[k] * nums[right + 1] + dp[k + 1][right])
    return dp[1][n]
print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))
print(maxCoins([2,4,8,4,0,7,8,9,1,2,4,6,8,9,3,2,5,7,8,9,3,2,4,5,6,7,8,9,0,4,3,2,2,4,5,6,7,8,9,0,5,4,3,2,1,2,3,4,5,6,7,8,9,0,4,3,2,2,4,5,6,7,8,9,0,5,4,3,2,1,2,3,4,5,6,7,8,9,0,4,3,2,2,4,5,6,7,8,9,0,5,4,3,2,1,2,3,4,5,6,7,8,9,0,4,3,2,2,4,5,6,7,8,9,0,5,4,3,2,1,2,3,4,5,6,7,8,9,0,4,3,2,2,4,5,6,7,8,9,0,5,4,3,2,1,2,3,4,5,6,7,8,9,0,4,3,2,2,4,5,6,7,8,
