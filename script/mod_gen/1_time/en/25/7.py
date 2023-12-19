def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0 for j in range(n)] for i in range(n)]
    for l in range(2, n):
        for i in range(0, n - l):
            j = i + l
            for k in range(i + 1, j):
                dp[i][j] = max(dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j])
    return dp[0][n - 1]
print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))
print(maxCoins([1,5,7,9]))
print(maxCoins([1,5,8,9,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,7,8,9,1,2,3,4,5,6,7,8,9]))
print("The values above should be 167, 10, 516, and 1750.")

if __name__ == '__main__':
    maxCoins()