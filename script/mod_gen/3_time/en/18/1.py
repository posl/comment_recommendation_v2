def countNumbersWithUniqueDigits(n):
    if n == 0:
        return 1
    elif n == 1:
        return 10
    elif n == 2:
        return 91
    else:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 10
        dp[2] = 91
        for i in range(3, n+1):
            dp[i] = dp[i-1] + (dp[i-1] - dp[i-2])*(10-(i-1))
        return dp[n]

if __name__ == '__main__':
    countNumbersWithUniqueDigits()