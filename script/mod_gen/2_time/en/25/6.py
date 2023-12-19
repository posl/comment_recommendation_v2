def maxCoins(nums):
    n = len(nums)
    dp = [[0]*n for _ in range(n)]
    for l in range(n):
        for i in range(n-l):
            j = i+l
            for k in range(i,j+1):
                left = 1
                right = 1
                if i != 0:
                    left = nums[i-1]
                if j != n-1:
                    right = nums[j+1]
                before = 0
                after = 0
                if k != i:
                    before = dp[i][k-1]
                if k != j:
                    after = dp[k+1][j]
                dp[i][j] = max(dp[i][j], before + left*nums[k]*right + after)
    return dp[0][n-1]
nums = [3,1,5,8]
print(maxCoins(nums))
