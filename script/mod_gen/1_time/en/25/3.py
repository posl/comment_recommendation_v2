def maxCoins(nums):
    # Fill this in.
    n = len(nums)
    nums.insert(0, 1)
    nums.append(1)
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            for k in range(i, j + 1):
                dp[i][j] = max(dp[i][j], dp[i][k - 1] + nums[i - 1] * nums[k] * nums[j + 1] + dp[k + 1][j])
    return dp[1][n]
print(maxCoins([3, 1, 5, 8]))
# 167
print(maxCoins([1, 5]))
# 10

if __name__ == '__main__':
    maxCoins()