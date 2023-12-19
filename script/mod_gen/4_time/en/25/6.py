def maxCoins(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-1):
        dp[i][i+1] = 0
    for k in range(2, n):
        for left in range(n-k):
            right = left + k
            for i in range(left+1, right):
                dp[left][right] = max(dp[left][right], dp[left][i] + dp[i][right] + nums[left] * nums[i] * nums[right])
    return dp[0][n-1]
print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))
print(maxCoins([2,3,4,5,6,7,8,9]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10]))
print("The values above should be 167, 10, 2010, and 14540.")

if __name__ == '__main__':
    maxCoins()