def integerBreak(n):
    dp = [0, 0, 1]
    for i in range(3, n + 1):
        dp.append(0)
        for j in range(1, i):
            dp[i] = max(dp[i], max(dp[i - j], i - j) * max(dp[j], j))
    return dp[n]
print(integerBreak(2))
print(integerBreak(10))
print(integerBreak(58))
