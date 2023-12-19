def splitArray(nums, k):
    n = len(nums)
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    sub = [0]
    for num in nums:
        sub.append(sub[-1] + num)
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            for p in range(i):
                dp[i][j] = min(dp[i][j], max(dp[p][j - 1], sub[i] - sub[p]))
    return dp[n][k]
nums = [7,2,5,10,8]
k = 2
result = splitArray(nums, k)
print(result)

if __name__ == '__main__':
    splitArray()